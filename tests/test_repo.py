import pytest

# @pytest.mark.xfail(sys.platform == "win32", reason="Runs only on Windows")
# @pytest.mark.skip("Repo Already Created")
# @pytest.mark.skipif(sys.platform == "win32", reason="Runs only on Windows")
@pytest.mark.create_repo
@pytest.mark.fun_e2e_test
def test_create_repo(create_repo):
    if create_repo.status_code == 422:
        # pytest.fail(reason="Repository Exists..")
        pytest.skip(reason="Repository Exists..")
    assert create_repo.status_code == 201


@pytest.mark.read_repo
@pytest.mark.fun_e2e_test
def test_get_repo(github_repo, test_config):
    response = github_repo.get_repo(
        test_config.END_POINTS['username'],
        test_config.REPOSITORY
        )
    assert response.status_code == 200


@pytest.mark.update_repo
@pytest.mark.fun_e2e_test
def test_update_repo(github_repo, test_config, github_user):
    payload = {
        "name": test_config.REPOSITORY,
        "description": "Updated repository through API"
    }
    response = github_repo.update_repo(
        github_user,
        test_config.REPOSITORY,
        payload
    )
    assert response.status_code == 200


@pytest.mark.remove_repo
@pytest.mark.fun_e2e_test
def test_remove_repo(github_repo, github_user, test_config, get_options):
    if get_options['env'] == "production":
        pytest.skip("Repository cant be deleted in Production server")

    response = github_repo.remove_repo(
        github_user,
        test_config.REPOSITORY
    )

    assert response.status_code == 204














