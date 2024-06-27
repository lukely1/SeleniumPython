from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

# 1. find the list of Checkboxes  using locator
ele_r = driver.find_elements(By.NAME,"checkbox")
time.sleep(2)

# 2. Using for loop iterate the list object and click on required option
for check_box in ele_r:
    check = check_box.get_attribute("value")
    print(check)
    if check == "c3":
        check_box.click()
        print("Is Selected : ", check_box.is_selected())
        break


time.sleep(2)
driver.quit()