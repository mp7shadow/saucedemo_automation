from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, keys):
        self.wait_for_element(locator).send_keys(keys)

    def get_text(self, locator):
        return self.wait_for_element(locator).text
