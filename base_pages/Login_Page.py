
from selenium.webdriver.common.by import By


class Login_Page:

    # locators
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    btn_login_id = "login-button"

    # constructor
    def __init__(self,driver):
        self.driver = driver

    # actions
    def enter_username(self,username):

        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def enter_password(self,password):

        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()

