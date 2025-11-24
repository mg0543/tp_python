prix_ht_str= input ('prix HT')

taux_tva_str= input ('taux TVA(%)')

prix_ht= float (prix_ht_str)
taux_tva= float (taux_tva_str)
 
tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

print ('prix TTC =', prix_ttc)