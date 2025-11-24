commandes = [
    {"id": 1, "client": "alice@example.com",   "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",     "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",   "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com", "montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",     "montant": 35.0,  "statut": "payee"},
]

def calculer_ca(commandes):
    """Retourne le chiffre d'affaires total pour les commandes payées."""
    ca_total = 0.0
    for commande in commandes:
        if commande["statut"] == "payee":
            ca_total = ca_total + commande["montant"]
    return ca_total


def compter_commandes_par_statut(commandes):
    """Retourne un dictionnaire {statut: nombre_de_commandes}."""
    compte = {}  

    for commande in commandes:
        statut = commande["statut"]
        if statut not in compte:
            compte[statut] = 0
        compte[statut] = compte[statut] + 1

    return compte

def totaux_par_client(commandes):
    """Retourne un dictionnaire {client: total_depense}."""
    totaux = {}  

    for commande in commandes:
        client = commande["client"]
        montant = commande["montant"]

        if client not in totaux:
            totaux[client] = 0.0

        totaux[client] = totaux[client] + montant

    return totaux

if __name__ == "__main__":

    ca = calculer_ca(commandes)
    print("Chiffre d'affaires total (commandes payées) :", ca)

    print() 

    stats_statuts = compter_commandes_par_statut(commandes)
    print("Nombre de commandes par statut :")
    for statut, nb in stats_statuts.items():
        print("-", statut, ":", nb)

    print()  

    totaux_clients = totaux_par_client(commandes)
    print("Montant total dépensé par client :")
    for client, total in totaux_clients.items():
        print("-", client, ":", total)