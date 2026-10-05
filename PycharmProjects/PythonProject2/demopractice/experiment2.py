import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"name").send_keys("abcd")

driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("abcd@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='btn btn-success']").click()
message=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(message)

assert "Success" in message













time.sleep(200)
