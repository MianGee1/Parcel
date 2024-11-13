import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
# from pytest_metadata.plugin import metadata_key
# import base64
# import os
# import pytest_html


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        driver = webdriver.Ie()
        driver.maximize_window()

    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    assert browser in ("chrome", "firefox", "ie")
    return browser



################# Pytest HTML Report ################

def pytest_html_report_title(report):
    report.title = "Nop Commerce Report"

# def pytest_configure(config):
#     config.option.htmlpath = 'report/report.html'
#     config.stash[metadata_key]["Project Name"] = "nop commerce"






    # @pytest.hookimpl(hookwrapper=True)
    # def pytest_runtest_makereport(item):
    #     outcome = yield
    #     report = outcome.get_result()
    #     extra = getattr(report, "extra", [])
    #     if report.when == "call":
    #         # Assuming your screenshot is saved correctly at the specified path
    #         screenshot_path = os.getenv("SCREENSHOT_PATH", ".Screenshots/test_screenshot.png")
    #         with open(screenshot_path, "rb") as image_file:
    #             encoded_string = base64.b64encode(
    #                 image_file.read()
    #             ).decode()  # https://github.com/pytest-dev/pytest-html/issues/265
    #         extra.append(pytest_html.extras.png(encoded_string))
    #         report.extra = extra




#     # # driver = Driver()
#     # #     # return driver
#     # base_path = Path('C:/Users/Umer QA/Desktop/QA/chromedriver-win64/chromedriver-win64')
#     # # if self.browser == 'chrome':
#     # chrome_opt = webdriver.ChromeOptions()
#     # chrome_opt.add_argument('--start-maximized')
#     # driver = webdriver.Chrome(executable_path=str(base_path / 'chromedriver.exe'), options=chrome_opt)
#     # return driver
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#
#     # Open a website
#     return driver
#
#     # Perform any actions here (e.g., searching, clicking, etc.)
#
#     # Close the browser
#     # driver.quit()
#
