def est_pair(n):
    """Retourne True si n est pair, False sinon."""
    return n % 2 == 0



def calculer_tva(prix_ht, taux):
    """Retourne le prix TTC à partir d'un prix HT et d'un taux de TVA en %."""
    tva = prix_ht * taux / 100
    prix_ttc = prix_ht + tva
    return prix_ttc


def moyenne(liste_nombres):
    """Retourne la moyenne des nombres d'une liste."""
    if len(liste_nombres) == 0:
        return 0

    total = 0
    for x in liste_nombres:
        total = total + x

    return total / len(liste_nombres)



if __name__ == "__main__":

    print("Tests de est_pair :")
    print("est_pair(4)  ->", est_pair(4))   
    print("est_pair(7)  ->", est_pair(7))   
    print("est_pair(0)  ->", est_pair(0))   
    print()


    print("Tests de calculer_tva :")
    print("Prix TTC pour 100€ HT, 20% ->", calculer_tva(100, 20))
    print("Prix TTC pour 50€ HT, 5.5% ->", calculer_tva(50, 5.5))
    print()

    print("Tests de moyenne :")
    notes1 = [10, 12, 14]
    notes2 = [9.99, 14.5, 3.2, 29.0]
    notes3 = []

    print("moyenne([10, 12, 14]) ->", moyenne(notes1))
    print("moyenne([9.99, 14.5, 3.2, 29.0]) ->", moyenne(notes2))
    print("moyenne([]) ->", moyenne(notes3))
