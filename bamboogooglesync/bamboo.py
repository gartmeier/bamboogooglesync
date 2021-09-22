from requests import Session


class BambooSession(Session):
    def __init__(self, subdomain, api_key) -> None:
        super().__init__()
        self.auth = (api_key, "x")
        self.base = f"https://api.bamboohr.com/api/gateway.php/{subdomain}/v1"
        self.headers = {"Accept": "application/json"}

    def request(self, method, url, **kwargs) -> dict:
        response = super().request(method, self.base + url, **kwargs)
        return response.json()
