import time
from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait

from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc


class Auto_Loan:

    # 초기화
    def __init__(self):
        self.Etc = Etc()



