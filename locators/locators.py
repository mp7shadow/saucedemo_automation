from selenium.webdriver.common.by import By

class LoginLocators:
    # Locators for the login page
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    # Error message locator
    # This locator is used to find the error message displayed on the login page
    error_message = (By.XPATH, "//h3[@data-test='error']")
   
    # # Error messages for the login page
    # error_message = "Epic sadface: Username and password do not match any user in this service"
    # error_message_empty_username = "Epic sadface: Username is required"
    # error_message_empty_password = "Epic sadface: Password is required"
    # error_message_empty_login = "Epic sadface: Username is required"
    # error_message_invalid_login = "Epic sadface: Username and password do not match any user in this service"

class InventoryLocators:
    # Locators for the inventory page
    # These locators are used to find elements on the inventory page
    
    # Inventory container locator
    inventory_container = (By.ID, "inventory_container")

    # Locators for the header elements
    header_title = (By.XPATH, "//span[@class='title']")
    menu_btn = (By.ID, "react-burger-menu-btn")
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

class InventoryItemLocators:    

    # Locators for inventory items
    inventory_item = (By.CLASS_NAME, "inventory_item")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    inventory_item_desc = (By.CLASS_NAME, "inventory_item_desc")

    inventory_item_img = (By.CLASS_NAME, "inventory_item_img")

class InventoryItemActionsLocators:   
    # Locators for inventory item actions
    add_to_cart_btn = (By.CLASS_NAME, "btn_inventory")
    remove_from_cart_btn = (By.CLASS_NAME, "btn_secondary")
    inventory_item_link = (By.CLASS_NAME, "inventory_item_link")


class MenuLocators:
    # Locators for the menu
    menu_button = (By.ID, "react-burger-menu-btn")
    all_items_link = (By.ID, "inventory_sidebar_link")
    about_link = (By.ID, "about_sidebar_link")
    logout_link = (By.ID, "logout_sidebar_link")
    reset_app_state_link = (By.ID, "reset_sidebar_link")

class ShoppingCartLocators:
    # Locators for the shopping cart
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
    cart_item = (By.CLASS_NAME, "cart_item")
    cart_item_name = (By.CLASS_NAME, "inventory_item_name")
    cart_item_price = (By.CLASS_NAME, "inventory_item_price")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")

class CheckoutLocators:
    # Locators for the checkout page
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    cancel_button = (By.ID, "cancel")   

    error_message = (By.XPATH, "//h3[@data-test='error']")


class CheckoutOverviewLocators:
    # Locators for the checkout overview page
    checkout_overview_header = (By.XPATH, "//span[@class='title']")
    item_total = (By.CLASS_NAME, "summary_subtotal_label")
    tax_total = (By.CLASS_NAME, "summary_tax_label")
    total = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.ID, "finish")
    cancel_button = (By.ID, "cancel")

class CheckoutCompleteLocators:
    # Locators for the checkout complete page
    checkout_complete_header = (By.XPATH, "//h2[@class='complete-header']")
    order_confirmation_message = (By.XPATH, "//div[@class='complete-text']")
    back_to_products_button = (By.ID, "back-to-products") 

class ErrorMessageLocators:
    # Locators for error messages
    error_message = (By.XPATH, "//h3[@data-test='error']")
    error_message_text = (By.XPATH, "//h3[@data-test='error']/text()")
    error_message_locator = (By.CSS_SELECTOR, "[data-test='error']")

class FooterLocators:
    # Locators for the footer
    footer = (By.CLASS_NAME, "footer")
    footer_text = (By.XPATH, "//div[@class='footer_copy']")
    footer_links = (By.CLASS_NAME, "social_link")
    footer_link_texts = (By.XPATH, "//div[@class='social_link']/text()")

class HeaderLocators:
    # Locators for the header
    header = (By.CLASS_NAME, "header")
    header_title = (By.XPATH, "//span[@class='title']")
    menu_button = (By.ID, "react-burger-menu-btn")
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
    logo = (By.CLASS_NAME, "app_logo")
    logo_image = (By.XPATH, "//div[@class='app_logo']/img")

