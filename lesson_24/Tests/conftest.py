import json
import logging
import os
from time import strftime, localtime, sleep

import pytest
import requests

from assertpy import assert_that
from logging import config
from requests import Response, Session
from requests.auth import HTTPBasicAuth

BASE_URL: str = "http://127.0.0.1:8080"

auth = HTTPBasicAuth('test_user', 'test_pass')

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    if "test_search.log" in os.listdir("./"):
        os.rename("./test_search.log",
                  f"./test_search_{strftime('%d-%m-%Y_%H:%M:%S', localtime())}.log")
    config_file = "./logging_config.json"
    with open(config_file) as file:
        desired_configuration = json.load(file)
    logging.config.dictConfig(desired_configuration)
    sleep(1)

@pytest.fixture()
def api_url(request):
    return BASE_URL + request.param

@pytest.fixture
def expected_gty_cars(request):
    return request.param

@pytest.fixture
def sorted_by(request):
    return request.param

@pytest.fixture
def expected_car_list(request):
    return request.param

@pytest.fixture(scope="session", autouse=True)
def authorization() -> Session:
    response: Response = requests.post(f"{BASE_URL}/auth", auth=auth)
    assert_that(response.status_code).is_equal_to(200)
    access_token: str = response.json().get("access_token")
    current_session = Session()
    current_session.headers.update({'Authorization': 'Bearer ' + access_token})
    yield current_session
