from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("women tops")
#aria=driver.find_elements(By.CSS_SELECTOR,".s-suggestion-container")
#print(len(aria))


for i in range(10):
    suggestions = driver.find_elements(By.CSS_SELECTOR, ".s-suggestion-container")

    if suggestions[i].text.strip().lower() == "women tops western":
        suggestions[i].click()
        break



driver.find_element(By.XPATH, "//span[@id='a-autoid-0-announce']").click()
#driver.find_element(By.XPATH,"//a[@id='s-result-sort-select_1']").click()
cart=driver.find_elements(By.XPATH,"//li[@class='a-dropdown-item a-declarative']")
print(len(cart))

products = driver.find_elements(
    By.XPATH,
    "//div[@data-component-type='s-search-result']"
)

count = 0

for product in products:
    if count == 5:     # Add first 5 products only
        break

    try:
        button = product.find_element(
            By.XPATH,
            ".//button[@aria-label='Add to cart']"
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )
        time.sleep(1)

        driver.execute_script("arguments[0].click();", button)
        count += 1
        print(f"Product {count} added.")

        time.sleep(2)

    except Exception as e:
        print("Skipped one product:", e)

print(f"Total products added: {count}")


