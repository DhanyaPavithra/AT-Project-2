"""
test.py
"""
# importing data and locator details from files
from Data import data
from Locator import locator


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Importing Pytest
import pytest

class Test:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    def test_title(self,boot):
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
        locator.WebLocators().clickBtn(self.driver, locator.WebLocators().loginBtnLocator)

        # Admin module:
        locator.WebLocators().clickBtn(self.driver, locator.WebLocators().adminModuleLocator)

        assert self.driver.title == data.WebData().title
        print("Title Validated")

        



