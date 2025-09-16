import os
import shutil
import tarfile
import zstandard as zstd
import re
import json
import io
import traceback
import sys

BASE_DIR = r"C:\Users\keren\Downloads\devops-master"
TARGET_DIR = r"C:\Users\keren\DevOps"

def extract_tar_zst(tar_zst_path, extract_to):
    dctx = zstd.ZstdDecompressor()
    try:
        with open(tar_zst_path, 'rb') as compressed:
            try:
                with dctx.stream_reader(compressed) as reader:
                    with tarfile.open(fileobj=reader, mode='r|*') as tar:
                        tar.extractall(path=extract_to)
            except tarfile.StreamError:
                compressed.seek(0)
                decompressed = dctx.decompress(compressed.read())
                with tarfile.open(fileobj=io.BytesIO(decompressed), mode='r:*') as tar:
                    tar.extractall(path=extract_to)
    except Exception as e:
        raise RuntimeError(f"Failed to extract {tar_zst_path}: {e}")

def clean_md_filename(filename):
    return re.sub(r'-[a-zA-Z0-9]{4,}\.md$', '.md', filename)

def fix_image_paths(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = re.sub(
        r'(!\[[^\]]*\])\((?:\.\.?/)*\.?guides/img/([^)\s]+)\)',
        r'\1(./\2)',
        content
    )

    if content != updated_content:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

def process_chapter(module_name, chapter_file):
    chapter_name = os.path.splitext(os.path.splitext(chapter_file)[0])[0]
    module_path = os.path.join(BASE_DIR, module_name)
    chapter_tar_path = os.path.join(module_path, chapter_file)
    target_chapter_dir = os.path.join(TARGET_DIR, module_name, chapter_name)
    os.makedirs(target_chapter_dir, exist_ok=True)

    tmp_extract_path = os.path.join(module_path, "__tmp_extract__")
    if os.path.exists(tmp_extract_path):
        shutil.rmtree(tmp_extract_path)
    os.makedirs(tmp_extract_path)

    extract_tar_zst(chapter_tar_path, tmp_extract_path)

    # Remove Codio clutter
    for unwanted in [".codio", ".settings", "README.md"]:
        unwanted_path = os.path.join(tmp_extract_path, unwanted)
        if os.path.exists(unwanted_path):
            if os.path.isdir(unwanted_path):
                shutil.rmtree(unwanted_path)
            else:
                os.remove(unwanted_path)

    guides_path = os.path.join(tmp_extract_path, ".guides")
    if os.path.exists(guides_path):
        # Move JSONs if present
        for json_file in ["metadata.json", "book.json", "assessments.json", "index.json"]:
            src = os.path.join(guides_path, json_file)
            if os.path.exists(src):
                shutil.move(src, os.path.join(target_chapter_dir, json_file))

        # Check for index.json inside .guides/content
        content_dir = os.path.join(guides_path, "content")
        if os.path.exists(content_dir):
            idx_src = os.path.join(content_dir, "index.json")
            if os.path.exists(idx_src):
                shutil.move(idx_src, os.path.join(target_chapter_dir, "index.json"))

            # Move markdown content
            for md_file in os.listdir(content_dir):
                if md_file.endswith(".md"):
                    new_name = clean_md_filename(md_file)
                    target_md_path = os.path.join(target_chapter_dir, new_name)
                    shutil.move(
                        os.path.join(content_dir, md_file),
                        target_md_path
                    )
                    fix_image_paths(target_md_path)

        # Move assessments directory if exists
        assessments_dir = os.path.join(guides_path, "assessments")
        if os.path.exists(assessments_dir) and os.path.isdir(assessments_dir):
            shutil.move(assessments_dir, os.path.join(target_chapter_dir, "assessments"))

        # Move images if any
        img_dir = os.path.join(guides_path, "img")
        if os.path.exists(img_dir) and os.listdir(img_dir):
            for img_file in os.listdir(img_dir):
                shutil.move(
                    os.path.join(img_dir, img_file),
                    os.path.join(target_chapter_dir, img_file)
                )

        shutil.rmtree(guides_path)

    # Move all remaining extracted files
    for f in os.listdir(tmp_extract_path):
        full_path = os.path.join(tmp_extract_path, f)
        if os.path.isfile(full_path):
            shutil.move(full_path, os.path.join(target_chapter_dir, f))
        elif os.path.isdir(full_path):
            shutil.move(full_path, os.path.join(target_chapter_dir, f))

    shutil.rmtree(tmp_extract_path)

    return chapter_name

def main():
    errors = []

    # Allow optional module name argument
    if len(sys.argv) > 1:
        modules = [sys.argv[1]]
    else:
        modules = os.listdir(BASE_DIR)

    for module_name in modules:
        module_path = os.path.join(BASE_DIR, module_name)
        if not os.path.isdir(module_path):
            continue

        for chapter_file in os.listdir(module_path):
            if chapter_file.endswith(".tar.zst"):
                print(f"Processing {module_name}/{chapter_file}")
                try:
                    process_chapter(module_name, chapter_file)
                except Exception:
                    tb = traceback.format_exc()
                    error_msg = f"ERROR: {module_name}/{chapter_file}\n{tb}\n"
                    errors.append(error_msg)

    if errors:
        with open(os.path.join(TARGET_DIR, "errors.txt"), "w", encoding="utf-8") as f:
            f.writelines(errors)
        print(f"\n⚠️ Finished with {len(errors)} errors. See 'errors.txt'.")
    else:
        print("\n✅ All chapters processed successfully.")

if __name__ == "__main__":
    main()
