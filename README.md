# mail-assistant-local/
│
├── README.md           ← Présentation pro + cas d’usage
├── main.py             ← Script principal (tri + prompt)
├── config.py           ← Variables : modèle, login, filtres
├── mail_utils.py       ← Extraction et parsing des mails
├── prompts/            ← Prompts personnalisés
│   └── tri_basique.txt
├── data/               ← Exemple de mails (fictifs, anonymisés)
└── requirements.txt    ← Dépendances (Python, model, etc.)

## Objectif

Gagner du temps dans la gestion quotidienne des emails grâce à un agent IA **entièrement local** (sans cloud, sans fuite de données), capable de :

- Lire et structurer les mails (via `.eml`, `.txt` ou IMAP)
- Identifier les messages importants, urgents, ou à archiver
- Générer des résumés simples ou des extraits utiles
- Proposer des actions à effectuer (réponse, suivi, suppression)

---

## ⚙️ Fonctionnalités

| Fonction | Description |
|----------|-------------|
| 📥 Chargement des mails | Lecture depuis fichiers locaux (ou IMAP à venir) |
| 🔎 Tri intelligent | Classification : `urgent`, `à lire`, `à archiver`, `spam` |
| 🧠 IA locale (LLM) | Résumés générés via un modèle open-source (ex: Mistral) |
| 📄 Export des résultats | Sauvegarde en `.json` ou `.txt` pour archivage |

---

## Stack

- Python 3.10+
- Mistral (via Ollama) ou OpenAI-compatible LLM (facultatif)
- Whisper / Vosk (à venir pour traitement vocal)
- Pandas, Email Parser, FAISS (version future)

---

## 🧪 Exemple d’usage

```bash
python main.py --input data/mails/ --model mistral
