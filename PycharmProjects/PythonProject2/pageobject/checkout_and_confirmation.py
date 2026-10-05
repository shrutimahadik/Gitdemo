from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.utils.browserutils import browserutils


class checkout_confirmation(browserutils):


    def __init__(self,driver):
        super().__init__(driver)

        self.driver = driver
        self.checkout_button=(By.XPATH, "//button[@class='btn btn-success']")
        self.country_input=(By.XPATH, "//input[@id='country']")
        self.country_option=(By.LINK_TEXT, "India")
        self.checkbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button=(By.XPATH, "//input[@type='submit']")
        self.suceess_msg=(By.CLASS_NAME, "alert-success")



    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()




    def enter_delivery_adrress(self,country_name):

        self.driver.find_element(*self.country_input).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option)) #no * required as it already a tuple

        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()





    def validate_order(self):
        successmsg = self.driver.find_element(*self.suceess_msg).text
        # we are using 'in' instead '==' because here we are not comparing whole success message that is Success! Thank you! Your order will be delivered in next few weeks :-).we are just partially checking it
        assert "Success! Thank you!" in successmsg

