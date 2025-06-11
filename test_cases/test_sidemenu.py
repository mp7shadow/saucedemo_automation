import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryLocators, LoginLocators, MenuLocators, ShoppingCartLocators
from pages.Cart_Page import Cart_Page
from pages.Inventory_Page import Inventory_Page
from pages.Login_Page import Login_Page
from pages.Menu_Page import Menu_Page
from configurations.config import Config

@pytest.mark.usefixtures("driver")
@pytest.mark.sidebar
class Test_03_Sidebar_Menu:

    base_url = Config.base_url

    @pytest.mark.open_sidebar_menu
    def test_open_sidebar_menu(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()

            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # Verify the presence of the sidebar menu button
            menu_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MenuLocators.menu_button)
            )
            assert menu_button.is_displayed(), "Sidebar menu button is not displayed."

            # Open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()

            # Verify that the sidebar menu is opened by checking the presence of the menu items
            all_items_link = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MenuLocators.all_items_link)
            )
            assert all_items_link.is_displayed(), "'All Items' link is not displayed in the sidebar menu."

            print("TS03_TC01 - Sidebar menu opened successfully.")
        except Exception as e:
            print(f"TS03_TC01 - Failed to open sidebar menu: {e}")
            assert False
        finally:
            driver.quit()

    @pytest.mark.all_items
    def test_sidebar_menu_allitems(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # First, navigate to shopping cart to ensure the sidebar menu "All Items" link is functioning correctly
            cart = Cart_Page(driver)
            cart.go_to_cart()
            # Verify that the cart page is loaded
            header_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(ShoppingCartLocators.cart_page_header)
            ).text
            assert header_text == "Your Cart", "Shopping cart page did not load correctly."
            # Now, open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()

            # Click on 'All Items' link
            menu.click_all_items()
            # Wait for the inventory page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(InventoryLocators.header_title)
            )
            # Verify that the inventory page is displayed
            act_inventory = driver.find_element(By.XPATH, "//span[text()='Products']")
            assert act_inventory.is_displayed(), "'All Items' link did not navigate to the Products page."

            print("TS03_TC02 - 'All Items' link verified successfully.")
        except Exception as e:
            print(f"TS03_TC02 - Failed to verify 'All Items' link: {e}")
            assert False
        finally:
            driver.quit()

    @pytest.mark.about
    def test_sidebar_menu_about(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()
            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # Open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()

            # Click on 'About' link
            menu.click_about()

            # Wait for the URL to change to Sauce Labs landing page
            WebDriverWait(driver, 10).until(
                EC.url_contains("saucelabs.com")
            )
            assert "saucelabs.com" in driver.current_url, "'About' link did not navigate to Sauce Labs landing page."

            print("TS03_TC03 - 'About' link navigates to Sauce Labs Landing page successfully.")
        except Exception as e:
            print(f"TS03_TC03 - Failed to verify 'About' link: {e}")
            assert False
        finally:
            driver.quit()

    @pytest.mark.logout
    def test_sidebar_menu_logout(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()

            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # Open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()

            # Click on 'Logout' link
            menu.click_logout()

           # Wait for the login button to be present
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginLocators.login_button)
            )
            login_button = driver.find_element(*LoginLocators.login_button)
            assert login_button.is_displayed(), "'Logout' did not navigate to the login page."

            print("TS03_TC04 - Logout successful.")
        except Exception as e:
            print(f"TS03_TC04 - Failed to verify 'Logout' link: {e}")
            assert False
        finally:
            driver.quit()
    
    @pytest.mark.reset_app_state
    def test_sidebar_menu_reset_app_state(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()

            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # Open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()
            assert menu.is_menu_open(), "Sidebar menu did not open properly."

            # Click on 'Reset App State' link
            menu.click_reset_app_state()

            # Verify that the app state is reset by checking if the inventory items are displayed again
            assert len(inventory_page.get_inventory_items()) > 0, "App state was not reset properly."

            print("TS03_TC05 - App state reset successfully.")
        except Exception as e:
            print(f"TS03_TC05 - Failed to reset app state: {e}")
            assert False
        finally:
            driver.quit()

    @pytest.mark.sidebar_menu_close
    def test_sidebar_menu_close(self, driver):
        try:
            inventory_page = Inventory_Page(driver)
            # Load the inventory page
            inventory_page.load_inventory_page()

            # Verify that the inventory page is loaded
            assert inventory_page.is_inventory_page_loaded() == True

            # Open the sidebar menu
            menu = Menu_Page(driver)
            menu.open_menu()

            # Close the sidebar menu
            menu.close_menu()

            # Verify that the sidebar menu is closed by checking if the menu button is still displayed
            assert driver.find_element(*MenuLocators.menu_button).is_displayed(), "Sidebar menu did not close properly."

            print("TS03_TC05 - Sidebar menu closed successfully.")
        except Exception as e:
            print(f"TS03_TC05 - Failed to close sidebar menu: {e}")
            assert False
        finally:
            driver.quit()