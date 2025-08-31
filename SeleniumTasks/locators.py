import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Azhar")
driver.find_element(By.CSS_SELECTOR,"input[value='option1']").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(" 1")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# //tagname[@attribute='value']
# tagname[attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success!" in message




time.sleep(2)