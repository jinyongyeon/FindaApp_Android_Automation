import time

from appium.webdriver.common.mobileby import MobileBy

from pages.mainlocator.home import Home
from drivers.aos_webdrivers import WebDriver


class MyHome:
    def __init__(self):
        self.home = Home()
    def comPariSonLoan(self):
        loan = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loan)
        loan.click()
        time.sleep(2)