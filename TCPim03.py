# importing data and locator details from files
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# importing exceptions
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AdminModule03:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def admin(self):
        try:

            self.boot()
            # Login Credentials
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().loginBtnLocator)

            # Admin module:
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().adminModuleLocator)
            details = self.driver.find_element(by=By.CLASS_NAME, value="oxd-sidepanel-body").text
            print(f"The Menu Options are : {details}")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = AdminModule03()
obj.admin()