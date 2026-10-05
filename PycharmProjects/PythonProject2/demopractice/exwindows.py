from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsopen=driver.window_handles
driver.switch_to.window(windowsopen[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsopen[0])
#assert "Opening a new window" ==driver.find_element(By.TAG_NAME,"h3").text
print(driver.find_element(By.TAG_NAME,"h3").text)


