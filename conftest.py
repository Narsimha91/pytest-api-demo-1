import time
import os
import datetime
import shutil
import pytest

from core import config
from core.logger import get_logger
from api.api_client import APIClient
from api.endpoints import EndpointBuilder
from api.github_repo import GithubAPI


@pytest.fixture(autouse=True)
def execution_time(test_logger, request):
    start = time.perf_counter()
    test_logger.info("Running Test case: %s", request.node.name)
    yield
    test_logger.info("Execution time of %s is: %.2f seconds"
                     , request.node.name, time.perf_counter() - start)


# hooks
def pytest_configure():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    with open("logs/api_automation.log", "w") as f:
        pass


def pytest_addoption(parser):
    parser.addoption(
        "--cleanup",
        action="store_true",
        help="Delete test repository after execution"
    )

    parser.addoption(
        "--env",
        action="store",
        help="Select test environment",
        default="testing"
    )


def pytest_sessionstart(session):
    session.start_time = time.perf_counter()

    print("=" * 60)
    print("GitHub API Automation")
    print(f"Started : {session.start_time}")
    print("=" * 60)

    if not os.getenv("GITHUB_API_TOKEN"):
        pytest.exit(
            "GITHUB_API_TOKEN environment variable is missing.",
            returncode=1
        )


def pytest_sessionfinish(session):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.make_archive(
        f"archives/logs_{timestamp}",
        "zip",
        "logs"
    )

    duration = time.perf_counter() - session.start_time
    print("=" * 60)
    print(f"End of Testing, Total Execution time: {duration:.2f} seconds")
    print("=" * 60)



@pytest.fixture
def get_options(request):
    return {
        "cleanup": request.config.getoption("--cleanup"),
        "env": request.config.getoption("--env")
    }

@pytest.fixture(scope="session")
def test_config():
    return config

@pytest.fixture(scope="session")
def test_logger():
    return get_logger("api_automation")


@pytest.fixture(scope="session")
def api_client(test_config):
    return APIClient(
        base_url = test_config.BASE_URL,
        token= test_config.GITHUB_API_TOKEN
        )

@pytest.fixture(scope="session")
def endpoints():
    return EndpointBuilder()

@pytest.fixture(scope="session")
def github_repo(api_client, endpoints):
    return GithubAPI(api_client, endpoints)


@pytest.fixture(scope="session")
def create_repo(github_repo, test_config):
    payload = {
        "name": test_config.REPOSITORY,
        "description": "Create an github repository through API",
        "auto_init": True,
        "private": False
    }
    return github_repo.create_repo(payload)


@pytest.fixture(scope="session")
def github_user(api_client, test_config):

    response = api_client.request("GET", test_config.END_POINTS['user'])
    assert response.status_code == 200
    return response.json()['login']



