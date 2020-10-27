from pagebjects.loginPage import Login
from testCases.conftest import setup,screenshot
from utilities.read_config import ConfigReader
from utilities.customLogger import LogGen
import pytest



class Test_001_Login:

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup ):
        self.logger.info("Generating log")
        self.driver = setup
        self.driver.get ( ConfigReader.get_application_url () )
        home_page_title = self.driver.title
        if home_page_title == "Your store. Login" :
            assert True
            self.driver.close ()
        else :
            screenshot ( self.driver )
            self.driver.close ()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login ( self, setup ) :
        self.driver = setup
        self.driver.get ( ConfigReader.get_application_url () )
        self.lg = Login ( self.driver )
        self.lg.set_username ( ConfigReader.get_login_username () )
        self.lg.set_password ( ConfigReader.get_login_password () )
        self.lg.click_login ()
        login_page_title = self.driver.title
        if login_page_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            screenshot(self.driver)
            self.driver.close()
            assert False
