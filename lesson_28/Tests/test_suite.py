from time import sleep

from assertpy import assert_that

from lesson_28.Pages.main_page import MainPage

class TestLogIn:
    main_page: MainPage

    def test_check_registration_with_exist_user_function(self, create_driver):
        self.main_page = MainPage(create_driver)

        self.main_page.click_sign_in_button()

        self.main_page.click_registration_button()

        self.main_page.enter_name_in_registration_form("TestT")
        self.main_page.enter_lastname_in_registration_form("TestT")
        self.main_page.enter_email_in_registration_form("test1@test1.com")
        self.main_page.enter_password_in_registration_form("TestTest1")
        self.main_page.enter_repeat_password_in_registration_form("TestTest1")
        self.main_page.click_register_button()

        assert_that(self.main_page.get_alert_message_exist_user_value()).is_equal_to(True)
