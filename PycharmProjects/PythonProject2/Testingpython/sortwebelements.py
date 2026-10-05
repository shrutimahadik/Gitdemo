import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(60)
veggies=[]
#click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veggi names=browsersortedveggi list
broswerveggi=driver.find_elements(By.XPATH,"//tr/td[1]")
for elements in broswerveggi:
    veggies.append(elements.text)

print(veggies)
originalbrowsersorted=veggies.copy()
veggies.sort()
assert veggies==originalbrowsersorted



#sort this brosersortedveggilist=newsortedlist
#veggilist==newsortedlist
