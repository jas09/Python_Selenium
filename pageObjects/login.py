from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signInButton = (By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signInButton).click()
        shop_page = ShopPage(self.driver)
        return shop_page
