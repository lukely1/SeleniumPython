from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

driver.get("http://www.dummypoint.com/Form.html")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

time.sleep(5)
driver.quit()