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
    def test_inventory_page_loaded(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            self.driver.get(self.login_page_url)
            # Wait for the login page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Login_Page.login_button_id))
            )   
            # Enter username and password, then submit
            self.login_page = Login_Page(self.driver)
            self.login_page.login()
            # Wait until the inventory container is present to verify the page is loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Inventory_Page.inventory_container_id))
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
    def test_inventory_items_displayed(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
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

    
    # Test case to verify the functionality of the sort dropdown
    # TS02_TC03
    @pytest.mark.inventory_sort
    def test_sort_by_name_ascending(self, driver):
        inventory = Inventory_Page(driver)
        inventory.load_inventory_page()
        assert inventory.is_inventory_page_loaded()

        inventory.select_sort_option("az")
        product_names = inventory.get_product_names()
        assert product_names == sorted(product_names), "Items not sorted by name A to Z"

    # TS02_TC04
    @pytest.mark.inventory_sort
    def test_sort_by_name_descending(self, driver):
        inventory = Inventory_Page(driver)
        inventory.load_inventory_page()
        assert inventory.is_inventory_page_loaded()

        inventory.select_sort_option("za")
        product_names = inventory.get_product_names()
        assert product_names == sorted(product_names, reverse=True), "Items not sorted by name Z to A"

    # TS02_TC05
    @pytest.mark.inventory_sort
    def test_sort_by_price_low_to_high(self, driver):
        inventory = Inventory_Page(driver)
        inventory.load_inventory_page()
        assert inventory.is_inventory_page_loaded()

        inventory.select_sort_option("lohi")
        product_prices = inventory.get_product_prices()
        assert product_prices == sorted(product_prices), "Items not sorted by price Low to High"

    # TS02_TC06
    @pytest.mark.inventory_sort
    def test_sort_by_price_high_to_low(self, driver):
        inventory = Inventory_Page(driver)
        inventory.load_inventory_page()
        assert inventory.is_inventory_page_loaded()

        inventory.select_sort_option("hilo")
        product_prices = inventory.get_product_prices()
        assert product_prices == sorted(product_prices, reverse=True), "Items not sorted by price High to Low"

    # Test case to verify the functionality of adding items to the cart
    # TS02_TC07
    @pytest.mark.inventory_add_to_cart
    def test_add_item_to_cart(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Add an item to the cart
            item_name = "Sauce Labs Backpack"
            inventory_page.add_item_to_cart_by_name(item_name)
            # Verify that the item is added to the cart
            assert inventory_page.get_cart_badge_count() > 0, "Item not added to cart"
            print(f" TS02_TC07 - Item '{item_name}' added to cart successfully.")
        except Exception as e:
            print(f" TS02_TC07 - Failed to add item to cart: {e}")
            assert False
        finally:
            self.driver.close()

    # Test case to verify the functionality of removing items from the cart
    # TS02_TC08
    @pytest.mark.inventory_remove_from_cart
    def test_remove_item_from_cart(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Add an item to the cart first
            item_name = "Sauce Labs Backpack"
            inventory_page.add_item_to_cart_by_name(item_name)
            # Remove the item from the cart
            inventory_page.remove_item_from_cart_by_name(item_name)
            # Verify that the item is removed from the cart
            assert inventory_page.get_cart_badge_count() == 0, "Item not removed from cart"
            print(f" TS02_TC08 - Item '{item_name}' removed from cart successfully.")
        except Exception as e:
            print(f" TS02_TC08 - Failed to remove item from cart: {e}")
            assert False
        finally:
            self.driver.close()

    # Test case to verify the functionality of viewing item details
    # TS02_TC09
    @pytest.mark.inventory_view_item_details
    def test_view_item_details(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # View details of an item
            item_name = "Sauce Labs Backpack"
            inventory_page.view_item_details(item_name)
            # Verify that the item details are displayed
            assert inventory_page.is_item_details_displayed(item_name), "Item details not displayed"
            print(f" TS02_TC09 - Item '{item_name}' details viewed successfully.")
        except Exception as e:
            print(f" TS02_TC09 - Failed to view item details: {e}")
            assert False
        finally:
            self.driver.close()
    
    # Test case to verify the functionality of the shopping cart link
    # TS02_TC10
    @pytest.mark.inventory_shopping_cart_link
    def test_shopping_cart_link(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Click on the shopping cart link
            inventory_page.click_on_cart_icon()
            # Verify that the shopping cart page is loaded
            assert inventory_page.is_shopping_cart_page_loaded(), "Shopping cart page not loaded"
            print(" TS02_TC10 - Shopping cart link works successfully.")
        except Exception as e:
            print(f" TS02_TC10 - Failed to navigate to shopping cart: {e}")
            assert False
        finally:
            self.driver.close()
    
    # Test case to verify the functionality of adding multiple items to the cart
    # TS02_TC11
    @pytest.mark.inventory_add_multiple_items_to_cart
    def test_add_multiple_items_to_cart(self, driver):
        self.driver = driver
        try:
            # self.driver = webdriver.Chrome()
            # Navigate to the login page
            inventory_page = Inventory_Page(self.driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Add multiple items to the cart
            item_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
            for item_name in item_names:
                inventory_page.add_item_to_cart_by_name(item_name)
            # Verify that the items are added to the cart
            assert inventory_page.get_cart_badge_count() == len(item_names), "Not all items added to cart"
            print(" TS02_TC11 - Multiple items added to cart successfully.")
        except Exception as e:
            print(f" TS02_TC11 - Failed to add multiple items to cart: {e}")
            assert False
        finally:
            self.driver.close()
