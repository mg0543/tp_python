mot_de_passe = input("Entrez un mot de passe : ")

a_longueur = len(mot_de_passe) >= 8

a_minuscule = False
a_majuscule = False
a_chiffre = False

for c in mot_de_passe:
    if c.islower():   
        a_minuscule = True
    if c.isupper():   
        a_majuscule = True
    if c.isdigit():    
        a_chiffre = True

if a_longueur and a_minuscule and a_majuscule and a_chiffre:
    print("Mot de passe valide ")
else:
    print("Mot de passe invalide , raisons :")
    if not a_longueur:
        print("- le mot de passe doit contenir au moins 8 caractères")
    if not a_minuscule:
        print("- il manque au moins une lettre minuscule")
    if not a_majuscule:
        print("- il manque au moins une lettre majuscule")
    if not a_chiffre:
        print("- il manque au moins un chiffre")
