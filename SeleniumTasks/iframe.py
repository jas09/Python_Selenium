import time
#Need to work on it - failing
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
#chrome_options.add_argument("--ignore-certificate-errors") #if any certificate errors
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"//a[@href='consulting']").click()
actualText = driver.find_element(By.TAG_NAME,"h1").text
print(actualText)
assert "JOB SUPPORT" == actualText

element = driver.find_element(By.CLASS_NAME,"dropdown-toggle")
print(element.is_displayed(),element.location,element.size)

driver.execute_script("window.scrollBy(0,1390)")
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CLASS_NAME,"dropdown-toggle")).perform()
driver.get_screenshot_as_file("1.png")
#moreOptions = driver.find_element(By.LINK_TEXT,"contact-us")
#print(moreOptions)
#name = driver.find_element(By.LINK_TEXT,"contact-us")
#print(name)
#name.click()
#action.click(driver.find_element(By.LINK_TEXT,"contact-us"))
#action.move_to_element(driver.find_element(By.LINK_TEXT,"contact-us")).click().perform()
#result = driver.find_element(By.XPATH,"//div[@class='info-inner']/h2").text
#assert "Contact Info" == result
time.sleep(5)