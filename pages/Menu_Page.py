from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MenuLocators

class Menu_Page:
    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MenuLocators.menu_button)
        ).click()

    def click_all_items(self):
        self.driver.find_element(*MenuLocators.all_items_link).click()

    def click_about(self):
        self.driver.find_element(*MenuLocators.about_link).click()

    def click_logout(self):
        self.driver.find_element(*MenuLocators.logout_link).click()

    def click_reset_app_state(self):
        self.driver.find_element(*MenuLocators.reset_app_state_link).click()
