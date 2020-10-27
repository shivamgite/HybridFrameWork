import random
import string
import pytest
from pagebjects.loginPage import Login
from testCases.conftest import setup, screenshot
from utilities.read_config import ConfigReader
from utilities.customLogger import LogGen
from pagebjects.addCustomerPage import *


class Test_001_Add_Customer:

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer ( self, setup ):
        self.driver = setup
        self.driver.get ( ConfigReader.get_application_url())
        self.lg = Login ( self.driver )
        self.lg.set_username ( ConfigReader.get_login_username())
        self.lg.set_password ( ConfigReader.get_login_password())
        self.lg.click_login ()
        self.logger.info("Login Successful")
        self.logger.info ("starting add customer test")
        self.add_customer = AddCustomerTest(self.driver)
        self.add_customer.click_on_customer_main_manu()
        self.add_customer.click_on_customer_mainItem()
        self.add_customer.click_on_add_new_button()
        self.logger.info("Providing customer information")
        self.email = randon_generator()+"@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password(randon_generator(15))
        self.add_customer.set_first_name(randon_generator(6))
        self.add_customer.set_last_name(randon_generator(6))
        self.add_customer.click_on_gender("male")
        self.add_customer.set_date_of_birth("12/02/1986")
        self.add_customer.set_company_name("moreyeahs")
        self.add_customer.click_on_is_tax_exempt()
        self.add_customer.set_customer_role ()
        self.add_customer.set_new_letter("Your store name")
        self.add_customer.select_manager_of_vendor()
        self.add_customer.click_on_active_button()
        self.add_customer.click_on_comment(randon_generator(40))
        self.add_customer.click_on_save_button()
        self.add_customer.check_customer_added_successfully()
        self.driver.close()


def randon_generator(size=8,chars= string.ascii_lowercase+string.digits ):
    return "".join( random.choice(chars) for x in range(size) )


