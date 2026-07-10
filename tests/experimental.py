# # ======================= BRANCH ===================================================
# @pytest.mark.get_sha
# @pytest.mark.test_branch
# @pytest.mark.functional_test
# def test_get_last_commit(github_user, api_request):
#     endpoint = END_POINTS["get_cmt"].format(owner=github_user, repo=REPOSITORY)
#     print("END POINT: ", endpoint)
#     response = api_request("GET", endpoint)
#     assert response.status_code == 200
#     global SHA
#     SHA = response.json()['object']['sha']
#
#
# @pytest.mark.test_branch
# @pytest.mark.functional_test
# def test_create_branch(github_user, api_request):
#     global SHA
#     payload = {
#         "ref": f"refs/heads/{BRANCH}",
#         "sha": SHA
#     }
#     endpoint = END_POINTS["refs"].format(owner=github_user, repo=REPOSITORY)
#
#     response = api_request("POST", endpoint, json=payload)
#     assert response.status_code == 201
#
#
# @pytest.mark.get_branch
# @pytest.mark.test_branch
# @pytest.mark.functional_test
# def test_get_branch(github_user, api_request):
#     endpoint = END_POINTS["branch"].format(owner=github_user, repo=REPOSITORY,
#                                            branch=BRANCH)
#
#     response = api_request("GET", endpoint)
#     assert response.status_code == 200
#
#
# @pytest.mark.test_branch
# @pytest.mark.delete_branch
# @pytest.mark.functional_test
# def test_remove_branch(github_user, api_request, get_options, request):
#     markers = [m.name for m in request.node.iter_markers()]
#
#     if get_options['cleanup'] or "delete_branch" in markers:
#         endpoint = END_POINTS["rm_branch"].format(owner=github_user, repo=REPOSITORY,
#                                                   branch=BRANCH)
#
#         response = api_request("DELETE", endpoint)
#         assert response.status_code == 204
#     else:
#         pytest.skip("Missing repo cleanup option, so skipping branch deletion.")
