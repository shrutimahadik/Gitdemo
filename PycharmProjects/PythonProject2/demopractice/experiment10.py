from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
source=driver.find_element(By.CSS_SELECTOR,"#column-a")
target=driver.find_element(By.CSS_SELECTOR,"#column-b")
actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()
