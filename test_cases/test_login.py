import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.config import Config	
from pages.Login_Page import Login_Page


class Test_01_Login:

    # Class variables for the login page URL and credentials

    login_page_url = Config.base_url	

    # Valid credentials for testing successful login
    username = Config.valid_username
    password = Config.valid_password

    # Error messages for the login page
    error_message = "Epic sadface: Username and password do not match any user in this service"
    error_message_empty_username = "Epic sadface: Username is required"
    error_message_empty_password = "Epic sadface: Password is required"
    error_message_empty_login = "Epic sadface: Username is required"
    error_message_invalid_login = "Epic sadface: Username and password do not match any user in this service"


    # Invalid credentials for testing login scenarios
    invalid_username = "asdfdf"
    invalid_password = "1112"
    empty_username = ""
    empty_password =""

    # Test case to verify the title of the login page
    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        act_title =  self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

# Test cases for login functionality
    # Test case to verify valid login
    def test_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()
        act_inventory = self.driver.find_element(By.XPATH,"//div[@class='header_secondary_container']//span[@class='title']").text
        if act_inventory == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Empty Username
    def test_empty_username_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.empty_username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()
        err_element = EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        err_message = EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        WebDriverWait(self.driver, 10).until(err_element)
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        print(err_message)
        # Check if the error message matches the expected message for empty username    
        if err_message == "Epic sadface: Username is required":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Empty Password
    def test_empty_password_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.empty_password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        if err_message == "Epic sadface: Password is required":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Empty Login
    def test_empty_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.empty_username)
        self.login_page.enter_password(self.empty_password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        if err_message == "Epic sadface: Username is required":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Invalid Login
    def test_invalid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.invalid_username)
        self.login_page.enter_password(self.invalid_password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        if err_message == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Invalid Username
    def test_invalid_username_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.invalid_username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        if err_message == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    # Test cases for invalid login scenarios - Invalid Password
    def test_invalid_password_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.invalid_password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        if err_message == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
