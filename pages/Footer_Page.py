from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import FooterLocators

class Footer_Page:

    footer_twitter_link = (FooterLocators.footer_twitter_link)
    footer_facebook_link = (FooterLocators.footer_facebook_link)
    footer_linkdin_link = (FooterLocators.footer_linkdin_link)
    footer_container = (FooterLocators.footer_container)

    def __init__(self, driver):
        self.driver = driver

    def is_footer_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FooterLocators.footer_container)
        )

    def get_footer_text(self):
        return self.driver.find_element(*FooterLocators.footer_container).text

    def is_twitter_link_present(self):
        return self.driver.find_element(*FooterLocators.footer_twitter_link).is_displayed()

    def is_facebook_link_present(self):
        return self.driver.find_element(*FooterLocators.footer_facebook_link).is_displayed()

    def is_linkedin_link_present(self):
        return self.driver.find_element(*FooterLocators.footer_linkdin_link).is_displayed()
    