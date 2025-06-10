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
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MenuLocators.all_items_link)
        )
        self.driver.execute_script("arguments[0].click();", element)  # JS click bypasses overlay issues
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MenuLocators.menu_sidebar_container)
        )


    def click_about(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MenuLocators.about_link)
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MenuLocators.about_link)
        )
        self.driver.execute_script("arguments[0].click();", element)


    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MenuLocators.logout_link)
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MenuLocators.logout_link)
        )
        self.driver.execute_script("arguments[0].click();", element)


    def click_reset_app_state(self):
        self.driver.find_element(*MenuLocators.reset_app_state_link).click()
