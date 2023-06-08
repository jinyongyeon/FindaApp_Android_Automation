import time
# import re
# import json

import requests
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import os

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

from pages.mainlocator.main import Main
from testscript.login_testscript.logincase import JoIn


class basemethod:


    def __init__(self):
        self.driver = WebDriver.driver
        self.info = InFo()
        self.main = Main()
        self.join = JoIn()
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

    def user_Token_Get(self):
        # API 엔드포인트 URL
        url = "https://stg-service-api.finda.co.kr/account/v1/user/token"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json"
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            # "userId": self.info.user_id,
            "userId": 2000936,
            "encryptedPincode": "91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203"
        }
        try:
            # POST 요청
            response = requests.post(url, headers=headers, json=data)
            # 응답 상태 코드 확인
            result = response.json()
            # print(result)
            if 'token' in result:
                parameter_value = result['token']
                self.info.usertoken.append(parameter_value)
            # print(self.info.usertoken)
        except Exception as e:
            print("요청 실패:", str(e))

    def user_TxSeqNo_Get(self):

        # API 엔드포인트 URL
        url = "https://stg-service-api.finda.co.kr/idcert/v1/ids"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json",
            "X-Auth-Token" : ''.join(self.info.usertoken)
        }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            "appEnvType": "DEBUG",
            "cellNumber": ''.join(self.info.phone_number),
            "name": ''.join(self.info.name),
            "rrnBirth": ''.join(self.info.rrn_a),
            "rrnGender": ''.join(self.info.rrn_b),
            "telco": 2
        }
        try:
            # POST 요청
            response = requests.post(url, headers=headers, json=data)
            # 응답 상태 코드 확인
            result = response.json()
            print(result)
            if 'txSeqNo' in result:
                parameter_value = result['txSeqNo']
                self.info.txseqno.append(parameter_value)
            print(self.info.txseqno)
        except Exception as e:
            print("요청 실패:", str(e))


    # def user_Id_Get(self):
    #     # network_logs = self.driver.stop_recording_network()
    #     # for log in network_logs:
    #     #     if log['method'] == 'POST' and log['url'] == 'https://service-api.finda.co.kr/account/v4/user/login':
    #     #         response_data = log['response']['body']
    #     #         # 필요한 API 응답 파라미터 값을 추출하여 리스트에 저장
    #     #         parameter_value = response_data['userId']
    #     #         self.info.user_id.append(parameter_value)
    #     # print(self.info.user_id)
    #     print("시작")
    #     log_data = """[통신 로그 데이터]"""  # 앱의 통신 로그 데이터를 문자열 형식으로 가져옵니다.
    #
    #     api_response = re.search(r'"POST/account/v4/user/login"\s*:\s*({.*?})', log_data)
    #     print(api_response)
    #     response_data = json.loads(api_response.group(1))
    #     print(response_data)
    #
    #     user_id = response_data["userId"]
    #     print(user_id)





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