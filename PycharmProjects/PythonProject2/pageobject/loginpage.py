from selenium.webdriver.common.by import By

from pageobject.shop_page import shopPage
from pageobject.utils.browserutils import browserutils


class loginpage(browserutils):
    def __init__(self,driver):
        super().__init__(driver)

        self.driver=driver
        self.username_input=(By.CSS_SELECTOR, "input#username") #()brackets are tuple here
        self.password=(By.CSS_SELECTOR, "input#password")
        self.login_button=(By.CSS_SELECTOR, "input#signInBtn")






    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy ") #if you put star=* infront of self,tuple will break into two parameters
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.login_button).click()

        shoppage_obj = shopPage(self.driver)
        return  shoppage_obj


    #for json file we can write above login method as
    #def login(self,username,password):
        #self.driver.find_element(*self.username_input).send_keys(username)  # if you put star=* infront of self,tuple will break into two parameters
        #self.driver.find_element(*self.password).send_keys(password)


