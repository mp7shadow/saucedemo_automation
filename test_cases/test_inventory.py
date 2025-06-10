import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.config import Config	
from pages.Inventory_Page import Inventory_Page
from pages.Login_Page import Login_Page

@pytest.mark.usefixtures("driver")
@pytest.mark.inventory
class Test_02_Inventory:

    # Class variables for the inventory page URL
    login_page_url = Config.base_url


    # Test case to verify that the inventory page is loaded
    # TS02_TC01
    @pytest.mark.inventory_page_loaded
    def test_inventory_page_loaded(self):
        try:
            self.driver = webdriver.Chrome()
            # Navigate to the login page
            self.driver.get(self.login_page_url)
            # Wait for the login page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-button"))
            )   
            # Enter username and password, then submit
            self.login_page = Login_Page(self.driver)
            self.login_page.login()
            # Wait until the inventory container is present to verify the page is loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "inventory_container"))
            )
            inventory_page = Inventory_Page(self.driver)
            assert inventory_page.is_inventory_page_loaded() == True
            print(" TS02_TC01 - Inventory page is loaded successfully.")
        except Exception as e:
            print(f" TS02_TC01 - Inventory page failed to load: {e}")
            assert False
        finally:
            self.driver.close()


    # Test case to verify that the inventory items are displayed
    # TS02_TC02
    @pytest.mark.inventory_items_displayed
    def test_inventory_items_displayed(self):
        try:
            self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Verify that the inventory items are displayed
            assert len(inventory_page.get_inventory_items()) > 0
            print(" TS02_TC02 - Inventory items are displayed successfully.")
        except Exception as e:
            print(f" TS02_TC02 - Inventory items failed to display: {e}")
            assert False
        finally:
            self.driver.close()

