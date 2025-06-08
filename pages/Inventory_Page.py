from selenium.webdriver.common.by import By
from locators.locators import InventoryLocators


class Inventory_Page:

    # locators
    inventory_container_id = InventoryLocators.INVENTORY_CONTAINER[1]

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def is_inventory_page_loaded(self):
        return self.driver.find_element(By.ID, self.inventory_container_id).is_displayed()

    def get_inventory_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")