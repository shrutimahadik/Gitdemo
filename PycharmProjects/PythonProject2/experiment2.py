from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service=Service("C:\\Users\GNESH\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
#driver=webdriver.Chrome(service=service)

#driver=webdriver.Firefox()
driver=webdriver.


driver.get("https://chatgpt.com/c/6a4289c2-9c8c-83e8-88c2-cb17e588780f")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

