import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    title_span_xpath = "//div[@class='header_secondary_container']/span[@class='title']"
    message_h2_xpath = "//div[@id='checkout_complete_container']/h2"

    def __init__(self,driver):
        self.driver=driver


    # def getPageTitle(self):
    #     pageTitle = WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located((By.XPATH, self.title_span_xpath))
    #     )
    #     return pageTitle.text

    def orderMessage(self):
        msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.message_h2_xpath))
        )
        return msg.text