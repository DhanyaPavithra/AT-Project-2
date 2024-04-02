# importing data and locator details from files
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResetPassword:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        to boot the webpage with the url

        """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        # Implicit waits
        self.driver.implicitly_wait(15)

    def quit(self):
        """
        to quit the webpage

        """
        self.driver.quit()

    def forgetPw(self):

        try:
            self.boot()

            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().forgetPwLocator)
            locator.WebLocators().enterText(self.driver,locator.WebLocators().frgtPwUserNameLocator,data.WebData().forgetUsername)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().resetPwLocator)

            print("Reset Password Link sent successfully ")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()

obj = ResetPassword()
obj.forgetPw()

