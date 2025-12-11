from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2  # 20 % par défaut

    @staticmethod
    def est_prix_valide(prix: float) -> bool:
        """Renvoie True si le prix est >= 0."""
        return prix >= 0

    @staticmethod
    def format_euro(montant: float) -> str:
        """Formate un montant avec 2 décimales et le symbole €."""
        return f"{montant:.2f} €"

    def __post_init__(self):
        # Normalisation du nom
        self.nom = self.nom.strip()

        # Validation du prix via la méthode statique
        if not Produit.est_prix_valide(self.prix_ht):
            raise ValueError("Le prix HT doit être positif")

        # Validation du taux de TVA
        if not (0 <= self.taux_tva <= 1):
            raise ValueError("Le taux de TVA doit être entre 0 et 1")

    def prix_ttc(self) -> float:
        """Calcule et renvoie le prix TTC du produit."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self) -> str:
        """Utilise format_euro pour afficher les montants."""
        prix_ht_str = Produit.format_euro(self.prix_ht)
        prix_ttc_str = Produit.format_euro(self.prix_ttc())
        return f"Produit {self.nom} – {prix_ht_str} HT – {prix_ttc_str} TTC"


if __name__ == "__main__":
    # Tests des méthodes statiques directement
    print("Produit.est_prix_valide(10) :", Produit.est_prix_valide(10))
    print("Produit.est_prix_valide(-5) :", Produit.est_prix_valide(-5))
    print("Produit.format_euro(123.456) :", Produit.format_euro(123.456))

    # Produits pour vérifier le formatage et la validation
    p1 = Produit(" Clavier ", 50.0)
    p2 = Produit("Souris", 30.0)
    p3 = Produit("Écran", 150.0, taux_tva=0.1)

    print(p1)
    print(p2)
    print(p3)

    # Cas invalide pour vérifier que les validations fonctionnent toujours
    try:
        p_invalide = Produit("Câble", -10.0)
    except ValueError as e:
        print("Erreur attendue (prix négatif) :", e)
