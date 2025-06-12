import pytest
from pages.Inventory_Page import Inventory_Page
from pages.Footer_Page import Footer_Page

@pytest.mark.usefixtures("driver")
@pytest.mark.footer
class Test_05_Footer:

    @pytest.mark.footer_display_and_content	
    def test_footer_display_and_content(self,driver):
        try:
            # Load inventory page
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()
            assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load properly."

            # Footer validation
            footer = Footer_Page(driver)
            footer_element = footer.is_footer_visible()
            assert footer_element.is_displayed(), "Footer is not visible."

            footer_text = footer.get_footer_text()
            assert "©" in footer_text, "Footer copyright missing."
            assert "Terms of Service" in footer_text, "'Terms of Service' not found in footer."
            assert "Privacy Policy" in footer_text, "'Privacy Policy' not found in footer."

            # Check social media links
            # Social media links
            assert footer.is_twitter_link_present(), "Twitter link not visible in footer."
            assert footer.is_facebook_link_present(), "Facebook link not visible in footer."
            assert footer.is_linkedin_link_present(), "LinkedIn link not visible in footer."

            # If all assertions pass, print success message
            print("Footer test passed: footer is visible and content is valid.")
        except Exception as e:
            print(f"Footer test failed: {e}")
            assert False
        finally:
            driver.quit()

    @pytest.mark.footer 
    def test_footer_social_media_links(self,driver):
        try:
            # Load inventory page
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()
            assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load properly."

            # Footer validation
            footer = Footer_Page(driver)

            # Check social media links
            assert footer.is_twitter_link_present(), "Twitter link not visible in footer."
            assert footer.is_facebook_link_present(), "Facebook link not visible in footer."
            assert footer.is_linkedin_link_present(), "LinkedIn link not visible in footer."

            print("Footer social media links test passed.")
        except Exception as e:
            print(f"Footer social media links test failed: {e}")
            assert False
        finally:
            driver.quit()

    # Test case to check if twitter links are functional
    @pytest.mark.footer_twitter_link
    def test_footer_twitter_link(self, driver):
        try:
            # Load inventory page
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()
            assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load properly."

            # Footer validation
            footer = Footer_Page(driver)

            # Check if Twitter link is present and functional
            assert footer.is_twitter_link_present(), "Twitter link not visible in footer."
            twitter_link = driver.find_element(*Footer_Page.footer_twitter_link)
            twitter_link.click()
            # Here twitter or X opens in a new tab, so we switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])
            # Wait for the new tab to load
            driver.implicitly_wait(10)  # Adjust the wait time as necessary
            # Check if the current URL contains the expected Twitter URL
            assert "https://x.com/saucelabs" in driver.current_url, "Twitter link did not redirect to Twitter."

            print("Footer Twitter link test passed.")
        except Exception as e:
            print(f"Footer Twitter link test failed: {e}")
            assert False
        finally:
            driver.quit()

    # Test case to check if Facebook links are functional
    @pytest.mark.footer_facebook_link
    def test_footer_facebook_link(self, driver):
        try:
            # Load inventory page
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()
            assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load properly."

            # Footer validation
            footer = Footer_Page(driver)

            # Check if Facebook link is present and functional
            assert footer.is_facebook_link_present(), "Facebook link not visible in footer."
            facebook_link = driver.find_element(*Footer_Page.footer_facebook_link)
            facebook_link.click()
            # Here Facebook opens in a new tab, so we switch to the new tab
            driver.switch_to.window(driver.window_handles[-1]) 
            # Wait for the new tab to load
            driver.implicitly_wait(10)  # Adjust the wait time as necessary
            # Check if the current URL contains the expected Facebook URL
            assert "facebook.com" in driver.current_url, "Facebook link did not redirect to Facebook."

            print("Footer Facebook link test passed.")
        except Exception as e:
            print(f"Footer Facebook link test failed: {e}")
            assert False
        finally:
            driver.quit()
    
    # Test case to check if LinkedIn links are functional
    @pytest.mark.footer_linkedin_link
    def test_footer_linkedin_link(self, driver):
        try:
            # Load inventory page
            inventory_page = Inventory_Page(driver)
            inventory_page.load_inventory_page()
            assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load properly."

            # Footer validation
            footer = Footer_Page(driver)

            # Check if LinkedIn link is present and functional
            assert footer.is_linkedin_link_present(), "LinkedIn link not visible in footer."
            linkedin_link = driver.find_element(*Footer_Page.footer_linkdin_link)
            linkedin_link.click()
            # Here LinkedIn opens in a new tab, so we switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])
            # Wait for the new tab to load
            driver.implicitly_wait(10)  # Adjust the wait time as necessary
            # Check if the current URL contains the expected LinkedIn URL
            assert "linkedin.com" in driver.current_url, "LinkedIn link did not redirect to LinkedIn."

            print("Footer LinkedIn link test passed.")
        except Exception as e:
            print(f"Footer LinkedIn link test failed: {e}")
            assert False
        finally:
            driver.quit()
