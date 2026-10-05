import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
#driver.find_element(By.NAME,"firstname").send_keys("hi")
driver.find_element(By.NAME,"lastname").send_keys("hm")
driver.find_element(By.NAME,"lastname").clear()
driver.find_element(By.ID,"sex").click()
driver.find_element(By.XPATH,"//button[@name='websubmit']").click()



time.sleep(200)