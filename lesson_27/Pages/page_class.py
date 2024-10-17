from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id=\"en\"]"))
        )
        input_field.clear()
        input_field.send_keys(tracking_number)

    def click_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=\"np-number-input-desktop-btn-search-en\"]"))
        )
        search_button.click()

    def get_status(self):
        (WebDriverWait(self.driver, 10).
         until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"chat\"]/header/div[2]/div[2]"))))
        status = self.driver.find_element(By.XPATH, "//*[@id=\"chat\"]/header/div[2]/div[2]/div[2]").text
        return  status