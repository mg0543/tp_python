def charger_commandes(nom_fichier):
    """Lit un fichier de commandes et retourne une liste de dictionnaires."""
    commandes = []

    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()          
            if ligne == "":                
                continue

            champs = ligne.split(";")     

            if len(champs) != 4:
                print("Ligne ignorée (format incorrect) :", ligne)
                continue

            id_str, client, montant_str, statut = champs

            commande = {
                "id": int(id_str),
                "client": client,
                "montant": float(montant_str),
                "statut": statut
            }

            commandes.append(commande)

    return commandes
