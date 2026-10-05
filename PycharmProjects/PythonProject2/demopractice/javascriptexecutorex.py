from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window

chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(30)
#driver.execute_script("window.scrollBy(0, 700)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen1.png")