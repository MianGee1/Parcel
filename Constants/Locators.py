from selenium.webdriver.common.by import By

class Locators:

    class LoginPageLocators:
        username = (By.NAME, 'domainAccount')
        password = (By.NAME, 'password')
        login_button = (By.CLASS_NAME, 'sso-btn-submit')

        incorrect_alert = "go3958317564"
        list_detail_logo = "lazada-logistics-box"

    class ListPageLocators:
        otp_field = (By.XPATH, "//input[@id='otp']")
        confirm_otp = (By.XPATH, "//button[@class='lazada-logistics-btn lazada-logistics-medium lazada-logistics-btn-primary lazada-logistics-dialog-btn']")
        cancel =(By.XPATH, '//button[@class="lazada-logistics-btn lazada-logistics-medium lazada-logistics-btn-normal lazada-logistics-dialog-btn"]')


