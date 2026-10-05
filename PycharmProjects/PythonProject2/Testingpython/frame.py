from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v138.log import clear
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[text()='iFrame']").click()
driver.switch_to.frame("mce_0_ifr")
driver.switch_to.default_content()
assert "An iFrame containing the TinyMCE WYSIWYG Editor" ==driver.find_element(By.XPATH,"//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']").text
#driver.find_element(By.XPATH,"//div[@class='tox-icon']").clear()
#driver.find_element(By.ID,"#tinymce").clear()
#driver.find_element(By.ID,"#tinymce").send_keys("hello")
