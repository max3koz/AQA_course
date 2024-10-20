import pathlib
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

PATH_TO_PROJECT = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course")

@pytest.fixture(scope="module")
def create_driver():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

    yield driver

    driver.quit()
