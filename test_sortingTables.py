import pytest
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    browserSortedVeggies = []
    driver = browserInstance
    driver.find_element(By.XPATH, "//a[text()='Top Deals']").click()
    offersWindow = driver.window_handles
    driver.switch_to.window(offersWindow[1])
    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collect all veggie names --> VeggieList
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for element in veggieWebElements:
        browserSortedVeggies.append(element.text)

    originalBrowserSortedList = browserSortedVeggies.copy()
    # sort this VeggieList ---> newSortedList
    browserSortedVeggies.sort()
    # VeggieList == newSortedList
    assert browserSortedVeggies == originalBrowserSortedList