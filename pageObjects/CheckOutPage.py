from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def checkOutButton(self):
        self.driver.find_element(*self.checkout_button).click()
        confirmation = ConfirmationPage(self.driver)
        return confirmation
