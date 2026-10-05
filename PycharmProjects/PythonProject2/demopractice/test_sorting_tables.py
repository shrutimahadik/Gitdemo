

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_sorting_table(browserinstance):
    driver=browserinstance



    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    veggies = []
    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all veggi names=browsersortedveggi list
    broswerveggi = driver.find_elements(By.XPATH, "//tr/td[1]")
    for elements in broswerveggi:
        veggies.append(elements.text)

    print(veggies)
    originalbrowsersorted = veggies.copy()
    veggies.sort()
    assert veggies == originalbrowsersorted

    # sort this brosersortedveggilist=newsortedlist
    # veggilist==newsortedlist










