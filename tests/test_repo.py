import pytest
from core.config import END_POINTS



def test_create_repo(github_user, api_request):
    
    # pytest.skip("Repo already created")

    payload = {
        "name": "pytest-api-demo-2",
        "description": "Create an repo using pytest automation.",
        "private": False
    }
   
    response = api_request('POST', END_POINTS["repos"], json=payload)
    assert response.status_code == 201


def test_read_repo(github_user, api_request):
    endpoint = END_POINTS["repo"].format(owner=github_user, repo="pytest-api-demo-1")

    response = api_request("GET", endpoint)
    assert response.status_code == 200


def test_update_repo(github_user, api_request):

    payload = {  
        "name": "pytest-api-demo-2",
        "description": "updated an repo using pytest automation.",
        "private": False
    }
    endpoint = END_POINTS["repo"].format(owner=github_user, repo="pytest-api-demo-2")

    response = api_request("PATCH", endpoint, json=payload)
    assert response.status_code == 200


def test_delete_repo(github_user, api_request):

    pytest.skip("skipping repo deletion")

    endpoint = END_POINTS["repo"].format(owner=github_user, repo="pytest-api-demo-1")

    response = api_request("DELETE", endpoint)
    assert response.status_code == 204



    


















# @pytest.mark.parametrize(
#     "endpoint, expected",
#     [
#         ("/user", 200),
#         ("/users/Narsimha91", 200),
#         ("/invalid", 404)
#     ]
# )
# def test_endpoints(api_request, endpoint, expected):

#     response = api_request("GET", endpoint)
#     assert response.status_code == expected



# def test_get_user(api_request, github_user):
    # print(github_user)

    # response = api_request("GET", f"/users/{github_user}")

    # assert response.status_code == 200 or github_user == "invalid_user"


