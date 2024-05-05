import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGeneration
from utilities import ExcelReader
import time


# The class represents the testcase name and the functions under it represent the steps/expected results
class Test_Login_DDT:
    #Read properties from the config.ini using read_config.py file
    baseUrl=ReadConfig.getApplicationURL()
    loginDataFile="./TestData/LoginData.xlsx"

    # initialize the logger
    logger=LogGeneration.generateLog()

    def test_login_DDT(self,setup):
        self.logger.info("*********************** verifying Login Test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginPage=LoginPage(self.driver)

        # Read data from excel file
        self.rows=ExcelReader.getRowCount(self.loginDataFile,"credentials")
        print("Number of rows: ",self.rows)
        for row in range(2,self.rows+1):
            self.username=ExcelReader.readData(self.loginDataFile,"credentials",row,1)
            self.password=ExcelReader.readData(self.loginDataFile, "credentials", row, 2)
            self.expected=ExcelReader.readData(self.loginDataFile, "credentials", row, 3)

            self.loginPage.enterUsername(self.username)
            self.loginPage.enterPassword(self.password)

            self.loginPage.clickOnLoginButton()
            time.sleep(5)

            title = self.driver.title

            if title == "Swag Labs":
                self.loginPage.openTheMenu()
                self.loginPage.clickOnLogoutLink()
                self.driver.close()
                self.logger.info("*********************** Login test Passed ***********************")
                assert True
            else:
                self.driver.save_screenshot("./Screenshots/"+"test_login.png")
                self.loginPage.clickOnLogoutLink()
                self.driver.close()
                self.logger.error("*********************** Login test Failed ***********************")
                assert False