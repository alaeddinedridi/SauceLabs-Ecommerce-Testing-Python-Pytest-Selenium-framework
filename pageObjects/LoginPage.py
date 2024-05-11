from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

    textbox_username_id="user-name"
    textbox_password_id="password"
    button_login_id="login-button"
    link_logout_id="logout_sidebar_link"
    button_menu_id="react-burger-menu-btn"
    div_loginError_xpath="//div[contains(@class, 'error-message-container error')]/h3"
    def __init__(self,driver):
        self.driver=driver

    def enterUsername(self,username):
        username_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_username_id))

        )
        username_textbox.clear()
        username_textbox.send_keys(username)


    def enterPassword(self,password):
        password_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_password_id))
        )
        password_textbox.clear()
        password_textbox.send_keys(password)

    def clickOnLoginButton(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.button_login_id))
        )
        login_button.click()

    def openTheMenu(self):
        menu_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.button_menu_id))
        )
        menu_button.click()

    def clickOnLogoutLink(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.link_logout_id))
        )
        logout_button.click()

    def isLogginErrorPresent(self):
        login_error_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.div_loginError_xpath))
        )

        if login_error_message.is_displayed():
            print("yes error displayed")
            return True

        print("error not displayed")
        return False
