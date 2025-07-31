import subprocess
import json

def classify_mail(mail):
    prompt = build_prompt(mail["subject"], mail["body"])
    response = query_ollama(prompt)
    return parse_response(response)

def build_prompt(subject, body):
    return f"""
Tu es un assistant IA local. Voici un mail à classer dans une de ces 4 catégories :

- Urgent
- À lire
- À archiver
- Spam

Donne uniquement la catégorie (une seule ligne).  
Sujet : {subject}  
Message : {body}
"""

def query_ollama(prompt, model="mistral"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")

def parse_response(response):
    # Nettoyage et simplification
    lines = response.strip().splitlines()
    if not lines:
        return "Non classé"
    last_line = lines[-1].strip().lower()
    if "urgent" in last_line:
        return "Urgent"
    elif "spam" in last_line:
        return "Spam"
    elif "à lire" in last_line or "a lire" in last_line:
        return "À lire"
    elif "archiver" in last_line:
        return "À archiver"
    else:
        return "Non classé"
