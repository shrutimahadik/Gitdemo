import document
from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,700);")
driver.get_screenshot_as_file("ex.png")
