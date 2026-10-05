from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions=ActionChains(driver)
actions.context_click(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()




