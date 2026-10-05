import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(20)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count>0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)

totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum==totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("Shruti")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)




