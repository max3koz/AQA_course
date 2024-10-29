
import allure
import logging
import pytest

from assertpy import assert_that
from logging import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from lesson_26.Tests.conftest import PATH_TO_PROJECT

logging.config.fileConfig(f"{PATH_TO_PROJECT}/logging_config.ini")
logging.getLogger('sampleLogger')

@allure.feature("test_frames_with_valid_data")
class TestSuiteApplication:
    @pytest.mark.parametrize("frame_number, parameters", [("frame1", ("input1", "Frame1_Secret")),
                                                          ("frame2", ("input2", "Frame2_Secret"))],
                             indirect=True)
    def test_frames_with_valid_data(self, driver_init, frame_number, parameters):
        logging.info(f"The testcase with valid data for frame \"{frame_number}\".")
        logging.info(f"Reconnect to frame \"{parameters[0]}\".")
        driver_init.switch_to.frame(driver_init.find_element(By.ID, frame_number))

        logging.info(f"Find text field and enter valid secret text \"{parameters[0]}\" to the field.")
        input_field = driver_init.find_element(By.ID, parameters[0])
        input_field.clear()
        input_field.send_keys(parameters[1])

        logging.info("Enter the button \"Перевiрити\"")
        verify_button = driver_init.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()

        logging.info("Waiting while the dialog window will be open")
        WebDriverWait(driver_init, 10).until(EC.alert_is_present())

        logging.info("Verify that the verification was done.")
        alert = Alert(driver_init)
        alert_text = alert.text
        expected_text = "Верифікація пройшла успішно!"
        assert_that(alert_text).is_equal_to(expected_text)

        logging.info("Close the dialog window and go out from the frame")
        alert.accept()
        driver_init.switch_to.default_content()

    @allure.feature("test_frames_with_invalid_data")
    @pytest.mark.parametrize("frame_number, parameters", [("frame1", ("input1", "Frame1_Secret_Invalid")),
                                                          ("frame2", ("input2", "Frame2_Secret_Invalid"))],
                             indirect=True)
    def test_frames_with_invalid_data(self, driver_init, frame_number, parameters):
        logging.info(f"The testcase with invalid data for frame \"{frame_number}\".")
        logging.info(f"Reconnect to frame \"{parameters[0]}\".")
        driver_init.switch_to.frame(driver_init.find_element(By.ID, frame_number))

        logging.info(f"Find text field and enter invalid secret text \"{parameters[0]}\" to the field.")
        input_field = driver_init.find_element(By.ID, parameters[0])
        input_field.clear()
        input_field.send_keys(parameters[1])

        logging.info("Enter the button \"Перевiрити\"")
        verify_button = driver_init.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()

        logging.info("Waiting while the dialog window will be open")
        WebDriverWait(driver_init, 10).until(EC.alert_is_present())

        logging.info("Verify that the verification was done.")
        alert = Alert(driver_init)
        alert_text = alert.text
        expected_text = "Введено неправильний текст!"
        assert_that(alert_text).is_equal_to(expected_text)

        logging.info("Close the dialog window and go out from the frame")
        alert.accept()
        driver_init.switch_to.default_content()

    @allure.feature("test_frames_with_empty_data")
    @pytest.mark.parametrize("frame_number, parameters", [("frame1", ("input1", "")),
                                                          ("frame2", ("input2", ""))],
                             indirect=True)
    def test_frames_with_empty_data(self, driver_init, frame_number, parameters):
        logging.info(f"The testcase with empty data field for frame \"{frame_number}\".")
        logging.info(f"Reconnect to frame \"{parameters[0]}\".")
        driver_init.switch_to.frame(driver_init.find_element(By.ID, frame_number))

        logging.info(f"Find text field, crear it and enter empty string to the field.")
        input_field = driver_init.find_element(By.ID, parameters[0])
        input_field.clear()
        input_field.send_keys(parameters[1])

        logging.info("Enter the button \"Перевiрити\"")
        verify_button = driver_init.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()

        logging.info("Waiting while the dialog window will be open")
        WebDriverWait(driver_init, 10).until(EC.alert_is_present())

        logging.info("Verify that the verification was done.")
        alert = Alert(driver_init)
        alert_text = alert.text
        expected_text = "Введено неправильний текст!"
        assert_that(alert_text).is_equal_to(expected_text)

        logging.info("Close the dialog window and go out from the frame")
        alert.accept()
        driver_init.switch_to.default_content()
