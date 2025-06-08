from selenium.webdriver.common.by import By

class LoginLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    # Error message locator
    # This locator is used to find the error message displayed on the login page
    error_message = (By.XPATH, "//h3[@data-test='error']")
    # Error messages for the login page
    error_message = "Epic sadface: Username and password do not match any user in this service"
    error_message_empty_username = "Epic sadface: Username is required"
    error_message_empty_password = "Epic sadface: Password is required"
    error_message_empty_login = "Epic sadface: Username is required"
    error_message_invalid_login = "Epic sadface: Username and password do not match any user in this service"

class InventoryLocators:

    # Locators for the inventory page
    # These locators are used to find elements on the inventory page
    
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

