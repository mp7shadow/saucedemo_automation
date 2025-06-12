from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators.locators import InventoryItemActionsLocators, InventoryItemDetailsLocators, InventoryItemLocators
from configurations.config import Config
from pages.Login_Page import Login_Page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryItemDetails_Page:
    def __init__(self, driver):
        self.driver = driver

    def load_item_detail_page(self, item_name):
        items = self.driver.find_elements(*InventoryItemLocators.inventory_item)
        for item in items:
            name = item.find_element(*InventoryItemLocators.inventory_item_name).text
            if name == item_name:
                item.find_element(*InventoryItemActionsLocators.inventory_item_link).click()
                break

    def get_item_name(self):
        return self.driver.find_element(*InventoryItemDetailsLocators.item_details_name).text

    def get_item_price(self):
        return self.driver.find_element(*InventoryItemDetailsLocators.item_details_price).text

    def add_to_cart(self):
        self.driver.find_element(*InventoryItemDetailsLocators.add_to_cart_button).click()

    def remove_from_cart(self):
        self.driver.find_element(*InventoryItemDetailsLocators.remove_from_cart_button).click()
    
    def get_cart_badge_count(self):
            try:
                return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
            except:
                return 0