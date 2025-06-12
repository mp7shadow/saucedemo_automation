from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import ShoppingCartLocators
from pages.Inventory_Page import Inventory_Page
from pages.Login_Page import Login_Page
from configurations.config import Config

class Cart_Page:

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ShoppingCartLocators.shopping_cart_link)
        )
        cart_link.click()

    def get_cart_items(self):
        return self.driver.find_elements(*ShoppingCartLocators.cart_item)

    def get_cart_item_names(self):
        return [item.text for item in self.driver.find_elements(*ShoppingCartLocators.cart_item_name)]

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ShoppingCartLocators.checkout_button)
        ).click()

    def click_continue_shopping(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ShoppingCartLocators.continue_shopping_button)
        ).click()

    def is_cart_empty(self):
        try:
            empty_cart_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ShoppingCartLocators.empty_cart_message)
            )
            return empty_cart_message.is_displayed()
        except:
            return False
    
    