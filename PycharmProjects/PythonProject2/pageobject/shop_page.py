from selenium.webdriver.common.by import By

from pageobject.checkout_and_confirmation import checkout_confirmation
from pageobject.utils.browserutils import browserutils


class shopPage(browserutils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shoplink=(By.CSS_SELECTOR, "a[href*='shop']")
        self.products_cards=(By.XPATH, "//div[@class='card h-100']")
        self.checkout_button=(By.XPATH, "//a[@class='nav-link btn btn-primary']")




    def add_product_to_card(self,product_name):
        # CSS For a[href*='shop'] XPATH //a[contains(@href,'shop')]
        self.driver.find_element(*self.shoplink).click()
        products = self.driver.find_elements(*self.products_cards)
        for product in products:

            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == product_name:
                product.find_element(By.XPATH, "div/button").click()


    def goto_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        #checkout_confirmation1=checkout_confirmation(self.driver) #we can create obj of checkout_and_confirmation class here also
        #return checkout_confirmation1

