import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.config import Config	
from locators.locators import InventoryLocators, LoginLocators
from pages.Login_Page import Login_Page

@pytest.mark.usefixtures("driver")
class Test_01_Login:

    # Class variables for the login page URL and credentials
    login_page_url = Config.base_url	
    # Valid credentials for testing successful login
    username = Config.valid_username
    password = Config.valid_password
    # Error messages for the login page
    login_error_message_locator = LoginLocators.login_error_message[1]

    # Invalid credentials for testing login scenarios
    invalid_username = "asdfdf"
    invalid_password = "1112"
    empty_username = ""
    empty_password =""

    # Test case to verify the title of the Web page
    def test_title_verification(self, driver):
        try:   
            self.driver = driver
            self.driver.get(self.login_page_url)
            act_title =  self.driver.title
            exp_title = "Swag Labs"
            assert act_title == exp_title, f"Expected title '{exp_title}' but got '{act_title}'"
            print(f"TS01_TC01 - Title verification passed: {act_title}")
        except Exception as e:
            print(f"TS01_TC01 - Title verification failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for login functionality
    # Test case to verify valid login
    @pytest.mark.login
    @pytest.mark.valid_login
    def test_valid_login(self, driver):
        try:
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.username)
            self.login_page.enter_password(self.password)
            self.login_page.click_login_button()
            act_inventory = self.driver.find_element(By.XPATH,InventoryLocators.header_title[1]).text
            assert act_inventory == "Products", f"Expected inventory title 'Products' but got '{act_inventory}'"
            print("TS01_TC01 - Valid login test passed.")
        except Exception as e:
            print(f"TS01_TC01 - Valid login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Empty Username
    def test_empty_username_login(self,driver):
        try:    
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.empty_username)
            self.login_page.enter_password(self.password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username    
            assert err_message == "Epic sadface: Username is required", f"Expected error message 'Epic sadface: Username is required' but got '{err_message}'"
            print("TS01_TC02 - Empty username login test passed.")
        except Exception as e:
            print(f"TS01_TC02 - Empty username login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Empty Password
    def test_empty_password_login(self, driver):
        try:
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.username)
            self.login_page.enter_password(self.empty_password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username  
            assert err_message == "Epic sadface: Password is required", f"Expected error message 'Epic sadface: Password is required' but got '{err_message}'"
            print("TS01_TC03 - Empty password login test passed.")
        except Exception as e:
            print(f"TS01_TC03 - Empty password login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Empty Login
    def test_empty_login(self, driver):
        try:   
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.empty_username)
            self.login_page.enter_password(self.empty_password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username  
            assert err_message == "Epic sadface: Username is required", f"Expected error message 'Epic sadface: Username is required' but got '{err_message}'"
            print("TS01_TC04 - Empty login test passed.")
        except Exception as e:
            print(f"TS01_TC04 - Empty login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Invalid Login
    def test_invalid_login(self,driver):
        try:
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.invalid_username)
            self.login_page.enter_password(self.invalid_password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username  
            assert err_message == "Epic sadface: Username and password do not match any user in this service", f"Expected error message 'Epic sadface: Username and password do not match any user in this service' but got '{err_message}'"
            print("TS01_TC05 - Invalid login test passed.")
        except Exception as e:
            print(f"TS01_TC05 - Invalid login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Invalid Username
    def test_invalid_username_login(self, driver):
        try:
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.invalid_username)
            self.login_page.enter_password(self.password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username  
            assert err_message == "Epic sadface: Username and password do not match any user in this service", f"Expected error message 'Epic sadface: Username and password do not match any user in this service' but got '{err_message}'"
            print("TS01_TC06 - Invalid username login test passed.")
        except Exception as e:
            print(f"TS01_TC06 - Invalid username login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()

    # Test cases for invalid login scenarios - Invalid Password
    def test_invalid_password_login(self, driver):
        try:
            self.driver = driver
            self.driver.get(self.login_page_url)
            self.login_page = Login_Page(self.driver)
            self.login_page.enter_username(self.username)
            self.login_page.enter_password(self.invalid_password)
            self.login_page.click_login_button()
            err_element = EC.presence_of_element_located((By.XPATH, self.login_error_message_locator))
            err_message = EC.visibility_of_element_located((By.XPATH, self.login_error_message_locator))
            # Wait for the error message to be present
            WebDriverWait(self.driver, 10).until(err_element)
            err_message = self.driver.find_element(By.XPATH, self.login_error_message_locator).text
            # Check if the error message matches the expected message for empty username  
            assert err_message == "Epic sadface: Username and password do not match any user in this service", f"Expected error message 'Epic sadface: Username and password do not match any user in this service' but got '{err_message}'"
            print("TS01_TC07 - Invalid password login test passed.")
        except Exception as e:
            print(f"TS01_TC07 - Invalid password login test failed: {e}")
            self.driver.close()
            assert False
        finally:
            self.driver.quit()
