from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\Users\\GNESH\\Downloads\\chromedriver-win64 (1)\\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

time.sleep(20)
driver.quit()
