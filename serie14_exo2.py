from dataclasses import dataclass, field

@dataclass
class Ligne:
    quantite: int
    prix_unitaire: float
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.quantite * self.prix_unitaire
from dataclasses import dataclass, field
from serie14_exo1 import Produit


@dataclass
class LigneFacture:
    produit: Produit
    quantite: int
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        # Validation de la quantité
        if self.quantite <= 0:
            raise ValueError("La quantité doit être strictement positive")

        # Calcul des totaux
        self.total_ht = self.quantite * self.produit.prix_ht
        self.total_ttc = self.quantite * self.produit.prix_ttc()

    def __str__(self) -> str:
        return (
            f"{self.quantite} x {self.produit.nom} – "
            f"{self.total_ht} € HT – {self.total_ttc} € TTC"
        )


if __name__ == "__main__":
    # On réutilise les produits de l'exercice 1
    p1 = Produit("Clavier", 50.0)
    p2 = Produit("Souris", 30.0)
    p3 = Produit("Écran", 150.0, taux_tva=0.1)

    ligne1 = LigneFacture(p1, 2)
    ligne2 = LigneFacture(p2, 3)
    ligne3 = LigneFacture(p3, 1)

    print(ligne1)
    print(ligne2)
    print(ligne3)

    # Cas de quantite invalide
    try:
        ligne_invalide = LigneFacture(p1, 0)
    except ValueError as e:
        print("Erreur attendue (quantité invalide) :", e)
