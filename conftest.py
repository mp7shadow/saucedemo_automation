import pytest
from selenium import webdriver

# // This fixture sets up a Selenium WebDriver instance for testing
# def driver():
#     driver = webdriver.Chrome()  # You can change this to any other browser driver
#     driver.get("http://example.com")  # Replace with the URL you want to test
#     yield driver
#     driver.quit()

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()