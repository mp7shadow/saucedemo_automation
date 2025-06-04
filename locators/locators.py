from selenium.webdriver.common.by import By

class LoginLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='Epic sadface']")

# class InventoryLocators:
#     INVENTORY_CONTAINER = (By.ID, "inventory_container")
