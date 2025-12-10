import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def recuperer_posts():
    """
    Envoie une requête GET vers API_URL,
    vérifie le code HTTP,
    retourne une liste de posts (ou [] en cas d'erreur).
    """
    try:
        # On envoie la requête avec un timeout (optionnel mais recommandé)
        response = requests.get(API_URL, timeout=5)
    except requests.exceptions.RequestException as e:
        # Erreur réseau : pas d'accès à l'API, problème de connexion, etc.
        print("Erreur réseau lors de la récupération des posts :", e)
        return []

    # Vérifier le code HTTP
    if response.status_code != 200:
        print("Erreur HTTP :", response.status_code)
        return []

    # Tenter de décoder le JSON
    try:
        data = response.json()
    except ValueError:
        print("Erreur : réponse non valide (JSON attendu).")
        return []

    # On vérifie que c'est bien une liste
    if not isinstance(data, list):
        print("Format inattendu des données :", type(data))
        return []

    return data


def afficher_resume_posts(posts, n=5):
    """
    Affiche un résumé des n premiers posts :
    Post #id (user userId) : titre
    """
    if not posts:
        print("Aucun post à afficher.")
        return

    nb = min(n, len(posts))
    print(f"Aperçu des {nb} premiers posts :")
    print("------------------------------------")

    for post in posts[:nb]:
        post_id = post.get("id")
        user_id = post.get("userId")
        titre = post.get("title")
        print(f"Post #{post_id} (user {user_id}) : {titre}")


if __name__ == "__main__":
    # 1) Récupérer les posts via l'API
    posts = recuperer_posts()

    # 2) Afficher le nombre total
    print("Nombre total de posts récupérés :", len(posts))
    print()

    # 3) Afficher un aperçu des 5 premiers
    afficher_resume_posts(posts, n=5)
