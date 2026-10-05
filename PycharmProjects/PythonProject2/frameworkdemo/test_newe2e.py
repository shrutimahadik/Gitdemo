import json
import os.path
import sys

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.checkout_and_confirmation import checkout_confirmation
from pageobject.loginpage import loginpage
from pageobject.shop_page import shopPage
from seleniumfile import driver
#sys.path.append(os.path.dirname(os.path.abspath(__file__))) use this instruction when module notfoundError: occures

#path for json file
test_data_path='../data/test_newe2e.json'
with open(test_data_path) as f: #here f is object
    test_data=json.load(f) #load method converts json file to python object
    test_list=test_data["data"]
@pytest.mark.smoke
#@pytest.mark.parametrize("test_list_item",test_list) #used for json file
#for json file method will be
# def test_e2e(browserInstNCE,test_list_item):
def test_e2e(browserInstNCE):
    driver=browserInstNCE

    #driver.get("https://rahulshettyacademy.com/loginpagePractise/"  #use this link to fail a test case to capture screenshot for fail
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)

    #loginpageobj=loginpage(driver)
    #loginpageobj.getTitle()
    #loginpageobj.login()
    #reference to method from login page #def login(self,username,password):
    #shopPage=loginpage.login("rahulshettyacademy ","learning") #if create obj of shop page in login page this instruction should write
   #for json file we can write above instruction as:
    # shopPage=loginpage.login(test_list_item["userEmail"],test_list_item["userpassword"])

    shoppage_obj=shopPage(driver)  #we can write obj of shop page in login page as well

    print(shoppage_obj.getTile())

    #shoppage_obj.add_product_to_card(test_list_item["productname"]) #ussed for json file
    shoppage_obj.add_product_to_card("Blackberry")
    shoppage_obj.goto_cart()

    checkout_confirmation1=checkout_confirmation(driver)

    print(checkout_confirmation1.getTile())

    checkout_confirmation1.checkout()
    checkout_confirmation1.enter_delivery_adrress("ind")
    checkout_confirmation1.validate_order()

    #if I created obj of checkout_confirmation class in shop class then i have to call methods of checkout_confirmation class as follow:
    #checkout_confirmation1 = checkout_confirmation(self.driver)
    #checkout_confirmation1=shoppage_obj.goto_cart()
    #checkout_confirmation1.checkout()
    #checkout_confirmation1.enter_delivery_adrress()
    #checkout_confirmation1.validate_order()





