import re
import time
import subprocess
import logging
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.mainlocator.etc import Etc
from pages.mainlocator.main import Main


class JoIn:

    def __init__(self):
        self.main = Main()
        self.info = InFo()
        self.base = basemethod()
        self.etc = Etc()

    # 다음버튼 선택
    def join_next(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.next_button)).click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"join_next : {e}")

    # 앱 종료
    def app_quit(self):
        self.result = subprocess.run(
            ['adb', 'shell', 'am', 'force-stop', f'{"kr.co.finda.finda"}'])
        time.sleep(3)

    # 앱 실행
    def app_start(self):
        self.result = subprocess.run(['adb', 'shell', 'am', 'start', '-n',f'{"kr.co.finda.finda"}/{".feature.splash.SplashActivity"}'])
        time.sleep(5)

    # 핀코드 입력
    def pin_code(self):
        try:
            pincode = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.pincode))
            for i in range(6):
                pincode.click()
                time.sleep(1)
        except Exception as e:
            logging.error(f"pin_code : {e}")

    # 온보딩 페이지 시작하기 버튼 선택
    def start_onboarding(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.start_onboarding)).click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"start_onboarding : {e}")

    # 악성앱 찾기 버튼 선택
    def malicious_app_search(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.malicious_app_search_button)).click()
        except:
            logging.warning("악성앱찾기서버 : FAIL")
        time.sleep(20)

    # MO 인증 동작
    def message_certification(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.message_certification)).click()
            time.sleep(5)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.send_message)).click()
            time.sleep(10)
        except Exception as e:
            logging.error(f"message_certification : {e}")

    # 개인 정보 입력
    def enter_personal_information(self):
        try:
            name = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.name))
            name.send_keys(self.info.name)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.next_button)).click()
            rrn_a = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.rrn_a))
            rrn_a.send_keys(self.info.rrn_a)
            rrn_b = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.rrn_b))
            rrn_b.send_keys(self.info.rrn_b)
            time.sleep(1)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.kt)).click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"enter_personal_information : {e}")
        # next_button.click()

    # 회원 가입 약관 진입
    def membership_terms_and_conditions_a(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_a)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_a : {e}")

    def membership_terms_and_conditions_b(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_b)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_b : {e}")

    def membership_terms_and_conditions_c(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_c)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_c : {e}")

    def membership_terms_and_conditions_c_a(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_c_a)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_c_a : {e}")

    def membership_terms_and_conditions_d(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_d)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_d : {e}")

    def membership_terms_and_conditions_aa(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_aa)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_aa : {e}")

    def membership_terms_and_conditions_ab(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_ab)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_ab : {e}")
        
    def membership_terms_and_conditions_ac(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_ac)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_ac : {e}")
        
    def membership_terms_and_conditions_ba(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_ba)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_ba : {e}")
        
    def membership_terms_and_conditions_bb(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_bb)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_bb : {e}")

    def membership_terms_and_conditions_bc(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_bc)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_bc : {e}")

    def membership_terms_and_conditions_ca(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_ca)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_ca : {e}")

    def membership_terms_and_conditions_cb(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_cb)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_cb : {e}")

    def membership_terms_and_conditions_cc(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_cc)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_cc : {e}")

    def membership_terms_and_conditions_cd(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_cd)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_cd : {e}")

    def membership_terms_and_conditions_ce(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_ce)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_ce : {e}")

    def membership_terms_and_conditions_da(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_da)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_da : {e}")

    # 회원 가입 > 약관 동의 후 확인 버튼 선택
    def membership_terms_and_conditions_all(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.membership_terms_and_conditions_all)).click()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.check)).click()
        except Exception as e:
            logging.error(f"membership_terms_and_conditions_all : {e}")

    # 회원 가입 > 인증 번호 초기화
    def join_mms_delete(self):
        WebDriver.driver.start_activity("com.samsung.android.messaging", "com.android.mms.ui.ConversationComposer")
        time.sleep(3)
        latest_message = WebDriver.driver.find_element(MobileBy.XPATH,'//android.widget.Button[@content-desc="검색"]')
        latest_message.click()
        time.sleep(2)
        search_field = WebDriver.driver.find_element(MobileBy.XPATH,'//*[@text ="검색"]')
        search_field.send_keys("02-708-100")
        message_button = WebDriver.driver.find_element(MobileBy.XPATH,'//*[@text= "02-708-1007"]')
        message_button.click()
        time.sleep(5)
        mms_set = WebDriver.driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="대화 설정"]')
        mms_set.click()
        time.sleep(2)
        mms_del = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="메시지 삭제"]')
        mms_del.click()
        time.sleep(2)
        mms_all_del = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="전체"]')
        mms_all_del.click()
        time.sleep(2)
        mms_dele = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="모두 삭제"]')
        mms_dele.click()
        time.sleep(5)
        self.base.android_back()
        time.sleep(2)
        self.base.android_back()
        time.sleep(2)
        self.base.android_back()
        time.sleep(2)

    # 회원 가입 > 인증 번호 리스트 저장 => 사용함
    def join_mms(self):
        time.sleep(10)
        command = "adb shell content query --uri content://sms/inbox"
        sms_data = subprocess.check_output(command, shell=True).decode("utf-8")
        sms_messages = sms_data.strip().split("\n\n")  # 각 SMS 메시지는 빈 줄로 구분
        filtered_messages = [msg for msg in sms_messages if "address=027081007" in msg]
        if filtered_messages:
            first_message = filtered_messages[0]
            match = re.search(r'인증번호\[(\d+)\]', first_message)
            if match:
                authentication_code = match.group(1)
                self.main.verification_codes.append(authentication_code)
                logging.info(self.main.verification_codes)
            else:
                logging.error("첫 번째 메시지에서 인증번호를 찾을 수 없습니다.")
        else:
            logging.error("address=027081007로 필터링된 메시지가 없습니다.")

    # 인증 번호 재요청
    def re_request_verification_code(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.Re_request_verification_code)).click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"re_request_verification_code : {e}")

    # 지문 인증 사용 여부 선택
    def use_fingerprint(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.use_fingerprint)).click()
        except Exception as e:
            logging.error(f"use_fingerprint : {e}")

    # 로그 아웃
    def log_out(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.logout)).click()
            time.sleep(2)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.logout)).click()
        except Exception as e:
            logging.error(f"log_out : {e}")

    # 회원 탈퇴
    def withdrawal(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.withdrawal)).click()
            time.sleep(2)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.withdrawal_agreement)).click()
            time.sleep(1)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.withdraw)).click()
            time.sleep(2)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.withdraw)).click()
            time.sleep(7)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.main.check)).click()
        except Exception as e:
            logging.error(f"withdrawal : {e}")