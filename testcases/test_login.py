import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGeneration

# The class represents the testcase name and the functions under it represent the steps/expected results
class Test_Login:
    #Read properties from the config.ini using read_config.py file
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    # initialize the logger
    logger=LogGeneration.generateLog()

    # to use a fixture, we put the name of the fixture as a parameter for a function where we want to use it
    def test_homePageTitle(self,setup):
        self.logger.info("*********************** Test_login ***********************")
        self.logger.info("*********************** verifying Home Page Title ***********************")
        self.driver= setup
        self.driver.get(self.baseUrl)
        title=self.driver.title
        if title=="Swag Labs":
            self.driver.close()
            self.logger.info("*********************** Home Page Title test Passed ***********************")
            assert True
        else:
            # Take a screenshot in case the test fails
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********************** Home Page Title test Failed ***********************")
            assert False

    def test_login(self,setup):
        self.logger.info("*********************** verifying Login Test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginPage=LoginPage(self.driver)
        self.loginPage.enterUsername(self.username)
        self.loginPage.enterPassword(self.password)
        self.loginPage.clickOnLoginButton()
        title = self.driver.title
        self.loginPage.openTheMenu()
        if title == "Swag Labs":
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