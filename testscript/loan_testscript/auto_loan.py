import time
from telnetlib import EC
import requests


from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.mainlocator.loan import Loan


class Auto_Loan:

    # 초기화
    def __init__(self):
        self.loan = Loan()
        self.info = InFo()


    # 자동차 대출 약관
    def autoLoan_Terms_Of_Use(self):
        auto_loan_inquiry = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_inquiry)
        auto_loan_inquiry.click()
        time.sleep(2)
    def auto_Loan_Terms_A_Unfold(self):
        auto_loan_terms_a_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_a_unfold)
        auto_loan_terms_a_unfold.click()
        time.sleep(2)
    def auto_Loan_Terms_Aa(self):
        auto_loan_terms_aa = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_aa)
        auto_loan_terms_aa.click()
        time.sleep(2)
    def auto_Loan_Terms_Ab(self):
        auto_loan_terms_ab = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ab)
        auto_loan_terms_ab.click()
        time.sleep(2)
    def auto_Loan_Terms_Ac(self):
        auto_loan_terms_ac = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ac)
        auto_loan_terms_ac.click()
        time.sleep(2)
    def auto_Loan_Terms_Ad(self):
        auto_loan_terms_ad = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ad)
        auto_loan_terms_ad.click()
        time.sleep(2)
    def auto_Loan_Terms_Ae(self):
        auto_loan_terms_ae = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ae)
        auto_loan_terms_ae.click()
        time.sleep(2)
    def auto_Loan_Terms_B_Unfold(self):
        auto_loan_terms_b_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_b_unfold)
        auto_loan_terms_b_unfold.click()
        time.sleep(2)
    def auto_Loan_Terms_Ba(self):
        auto_loan_terms_ba = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ba)
        auto_loan_terms_ba.click()
        time.sleep(2)
    def auto_Loan_Terms_Bb(self):
        auto_loan_terms_bb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_bb)
        auto_loan_terms_bb.click()
        time.sleep(2)
    def auto_Loan_Terms_C_Unfold(self):
        auto_loan_terms_c_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_c_unfold)
        auto_loan_terms_c_unfold.click()
        time.sleep(2)
    def auto_Loan_Terms_Ca(self):
        auto_loan_terms_ca = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ca)
        auto_loan_terms_ca.click()
        time.sleep(2)
    def auto_Loan_Terms_Cb(self):
        auto_loan_terms_cb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cb)
        auto_loan_terms_cb.click()
        time.sleep(2)
    def auto_Loan_Terms_Cc(self):
        auto_loan_terms_cc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cc)
        auto_loan_terms_cc.click()
        time.sleep(2)
    def auto_Loan_Terms_Cd(self):
        auto_loan_terms_cd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cd)
        auto_loan_terms_cd.click()
        time.sleep(2)
    def auto_Loan_Terms_Ce(self):
        auto_loan_terms_ce = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ce)
        auto_loan_terms_ce.click()
        time.sleep(2)
    def auto_Loan_Terms_Cf(self):
        auto_loan_terms_cf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cf)
        auto_loan_terms_cf.click()
        time.sleep(2)
    def auto_Loan_Terms_All(self):
        auto_loan_terms_all = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_all)
        auto_loan_terms_all.click()
        time.sleep(2)
    def auto_Loan_Terms_Check(self):
        auto_loan_terms_check = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_check)
        auto_loan_terms_check.click()
        time.sleep(2)
    def auto_Loan_Terms_Next(self):
        auto_loan_terms_next = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_next)
        auto_loan_terms_next.click()
        time.sleep(2)

    # 주민등록번호 뒷자리 입력
    def auto_Loan_Rrn(self):
        auto_loan_rrn = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_rrn)
        # auto_loan_rrn.send_keys("0")
        auto_loan_rrn.click()
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(2)
    def auto_Loan_Annual_Income(self):
        auto_loan_annual_income = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_annual_income)
        auto_loan_annual_income.click()
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
    def auto_Loan_New(self):
        auto_loan_new = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_new)
        auto_loan_new.click()
        time.sleep(1)
    def auto_Loan_Newcar(self):
        auto_loan_newcar = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_newcar)
        auto_loan_newcar.click()
        time.sleep(1)
    def auto_Loan_Detail(self):
        auto_loan_detail = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_detail)
        auto_loan_detail.click()
        time.sleep(1)
    def auto_Loan_Application(self):
        auto_loan_application = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_application)
        auto_loan_application.click()
        time.sleep(1)
    def auto_Loan_Application_Exit(self):
        auto_loan_application_exit = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_application_exit)
        auto_loan_application_exit.click()
        time.sleep(1)


    def auto_Loan_New_UsedCar(self):
        # API 엔드포인트 URL
        url = "https://stg-service-api.finda.co.kr/account/v1/user/token"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {
            "Content-Type" : "application/json"
        }

        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            "userId": 2000936,
            "encryptedPincode": "91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203"

        }


        try:
            # GET 요청
            # response = requests.get(url, headers=headers, json=data)

            # POST 요청
            response = requests.post(url, headers=headers, json=data)

            # 응답 상태 코드 확인

            # print(response.json)

            result = response.json()
            print(result)

            # if response.status_code == 200:
            #     # 응답 데이터 가져오기
            #     result = response.json()
            #     # 결과 처리
            #     print(result)
            # else:
            #     print("요청 실패:", response.status_code)


        except Exception as e:
            print("요청 실패:", str(e))

    # def auto_Loan_existing_NewCar(self):

    # def auto_Loan_existing_UsedCar(self):