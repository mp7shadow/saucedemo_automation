from selenium.webdriver.common.by import By
from locators.locators import InventoryLocators, LoginLocators
from configurations.config import Config
from pages.Login_Page import Login_Page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Inventory_Page:

    # locators
    inventory_container_id = InventoryLocators.inventory_container[1]
    login_button_id = LoginLocators.login_button[1]

    # Class variables for the login page URL
    login_page_url = Config.base_url

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    # This method checks if the inventory page is loaded by verifying the presence of the inventory container
    # It returns True if the inventory container is displayed, otherwise it returns False
    def is_inventory_page_loaded(self):
        return self.driver.find_element(By.ID, self.inventory_container_id).is_displayed()
    
    def load_inventory_page(self) -> None:
        self.driver.get(self.login_page_url)
        # Wait for the login page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.login_button_id))
        )   
        # Enter username and password, then submit
        self.login_page = Login_Page(self.driver)
        self.login_page.login()
        # Wait until the inventory container is present to verify the page is loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.inventory_container_id))
        )


    # This method returns a list of inventory items displayed on the page
    # Each item is represented by an element with the class name "inventory_item"
    def get_inventory_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")