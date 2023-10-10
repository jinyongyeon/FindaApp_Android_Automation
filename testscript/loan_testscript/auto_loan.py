import logging
import time
from datetime import date
import pickle

import requests
from appium.webdriver.common.mobileby import MobileBy


from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.loan import Loan


class Auto_Loan:

    # 초기화
    def __init__(self):
        self.loan = Loan()
        self.info = InFo()

    # 자동차 대출 약관
    def auto_loan_terms_of_use(self):
        try:
            auto_loan_inquiry = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_inquiry)
            auto_loan_inquiry.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_of_use : {e}")
    def auto_loan_terms_a_unfold(self):
        try:
            auto_loan_terms_a_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_a_unfold)
            auto_loan_terms_a_unfold.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_a_unfold : {e}")
    def auto_loan_terms_aa(self):
        try:
            auto_loan_terms_aa = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_aa)
            auto_loan_terms_aa.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_aa : {e}")
    def auto_loan_terms_ab(self):
        try:
            auto_loan_terms_ab = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ab)
            auto_loan_terms_ab.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ab : {e}")
    def auto_loan_terms_ac(self):
        try:
            auto_loan_terms_ac = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ac)
            auto_loan_terms_ac.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ac : {e}")
    def auto_loan_terms_ad(self):
        try:
            auto_loan_terms_ad = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ad)
            auto_loan_terms_ad.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ad : {e}")
    def auto_loan_terms_ae(self):
        try:
            auto_loan_terms_ae = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ae)
            auto_loan_terms_ae.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ae : {e}")
    def auto_loan_terms_b_unfold(self):
        try:
            auto_loan_terms_b_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_b_unfold)
            auto_loan_terms_b_unfold.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_b_unfold : {e}")
    def auto_loan_terms_ba(self):
        try:
            auto_loan_terms_ba = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ba)
            auto_loan_terms_ba.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ba : {e}")
    def auto_loan_terms_bb(self):
        try:
            auto_loan_terms_bb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_bb)
            auto_loan_terms_bb.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_bb : {e}")
    def auto_loan_terms_c_unfold(self):
        try:
            auto_loan_terms_c_unfold = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_c_unfold)
            auto_loan_terms_c_unfold.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_c_unfold : {e}")
    def auto_loan_terms_ca(self):
        try:
            auto_loan_terms_ca = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ca)
            auto_loan_terms_ca.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ca : {e}")
    def auto_loan_terms_cb(self):
        try:
            auto_loan_terms_cb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cb)
            auto_loan_terms_cb.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_cb : {e}")
    def auto_loan_terms_cc(self):
        try:
            auto_loan_terms_cc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cc)
            auto_loan_terms_cc.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_cc : {e}")
    def auto_loan_terms_cd(self):
        try:
            auto_loan_terms_cd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cd)
            auto_loan_terms_cd.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_cd : {e}")
    def auto_loan_terms_ce(self):
        try:
            auto_loan_terms_ce = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_ce)
            auto_loan_terms_ce.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_ce : {e}")
    def auto_loan_terms_cf(self):
        try:
            auto_loan_terms_cf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_cf)
            auto_loan_terms_cf.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_cf : {e}")
    def auto_loan_terms_all(self):
        try:
            auto_loan_terms_all = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_all)
            auto_loan_terms_all.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_all : {e}")
    def auto_loan_terms_check(self):
        try:
            auto_loan_terms_check = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_check)
            auto_loan_terms_check.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_check : {e}")
    def auto_loan_terms_next(self):
        try:
            auto_loan_terms_next = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_next)
            auto_loan_terms_next.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_terms_next : {e}")
    # 주민등록번호 뒷자리 입력
    def auto_loan_rrn(self):
        try:
            auto_loan_rrn = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_rrn)
            auto_loan_rrn.send_keys(self.info.autoloan_rrn)
        except Exception as e:
            logging.error(f"auto_loan_rrn : {e}")
    #오토론 연소득 입력
    def auto_loan_annual_income(self):
        try:
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
        except Exception as e:
            logging.error(f"auto_loan_annual_income : {e}")
    def auto_loan_new(self):
        try:
            auto_loan_new = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_new)
            auto_loan_new.click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"auto_loan_new : {e}")
    def auto_loan_newcar(self):
        try:
            auto_loan_newcar = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_newcar)
            auto_loan_newcar.click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"auto_loan_newcar : {e}")
    def auto_loan_detail(self):
        try:
            auto_loan_detail = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_detail)
            auto_loan_detail.click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"auto_loan_detail : {e}")
    def auto_loan_application(self):
        try:
            auto_loan_application = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_application)
            auto_loan_application.click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"auto_loan_application : {e}")
    def auto_loan_application_exit(self):
        try:
            auto_loan_application_exit = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_application_exit)
            auto_loan_application_exit.click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"auto_loan_application_exit : {e}")
    def auto_loan_new_used_car(self):
        # API 엔드포인트 URL

        # 오늘 날짜를 가져옵니다.
        today = date.today()

        # day 변수에 오늘 날짜를 넣습니다.
        day = today.isoformat()
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        url = "https://service-api.finda.co.kr/autoloan/v1/application"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            "annualSalary": 10000000,
            "applicationTerms": [
                {
                    "termsId": 265,
                    "termsYn": "true"
                },
                {
                    "termsId": 266,
                    "termsYn": "true"
                },
                {
                    "termsId": 267,
                    "termsYn": "true"
                },
                {
                    "termsId": 268,
                    "termsYn": "true"
                },
                {
                    "termsId": 276,
                    "termsYn": "true"
                },
                {
                    "termsId": 300,
                    "termsYn": "true"
                },
                {
                    "termsId": 301,
                    "termsYn": "true"
                },
                {
                    "termsId": 302,
                    "termsYn": "true"
                },
                {
                    "termsId": 303,
                    "termsYn": "true"
                },
                {
                    "termsId": 304,
                    "termsYn": "true"
                },
                {
                    "termsId": 305,
                    "termsYn": "true"
                },
                {
                    "termsId": 306,
                    "termsYn": "true"
                },
                {
                    "termsId": 307,
                    "termsYn": "true"
                }
            ],
            "autoReleaseDate": ''.join(day),
            "idToken": ''.join(self.info.idtoken),
            "loanAutoType": "USED",
            "loanCategoryType": "NEW",
            "rrn": ''.join(self.info.rrnfull)
        }
        try:

            response = requests.post(url, headers=headers, json=data, verify=False)
            result = response.json()
            print(result)

        except Exception as e:
            logging.error(f"auto_loan_new_used_car API요청 실패 : {e}")

    def auto_loan_existing_new_car(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/autoloan/v1/application"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            "annualSalary": 10000000,
            "applicationTerms": [
                {
                    "termsId": 265,
                    "termsYn": "true"
                },
                {
                    "termsId": 266,
                    "termsYn": "true"
                },
                {
                    "termsId": 267,
                    "termsYn": "true"
                },
                {
                    "termsId": 268,
                    "termsYn": "true"
                },
                {
                    "termsId": 276,
                    "termsYn": "true"
                },
                {
                    "termsId": 300,
                    "termsYn": "true"
                },
                {
                    "termsId": 301,
                    "termsYn": "true"
                },
                {
                    "termsId": 302,
                    "termsYn": "true"
                },
                {
                    "termsId": 303,
                    "termsYn": "true"
                },
                {
                    "termsId": 304,
                    "termsYn": "true"
                },
                {
                    "termsId": 305,
                    "termsYn": "true"
                },
                {
                    "termsId": 306,
                    "termsYn": "true"
                },
                {
                    "termsId": 307,
                    "termsYn": "true"
                }
            ],
            "autoNo": ''.join(self.info.autoNo),
            "idToken": ''.join(self.info.idtoken),
            "loanAutoType": "NEW",
            "loanCategoryType": "REDEMP",
            "rrn": ''.join(self.info.rrnfull)
        }
        try:

            response = requests.post(url, headers=headers, json=data, verify=False)
            result = response.json()
            print(result)

        except Exception as e:
            logging.error(f"auto_loan_existing_new_car API 요청 실패 : {e}")

    def auto_loan_existing_used_car(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/autoloan/v1/application"

        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
            "annualSalary": 10000000,
            "applicationTerms": [
                {
                    "termsId": 265,
                    "termsYn": "true"
                },
                {
                    "termsId": 266,
                    "termsYn": "true"
                },
                {
                    "termsId": 267,
                    "termsYn": "true"
                },
                {
                    "termsId": 268,
                    "termsYn": "true"
                },
                {
                    "termsId": 276,
                    "termsYn": "true"
                },
                {
                    "termsId": 300,
                    "termsYn": "true"
                },
                {
                    "termsId": 301,
                    "termsYn": "true"
                },
                {
                    "termsId": 302,
                    "termsYn": "true"
                },
                {
                    "termsId": 303,
                    "termsYn": "true"
                },
                {
                    "termsId": 304,
                    "termsYn": "true"
                },
                {
                    "termsId": 305,
                    "termsYn": "true"
                },
                {
                    "termsId": 306,
                    "termsYn": "true"
                },
                {
                    "termsId": 307,
                    "termsYn": "true"
                }
            ],
            "autoNo": ''.join(self.info.autoNo),
            "idToken": ''.join(self.info.idtoken),
            "loanAutoType": "USED",
            "loanCategoryType": "REDEMP",
            "rrn": ''.join(self.info.rrnfull)
        }
        try:

            response = requests.post(url, headers=headers, json=data, verify=False)
            result = response.json()
            print(result)

        except Exception as e:
            logging.error(f"auto_loan_existing_used_car API 요청 실패 : {e}")