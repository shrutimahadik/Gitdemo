import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name= " shruti"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.NAME,"enter-name").send_keys("shruti")
driver.find_element(By.ID,"alertbtn").click()
alertmsg=driver.switch_to.alert
savetext=alertmsg.text
print(savetext)
assert name in savetext
#alertmsg.accept()
alertmsg.dismiss()





time.sleep(2)
