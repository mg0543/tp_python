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