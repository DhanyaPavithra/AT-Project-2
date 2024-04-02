"""
locator.py

File contains the Locator details
"""

from selenium.webdriver.common.by import By

class WebLocators:
    """
    class contains all the locators
    """
    def __init__(self):
        self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.loginBtnLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.forgetPwLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
        self.frgtPwUserNameLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input'
        self.resetPwLocator ='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
        self.adminModuleLocator ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        self.bodyAdminLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]'


    def enterText(self, driver, locator, textvalue):
        driver.find_element(by=By.XPATH, value=locator).send_keys(textvalue)

    def clickBtn(self,driver,locator):
        driver.find_element(by=By.XPATH, value=locator).click()