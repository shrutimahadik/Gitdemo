from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(12)
driver.get("https://www.saucedemo.com/inventory.html")
