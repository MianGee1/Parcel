import time
from PageObjects.list_page import list_page
from PageObjects.Login import Login
from Utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ParcelOut:

    baseURL = ReadConfig.getWebsiteURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()

    login = Login()

    def


    def out(self, result):

        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)
        driver.get(self.baseURL)
        self.login = list_page(driver)
        time.sleep(2)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        time.sleep(2)
        self.login.clickLogin()
        time.sleep(5)
        self.login.out(result)






