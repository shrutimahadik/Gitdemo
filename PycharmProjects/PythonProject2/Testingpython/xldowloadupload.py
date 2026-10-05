from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

file_path = "C:\\Users\\GNESH\\Downloads\\download.xlsx"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()

file_inputexample = driver.find_element(By.CSS_SELECTOR, "#fileinput")
file_inputexample.send_keys(file_path)
fruit_name="Apple"

wait = WebDriverWait(driver, 15)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.presence_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)

pricecolumn=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
#Xpath made as went to parent class-div,again parent class div from that parent class to immidiate locator
actualprice=driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+pricecolumn+"-undefined']").text
print(actualprice)