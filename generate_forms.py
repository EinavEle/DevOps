import os, json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ========= CONFIG =========
# Path to your repository (👈 change this to your local repo path)
REPO_DIR = r"C:\Users\keren\DevOps"

# Required scopes for Forms + Classroom
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.coursework.me",
    "https://www.googleapis.com/auth/classroom.coursework.students"
]

# ========= AUTH =========
def get_service(api_name, version):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build(api_name, version, credentials=creds)

forms_service = get_service("forms", "v1")
classroom_service = get_service("classroom", "v1")

# ========= COURSE PICKER =========
def pick_course():
    results = classroom_service.courses().list(pageSize=50).execute()
    courses = results.get("courses", [])

    if not courses:
        raise RuntimeError("No Classroom courses found for your account.")

    print("\nAvailable Classroom courses:")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course['name']}  (id={course['id']})")

    choice = int(input("\nSelect a course [1-{}]: ".format(len(courses))))
    selected = courses[choice - 1]
    print(f"\n✅ Selected course: {selected['name']} (id={selected['id']})\n")
    return selected["id"]

COURSE_ID = pick_course()

# ========= HELPERS =========
def load_assessments(chapter_path):
    """Return list of questions from a chapter assessments dir or file"""
    questions = []
    assess_dir = os.path.join(chapter_path, "assessments")
    if os.path.isdir(assess_dir):
        for f in os.listdir(assess_dir):
            if f.endswith(".json"):
                path = os.path.join(assess_dir, f)
                with open(path, encoding="utf-8") as fp:
                    q = json.load(fp)
                    q["_source_file"] = path
                    questions.append(q)

    assess_file = os.path.join(chapter_path, "assessments.json")
    if os.path.exists(assess_file):
        with open(assess_file, encoding="utf-8") as fp:
            data = json.load(fp)
            if isinstance(data, list):
                for q in data:
                    q["_source_file"] = assess_file
                    questions.append(q)
            else:
                data["_source_file"] = assess_file
                questions.append(data)
    return questions

def clean_text(text: str) -> str:
    """Remove newlines and extra spaces from text"""
    return " ".join(text.split()) if text else ""

def map_question(q, log_warnings):
    """Convert your JSON schema → Forms API item, handle multiple types"""
    question_text = clean_text(q.get("source", {}).get("instructions", "Untitled question"))
    q_type = q.get("type", "multiple-choice")
    src_file = q.get("_source_file", "unknown file")

    # Multiple choice / checkbox style
    if q_type in ("multiple-choice", "checkbox"):
        if "answers" not in q.get("source", {}):
            msg = f"⚠️ Skipping (no answers field) in {src_file}: {question_text[:60]}..."
            print(msg); log_warnings.append(msg)
            return None

        # Clean and dedupe answers
        seen = set()
        answers = []
        correct = []
        for a in q["source"]["answers"]:
            ans = clean_text(a.get("answer", ""))
            if ans not in seen:
                seen.add(ans)
                answers.append(ans)
                if a.get("correct"):
                    correct.append(ans)

        return {
            "createItem": {
                "item": {
                    "title": question_text,
                    "questionItem": {
                        "question": {
                            "required": True,
                            "grading": {
                                "pointValue": q["source"].get("points", 1),
                                "correctAnswers": {"answers": [{"value": c} for c in correct]}
                            },
                            "choiceQuestion": {
                                "type": "RADIO" if not q["source"].get("multipleResponse") else "CHECKBOX",
                                "options": [{"value": a} for a in answers],
                                "shuffle": False
                            }
                        }
                    }
                },
                "location": {"index": 0}
            }
        }

    # Short answer / text type
    elif q_type in ("short-answer", "text"):
        return {
            "createItem": {
                "item": {
                    "title": question_text,
                    "questionItem": {
                        "question": {
                            "required": True,
                            "textQuestion": {}
                        }
                    }
                },
                "location": {"index": 0}
            }
        }

    else:
        msg = f"⚠️ Unsupported type '{q_type}' in {src_file}, skipping: {question_text[:60]}..."
        print(msg); log_warnings.append(msg)
        return None

# ========= MAIN =========
def process_repo():
    skipped_log = []

    for module in os.listdir(REPO_DIR):
        module_path = os.path.join(REPO_DIR, module)
        if not os.path.isdir(module_path):
            continue

        all_questions = []
        for chapter in os.listdir(module_path):
            chap_path = os.path.join(module_path, chapter)
            if os.path.isdir(chap_path):
                all_questions.extend(load_assessments(chap_path))

        if not all_questions:
            continue

        # Step 1: Create Google Form (only title allowed at creation)
        form = {"info": {"title": f"{module} Assessments"}}
        form_obj = forms_service.forms().create(body=form).execute()
        form_id = form_obj["formId"]

        # Step 2: Enable quiz mode
        forms_service.forms().batchUpdate(
            formId=form_id,
            body={
                "requests": [
                    {
                        "updateSettings": {
                            "settings": {"quizSettings": {"isQuiz": True}},
                            "updateMask": "quizSettings.isQuiz"
                        }
                    }
                ]
            }
        ).execute()

        # Step 3: Add questions
        requests = [r for q in all_questions if (r := map_question(q, skipped_log)) is not None]
        if requests:
            forms_service.forms().batchUpdate(formId=form_id, body={"requests": requests}).execute()
        form_url = form_obj["responderUri"]
        print(f"✅ Created form for {module}: {form_url}")

        # Step 4: Post into Classroom as assignment
        coursework = {
            "title": f"{module} Assessments",
            "description": "Complete the module assessments.",
            "materials": [{"link": {"url": form_url}}],
            "workType": "ASSIGNMENT",
            "state": "PUBLISHED"
        }
        classroom_service.courses().courseWork().create(courseId=COURSE_ID, body=coursework).execute()
        print(f"📌 Posted assignment in Classroom for {module}")

    # Write skipped warnings to file
    if skipped_log:
        with open("skipped_questions.log", "w", encoding="utf-8") as logf:
            logf.write("\n".join(skipped_log))
        print(f"\n⚠️ Some questions were skipped. See skipped_questions.log for details.")

if __name__ == "__main__":
    process_repo()
