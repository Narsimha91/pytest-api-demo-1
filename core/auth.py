from core.config import GITHUB_API_TOKEN

def get_header():
    return {
        "Authorization": f"Bearer {GITHUB_API_TOKEN}"
    }