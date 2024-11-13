import time
from PageObjects.list_page import list_page
from Utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ParcelOut:

    baseURL = ReadConfig.getWebsiteURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()
    #
    # def out_parcel(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #
    #     title = self.driver.title
    #
    #     if title == "WiseMarket - Admin Panel":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
    #         assert False

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






