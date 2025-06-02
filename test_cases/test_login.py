import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Login_Page import Login_Page


class Test_01_Login:

    login_page_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    invalid_username = "asdfdf"
    invalid_password = "1112"

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

    def test_invalid_username_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.invalid_username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']//h3//button").text
        if err_message == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_password_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.invalid_password)
        self.login_page.click_login_button()
        err_message = self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']//h3//button").text
        if err_message == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
