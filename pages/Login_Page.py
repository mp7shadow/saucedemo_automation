from selenium.webdriver.common.by import By
from locators.locators import LoginLocators
from configurations.config import Config


class Login_Page:

    # locators
    # these are the locators for the login page elements
    # they are used to find the elements on the page
    textbox_username_id = LoginLocators.username_input[1]
    textbox_password_id = LoginLocators.password_input[1]   
    login_button_id = LoginLocators.login_button[1]

    # constructor
    def __init__(self,driver):
        self.driver = driver

    # action methods
    # these methods are used to perform actions on the login page

    # this method is used to enter the username in the username textbox
    def enter_username(self,username):

        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    # this method is used to enter the password in the password textbox
    def enter_password(self,password):

        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    # this method is used to click on the login button
    def click_login_button(self):
        self.driver.find_element(By.ID,self.login_button_id).click()

    # combined action for login
    # this method can be used to login with username and password
    def login(self, username = Config.valid_username, password = Config.valid_password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


#     def get_error_message(self):
#         return self.get_text(LoginLocators.ERROR_MESSAGE)
