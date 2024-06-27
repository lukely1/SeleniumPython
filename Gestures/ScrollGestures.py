from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

driver = webdriver.Chrome()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template" in driver.title
time.sleep(2)

driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait.until(ec.presence_of_element_located((By.LINK_TEXT,"Form"))).click()
#wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/section/div[1]/div/div[2]/a"))).click()
#driver.find_element(By.LINK_TEXT, "Form").click()
wait.until(ec.presence_of_element_located((By.ID,"reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.ID, "name"))).send_keys("Code2Lead")
wait.until(ec.presence_of_element_located((By.ID, "email"))).send_keys("abc@gmail.com")
wait.until(ec.presence_of_element_located((By.ID, "message"))).send_keys("ABCDEFG")
captcha = wait.until(ec.presence_of_element_located((By.ID,"captcha_image")))
wait.until(ec.presence_of_element_located((By.ID, "captcha"))).send_keys(captcha.text)

postButton = wait.until(ec.presence_of_element_located((By.ID, "btnContactUs")))

# Scroll Gesture
actions = ActionChains(driver)
actions.move_to_element(postButton).perform()
postButton.click()

time.sleep(5)
driver.quit()