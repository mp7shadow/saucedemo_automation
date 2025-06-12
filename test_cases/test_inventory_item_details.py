import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.config import Config	
from pages.InventoryItemDetails_Page import InventoryItemDetails_Page
from pages.Inventory_Page import Inventory_Page
from pages.Login_Page import Login_Page

@pytest.mark.usefixtures("driver")
@pytest.mark.inventory_details
def test_item_details_display(driver):
    try:
        inventory_page = Inventory_Page(driver)
        inventory_page.load_inventory_page()
        assert inventory_page.is_inventory_page_loaded() == True
        assert inventory_page.get_inventory_items_count() > 0
        # Click on item name of the Sauce Labs Backpack item to view its details
        inventory_page.select_inventory_item(0).find_element(By.CLASS_NAME, "inventory_item_name").click()
        detail_page = InventoryItemDetails_Page(driver)
        detail_page.load_item_detail_page("Sauce Labs Backpack")
        # Wait for the item details page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_desc"))
        )

        detail_page = InventoryItemDetails_Page(driver)
        detail_page.load_item_detail_page("Sauce Labs Backpack")

        assert "Sauce Labs Backpack" in detail_page.get_item_name()
        assert "$29.99" in detail_page.get_item_price()

    except Exception as e:
        print(f" TS02_TC03 - Item details page failed to load: {e}")
        assert False
    finally:
        driver.quit()

@pytest.mark.inventory_details
def test_add_and_remove_from_details_page(driver):
    inventory_page = Inventory_Page(driver)
    inventory_page.load_inventory_page()

    detail_page = InventoryItemDetails_Page(driver)
    detail_page.load_item_detail_page("Sauce Labs Backpack")

    detail_page.add_to_cart()
    assert inventory_page.get_cart_badge_count() == 1

    detail_page.remove_from_cart()
    assert inventory_page.get_cart_badge_count() == 0
