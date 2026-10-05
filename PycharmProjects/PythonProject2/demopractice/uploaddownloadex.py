import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

filepath="C:\\Users\\GNESH\\Downloads\\download (8).xlsx"
filename="Apple"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,"downloadButton").click()
time.sleep(5)

fileinput=driver.find_element(By.XPATH,"//input[@type='file']")
fileinput.send_keys(filepath)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[text()='Updated Excel Data Successfully.']")))
