import pytest
from pages.Inventory_Page import Inventory_Page
from pages.Cart_Page import Cart_Page
from pages.Login_Page import Login_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
@pytest.mark.cart
class Test_04_Cart:

    def test_add_item_to_cart_and_verify(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()

            # Add first item to cart
            add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
            assert add_to_cart_buttons, "No Add to Cart buttons found."
            add_to_cart_buttons[0].click()

            # Go to cart page
            cart_page = Cart_Page(driver)
            cart_page.go_to_cart()

            # Verify item is in cart
            cart_items = cart_page.get_cart_items()
            assert len(cart_items) == 1, "Cart does not contain exactly one item."

            print("TS04_TC01 - Item successfully added to cart and verified.")
        except Exception as e:
            print(f"TS04_TC01 - Failed to verify item in cart: {e}")
            assert False

    def test_continue_shopping_button(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()

            # Add an item and go to cart
            driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
            cart_page = Cart_Page(driver)
            cart_page.go_to_cart()

            # Click Continue Shopping
            cart_page.click_continue_shopping()

            # Verify we are back on inventory page
            assert inventory_page.is_inventory_page_loaded(), "Failed to return to inventory page."

            print("TS04_TC02 - Continue Shopping button works as expected.")
        except Exception as e:
            print(f"TS04_TC02 - Failed to test Continue Shopping button: {e}")
            assert False
