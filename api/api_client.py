import requests

class APIClient:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.__token = token

        self.session = requests.session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json"
            })


    def request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint

        return self.session.request(method, url, **kwargs)


    #
    # def get(self):
    #     pass


