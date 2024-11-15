import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class Login:
    username = "domainAccount"
    password = "password"
    button_login = "sso-btn-submit"
    incorrect_alert = "go3958317564"
    list_detail_logo = "lazada-logistics-box"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):

        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        user_name = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.NAME, self.username)))
        time.sleep(1)
        user_name.clear()
        user_name.send_keys(username)

    def setPassword(self, password):
        user_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.password)))
        time.sleep(1)
        user_password.clear()
        user_password.send_keys(password)

    def clickLogin(self):
        # self.driver.switch_to.frame('loginTarget')  # Switch to the first iframe

        sign_in = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.button_login)))
        sign_in.click()
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
