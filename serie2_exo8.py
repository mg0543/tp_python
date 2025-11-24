import json

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
   
    with open("commandes.json", "r", encoding="utf-8") as f:
        commandes = json.load(f)  
    ca = calculer_ca(commandes)
    stats_statuts = compter_commandes_par_statut(commandes)
    totaux_clients = totaux_par_client(commandes)


    print("=== Tableau de bord commandes ===")
    print(f"Chiffre d'affaires (commandes payées) : {ca:.2f} €")
    print()

    print("Nombre de commandes par statut :")

    for statut in ["payee", "annulee", "en_attente"]:
        nb = stats_statuts.get(statut, 0)

        print("  -", statut.ljust(11), ":", nb)
    print()

    print("Top clients :")

    clients_tries = sorted(
        totaux_clients.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for client, total in clients_tries:
        print(f"  - {client:<20} : {total:.2f} €")
