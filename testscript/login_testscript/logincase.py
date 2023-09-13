import re
import time
import subprocess
from appium.webdriver.common.mobileby import MobileBy
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
        next_button = WebDriver.driver.find_element(MobileBy.XPATH, self.main.next_button)
        next_button.click()
        time.sleep(2)

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
        pincode = WebDriver.driver.find_element(MobileBy.XPATH, self.main.pincode)
        for i in range(6):
            pincode.click()
            time.sleep(1)

    # 온보딩 페이지 시작하기 버튼 선택
    def start_onboarding(self):
        start_onboarding = WebDriver.driver.find_element(MobileBy.XPATH, self.main.start_onboarding)
        start_onboarding.click()
        time.sleep(2)

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # 악성앱 찾기 버튼 선택
    def malicious_app_search(self):
        try:
            malicious_app_search_button = WebDriver.driver.find_element(MobileBy.XPATH, self.main.malicious_app_search_button)
            malicious_app_search_button.click()
        except:
            print("악성앱찾기서버 : FAIL")
        time.sleep(20)

    # MO 인증 동작
    def message_certification(self):
        message_certification = WebDriver.driver.find_element(MobileBy.XPATH, self.main.message_certification)
        message_certification.click()
        time.sleep(5)
        send_message = WebDriver.driver.find_element(MobileBy.XPATH, self.main.send_message)
        send_message.click()
        time.sleep(10)

    # 개인 정보 입력
    def enter_personal_information(self):
        name = WebDriver.driver.find_element(MobileBy.XPATH, self.main.name)
        name.send_keys(self.info.name)
        next_button = WebDriver.driver.find_element(MobileBy.XPATH, self.main.next_button)
        next_button.click()
        rrn_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.rrn_a)
        rrn_a.send_keys(self.info.rrn_a)
        rrn_b = WebDriver.driver.find_element(MobileBy.XPATH, self.main.rrn_b)
        rrn_b.send_keys(self.info.rrn_b)
        time.sleep(1)
        kt = WebDriver.driver.find_element(MobileBy.XPATH, self.main.kt)
        kt.click()
        time.sleep(2)
        # next_button.click()

    # 회원 가입 약관 진입
    def membership_terms_and_conditions_a(self):
        membership_terms_and_conditions_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_a)
        membership_terms_and_conditions_a.click()
        time.sleep(1)

    def membership_terms_and_conditions_b(self):
        membership_terms_and_conditions_b = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_b)
        membership_terms_and_conditions_b.click()
        time.sleep(1)

    def membership_terms_and_conditions_c(self):
        membership_terms_and_conditions_c = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_c)
        membership_terms_and_conditions_c.click()
        time.sleep(1)

    def membership_terms_and_conditions_c_a(self):
        membership_terms_and_conditions_c_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_c_a)
        membership_terms_and_conditions_c_a.click()
        time.sleep(1)

    def membership_terms_and_conditions_d(self):
        membership_terms_and_conditions_d = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_d)
        membership_terms_and_conditions_d.click()
        time.sleep(1)

    def membership_terms_and_conditions_aa(self):
        membership_terms_and_conditions_aa = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_aa)
        membership_terms_and_conditions_aa.click()
        time.sleep(5)

    def membership_terms_and_conditions_ab(self):
        membership_terms_and_conditions_ab = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ab)
        membership_terms_and_conditions_ab.click()
        time.sleep(5)
        
    def membership_terms_and_conditions_ac(self):
        membership_terms_and_conditions_ac = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ac)
        membership_terms_and_conditions_ac.click()
        time.sleep(5)
        
    def membership_terms_and_conditions_ba(self):
        membership_terms_and_conditions_ba = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ba)
        membership_terms_and_conditions_ba.click()
        time.sleep(5)
        
    def membership_terms_and_conditions_bb(self):
        membership_terms_and_conditions_bb = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_bb)
        membership_terms_and_conditions_bb.click()
        time.sleep(5)

    def membership_terms_and_conditions_bc(self):
        membership_terms_and_conditions_bc = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_bc)
        membership_terms_and_conditions_bc.click()
        time.sleep(5)

    def membership_terms_and_conditions_ca(self):
        membership_terms_and_conditions_ca = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ca)
        membership_terms_and_conditions_ca.click()
        time.sleep(5)

    def membership_terms_and_conditions_cb(self):
        membership_terms_and_conditions_cb = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cb)
        membership_terms_and_conditions_cb.click()
        time.sleep(5)

    def membership_terms_and_conditions_cc(self):
        membership_terms_and_conditions_cc = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cc)
        membership_terms_and_conditions_cc.click()
        time.sleep(5)

    def membership_terms_and_conditions_cd(self):
        membership_terms_and_conditions_cd = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cd)
        membership_terms_and_conditions_cd.click()
        time.sleep(5)

    def membership_terms_and_conditions_ce(self):
        membership_terms_and_conditions_ce = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ce)
        membership_terms_and_conditions_ce.click()
        time.sleep(5)

    def membership_terms_and_conditions_da(self):
        membership_terms_and_conditions_da = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_da)
        membership_terms_and_conditions_da.click()
        time.sleep(5)

    # 회원 가입 > 약관 동의 후 확인 버튼 선택
    def membership_terms_and_conditions_all(self):
        membership_terms_and_conditions_all = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_all)
        membership_terms_and_conditions_all.click()
        check = WebDriver.driver.find_element(MobileBy.XPATH, self.main.check)
        check.click()

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
        # SMS 데이터를 가져오는 ADB 명령 실행
        command = "adb shell content query --uri content://sms/inbox"
        sms_data = subprocess.check_output(command, shell=True).decode("utf-8")

        # SMS 데이터 파싱 및 필터링
        sms_messages = sms_data.strip().split("\n\n")  # 각 SMS 메시지는 빈 줄로 구분

        # address=027081007로 필터링된 메시지 찾기
        filtered_messages = [msg for msg in sms_messages if "address=027081007" in msg]

        # 필터링된 메시지 중에서 첫 번째 메시지에서 인증번호 추출 (정규 표현식 사용)
        if filtered_messages:
            first_message = filtered_messages[0]
            match = re.search(r'인증번호\[(\d+)\]', first_message)
            if match:
                authentication_code = match.group(1)
                self.main.verification_codes.append(authentication_code)
                print(self.main.verification_codes)
            else:
                print("첫 번째 메시지에서 인증번호를 찾을 수 없습니다.")
        else:
            print("address=027081007로 필터링된 메시지가 없습니다.")
        # WebDriver.driver.start_activity("com.samsung.android.messaging", "com.android.mms.ui.ConversationComposer")
        # time.sleep(3)
        # latest_message = WebDriver.driver.find_element(MobileBy.XPATH,'//android.widget.Button[@content-desc="검색"]')
        # latest_message.click()
        # time.sleep(2)
        # search_field = WebDriver.driver.find_element(MobileBy.XPATH,'//*[@text ="검색"]')
        # search_field.send_keys("02-708-100")
        # message_button = WebDriver.driver.find_element(MobileBy.XPATH,'//*[@text= "02-708-1007"]')
        # message_button.click()
        # time.sleep(5)
        # message_content = WebDriver.driver.find_element(MobileBy.ID, "com.samsung.android.messaging:id/content_text_view")
        # verification_code = re.search(r'(?<=<#>\[핀다\] 인증번호\[).+?(?=\])', message_content.text).group()
        # self.main.verification_codes.append(verification_code)
        # print(self.main.verification_codes)
        # time.sleep(5)
        # mms_set = WebDriver.driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="대화 설정"]')
        # mms_set.click()
        # time.sleep(2)
        # mms_del = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="메시지 삭제"]')
        # mms_del.click()
        # time.sleep(2)
        # mms_dele = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="모두 삭제"]')
        # mms_dele.click()
        # time.sleep(5)
        # self.base.android_back()
        # time.sleep(2)
        # self.base.android_back()
        # time.sleep(2)
        # self.base.android_back()
        # time.sleep(2)

    # 인증 번호 재요청
    def re_request_verification_code(self):
        Re_request_verification_code = WebDriver.driver.find_element(MobileBy.XPATH, self.main.Re_request_verification_code)
        Re_request_verification_code.click()
        time.sleep(5)

    # 지문 인증 사용 여부 선택
    def use_fingerprint(self):
        use_fingerprint = WebDriver.driver.find_element(MobileBy.XPATH, self.main.use_fingerprint)
        use_fingerprint.click()

    # 로그 아웃
    def log_out(self):
        logout = WebDriver.driver.find_element(MobileBy.XPATH, self.main.logout)
        logout.click()
        time.sleep(2)
        logout_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.logout)
        logout_a.click()

    # 회원 탈퇴
    def withdrawal(self):
        withdrawal = WebDriver.driver.find_element(MobileBy.XPATH, self.main.withdrawal)
        withdrawal.click()
        time.sleep(2)
        withdrawal_agreement = WebDriver.driver.find_element(MobileBy.XPATH, self.main.withdrawal_agreement)
        withdrawal_agreement.click()
        time.sleep(1)
        withdraw = WebDriver.driver.find_element(MobileBy.XPATH, self.main.withdraw)
        withdraw.click()
        time.sleep(2)
        withdraw_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.withdraw)
        withdraw_a.click()
        time.sleep(7)
        check = WebDriver.driver.find_element(MobileBy.XPATH, self.main.check)
        check.click()






