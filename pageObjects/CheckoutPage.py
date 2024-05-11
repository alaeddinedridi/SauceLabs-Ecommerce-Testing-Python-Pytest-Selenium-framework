import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    firstname_textfield_id="first-name"
    lastname_textfield_id="last-name"
    postalCode_textfield_id="postal-code"
    continue_button_id="continue"
    finish_button_id="finish"
    totalItemsPrice_class="summary_subtotal_label"
    tax_class="summary_tax_label"


    def __init__(self,driver):
        self.driver=driver


    def enterFirstname(self,firstname):
        firstname_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.firstname_textfield_id))
        )
        firstname_textbox.clear()
        firstname_textbox.send_keys(firstname)


    def enterLastname(self,lastname):
        lastname_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.lastname_textfield_id))
        )
        lastname_textbox.clear()
        lastname_textbox.send_keys(lastname)

    def enterPostalCode(self,postalCode):
        postalcode_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.postalCode_textfield_id))
        )
        postalcode_textbox.clear()
        postalcode_textbox.send_keys(postalCode)


    def getItemsPrice(self):
        totalPrice_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.totalItemsPrice_class))
        )
        totalPrice=float(totalPrice_element.text.split("$",1)[1])
        print("This is items price: ",totalPrice)
        return totalPrice

    def getTax(self):
        tax_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.tax_class))
        )
        tax=float(tax_element.text.split("$",1)[1])
        print("this is the tax : ",tax)
        return tax


    def continueCheckout(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.continue_button_id))
        )
        continue_button.click()


    def finish(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.finish_button_id))
        )
        finish_button.click()