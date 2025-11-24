n_str = input("Entrez un entier n : ")
n = int(n_str)

print("Table de multiplication de", n, "de 1 à 10 :")
for i in range(1, 10):  
    print(n, "x", i, "=", n * i)

somme = 0   
i = 1       

while i <= n:
    somme = somme + i   
    i = i + 1           

print("La somme des entiers de 1 à", n, "vaut", somme)