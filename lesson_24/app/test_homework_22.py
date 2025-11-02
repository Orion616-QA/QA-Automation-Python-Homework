import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASIC_URL = 'http://127.0.0.1:8080/'
AUTH = HTTPBasicAuth("test_user", "test_pass")

"""Set up logging into console and file"""
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""Fixstures for received access token and put it into auth header"""
@pytest.fixture(scope="class")
def auth_token():
    r = requests.post(BASIC_URL + "auth", auth=AUTH)
    r.raise_for_status()
    token = r.json().get("access_token")
    return token


@pytest.fixture(scope="class")
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}

"""Parametrize settings for tests"""
@pytest.mark.parametrize("sort_by", ["brand", "year", "price", None])
@pytest.mark.parametrize("limit", [None, 1, 3, 5])
class TestCarsAPI:

    def test_get_cars_sorted_and_limited(self, auth_headers, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Request: GET /cars, sort_by={sort_by}, limit={limit}")

        response = requests.get(BASIC_URL + "cars", headers=auth_headers, params=params)
        assert response.status_code == 200, logger.error(f"Expect status 200, but got {response.status_code}")

        data = response.json()
        logger.info(f"Received {len(data)} cars")

        if limit:
            assert len(data) <= limit, logger.error(f"Count of elements greater then {limit}")
            logger.info(f"Check 'limit = {limit}' success")

        if sort_by:
            sorted_values = sorted(data, key=lambda x: x.get(sort_by, 0))
            assert data == sorted_values, logger.error(f"Sorting by {sort_by} invalid")
            logger.info(f"Check sorting by {sort_by} success")
        logger.info("---------------------------------------")