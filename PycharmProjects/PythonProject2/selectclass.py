import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()

day=Select(driver.find_element(By.ID,"day"))
day.select_by_visible_text("21")
month=Select(driver.find_element(By.NAME,"birthday_month"))
month.select_by_index(3)
Year=Select(driver.find_element(By.NAME,"birthday_year"))
Year.select_by_value("1997")
#driver.find_element(By.XPATH,"//button[@name='websubmit']").click()



time.sleep(200)