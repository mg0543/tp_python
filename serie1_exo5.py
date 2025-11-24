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
