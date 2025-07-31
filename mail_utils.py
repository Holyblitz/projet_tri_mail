import os

def load_mails(folder_path):
    mails = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") or filename.endswith(".eml"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = f.read()
                mails.append({
                    "filename": filename,
                    "subject": extract_subject(content),
                    "body": content
                })
    return mails

def extract_subject(content):
    # Parser simple pour tester - à améliorer plus tard
    for line in content.splitlines():
        if line.lower().startswith("subject:"):
            return line.split(":", 1)[1].strip()
    return "Sans sujet"
