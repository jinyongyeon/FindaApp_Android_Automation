import time
from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait

from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc


class Seting:

    # 초기화
    def __init__(self):
        self.Etc = Etc()

    # 설정 진입
    def setingIn(self):
        seting_buttun = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_buttun)
        seting_buttun.click()
        time.sleep(2)



