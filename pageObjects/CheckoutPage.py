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
    title_span_xpath="//span[@class,'title']"

    def __init__(self,driver):
        self.driver=driver

    # Enter firstname
    def enterFirstname(self,firstname):
        firstname_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.firstname_textfield_id))
        )
        firstname_textbox.clear()
        firstname_textbox.send_keys(firstname)

    # Enter lastname
    def enterLastname(self,lastname):
        lastname_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.lastname_textfield_id))
        )
        lastname_textbox.clear()
        lastname_textbox.send_keys(lastname)

    # Enter postal code
    def enterPostalCode(self,postalCode):
        postalcode_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.postalCode_textfield_id))
        )
        postalcode_textbox.clear()
        postalcode_textbox.send_keys(postalCode)

    # Get the total price of the items
    def getItemsPrice(self):
        totalPrice_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.totalItemsPrice_class))
        )
        totalPrice=float(totalPrice_element.text.split("$",1)[1])
        print("This is items price: ",totalPrice)
        return totalPrice

    # Get the total tax to pay
    def getTax(self):
        tax_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.tax_class))
        )
        tax=float(tax_element.text.split("$",1)[1])
        print("this is the tax : ",tax)
        return tax

    # Go to Checkout: Overview page
    def continueCheckout(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.continue_button_id))
        )
        continue_button.click()


    # Validate order
    def finish(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.finish_button_id))
        )
        finish_button.click()

    # def getPageTitle(self):
    #     pageTitle = WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located((By.XPATH, self.title_span_xpath))
    #     )
    #     return pageTitle.text