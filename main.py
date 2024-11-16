import time
import pytest

from Functions.TrackingList import TrackingList
from PageObjects.ListPage import ListPage
from PageObjects.Login import Login
from Utilities.readProperties import ReadConfig

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

baseURL = ReadConfig.getWebsiteURL()
username = ReadConfig.getUseremail()
password = ReadConfig.getUserpassword()

tracking = TrackingList()
result = tracking.tracking_list()

# out = ParcelOut()
# time.sleep(2)
# out.out(result)


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get(baseURL)
time.sleep(2)

login = Login(driver)
time.sleep(2)

login.setUserName(username)
login.setPassword(password)
time.sleep(2)
login.clickLogin()
time.sleep(5)

parcel_out = ListPage(driver)
parcel_out.out(result)



