from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Tables(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage = "Tables"  # link
    _Tablespage = "card-title"  # class
    _submitButton = "submitbutton"  # id
    # _tableRows = "//*[@id='tt']/div/table/tbody/tr"
    # _tableColumns = "//*[@id='tt']/div/table/thead/tr/th"

    def clickTables(self):
        self.clickOnElement(self._locatorsPage, "link")
        cl.allureLogs("Clicked on Contact Form")

    def verifyTablesPage(self):
        element = self.isElementDisplayed(self._Tablespage, "class")
        assert element == True
        cl.allureLogs("Verified Tables displayed")

    def tableRowCount(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        rows = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/tbody/tr")))

        #rows = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/tbody/tr")
        number_of_rows = len(rows)
        print("The Rows  # :", number_of_rows)

    def tableColumnCount(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        cols = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")))
        # cols = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")
        number_of_cols = len(cols)
        print("The Columns # :", number_of_cols)

        # to get the data from 2nd row and 2nd column directly
        # val = driver.find_elements_by_xpath("//table/tbody/tr[2]/td[2]").text

    def getAllTextTable(self, val):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        data_table = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/tbody/tr")))

        for data in data_table:
            if data == val:
                assert True
                print(val.text)
        # cols = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")

        # print("The Columns # :", cols)

        # to get the data from 2nd row and 2nd column directly
        # val = driver.find_elements_by_xpath("//table/tbody/tr[2]/td[2]").text
