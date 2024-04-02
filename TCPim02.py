# importing data and locator details from files
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AdminModule02:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        # implicit wait
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def admin(self):
        try:

            self.boot()
            # Login credentials
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().loginBtnLocator)

            # Admin module:
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().adminModuleLocator)
            admin_title = self.driver.title
            print(f"The title is:{admin_title}")

            details = self.driver.find_element(by=By.CLASS_NAME, value="oxd-topbar-body-nav").text
            print(f"The admin page headers are : {details}")


        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()

obj = AdminModule02()
obj.admin()

