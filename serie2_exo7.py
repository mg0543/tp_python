import json

commandes = [
    {"id": 1, "client": "alice@example.com",   "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",     "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",   "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com", "montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",     "montant": 35.0,  "statut": "payee"},
]

json_str = json.dumps(commandes, indent=2, ensure_ascii=False)

print(json_str)

with open("commandes.json", "w", encoding="utf-8") as f:
    f.write(json_str)
