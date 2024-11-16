import time

from Constants.Locators import Locators

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Login:

    def __init__(self,driver):
        self.driver = driver
        self.locator = Locators().LoginPageLocators

    def setUserName(self, username):
        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        user_name = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((self.locator.username)))
        time.sleep(1)
        user_name.clear()
        user_name.send_keys(username)

    def setPassword(self, password):
        user_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.locator.password)))
        time.sleep(1)
        user_password.clear()
        user_password.send_keys(password)

    def clickLogin(self):
        sign_in = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.locator.login_button)))
        time.sleep(1)
        sign_in.click()
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
