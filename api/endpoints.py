from core import config

class EndpointBuilder:
    def __init__(self):
        self.endpoint = ''

        self.github_user = config.END_POINTS["username"]
        self.repos = config.END_POINTS["repos"]
        self.repo = config.END_POINTS["repo"]
        self.get_commit = config.END_POINTS["get_cmt"]
        self.refs = config.END_POINTS["refs"]
        self.branches = config.END_POINTS["branches"]
        self.branch = config.END_POINTS["branch"]
        self.rm_branch = config.END_POINTS["rm_branch"]


    def get_repo(self, owner, repo):
        return self.repo.format(owner=owner, repo=repo)

    def get_commit(self, owner, repo):
        return self.get_commit.format(owner=owner, repo=repo)

    def get_refs(self, owner, repo):
        return self.refs.format(owner=owner, repo=repo)

    def get_branches(self, owner, repo):
        return self.branches.format(owner=owner, repo=repo)

    def get_branch(self, owner, repo):
        return self.branch.format(owner=owner, repo=repo)

    def remove_branch(self, owner, repo, branch):
        return self.rm_branch.format(owner=owner, repo=repo, branch=branch)



