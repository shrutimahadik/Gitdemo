import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
phone=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for mobile in phone:
    if mobile.text=="Blackberry":
        #driver.find_element(By.XPATH,"//a[text()='Blackberry']")
        driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()

        time.sleep(15)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
message=print(driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)
time.sleep(15)
assert "Success! Thank you!" in message
driver.quit()


