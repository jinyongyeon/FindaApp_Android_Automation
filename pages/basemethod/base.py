import logging
import subprocess
import time
import requests
import pickle
# import subprocess
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy
import os
from config.info import InFo
from drivers.aos_webdrivers import WebDriver
# from drivers.ChromeDriver import ChromeWebDriver
from appium.webdriver.common.touch_action import TouchAction
from pages.mainlocator.main import Main


class basemethod:

    def __init__(self):
        self.driver = WebDriver.driver
        self.info = InFo()
        self.main = Main()
        # self.chromedriver = ChromeWebDriver.driver
    def appium_run(self):
        appium_command = "appium -a 127.0.0.1 -p 4723 -pa /wd/hub"
        subprocess.Popen(appium_command, shell=True)

    def android_back(self):
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

    def scroll_right(self, scroll_distance):
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        # 스크롤할 거리 계산
        distance = int(width * scroll_distance)

        # 스크롤 이벤트 생성
        action = TouchAction(self.driver)

        # 시작 지점은 화면의 좌측 중간, 끝 지점은 화면의 우측 중간
        start_x = int(width * 0.8)  # 좌측 중간 (예: 디바이스 폭의 20%)
        start_y = int(height * 0.2)  # 화면 중간 (예: 디바이스 높이의 50%)

        end_x = int(width * 0.2)  # 우측 중간 (예: 디바이스 폭의 80%)
        end_y = int(height * 0.2)  # 화면 중간 유지

        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release()
        return action.perform()

    def scroll_left(self, scroll_distance):
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        # 스크롤할 거리 계산
        distance = int(width * scroll_distance)

        # 스크롤 이벤트 생성
        action = TouchAction(self.driver)

        # 시작 지점은 화면의 좌측 중간, 끝 지점은 화면의 우측 중간
        start_x = int(width * 0.2)  # 좌측 중간 (예: 디바이스 폭의 20%)
        start_y = int(height * 0.2)  # 화면 중간 (예: 디바이스 높이의 50%)

        end_x = int(width * 0.8)  # 우측 중간 (예: 디바이스 폭의 80%)
        end_y = int(height * 0.2)  # 화면 중간 유지

        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release()
        return action.perform()

    def save_screenshot(self, name):
        try:
            today_date = datetime.now().strftime("%Y-%m-%d")
            screenshot_dir = os.path.join('screenshots', today_date)
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, f'{name}.png')
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved: {screenshot_path}')
        except:
            logging.warning("개인정보관련 페이지로 캡처 불가능")

    def user_token_get(self):
        # API 엔드포인트 URL
        with open('user_id.pickle', 'rb') as f:
            user_id = pickle.load(f)
        url = "https://service-api.finda.co.kr/account/v1/user/token"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json"
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            # "userId": self.info.user_id,
            "userId": ''.join(user_id),
            "encryptedPincode": "3ea87a56da3844b420ec2925ae922bc731ec16a4fc44dcbeafdad49b0e61d39c"
        }
        try:
            # POST 요청
            response = requests.post(url, headers=headers, json=data, verify=False)
            # 응답 상태 코드 확인
            result = response.json()
            print(result)
            if 'token' in result:
                parameter_value = result['token']
                self.info.usertoken.append(parameter_value)
            logging.info(self.info.usertoken)
            with open('usertoken.pickle', 'wb') as f:
                pickle.dump(self.info.usertoken, f)
        except Exception as e:
            logging.error(f"요청 실패: {e}")

    def user_txseqno_get(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/idcert/v1/ids"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json",
            "X-Auth-Token" : ''.join(usertoken)
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
            response = requests.post(url, headers=headers, json=data, verify=False)
            # 응답 상태 코드 확인
            result = response.json()
            logging.info(result)
            if 'txSeqNo' in result:
                parameter_value = result['txSeqNo']
                self.info.txseqno.append(parameter_value)
            logging.info(self.info.txseqno)
        except Exception as e:
            logging.error(f"요청 실패 : {e}")

    def user_id_get(self):
        userid = MobileBy.XPATH, "//*[contains(@text, '사용자ID')]"
        text = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(userid)).text
        logging.info(text)
        self.info.user_id = ''.join(filter(str.isdigit, text))
        logging.info(self.info.user_id)
        with open('user_id.pickle', 'wb') as f:
            pickle.dump(self.info.user_id, f)


    def user_idtoken_get(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/idcert/v1/ids"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json",
            "X-Auth-Token" : ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            # "userId": self.info.user_id,
            "cellNumber": ''.join(self.info.phone_number),
            "optNo": ''.join(self.main.verification_codes),
            "txSeqNo": ''.join(self.info.txseqno)
        }
        try:
            # POST 요청
            response = requests.put(url, headers=headers, json=data, verify=False)
            # 응답 상태 코드 확인
            result = response.json()
            logging.info(result)
            if 'idToken' in result:
                parameter_value = result['idToken']
                self.info.idtoken.append(parameter_value)
            logging.info(self.info.idtoken)
        except Exception as e:
            logging.error(f"요청 실패: {e}")

    def context_switch_web(self):
        # 앱이 로드될 시간을 기다림
        time.sleep(5)

        # 현재 가능한 모든 컨텍스트 출력 (네이티브 앱, 웹뷰 포함)
        contexts = self.driver.contexts
        print("Available contexts:", contexts)

        # 웹뷰로 컨텍스트 전환
        webview_context = None
        for context in contexts:
            if 'WEBVIEW' in context:
                webview_context = context
                break

        if webview_context:
            self.driver.switch_to.context(webview_context)
            print("Switched to WebView context:", webview_context)
        else:
            print("No WebView context found")
            self.driver.quit()
            exit()

    def context_switch_app(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.quit()

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