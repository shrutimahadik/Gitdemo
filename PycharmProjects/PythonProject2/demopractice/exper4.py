import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/#/auth/login/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("abc@com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("12345678")





time.sleep(300)