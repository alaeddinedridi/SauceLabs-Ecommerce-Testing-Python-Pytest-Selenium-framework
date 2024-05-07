import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.InventoryPage import InventoryPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGeneration


class Test_addToCart:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # initialize the logger
    logger = LogGeneration.generateLog()



    def test_addToCart(self,setup):
        self.logger.info("*********************** verifying Login Test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enterUsername(self.username)
        self.loginPage.enterPassword(self.password)
        self.loginPage.clickOnLoginButton()
        title = self.driver.title

        if title == "Swag Labs":
            self.logger.info("*********************** Login test Passed ***********************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.logger.error("*********************** Login test Failed ***********************")
            assert False

        self.inventoryPage = InventoryPage(self.driver)
        self.inventoryPage.addToCart()
        self.inventoryPage.checkout()

        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.enterFirstname("Alaeddine")
        self.checkoutPage.enterLastname("Dridi")
        self.checkoutPage.enterPostalCode("7000")
        self.checkoutPage.continueCheckout()

        self.tax = self.checkoutPage.getTax()
        self.totalPrice= self.checkoutPage.getItemsPrice() + self.tax

        self.expectedTotalPrice=self.inventoryPage.getTotalItemsPrice() + self.tax

        assert self.totalPrice == self.expectedTotalPrice