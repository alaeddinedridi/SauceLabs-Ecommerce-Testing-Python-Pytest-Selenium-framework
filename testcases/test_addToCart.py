import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.InventoryPage import InventoryPage
from pageObjects.CartPage import CartPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGeneration


class Test_addToCart:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstname()
    lastname = ReadConfig.getLastname()
    postalcode = ReadConfig.getPostalcode()
    # initialize the logger
    logger = LogGeneration.generateLog()

    @pytest.mark.dev

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
        # Add to cart 3 products
        self.inventoryPage.addToCart(3)

        self.inventoryPage.goToCart()
        self.cartPage = CartPage(self.driver)
        self.cartItems=self.cartPage.getCartItems()

        assert len(self.cartItems) == 3, "The number of products added to cart is NOT correct"

        self.inventoryPage.checkout()

        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.enterFirstname(self.firstname)
        self.checkoutPage.enterLastname(self.lastname)
        self.checkoutPage.enterPostalCode(self.postalcode)
        self.checkoutPage.continueCheckout()

        self.tax = self.checkoutPage.getTax()
        self.inventoryPage.calculateTax()
        self.expectedTax= self.inventoryPage.getTotalTax()
        assert self.tax == self.expectedTax, "The tax is not correct"

        self.totalPrice= self.checkoutPage.getItemsPrice() + self.tax
        self.expectedTotalPrice=self.inventoryPage.getTotalItemsPrice() + self.expectedTax
        assert self.totalPrice == self.expectedTotalPrice, "The total price is not correct"

        self.totalToPay= self.totalPrice + self.tax
        self.ExpectedTotalToPay= self.expectedTotalPrice + self.expectedTax

        # when we add a message to be returned, it becomes soft assertion which means if the first assertion fails, the next assertion will still get executed
        # otherwise it is a hard assertion and if the first assert fails, it won't check the next assertions
        assert self.totalToPay == self.ExpectedTotalToPay, "The total price to pay is not correct"