from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template — DummyPoint" in driver.title

driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()

time.sleep(5)
driver.quit()