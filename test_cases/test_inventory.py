import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.config import Config	
from pages.Inventory_Page import Inventory_Page

class Test_02_Inventory:

    # Class variables for the inventory page URL
    inventory_page_url = Config.base_url


    # Test case to verify that the inventory page is loaded
    def test_inventory_page_loaded(self):
        self.driver = webdriver.Chrome()
        # Navigate to the login page
        self.driver.get(self.inventory_page_url)
        # Wait for the login page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )   
        # Enter username and password, then submit
        self.driver.find_element(By.ID, "user-name").send_keys(Config.username)
        self.driver.find_element(By.ID, "password").send_keys(Config.password)
        self.driver.find_element(By.ID, "login-button").click()
        # Wait until the inventory container is present to verify the page is loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        inventory_page = Inventory_Page(self.driver)
        assert inventory_page.is_inventory_page_loaded() == True
        self.driver.close()