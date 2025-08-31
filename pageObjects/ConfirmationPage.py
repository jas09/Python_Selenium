from openai import timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.Utilities import Utilities


class ConfirmationPage(Utilities):
    def __init__(self,driver):
        super().__init__(driver,timeout=5)
        self.driver = driver
        #self.wait_utils = WaitUtils(driver,timeout=5)
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def location_select(self,countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        self.wait_for_presence(self.country_option)
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):
        success_message = self.driver.find_element(*self.success_message).text
        # success_message = driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in success_message