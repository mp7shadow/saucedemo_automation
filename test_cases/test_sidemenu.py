import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryLocators, MenuLocators, ShoppingCartLocators
from pages.Cart_Page import Cart_Page
from pages.Inventory_Page import Inventory_Page
from pages.Login_Page import Login_Page
from pages.Menu_Page import Menu_Page
from configurations.config import Config

@pytest.mark.usefixtures("driver")
@pytest.mark.sidebar
class Test_03_Sidebar_Menu:

    base_url = Config.base_url


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
                EC.presence_of_element_located(By.XPATH, InventoryLocators.header_title)
            )
            # Verify that the inventory page is displayed
            act_inventory = driver.find_element(InventoryLocators.header_title).text
            assert "Products" in act_inventory, "'All Items' link did not navigate to the Products page."

            print("TS03_TC02 - 'All Items' link verified successfully.")
        except Exception as e:
            print(f"TS03_TC02 - Failed to verify 'All Items' link: {e}")
            assert False
        finally:
            driver.quit()

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
                EC.presence_of_element_located(Login_Page.login_button_id)
            )
            login_button = driver.find_element(Login_Page.login_button_id).text
            assert "login" in login_button, "'Logout' did not navigate to the login page."

            print("TS03_TC04 - Logout successful.")
        except Exception as e:
            print(f"TS03_TC04 - Failed to verify 'Logout' link: {e}")
            assert False
        finally:
            driver.quit()

    # def login(self, driver):
    #     driver.get(self.base_url)
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "login-button"))
    #     )
    #     Login_Page(driver).login()

    # @pytest.mark.all_items
    # def test_all_items_link(self, driver):
        
    #     self.login(driver)
    #     menu = Menu_Page(driver)
    #     menu.open_menu()
    #     menu.click_all_items()
    #     act_inventory = driver.find_element(By.XPATH,InventoryLocators.header_title).text
    #     assert "Products" in act_inventory
    #     print("TS03_TC01 - 'All Items' link verified.")

    # @pytest.mark.about
    # def test_about_link(self, driver):
    #     self.login(driver)
    #     menu = Menu_Page(driver)
    #     menu.open_menu()
    #     menu.click_about()
    #     WebDriverWait(driver, 10).until(
    #         EC.url_contains("saucelabs.com")
    #     )
    #     assert "saucelabs.com" in driver.current_url
    #     print("TS03_TC02 - 'About' link navigates to Sauce Labs Landing page successfully.")

    # @pytest.mark.logout
    # def test_logout_link(self, driver):
    #     self.login(driver)
    #     menu = Menu_Page(driver)
    #     menu.open_menu()
    #     menu.click_logout()
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, Login_Page.login_button_id))
    #     )
    #     assert "login" in driver.current_url
    #     print("TS03_TC03 - Logout successful.")

    # @pytest.mark.reset
    # def test_reset_app_state_link(self, driver):
    #     self.login(driver)
    #     menu = Menu_Page(driver)
    #     menu.open_menu()
    #     menu.click_reset_app_state()
    #     print("TS03_TC04 - Reset App State clicked (no visible change).")
