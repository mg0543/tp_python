notes =[]

with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne:
            note = float(ligne)
            notes.append(note)  

            if len (notes) ==0:
                print("Aucune note trouvée dans le fichier.")    

                note_min = min(notes)
                note_max = max(notes) 
                moyenne = sum(notes) / len(notes)
                nbreussites=0
                for note in notes:
                    if note >=10:
                        nbreussites +=1 
                        print("Notes lues : {notes}")
                        print(f"Note minimale : {note_min}")
                        print(f"Note maximale : {note_max}")    
                        print(f"Moyenne des notes : {moyenne:.2f}")
                        print(f"Nombre de réussites (note >= 10) : {nbreussites}")
                        