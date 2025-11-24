notes = [12, 5.5, 17, 9, 13, 8, 10]


note_min = min(notes)
note_max = max(notes)

moyenne = sum(notes) / len(notes)

nb_reussites = 0
for note in notes:
    if note >= 10:
        nb_reussites = nb_reussites + 1

pourcentage_reussite = nb_reussites / len(notes) * 100

print("Notes :", notes)
print("Note minimale :", note_min)
print("Note maximale :", note_max)
print("Moyenne de la classe :", moyenne)
print("Nombre de notes >= 10 :", nb_reussites)
print("Pourcentage de réussite :", pourcentage_reussite, "%")
