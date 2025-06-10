import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Login_Page import Login_Page
from pages.Menu_Page import Menu_Page
from configurations.config import Config

@pytest.mark.usefixtures("driver")
@pytest.mark.sidebar
class Test_03_Sidebar_Menu:
    base_url = Config.base_url

    def login(self, driver):
        driver.get(self.base_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        Login_Page(driver).login()

    @pytest.mark.all_items
    def test_all_items_link(self, driver):
        self.login(driver)
        menu = Menu_Page(driver)
        menu.open_menu()
        menu.click_all_items()
        assert "inventory.html" in driver.current_url
        print("TS03_TC01 - All Items link verified.")

    @pytest.mark.about
    def test_about_link(self, driver):
        self.login(driver)
        menu = Menu_Page(driver)
        menu.open_menu()
        menu.click_about()
        WebDriverWait(driver, 10).until(
            EC.url_contains("saucelabs.com")
        )
        assert "saucelabs.com" in driver.current_url
        print("TS03_TC02 - About link navigates to Sauce Labs.")

    @pytest.mark.logout
    def test_logout_link(self, driver):
        self.login(driver)
        menu = Menu_Page(driver)
        menu.open_menu()
        menu.click_logout()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        assert "login" in driver.current_url
        print("TS03_TC03 - Logout successful.")

    @pytest.mark.reset
    def test_reset_app_state_link(self, driver):
        self.login(driver)
        menu = Menu_Page(driver)
        menu.open_menu()
        menu.click_reset_app_state()
        print("TS03_TC04 - Reset App State clicked (no visible assertion).")
