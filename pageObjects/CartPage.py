from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    cartItems_div_xpath="//div[@class='cart_list']/div[@class='cart_item']"

    def __init__(self,driver):
        self.driver=driver

    # Return cart items
    def getCartItems(self):
        cartItems=WebDriverWait(self.driver,20).until(
            EC.visibility_of_all_elements_located((By.XPATH,self.cartItems_div_xpath))
        )
        return cartItems

    # Remove the number of cart items -1
    def removeItemsFromCart(self):
        cartItems = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.cartItems_div_xpath))
        )
        for item in range(len(cartItems)-1):
            cartItemBtn=cartItems[item].find_element(By.TAG_NAME,'button')
            cartItemBtn.click()