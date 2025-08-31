from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.XPATH,"//div[@class='example']").text)
driver.switch_to.window(windowsOpened[0])
