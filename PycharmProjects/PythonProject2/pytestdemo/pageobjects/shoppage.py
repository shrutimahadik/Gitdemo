from selenium.webdriver.common.by import By

from demopractice.utils.browserutils import Browserutil


class ShopPage(Browserutil):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.shopnelement=(By.XPATH, "//a[@href='/angularpractice/shop']")
        self.products=(By.XPATH, "//div[@class='card h-100']")
        self.productbuttonclick=By.XPATH, "//button[@class='btn btn-info']"

        self.gotocart=(By.XPATH, "//a[@class='nav-link btn btn-primary']")



    def shoppage(self,productname):
        self.driver.find_element(*self.shopnelement).click()
        phone = self.driver.find_elements(*self.products)
        for mobile in phone:
            if mobile.text == productname:
                # driver.find_element(By.XPATH,"//a[text()='Blackberry']")
                self.driver.find_element(*self.productbuttonclick).click()

    def go_to_cart(self):
        self.driver.find_element(*self.gotocart).click()

