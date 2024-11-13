import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class list_page:

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

    def out(self, dic):
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        action = ActionChains(self.driver)
        # action.key_down(Keys.CONTROL).send_keys("f").key_up(Keys.CONTROL).perform()



        for pk_dex, value in dic.items():
            not_out=[]
            # action.send_keys(pk_dex).perform()
            # action.send_keys(Keys.RETURN).perform()

            tracking = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[text()='{pk_dex}']")))

            self.driver.execute_script("arguments[0].scrollIntoView();", tracking)
            time.sleep(2)
            if tracking.is_displayed():
                otp = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"// div[text() = '{pk_dex}'] / ancestor::tr // button[ @class = 'lazada-logistics-btn lazada-logistics-small lazada-logistics-btn-normal components--action-button--ainyAP7']")))
                self.driver.execute_script("arguments[0].scrollIntoView();", otp)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", otp)

                otp1 = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@id='otp']")))
                self.driver.execute_script("arguments[0].scrollIntoView();", otp1)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", otp1)
                action.send_keys(value).perform()
                time.sleep(3)

                otpout = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='lazada-logistics-btn lazada-logistics-medium lazada-logistics-btn-primary lazada-logistics-dialog-btn']")))
                self.driver.execute_script("arguments[0].scrollIntoView();", otpout)
                time.sleep(2)
            else:
                not_out.append(pk_dex)
                continue
            if otpout.is_enabled():
                self.driver.execute_script("arguments[0].click();", otpout)
                time.sleep(3)
            else:
                not_out.append(pk_dex)

        print(not_out)






