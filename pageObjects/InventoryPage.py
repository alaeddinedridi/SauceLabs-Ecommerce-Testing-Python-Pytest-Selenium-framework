import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    inventory_item_id="item_4_img_link"
    inventory_item_xpath="//div[contains(@class,'inventory_item')]//div//a"
    addToCart_button_id="add-to-cart"
    backToProducts_link_id="back-to-products"
    shopppingCart_link_class="shopping_cart_link"
    checkout_button_id="checkout"
    itemPrice_class="inventory_details_price"


    def __init__(self,driver):
        self.driver=driver
        self.totalPrice=0.0


    def addToCart(self):
        # items = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_all_elements_located((By.XPATH,self.inventory_item_xpath))
        # )
        #
        # for item in items:
        #     print("these are the itmes:",item)
        #
        #     item.click()
        #
        #     addToCartBtn = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.ID, self.addToCart_button_id))
        #     )
        #     addToCartBtn.click()
        #
        #     backToProducts = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.ID, self.backToProducts_link_id))
        #     )
        #     backToProducts.click()


        item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,self.inventory_item_id))
        )
        item.click()

        self.calcTotalItemsPrice()

        addToCartBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.addToCart_button_id))
        )
        addToCartBtn.click()

        backToProducts = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.backToProducts_link_id))
        )
        backToProducts.click()


    def checkout(self):
        cartBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.shopppingCart_link_class))
        )
        cartBtn.click()

        checkoutBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.checkout_button_id))
        )
        checkoutBtn.click()

    def calcTotalItemsPrice(self):
        itemPrice_elm = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.itemPrice_class))
        )
        self.totalPrice+=float(itemPrice_elm.text.split("$", 1)[1])

    def getTotalItemsPrice(self):
        return self.totalPrice