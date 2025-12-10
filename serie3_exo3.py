import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def recuperer_posts():
    try:
        response = requests.get(API_URL, timeout=5)
    except requests.exceptions.RequestException:
        return []
    if response.status_code != 200:
        return []
    try:
        data = response.json()
    except ValueError:
        return []
    if not isinstance(data, list):
        return []
    return data


def calculer_stats_par_user(posts):
    stats_par_user = {}
    for post in posts:
        user_id = post.get("userId")
        titre = post.get("title", "")
        if user_id not in stats_par_user:
            stats_par_user[user_id] = {
                "nb_posts": 0,
                "total_longueur_titre": 0
            }
        stats_par_user[user_id]["nb_posts"] += 1
        stats_par_user[user_id]["total_longueur_titre"] += len(titre)
    for user_id, stats in stats_par_user.items():
        nb = stats["nb_posts"]
        total_len = stats["total_longueur_titre"]
        stats["longueur_moyenne_titre"] = total_len / nb if nb > 0 else 0.0
        del stats["total_longueur_titre"]
    return stats_par_user


def afficher_top_users(stats_par_user, top_n=3):
    users_tries = sorted(
        stats_par_user.items(),
        key=lambda item: item[1]["nb_posts"],
        reverse=True
    )
    for user_id, stats in users_tries[:top_n]:
        nb = stats["nb_posts"]
        moy = stats["longueur_moyenne_titre"]
        print(f"User {user_id} : {nb} posts (longueur moyenne titre : {moy:.1f})")


if __name__ == "__main__":
    posts = recuperer_posts()
    print("Nombre total de posts récupérés :", len(posts))
    print()
    stats_par_user = calculer_stats_par_user(posts)
    afficher_top_users(stats_par_user, top_n=3)
