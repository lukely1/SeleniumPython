from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

elements = driver.find_elements(By.CLASS_NAME, "section-header-breadcrumb")
for element in elements:
    print(element.text)
time.sleep(5)
driver.quit()