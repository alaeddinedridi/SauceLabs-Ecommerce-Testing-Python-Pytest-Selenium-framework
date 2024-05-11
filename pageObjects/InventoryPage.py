import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from random import randrange

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
        self.tax = 0.0

    def addToCart(self,numberOfProducts):
        chosenProducts=[]
        for num in range(numberOfProducts):
            products=WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH,self.inventory_item_xpath))
            )
            randomProduct=randrange(len(products))
            while randomProduct in chosenProducts:
                randomProduct = randrange(len(products))


            chosenProducts.insert(num,randomProduct)
            product=products[randomProduct]
            print("this is the item: ", product)
            product.click()

            self.calculateTotalItemsPrice()

            addToCartBtn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.addToCart_button_id))
            )
            addToCartBtn.click()

            backToProducts = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.backToProducts_link_id))
            )
            backToProducts.click()

            time.sleep(2)

        # item = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.ID,self.inventory_item_id))
        # )
        # item.click()
        #
        # self.calcTotalItemsPrice()
        #
        # addToCartBtn = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, self.addToCart_button_id))
        # )
        # addToCartBtn.click()
        #
        # backToProducts = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, self.backToProducts_link_id))
        # )
        # backToProducts.click()


    def checkout(self):
        cartBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.shopppingCart_link_class))
        )
        cartBtn.click()

        checkoutBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.checkout_button_id))
        )
        checkoutBtn.click()

    def calculateTotalItemsPrice(self):
        itemPrice_elm = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.itemPrice_class))
        )
        self.totalPrice+=float(itemPrice_elm.text.split("$", 1)[1])
        print("The sum of items price: ", self.totalPrice)

    def getTotalItemsPrice(self):
        return self.totalPrice

    def calculateTax(self):
        self.tax=round(self.getTotalItemsPrice() * 0.08,2)

    def getTotalTax(self):
        return self.tax