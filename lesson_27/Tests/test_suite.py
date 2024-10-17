from assertpy import assert_that

from lesson_27.Pages.main_page import MainPage

class TestLogIn:
    main_page: MainPage

    def test_that_package_received(self, create_driver):
        tracking_number = "59001238914598"
        self.main_page = MainPage(create_driver)
        self.main_page.enter_tracking_number(tracking_number)
        self.main_page.click_search_button()
        status_result_value = self.main_page.get_status()
        assert_that(status_result_value.text).is_equal_to("Отримана")
