import pytest
import yaml
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox", help="browser selection")
    parser.addoption("--url_key", action="store", default="PRACTICE", help="Choose URL key")

#If you are using via config.yaml file
#def load_config():
    #with open("config.yaml","r") as f:
        #return yaml.safe_load(f)
#config = load_config()

#pytest --url_key=PRACTICE
URL_MAP = {"GREENKART": "https://rahulshettyacademy.com/seleniumPractise/#/",
           "UPLOAD_DOWNLOAD": "https://rahulshettyacademy.com/upload-download-test/index.html",
           "CLIENT": "https://rahulshettyacademy.com/client/#/auth/login",
           "PRACTICE": "https://rahulshettyacademy.com/AutomationPractice/",
           "MOBILE_SHOP": "https://rahulshettyacademy.com/loginpagePractise/"}

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    url_key = request.config.getoption("url_key")
    base_url = URL_MAP.get(url_key)
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)
    yield driver
    driver.close()