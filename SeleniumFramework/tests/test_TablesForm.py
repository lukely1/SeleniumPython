import unittest
import pytest
import time
from SeleniumFramework.pages.TablesPage import Tables


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Actions(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.tb = Tables(self.driver)

    @pytest.mark.run(order=1)
    def test_Tables(self):
        self.tb.clickTables()
        self.tb.verifyTablesPage()
        self.tb.tableRowCount()
        self.tb.tableColumnCount()
        self.tb.getAllTextTable('')

