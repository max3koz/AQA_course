from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.Pages.AbstractPage import AbstractPage

class MainPage(AbstractPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    sign_in_button_locator: tuple[str,str] = (By.XPATH, "//button[@class=\"btn btn-outline-white header_signin\"]")
    registration_button_locator: tuple[str,str] = (By.XPATH,  "//button[contains(text(), \"Registration\")]")
    name_registration_field_locator: tuple[str,str] = (By.XPATH,  "//input[@id=\"signupName\"]")
    lastname_registration_field_locator: tuple[str, str] = (By.XPATH, "//input[@id=\"signupLastName\"]")
    email_registration_field_locator: tuple[str, str] = (By.XPATH, "//input[@id=\"signupEmail\"]")
    password_registration_field_locator: tuple[str, str] = (By.XPATH, "//input[@id=\"signupPassword\"]")
    repeat_password_registration_field_locator: tuple[str, str] = (By.XPATH, "//input[@id=\"signupRepeatPassword\"]")
    register_button_locator: tuple[str,str] = (By.XPATH,  "//button[contains(text(), \"Register\")]")
    alert_message_exist_user_locator: tuple[str,str] = (By.XPATH,  "//p[contains(text(), \"User already exists\")]")

    @property
    def sign_in_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.sign_in_button_locator)

    def click_sign_in_button(self):
        self._wrapped_element.wait_to_be_clickable(self.sign_in_button)
        self.sign_in_button.click()

    @property
    def registration_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.registration_button_locator)

    def click_registration_button(self):
        element = self._driver.find_element(By.XPATH, self.registration_button_locator[1])
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        self._wrapped_element.wait_to_be_clickable(self.registration_button)
        self.registration_button.click()

    @property
    def name_registration_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.name_registration_field_locator)

    def enter_name_in_registration_form(self, name):
        input_field = self._wrapped_element.wait_for_visible(self.name_registration_field)
        input_field.clear()
        input_field.send_keys(name)

    @property
    def lastname_registration_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.lastname_registration_field_locator)

    def enter_lastname_in_registration_form(self, lastname):
        input_field = self._wrapped_element.wait_for_visible(self.lastname_registration_field)
        input_field.clear()
        input_field.send_keys(lastname)

    @property
    def email_registration_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.email_registration_field_locator)

    def enter_email_in_registration_form(self, email):
        input_field = self._wrapped_element.wait_for_visible(self.email_registration_field)
        input_field.clear()
        input_field.send_keys(email)

    @property
    def password_registration_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.password_registration_field_locator)

    def enter_password_in_registration_form(self, password):
        input_field = self._wrapped_element.wait_for_visible(self.password_registration_field)
        input_field.clear()
        input_field.send_keys(password)

    @property
    def repeat_password_registration_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.repeat_password_registration_field_locator)

    def enter_repeat_password_in_registration_form(self, password):
        input_field = self._wrapped_element.wait_for_visible(self.repeat_password_registration_field)
        input_field.clear()
        input_field.send_keys(password)

    @property
    def register_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.register_button_locator)

    def click_register_button(self):
        element = self._driver.find_element(By.XPATH, self.register_button_locator[1])
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        self._wrapped_element.wait_to_be_clickable(self.register_button)
        self.register_button.click()

    @property
    def alert_message_exist_user(self) -> WebElement:
        return self._wrapped_element.find_element(self.alert_message_exist_user_locator)

    def get_alert_message_exist_user_value(self):
        self._wrapped_element.wait_for_visible(self.alert_message_exist_user)
        status_value = self.alert_message_exist_user.is_displayed()
        return status_value
