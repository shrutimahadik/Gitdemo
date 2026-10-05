from selenium.webdriver.common.by import By

from demopractice.utils.browserutils import Browserutil


class LoginPage(Browserutil):
    def __init__(self,driver ):
        super().__init__(driver)
        self.driver=driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.submitbutton=(By.ID, "signInBtn")

    def loginpage(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submitbutton).click()












