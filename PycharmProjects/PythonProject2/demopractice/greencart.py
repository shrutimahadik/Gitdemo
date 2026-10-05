import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(4)
products=driver.find_elements(By.XPATH,"//div[@class='product']")
print(len(products))
for product in products:
    product.find_element(By.XPATH,"//div[@class='product']").click()