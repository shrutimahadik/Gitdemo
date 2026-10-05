import time

from selenium.webdriver.common.by import By

from demopractice.utils.browserutils import Browserutil


class Checkoutnconfirmation(Browserutil):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkoutelement=(By.XPATH, "//button[@class='btn btn-success']")
        self.checkboxbtn=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.successbtn=(By.XPATH, "//input[@class='btn btn-success btn-lg']")

        self.alertmessage=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def checkout(self):
        self.driver.find_element(*self.checkoutelement).click()

    def enter_delivery_adress(self):

        self.driver.find_element(*self.checkboxbtn).click()
        self.driver.find_element(*self.successbtn).click()


    def validate_order(self):
            message = self.driver.find_element(*self.alertmessage).text
            print(message)
            assert "Success! Thank you!" in message


