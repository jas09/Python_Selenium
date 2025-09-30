import pytest
import yaml
from selenium import webdriver
driver = None

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

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)