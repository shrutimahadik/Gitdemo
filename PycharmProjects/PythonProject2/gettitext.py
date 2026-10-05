import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()

driver.find_element(By).click()
#driver.find_element(By.XPATH,"//button[@name='websubmit']").click()



time.sleep(200)