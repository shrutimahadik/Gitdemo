import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(25)
driver.find_element(By.PARTIAL_LINK_TEXT,"Click Here").click()
windowopened=driver.window_handles
driver.switch_to.window(windowopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowopened[0])
gettext=print(driver.find_element(By.TAG_NAME,"h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text