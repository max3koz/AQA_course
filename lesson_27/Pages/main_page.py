from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.Pages.AbstractPage import AbstractPage

class MainPage(AbstractPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    enter_tracking_number_field_locator: tuple[str,str] = (By.XPATH, "//input[@class=\"track__form-group-input\"]")
    search_button_locator: tuple[str, str] = (By.XPATH, "//input[@value=\"Пошук\"]")
    status_field_value_locator: tuple[str, str] = (By.XPATH, "//div[@class=\"header__status-text\"]")

    @property
    def enter_tracking_number_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.enter_tracking_number_field_locator)

    @property
    def search_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.search_button_locator)

    @property
    def status_field_value(self) -> WebElement:
        return self._wrapped_element.find_element(self.status_field_value_locator)

    def enter_tracking_number(self, tracking_number):
        input_field = self._wrapped_element.wait_for_visible(self.enter_tracking_number_field)
        input_field.clear()
        input_field.send_keys(tracking_number)

    def click_search_button(self):
        self._wrapped_element.wait_to_be_clickable(self.search_button)
        self.search_button.click()

    def get_status(self):
        self._wrapped_element.wait_for_visible(self.status_field_value)
        status_value = self.status_field_value
        return status_value
