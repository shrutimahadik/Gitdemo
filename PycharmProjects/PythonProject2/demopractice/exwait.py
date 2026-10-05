import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input[class='search-keyword']").send_keys("ber")
time.sleep(2)
veggi=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(veggi))

for veggies in veggi:
    veggies.find_element(By.XPATH,"div/button").click()

time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(2)
#dropper=Select(driver.find_element(By.XPATH,"//select[@fdprocessedid='u044q5']"))
dropper = Select(driver.find_element(By.TAG_NAME, "select"))
dropper.select_by_value("India")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='chkAgree']").click()

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)



