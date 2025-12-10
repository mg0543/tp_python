# remise.py

def calculer_prix_ttc(prix_ht, taux_tva):
    """
    Calcule le prix TTC à partir d'un prix HT et d'un taux de TVA.
    :param prix_ht: prix hors taxe (doit être >= 0)
    :param taux_tva: taux de TVA (ex: 0.2 pour 20 %)
    """
    if prix_ht < 0:
        raise ValueError("Le prix HT doit être positif")
    return prix_ht * (1 + taux_tva)
