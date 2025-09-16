import os
import re
import json

TARGET_DIR = r"C:\Users\keren\DevOps"

def clean_md_filename(filename):
    """Remove Codio hash suffixes like -abcd1234.md → .md"""
    return re.sub(r'-[a-zA-Z0-9]{4,}\.md$', '.md', filename)

def ensure_readme(path, title, is_root=False):
    """Create a minimal README.md if it doesn't exist"""
    readme_path = os.path.join(path, "README.md")
    if os.path.exists(readme_path):
        return
    lines = [f"# {title}", ""]
    if is_root:
        lines.append("_This is the course root._")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"📝 Created README.md in {path}")

# -------- Chapter-level --------
def generate_sidebar_from_metadata(metadata_path, chapter_dir, chapter_title):
    with open(metadata_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lines = [f"- [{chapter_title} Home](./README.md)", ""]

    for section in data.get("sections", []):
        content_file = section.get("content-file")
        if not content_file:
            continue
        md_name = clean_md_filename(os.path.basename(content_file))
        if os.path.basename(md_name).startswith("Comprehension-Check"):
            continue
        title = os.path.splitext(md_name)[0]
        lines.append(f'- [{title}](./{md_name} "{title}")')

    # put back links at the bottom
    lines.extend([
        "",
        f"- [⬅ Back to Module](../README.md)",
        f"- [⬅ Back to Course](../../README.md)"
    ])

    with open(os.path.join(chapter_dir, "_sidebar.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ensure_readme(chapter_dir, chapter_title)

def generate_sidebar_from_index(index_path, chapter_dir, chapter_title):
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lines = [f"- [{chapter_title} Home](./README.md)", ""]

    for item in data.get("order", []):
        md_name = clean_md_filename(item + ".md")
        if md_name.startswith("Comprehension-Check"):
            continue
        title = os.path.splitext(md_name)[0]
        if os.path.exists(os.path.join(chapter_dir, md_name)):
            lines.append(f'- [{title}](./{md_name} "{title}")')

    # back links at bottom
    lines.extend([
        "",
        f"- [⬅ Back to Module](../README.md)",
        f"- [⬅ Back to Course](../../README.md)"
    ])

    with open(os.path.join(chapter_dir, "_sidebar.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ensure_readme(chapter_dir, chapter_title)

# -------- Module-level --------
def generate_module_sidebar(module_path, module_name):
    lines = [f"- [{module_name.replace('-', ' ').title()} Home](./README.md)", ""]

    for chapter_name in sorted(os.listdir(module_path)):
        chapter_dir = os.path.join(module_path, chapter_name)
        if not os.path.isdir(chapter_dir):
            continue
        chapter_title = chapter_name.replace("-", " ").title()
        lines.append(f'- [{chapter_title}](./{chapter_name}/README.md "{chapter_title}")')

    # back link at bottom
    lines.extend([
        "",
        f"- [⬅ Back to Course](../README.md)"
    ])

    sidebar_path = os.path.join(module_path, "_sidebar.md")
    with open(sidebar_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ensure_readme(module_path, module_name.replace("-", " ").title())

# -------- Root-level --------
def generate_root_sidebar():
    lines = ["- [Course Home](./README.md)", ""]

    for module_name in sorted(os.listdir(TARGET_DIR)):
        module_path = os.path.join(TARGET_DIR, module_name)
        if not os.path.isdir(module_path):
            continue
        module_title = module_name.replace("-", " ").title()
        lines.append(f'- [{module_title}](./{module_name}/README.md "{module_title}")')

    sidebar_path = os.path.join(TARGET_DIR, "_sidebar.md")
    with open(sidebar_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    ensure_readme(TARGET_DIR, "Course Modules", is_root=True)

# -------- Main --------
def main():
    for module_name in os.listdir(TARGET_DIR):
        module_path = os.path.join(TARGET_DIR, module_name)
        if not os.path.isdir(module_path):
            continue

        has_chapters = False
        for chapter_name in os.listdir(module_path):
            chapter_dir = os.path.join(module_path, chapter_name)
            if not os.path.isdir(chapter_dir):
                continue
            has_chapters = True
            chapter_title = chapter_name.replace("-", " ").title()
            metadata_path = os.path.join(chapter_dir, "metadata.json")
            index_path = os.path.join(chapter_dir, "index.json")

            if os.path.exists(metadata_path):
                print(f"📘 Generating sidebar from metadata.json for {module_name}/{chapter_name}")
                generate_sidebar_from_metadata(metadata_path, chapter_dir, chapter_title)
            elif os.path.exists(index_path):
                print(f"📘 Generating sidebar from index.json for {module_name}/{chapter_name}")
                generate_sidebar_from_index(index_path, chapter_dir, chapter_title)
            else:
                print(f"⚠️ No metadata.json or index.json found in {module_name}/{chapter_name}")
                ensure_readme(chapter_dir, chapter_title)

        if has_chapters:
            print(f"📂 Generating module-level sidebar for {module_name}")
            generate_module_sidebar(module_path, module_name)

    print("📚 Generating root-level sidebar")
    generate_root_sidebar()

if __name__ == "__main__":
    main()
