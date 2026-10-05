import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":

        checkbox.click()
        assert checkbox.is_selected()
        break

radiobutton=driver.find_elements(By.CSS_SELECTOR,".radioButton")
print(len(radiobutton))
for radiobutton in radiobutton:
    if radiobutton.get_attribute("value")=="radio3":
        radiobutton.click()
        
assert radiobutton.is_selected()




#radiobutton=driver.find_elements(By.CSS_SELECTOR,".radioButton")
#print(len(radiobutton))
#radiobutton[1].click()
#assert radiobutton[1].is_selected()




time.sleep(20)
