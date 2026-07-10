
class GithubAPI:
    def __init__(self, api_client, endpoint):
        self.api_client = api_client
        self.endpoint = endpoint

    def create_repo(self, payload):
        return self.api_client.request("POST",
                    self.endpoint.repos, json=payload)

    def get_repo(self, owner, repo):
        url = self.endpoint.get_repo(owner, repo)
        return self.api_client.request("GET", url)

    def update_repo(self, owner, repo, payload):
        url = self.endpoint.get_repo(owner, repo)
        return self.api_client.request("POST", url, json=payload)

    def remove_repo(self, owner, repo):
        url = self.endpoint.get_repo(owner, repo)
        return self.api_client.request("DELETE", url)

    def create_branch(self):
        pass
    def get_branch(self):
        pass
    def remove_branch(self):
        pass





