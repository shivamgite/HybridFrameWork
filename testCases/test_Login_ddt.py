import time

import pytest

from pagebjects.loginPage import Login
from testCases.conftest import setup,screenshot
from utilities.read_config import ConfigReader
from utilities.customLogger import LogGen
from utilities.excelUtils import *



class Test_002_DDT_Login:

    logger = LogGen.loggen()
    app_url = ConfigReader.get_application_url ()
    file_path = "C:\\Users\\sgite\\PycharmProjects\\HybridFrameWork\\TestData\\testData.xlsx"


    @pytest.mark.regression
    def test_login_ddt( self, setup ):
        self.driver = setup
        self.driver.get ( self.app_url )
        self.lg = Login ( self.driver )
        self.rows = get_row_count(self.file_path,"Sheet1")
        print("Num of rows-- ",self.rows)
        list_status = []
        for row in range(2,self.rows+1):
           self.username = read_data(self.file_path,'Sheet1',row,1)
           self.password = read_data(self.file_path,'Sheet1',row,2)
           self.exp_result = read_data(self.file_path,'Sheet1',row,3)
           self.lg.set_username ( self.username )
           self.lg.set_password ( self.password )
           self.lg.click_login ()
           time.sleep(5)
           act_title = self.driver.title
           exp_title = "Dashboard / nopCommerce administration"
           if act_title == exp_title:
               if self.exp_result=="pass":
                   self.logger.info(("**Pass**"))
                   self.lg.click_logout()
                   list_status.append("Pass")
               elif self.exp_result == "fail":
                   self.logger.info ( ("**Pass**") )
                   self.lg.click_logout()
                   list_status.append("Fail")
           elif act_title != exp_title:
               if self.exp_result=="pass":
                   self.logger.info(("**Fail**"))
                   list_status.append("Fail")
               elif self.exp_result == "fail":
                   self.logger.info ( ("**Pass**") )
                   list_status.append("pass")
        if "Fail" not in list_status :
            self.driver.close ()
            self.logger.info ( "Test Case Pass" )
            assert True
        else :
            self.driver.close ()
            self.logger.info ( "Test Case Pass" )
            assert False