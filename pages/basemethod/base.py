import time
from telnetlib import EC
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import os

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class basemethod:


    def __init__(self):
        self.driver = WebDriver.driver
        # self.driver = WebDriver.__init__().driver



    # android back 키
    # def android_Back(self):
    #     if self.driver is not None:
    #         self.driver.press_keycode(4)
    def android_Back(self):
        self.driver.press_keycode(4)
        time.sleep(4)



    def scroll(self, scroll_distance):

        screen_size = self.driver.get_window_size()
        height = screen_size['height']

        # 스크롤할 거리 계산
        distance = int(height * scroll_distance)

        # 스크롤 이벤트 생성
        action = TouchAction(self.driver)
        action.press(x=500, y=1500).move_to(x=500, y=1500 - distance).release()
        return action.perform()

    def scroll_up(self, scroll_distance):
        # 화면 크기 얻어오기
        screen_size = self.driver.get_window_size()
        height = screen_size['height']

        # 스크롤할 거리 계산
        distance = int(height * scroll_distance)

        # 스크롤 이벤트 생성
        action = TouchAction(self.driver)
        action.press(x=900, y=2200 - distance).move_to(x=900, y=2200).release()
        return action.perform()

    def save_screenshot(self, name):
        screenshot_dir = 'screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f'{name}.png')
        self.driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved: {screenshot_path}')



# class ProviderJoinCertificateLocator(ProviderCommonMethod):
#     #공동인증서 로케이터
#     #입력완료
#     inputBtn = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "입력완료"`][1]')
#     #비밀번호
#     def __init__(self, driver, button_name):
#         super().__init__(driver)
#         self.password = (MobileBy.XPATH, f'//XCUIElementTypeButton[contains(@name, "{button_name}")]')
#
#
# class JoinCertificateInputClass():
#     def joinCertificateInputFlow(self):
#         for num in PassWord.password:
#             button_name = str(num)
#             pwClick = ProviderJoinCertificateLocator(self.driver, button_name)
#             pwClick.click(ProviderJoinCertificateLocator(self.driver, button_name).password)
#
#         inputBtn = ProviderJoinCertificateLocator(self.driver,button_name)
#         inputBtn.click(ProviderJoinCertificateLocator.inputBtn)