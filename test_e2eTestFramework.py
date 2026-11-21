import json
import pytest

from pageObjects.login import LoginPage

test_data_path = 'Data/test_e2eTestFramework.json'
try:
    with open(test_data_path) as f:
        test_data = json.load(f)
        test_dataList = test_data["data"]
except Exception as e:
    print(f"Test data file not found: {test_data_path}")



@pytest.mark.parametrize("test_dataList_items",test_dataList)
def test_e2e_Mobile_Shop(browserInstance,test_dataList_items):
    driver = browserInstance
    loginPage = LoginPage(driver)
    shop_page = loginPage.login(test_dataList_items["userEmail"],test_dataList_items["userPassword"])
    shop_page.add_product_to_cart(test_dataList_items["productName"])
    checkout = shop_page.goToCart()
    confirmation = checkout.checkOutButton()
    confirmation.location_select(test_dataList_items["countryName"])
    confirmation.validate_order()
