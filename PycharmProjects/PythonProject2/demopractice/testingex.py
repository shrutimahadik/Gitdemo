import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(39)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
button=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(button))
for buttons in button:
    if buttons.get_attribute("value")=="Option3":
        buttons.click()
        time.sleep(10)
        break

radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value")==" Radio2":
        radiobutton.click()


#assert driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.ID,"displayed-text").click()
assert  driver.find_element(By.CSS_SELECTOR,"#show-textbox").is_displayed()

