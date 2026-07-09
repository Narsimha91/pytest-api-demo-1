"""API Client module to send HTTP requests"""

import requests
from core.config import BASE_URL, TIMEOUT
from core.auth import get_header


def send_request(method, endpoint, logger, **kwargs):
    """Send HTTP request and return response."""

    url = f"{BASE_URL}{endpoint}"
    print("URL:    ", url)

    try:
        logger.info("Request: %s %s ", method, url)

        response = requests.request(
                method=method,
                url=url,
                headers=get_header(),
                timeout=TIMEOUT,
                **kwargs
            )
        logger.info("Response of %s: %s", url, response.status_code)
        return response
    except requests.exceptions.HTTPError as error:
        logger.error("HTTP error: %s", error)
        raise
    except requests.exceptions.RequestException as error:
        logger.error("API request failed: %s", error)
        raise
    except Exception as error:
        logger.exception("Request failed for URL: %s. Error: %s", url, error)
        raise
