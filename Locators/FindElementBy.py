from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
driver.maximize_window()
time.sleep(2)
#driver.find_element(By.ID, "user_input").send_keys("Code2Lead")
#driver.find_element(By.CLASS_NAME, "entertext").send_keys("Code2Lead")
#driver.find_element(By.NAME, "textbox").send_keys("Code2Lead")
#driver.find_element(By.TAG_NAME, "input").send_keys("Code2Lead")

driver.find_element(By.LINK_TEXT, "Form").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'FOR').click()


time.sleep(5)
driver.quit()