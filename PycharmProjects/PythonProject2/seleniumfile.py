import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



service_obj=(Service("C:\\Users\\GNESH\\Downloads\\chromedriver-win64 (1)\\chromedriver.exe"))
driver=webdriver.Chrome(service_obj)


#driver = webdriver.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)






time.sleep(20)
