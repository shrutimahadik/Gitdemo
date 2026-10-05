import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Testingpython.uicontrils import checkbox

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
lists=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(lists))
for list in lists:
    if list.get_attribute("value")=="option2":

        list.click()
        assert checkbox.is_selected()



radiobuttons=driver.find_elements(By.XPATH,"//input[@class='radioButton']")
print(len(radiobuttons))
for radio in radiobuttons:
    if radio.get_attribute("value")=="radio1":
        radio.click()

time.sleep(2)

dropdowns=Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdowns.select_by_value("option1")




time.sleep(2)