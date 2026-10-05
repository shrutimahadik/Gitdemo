from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v138.log import clear
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.implicitly_wait(19)
driver.switch_to.frame("moneyiframe")
driver.find_element(By.CSS_SELECTOR,"#query").send_keys("hi there")

driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//h1[text()='TOP STORIES']").text)
assert "TOP STORIES" == driver.find_element(By.XPATH,"//h1[text()='TOP STORIES']").text