import os
import json
from mail_utils import load_mails
from llm import classify_mail

INPUT_DIR = "data"
OUTPUT_FILE = "output/tri_resultats.json"

def main():
    mails = load_mails(INPUT_DIR)
    results = []

    for i, mail in enumerate(mails):
        print(f"⏳ Traitement du mail {i + 1}...")
        classification = classify_mail(mail)
        results.append({
            "mail_id": i + 1,
            "subject": mail.get("subject", "No subject"),
            "classification": classification
        })

    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"✅ Tri terminé. Résultats dans {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
