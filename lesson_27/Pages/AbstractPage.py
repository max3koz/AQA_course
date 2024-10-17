from abc import ABC
from selenium.webdriver.ie.webdriver import WebDriver

from lesson_27.Web_elements.abstract_element import AbstractElement


class AbstractPage(ABC):
    _driver: WebDriver
    _wrapped_element: AbstractElement

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wrapped_element = AbstractElement(self._driver)
