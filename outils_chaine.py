# outils_chaine.py

SEPARATEUR = "-" * 40


def compter_mots(texte: str) -> int:
    """Compte le nombre de mots dans le texte en utilisant split()."""
    mots = texte.split()
    return len(mots)


def est_palindrome(texte: str) -> bool:
    """
    Renvoie True si le texte est un palindrome (sans espaces, en minuscules),
    sinon False.
    """
    # Normaliser : minuscules + suppression des espaces
    normalise = texte.replace(" ", "").lower()
    # On compare avec sa version inversée
    return normalise == normalise[::-1]
