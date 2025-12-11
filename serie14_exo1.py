from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2  # 20 % par défaut

    def __post_init__(self):
        # Normalisation du nom : on enlève les espaces autour
        self.nom = self.nom.strip()

        # Validation du prix
        if self.prix_ht < 0:
            raise ValueError("Le prix HT doit être positif")

        # Validation du taux de TVA
        if not (0 <= self.taux_tva <= 1):
            raise ValueError("Le taux de TVA doit être entre 0 et 1")

    def prix_ttc(self) -> float:
        """Calcule et renvoie le prix TTC du produit."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self) -> str:
        """Affichage lisible pour print(produit)."""
        return (
            f"Produit {self.nom} – {self.prix_ht} € HT – "
            f"{self.prix_ttc()} € TTC"
        )


if __name__ == "__main__":
    # Produits valides
    p1 = Produit("Clavier", 50.0)
    p2 = Produit(" Souris ", 30.0)  # espaces autour du nom
    p3 = Produit("Écran", 150.0, taux_tva=0.1)

    print(p1)
    print(p2)
    print(p3)

    # Cas invalides pour tester les validations
    try:
        p_invalide_prix = Produit("Câble", -10.0)
    except ValueError as e:
        print("Erreur attendue (prix négatif) :", e)

    try:
        p_invalide_tva = Produit("Support écran", 20.0, taux_tva=1.5)
    except ValueError as e:
        print("Erreur attendue (taux TVA hors [0,1]) :", e)
