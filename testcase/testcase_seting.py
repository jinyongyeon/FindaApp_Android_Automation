import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod



class Seting_Testcase(unittest.TestCase):



    # 설정 > 내정보 수정 테스트
    def test_My_Info(self):
        driver = WebDriver.driver()







if __name__ == '__main__':
    unittest.main()