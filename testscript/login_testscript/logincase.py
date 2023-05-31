import re
import time
from appium import webdriver

from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

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
        # desired_caps = {
        #     "appium:device": self.info.devices,
        #     "platformName": "Android",
        #     "appium:ensureWebviewsHavePages": True,
        #     "appium:nativeWebScreenshot": True,
        #     "appium:newCommandTimeout": 3600,
        #     "appium:connectHardwareKeyboard": True,
        #     'appActivity': '.ui.splash.SplashActivity',
        #     'noReset': 'true',
        #     "appPackage": "kr.co.finda.finda"
        #     # "appActivity": "kr.co.finda.finda.ui.main.MainActivity"
        # }
        # self.wd = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    #다음버튼 선택
    def join_Next(self):
        next_button = WebDriver.driver.find_element(MobileBy.XPATH, self.main.next_button)
        next_button.click()
        time.sleep(2)

    # 앱 실행
    def appStart(self):
        FindaApp = WebDriver.driver.find_element(MobileBy.XPATH, self.main.findaapp)
        FindaApp.click()
        time.sleep(5)
    # def appStart(self):
    #     # WebDriver.driver.start_activity('kr.co.finda.finda', '.ui.splash.SplashActivity')
    #     # time.sleep(5)
    #
    #     self.wd.start_activity('kr.co.finda.finda', '.ui.splash.SplashActivity')
    #     time.sleep(5)
    #     # self.wd.quit()

    # 핀코드 입력
    def pinCode(self):
        pincode = WebDriver.driver.find_element(MobileBy.XPATH, self.main.pincode)
        for i in range(6):
            pincode.click()
            time.sleep(1)

    #온보딩 페이지 시작하기 버튼 선택
    def start_Onboarding(self):
        start_onboarding = WebDriver.driver.find_element(MobileBy.XPATH, self.main.start_onboarding)
        start_onboarding.click()
        time.sleep(2)

    #악성앱 찾기 버튼 선택
    def malicious_App_Search(self):
        malicious_app_search_button = WebDriver.driver.find_element(MobileBy.XPATH, self.main.malicious_app_search_button)
        malicious_app_search_button.click()
        time.sleep(15)

    # MO인증 동작
    def message_Certification(self):
        message_certification = WebDriver.driver.find_element(MobileBy.XPATH, self.main.message_certification)
        message_certification.click()
        time.sleep(5)
        send_message = WebDriver.driver.find_element(MobileBy.XPATH, self.main.send_message)
        send_message.click()
        time.sleep(10)

    # 개인정보 입력
    def enter_Personal_Information(self):
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

    #회원가입 약관 진입
    def membership_Terms_And_Conditions_A(self):
        membership_terms_and_conditions_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_a)
        membership_terms_and_conditions_a.click()
        time.sleep(1)

    def membership_Terms_And_Conditions_B(self):
        membership_terms_and_conditions_b = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_b)
        membership_terms_and_conditions_b.click()
        time.sleep(1)

    def membership_Terms_And_Conditions_C(self):
        membership_terms_and_conditions_c = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_c)
        membership_terms_and_conditions_c.click()
        time.sleep(1)

    def membership_Terms_And_Conditions_C_A(self):
        membership_terms_and_conditions_c_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_c_a)
        membership_terms_and_conditions_c_a.click()
        time.sleep(1)

    def membership_Terms_And_Conditions_D(self):
        membership_terms_and_conditions_d = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_d)
        membership_terms_and_conditions_d.click()
        time.sleep(1)

    def membership_Terms_And_Conditions_Aa(self):
        membership_terms_and_conditions_aa = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_aa)
        membership_terms_and_conditions_aa.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_Ab(self):
        membership_terms_and_conditions_ab = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ab)
        membership_terms_and_conditions_ab.click()
        time.sleep(5)
        
    def membership_Terms_And_Conditions_Ac(self):
        membership_terms_and_conditions_ac = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ac)
        membership_terms_and_conditions_ac.click()
        time.sleep(5)
        
    def membership_Terms_And_Conditions_Ba(self):
        membership_terms_and_conditions_ba = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ba)
        membership_terms_and_conditions_ba.click()
        time.sleep(5)
        
    def membership_Terms_And_Conditions_Bb(self):
        membership_terms_and_conditions_bb = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_bb)
        membership_terms_and_conditions_bb.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_Bc(self):
        membership_terms_and_conditions_bc = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_bc)
        membership_terms_and_conditions_bc.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_ca(self):
        membership_terms_and_conditions_ca = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ca)
        membership_terms_and_conditions_ca.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_cb(self):
        membership_terms_and_conditions_cb = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cb)
        membership_terms_and_conditions_cb.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_cc(self):
        membership_terms_and_conditions_cc = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cc)
        membership_terms_and_conditions_cc.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_cd(self):
        membership_terms_and_conditions_cd = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_cd)
        membership_terms_and_conditions_cd.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_ce(self):
        membership_terms_and_conditions_ce = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_ce)
        membership_terms_and_conditions_ce.click()
        time.sleep(5)

    def membership_Terms_And_Conditions_da(self):
        membership_terms_and_conditions_da = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_da)
        membership_terms_and_conditions_da.click()
        time.sleep(5)

    #회원가입 > 약관 동의 후 확인 버튼 선택
    def membership_Terms_And_Conditions_All(self):
        membership_terms_and_conditions_all = WebDriver.driver.find_element(MobileBy.XPATH, self.main.membership_terms_and_conditions_all)
        membership_terms_and_conditions_all.click()
        check = WebDriver.driver.find_element(MobileBy.XPATH, self.main.check)
        check.click()

    #회원가입 인증번호 리스트 저장 => 사용함
    def join_Mms(self):
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
        message_content = WebDriver.driver.find_element(MobileBy.ID, "com.samsung.android.messaging:id/content_text_view")
        verification_code = re.search(r'(?<=<#>\[핀다\] 인증번호\[).+?(?=\])', message_content.text).group()
        self.main.verification_codes.append(verification_code)
        print(self.main.verification_codes)
        time.sleep(5)
        mms_set = WebDriver.driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="대화 설정"]')
        mms_set.click()
        time.sleep(2)
        mms_del = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="메시지 삭제"]')
        mms_del.click()
        time.sleep(2)
        mms_dele = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text="모두 삭제"]')
        mms_dele.click()
        time.sleep(5)

    #인증번호 재요청
    def re_Request_Verification_Code(self):
        Re_request_verification_code = WebDriver.driver.find_element(MobileBy.XPATH, self.main.Re_request_verification_code)
        Re_request_verification_code.click()
        time.sleep(5)

    #지문인증 사용여부 선택
    def use_Fingerprint(self):
        use_fingerprint = WebDriver.driver.find_element(MobileBy.XPATH, self.main.use_fingerprint)
        use_fingerprint.click()

    #로그아웃
    def logOut(self):
        logout = WebDriver.driver.find_element(MobileBy.XPATH, self.main.logout)
        logout.click()
        time.sleep(2)
        logout_a = WebDriver.driver.find_element(MobileBy.XPATH, self.main.logout)
        logout_a.click()

    #회원탈퇴
    def withdrawal(self):
        # etc_in = WebDriver.driver.find_element(MobileBy.XPATH, self.etc.etc)
        # etc_in.click()
        # time.sleep(2)
        # seting_buttun = WebDriver.driver.find_element(MobileBy.XPATH, self.etc.seting_buttun)
        # seting_buttun.click()
        # time.sleep(2)
        # self.base.scroll(2)
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






