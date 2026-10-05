import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(13)
action=ActionChains(driver)
#action.double_click()
#action.drag_and_drop()
#action.click_and_hold()
#action.context_click()
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()