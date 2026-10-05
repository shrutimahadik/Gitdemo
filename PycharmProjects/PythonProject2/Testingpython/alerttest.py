import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name="shruti"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("shruti")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert=driver.switch_to.alert
alertText=alert.text
print(alertText)
time.sleep(20)
assert name in alertText
#alert.accept()
alert.dismiss()

time.sleep(20)