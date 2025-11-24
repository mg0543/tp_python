commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

ca_total = 0.0

for commande in commandes:
    if commande["statut"] == "payee":
        ca_total = ca_total + commande["montant"]

print("Chiffre d'affaires total (payé) :", ca_total)

compte_statuts = {
    "payee": 0,
    "annulee": 0,
    "en_attente": 0
}

for commande in commandes:
    statut = commande["statut"]
    compte_statuts[statut] = compte_statuts[statut] + 1

print("Nombre de commandes par statut :", compte_statuts)
totaux_par_client = {}  

for commande in commandes:
    email = commande["client"]
    montant = commande["montant"]

    if email not in totaux_par_client:
        totaux_par_client[email] = 0.0

    totaux_par_client[email] = totaux_par_client[email] + montant

print("Montant total dépensé par client :", totaux_par_client)
