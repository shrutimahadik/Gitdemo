import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
conties=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(conties))
for country in conties:
    if country.text=="India":
        country.click()


assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"






time.sleep(20)