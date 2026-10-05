# CSS For a[href*='shop'] XPATH //a[contains(@href,'shop')]
from selenium.webdriver.common.by import By

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:

    productname = product.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successmsg = driver.find_element(By.CLASS_NAME, "alert-success").text
# we are usinf 'in' instead '==' because here we are not comparing whole success message that is Success! Thank you! Your order will be delivered in next few weeks :-).we are just partially checking it
assert "Success! Thank you!" in successmsg
driver.close()


