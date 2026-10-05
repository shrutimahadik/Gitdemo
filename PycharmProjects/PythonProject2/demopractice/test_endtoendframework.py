import json
import time
import pytest
from pygments.lexers import data


from selenium.webdriver.common.by import By

from pageobject.checkout_and_confirmation import checkout_confirmation
from pytestdemo.pageobjects.checkoutnconfirmation import Checkoutnconfirmation
from pytestdemo.pageobjects.logibpage import LoginPage
from pytestdemo.pageobjects.shoppage import ShopPage

test_data_path1 = 'data/test_endtoendframework.json'
with open(test_data_path1) as f:
    test_data=json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserinstance,test_list_item):
    driver=browserinstance

    loginpage = LoginPage(driver)
    print(loginpage.gettitle())
    loginpage.loginpage(test_list_item["Username"],test_list_item["Userpassword"])

    shoppage=ShopPage(driver)
    print(shoppage.gettitle())
    shoppage.shoppage("Productname")
    shoppage.go_to_cart()

    checkout_confirmation=Checkoutnconfirmation(driver)
    print(checkout_confirmation.gettitle())
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_adress()
    checkout_confirmation.validate_order()












