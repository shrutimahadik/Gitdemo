import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzYyMzU0NDQ4LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
driver.find_element(By.XPATH,"")

#driver.find_element(By.XPATH,"//button[@name='login']").click()
#driver.find_element(By.CSS_SELECTOR,"button[id='loginbutton']").click()

#message=driver.find_element(By.CLASS_NAME,"_9ay7").text
#assert "connected1234" in message
#print(message)


time.sleep(20)