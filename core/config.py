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
        "actions": r"/repos/{owner}/{repo}/actions/workflows",
        "get_cmt": r"/repos/{owner}/{repo}/git/ref/heads/main",
        "refs":    r"/repos/{owner}/{repo}/git/refs",
        "branches": r"/repos/{owner}/{repo}/branches",
        "branch":   r"/repos/{owner}/{repo}/branches/{branch}",
        "rm_branch": r"/repos/{owner}/{repo}/git/refs/heads/{branch}"
    
    }

# /repos/{owner}/{repo}/branches
# /repos/{owner}/{repo}/commits
# /repos/{owner}/{repo}/contents/{path} 
# /repos/{owner}/{repo}/issues
