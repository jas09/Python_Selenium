import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name="Azhar"
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()