import pathlib
import pytest

from selenium import webdriver

PATH_TO_PROJECT = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course")
BASE_URL: str = "http://localhost:8000/dz.html"

@pytest.fixture(autouse=True)
def driver_init():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def frame_number(request):
    return request.param

@pytest.fixture
def parameters(request):
    return request.param
