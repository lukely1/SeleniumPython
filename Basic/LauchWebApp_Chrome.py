from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()