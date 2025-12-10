import requests


class JsonPlaceholderClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")

    def _get(self, endpoint):
        url = self.base_url + "/" + endpoint.lstrip("/")
        try:
            response = requests.get(url, timeout=5)
        except requests.exceptions.RequestException as e:
            print("Erreur réseau :", e)
            return None

        if response.status_code != 200:
            print("Erreur HTTP :", response.status_code)
            return None

        try:
            return response.json()
        except ValueError:
            print("Réponse non valide (JSON attendu)")
            return None

    def get_posts(self):
        data = self._get("/posts")
        if isinstance(data, list):
            return data
        return []

    def get_post(self, post_id):
        data = self._get(f"/posts/{post_id}")
        if isinstance(data, dict):
            return data
        return None


if __name__ == "__main__":
    client = JsonPlaceholderClient()

    posts = client.get_posts()
    print("Nombre total de posts :", len(posts))

    post_1 = client.get_post(1)
    if post_1 is not None:
        print("Titre du post 1 :", post_1.get("title"))
        print("Contenu du post 1 :", post_1.get("body"))
    else:
        print("Impossible de récupérer le post 1")
