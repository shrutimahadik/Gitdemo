from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v138.log import clear
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chrome_options=webdriver.ChromeOptions()
#if your site restricted use below
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")


service_obj = Service("C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options= chrome_options)
driver.get("https://stackoverflow.com/questions/12698843/how-do-i-pass-options-to-the-selenium-chrome-driver-using-python")
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(60)