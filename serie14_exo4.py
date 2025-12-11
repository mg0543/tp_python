
from dataclasses import dataclass, field
from serie14_exo3 import Produit
from serie14_exo2 import LigneFacture


@dataclass
class LigneFacture:
    produit: Produit
    quantite: int
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        if self.quantite <= 0:
            raise ValueError("La quantité doit être strictement positive")

        self.total_ht = self.quantite * self.produit.prix_ht
        self.total_ttc = self.quantite * self.produit.prix_ttc()

    def __str__(self) -> str:
        total_ht_str = Produit.format_euro(self.total_ht)
        total_ttc_str = Produit.format_euro(self.total_ttc)
        return (
            f"{self.quantite} x {self.produit.nom} – "
            f"{total_ht_str} HT – {total_ttc_str} TTC"
        )


@dataclass
class Facture:
    numero: int
    client: str
    lignes: list[LigneFacture]
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        if not self.lignes:
            raise ValueError("Une facture doit contenir au moins une ligne")

        self._recalculer_totaux()

    def _recalculer_totaux(self):
        """Méthode interne pour recalculer les totaux."""
        self.total_ht = sum(ligne.total_ht for ligne in self.lignes)
        self.total_ttc = sum(ligne.total_ttc for ligne in self.lignes)

    def ajouter_ligne(self, ligne: LigneFacture):
        """Ajoute une ligne à la facture et recalcule les totaux."""
        self.lignes.append(ligne)
        self._recalculer_totaux()

    def __str__(self) -> str:
        lignes_str = "\n".join(str(ligne) for ligne in self.lignes)
        total_ht_str = Produit.format_euro(self.total_ht)
        total_ttc_str = Produit.format_euro(self.total_ttc)
        header = f"Facture n°{self.numero} – Client : {self.client}"
        footer = f"TOTAL : {total_ht_str} HT – {total_ttc_str} TTC"
        return f"{header}\n{lignes_str}\n{footer}"


if __name__ == "__main__":
    # Quelques produits
    p1 = Produit("Clavier", 50.0)
    p2 = Produit("Souris", 30.0)
    p3 = Produit("Écran", 150.0, taux_tva=0.1)

    # Lignes de facture
    l1 = LigneFacture(p1, 2)  # 2 claviers
    l2 = LigneFacture(p2, 3)  # 3 souris
    l3 = LigneFacture(p3, 1)  # 1 écran

    # Facture avec lignes
    facture = Facture(numero=1, client="Alice", lignes=[l1, l2, l3])
    print(facture)

    print("\nAjout d'une nouvelle ligne...")
    l4 = LigneFacture(p2, 1)  # 1 souris de plus
    facture.ajouter_ligne(l4)
    print(facture)

    # Cas d'erreur : facture sans lignes
    try:
        facture_vide = Facture(numero=2, client="Bob", lignes=[])
    except ValueError as e:
        print("\nErreur attendue (facture vide) :", e)
