import pytest

from pagebjects.loginPage import Login
from testCases.conftest import setup,screenshot
from utilities.read_config import ConfigReader
from utilities.customLogger import LogGen
from pagebjects.addCustomerPage import *
from pagebjects.searchCustomerPage import SearchCustomer

class Test_001_Search_Customer:

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer ( self, setup ):
        self.driver = setup
        self.driver.get ( ConfigReader.get_application_url () )
        self.lg = Login ( self.driver )
        self.lg.set_username ( ConfigReader.get_login_username () )
        self.lg.set_password ( ConfigReader.get_login_password () )
        self.lg.click_login ()
        self.logger.info("Login Successful")
        self.logger.info ( "starting search customer test" )

        self.go_to_customer_page = AddCustomerTest ( self.driver )
        self.go_to_customer_page.click_on_customer_main_manu ()
        self.go_to_customer_page.click_on_customer_mainItem ()

        self.searchCustomer = SearchCustomer(self.driver)
        flag = self.searchCustomer.search_customer_by_attribute(attribute=ConfigReader.getArrtibute())
        assert flag
        self.logger.info("Test search customer pass")
        self.driver.close()


