from requests import get
from requests import post
from requests.auth import HTTPBasicAuth
from variables.credentials import *


class Main:
    """Основной функционал"""

    headers = None
    base = "https://oauth.reddit.com"

    def set_authenticated_headers(self):
        """Установка аутентифицированных заголовков"""
        auth = HTTPBasicAuth(client_id, secret_token)
        data = {"grant_type": "password", "username": username, "password": password}
        headers = {"User-Agent": "MyBot/0.0.2"}
        access_token = post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data=data,
            headers=headers,
        ).json()["access_token"]
        headers |= {"Authorization": f"bearer {access_token}"}
        self.headers = headers

    def get_subreddit_comments(self, subreddit, limit=2):
        """Получение комментариев сабреддита"""
        self.headers is None and self.set_authenticated_headers()
        return get(
            f"{self.base}/r/{subreddit}/new",
            headers=self.headers,
            params={"limit": limit},
        ).json()

    def post_comment(self, text, thing_id):
        """Отправка комментария"""
        self.headers is None and self.set_authenticated_headers()
        params = {
            "api_type": "json",
            "return_rtjson": True,
            "text": text,
            "thing_id": thing_id,
        }
        return post(
            f"{self.base}/api/comment", headers=self.headers, params=params
        ).json()

    def delete_comment(self, thing_id):
        """Удаление комментария"""
        self.headers is None and self.set_authenticated_headers()
        request = post(
            f"{self.base}/api/del", headers=self.headers, params={"id": thing_id}
        )
        assert (
            request.status_code == 200
        ), f"Wrong status code received during comment deletion: {request.status_code}."
