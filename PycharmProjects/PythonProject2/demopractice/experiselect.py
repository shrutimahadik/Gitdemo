import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
drop=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
drop.select_by_value("Male")









time.sleep(200)
