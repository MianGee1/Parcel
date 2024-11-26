import time

from Constants.Locators import Locators

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class ListPage:

    def __init__(self,driver):
        self.driver = driver
        self.locators = Locators.ListPageLocators()

    def scroll(self):
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        # Set the scroll step and delay
        scroll_step = 20  # Number of pixels to scroll in each step
        scroll_delay = 0.05  # Delay between each scroll in seconds

        # Get the total height of the page
        total_height = self.driver.execute_script("return document.body.scrollHeight")

        # Start scrolling in steps
        for scroll_position in range(0, total_height, scroll_step):
            self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(scroll_delay)  # Add delay to avoid scrolling too fast

        # Ensure the final position is reached
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def out(self, out_list):
        WebDriverWait(self.driver, 60).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        action = ActionChains(self.driver)

        not_out=[]
        not_found = []
        count =0

        for pk_dex, value in out_list.items():
            count+=1
            try:
                if count > 1:
                    tracking_id = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, f"//div[text()='{pk_dex}']")))
                else:
                    tracking_id = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, f"//div[text()='{pk_dex}']")))

                self.driver.execute_script("arguments[0].scrollIntoView();", tracking_id)
                time.sleep(2)

                customer_collection = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//div[text()='{pk_dex}']/ancestor::tr//button[@class='lazada-logistics-btn lazada-logistics-small lazada-logistics-btn-normal components--action-button--ainyAP7']"
)))
                self.driver.execute_script("arguments[0].click();", customer_collection)

                otp = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.locators.otp_field))
                self.driver.execute_script("arguments[0].click();", otp)

                action.send_keys(value).perform()
                try:
                    otp_out = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((self.locators.confirm_otp)))
                    self.driver.execute_script("arguments[0].click();", otp_out)
                    time.sleep(2)
                    print ('out'+ {pk_dex} + {otp_out} + '\n')
                except TimeoutException:
                    cancel = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.locators.cancel))
                    self.driver.execute_script("arguments[0].click();", cancel)
                    not_out.append(pk_dex)

            except TimeoutException:
                not_found.append(pk_dex)

            except Exception as e:
                print(f"Error occurred for {pk_dex}: {e}")
                not_found.append((pk_dex))

        print("Parcels Not Found List: " + str(not_found) + "\n")

        print("Parcels: Not Out List: " + str(not_out) + "\n")






