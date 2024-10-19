from abc import ABC

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractElement(ABC):

    _driver: WebDriver

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def find_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_visible(self, element: WebElement, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of(element)
        )

    def wait_to_be_clickable(self, element: WebElement, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(element)
        )
