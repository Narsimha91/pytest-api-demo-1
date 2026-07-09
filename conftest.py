"""Pytest fixtures for API automation."""

import pytest
import os
import time
import shutil
import datetime

from core.logger import get_logger
from core.api_client import send_request
from core.config import END_POINTS


# AutoUse
@pytest.fixture(autouse=True)
def execution_time(test_logger, request):
    """Log test execution automatically."""

    start = time.perf_counter()
    yield    
    test_logger.info("Execution time of %s is: %.2f seconds"
                     , request.node.name, time.perf_counter() - start)


# hooks
def pytest_configure(config):
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

def pytest_addoption(parser):
    parser.addoption(
        "--cleanup",
        action="store_true",
        help="Delete test repository after execution"
        )
    parser.addoption(
        "--env",
        action="store_true",
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
    # shutil.make_archive(
    #     f"archives/logs_{timestamp}",
    #     "zip",
    #     "logs"
    # )

    duration = time.perf_counter() - session.start_time
    print("=" * 60)
    print(f"End of Testing, Total Execution time: {duration:.2f} seconds")
    print("=" * 60)


# Test Fixtures
@pytest.fixture(scope="session")
def test_logger():
    """Create reusable logger."""

    return get_logger("api_automation")


@pytest.fixture(scope="session")
def api_request(test_logger):
    """Provide reusable API request function."""

    def api_call(method, endpoint, **kwargs):
        return send_request(method, endpoint, test_logger, **kwargs)
    return api_call


# @pytest.fixture(scope="session")
# def create_repo(api_request):



@pytest.fixture(scope="session")
def github_user(api_request):
    return api_request("GET", f"/user").json()['login']    

# parameterized fixture
@pytest.fixture(params=["Narsimha91", "invalid_user"])
def username(request):
    return request.param
