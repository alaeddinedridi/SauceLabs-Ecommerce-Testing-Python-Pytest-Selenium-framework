from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    title_span_xpath = "//div[@id='header_container']/div[@class='header_secondary_container']/span"


    def getPageTitle(self,driver):
        print("inside getPageTitle -------------------------")
        pageTitle = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.title_span_xpath))
        )
        return pageTitle.text