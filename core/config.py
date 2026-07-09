import os

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

BASE_URL = "https://api.github.com"

TIMEOUT = (5, 30)

END_POINTS = {

        "username": "Narsimha91",
        "user"  :  "/user",
        "repos" :  "/user/repos",
        "repo"  :  r"/repos/{owner}/{repo}",
        "issues":  r"/repos/{owner}/{repo}/issues",
        "pull"  :  r"/repos/{owner}/{repo}/pulls",
        "actions": r"/repos/{owner}/{repo}/actions/workflows"
    }

# /repos/{owner}/{repo}/branches
# /repos/{owner}/{repo}/commits
# /repos/{owner}/{repo}/contents/{path} 
# /repos/{owner}/{repo}/issues
