exo1
largeur = 6
hauteur = 4.2
 
surface= largeur * hauteur

perimetre= 2 * (largeur + hauteur)

print("Surface =", surface, "Perimetre =", perimetre)
exo2
prix_ht_str= input ('prix HT')

taux_tva_str= input ('taux TVA(%)')

prix_ht= float (prix_ht_str)
taux_tva= float (taux_tva_str)
 
tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

print ('prix TTC =', prix_ttc)

exo3
age = int(input("Entrer votre age: "))
if age < 12:
    print("tarif=5.")
elif 12 < age <= 17:
    print("tarif=7.")

elif 18 <= age <= 25:
    print("tarif=8,5.")

elif age > 25:
    print("tarif=10.")

else:
    print("tarif=7.")
    exo4
    n_str = input("Entrez un entier n : ")
n = int(n_str)

print("Table de multiplication de", n, "de 1 à 10 :")
for i in range(1, 11):  
    print(n, "x", i, "=", n * i)

somme = 0   
i = 1       

while i <= n:
    somme = somme + i   
    i = i + 1           

print("La somme des entiers de 1 à", n, "vaut", somme)
exo5
prix = [9.99, 14.5, 3.2, 29.0]

print("Liste des prix :")
for p in prix:
    print("Prix :", p)

total = 0
for p in prix:
    total = total + p

print("Total des prix :", total)


moyenne = total / len(prix)
print("Prix moyen :", moyenne)

print("Prix strictement supérieurs à 10€ :")
for p in prix:
    if p > 10:
        print(p)
exo6
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
