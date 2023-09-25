import time
import pickle

import requests
from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo
from pages.mainlocator.home import Home
from drivers.aos_webdrivers import WebDriver


class MyHome:
    def __init__(self):
        self.home = Home()
        self.info = InFo()

    # 비교대출 배너
    def comPariSonLoan_In_a(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_a)
        loans.click()
        time.sleep(2)
    def comPariSonLoan_In_b(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_b)
        loans.click()
        time.sleep(2)
    def comPariSonLoan_In_c(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_c)
        loans.click()
        time.sleep(2)
    def comPariSonLoan_In_d(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_d)
        loans.click()
        time.sleep(2)
    def comPariSonLoan_In_e(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_e)
        loans.click()
        time.sleep(2)

    # 대출진단 배너
    def loanDiagnosisBanner_A(self):
        loandiagnosisbanner_a = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_aa)
        loandiagnosisbanner_a.click()
        time.sleep(2)
    def loanDiagnosisBanner_B(self):
        loandiagnosisbanner_b = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_bb)
        loandiagnosisbanner_b.click()
        time.sleep(2)

    def loanDiagnosisBanner_G(self):
        loandiagnosisbanner_g = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_gg)
        loandiagnosisbanner_g.click()
        time.sleep(2)

    def loanDiagnosisBanner_C(self):
        loandiagnosisbanner_c = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_c)
        loandiagnosisbanner_c.click()
        time.sleep(2)
    def loanDiagnosisBanner_D(self):
        loandiagnosisbanner_d = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_d)
        loandiagnosisbanner_d.click()
        time.sleep(2)
    def loanDiagnosisBanner_E(self):
        loandiagnosisbanner_e = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_e)
        loandiagnosisbanner_e.click()
        time.sleep(2)
    def loanDiagnosisBanner_F(self):
        loandiagnosisbanner_f = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_f)
        loandiagnosisbanner_f.click()
        time.sleep(2)

    def loanDiagnosisBanner_H(self):
        loandiagnosisbanner_h = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loandiagnosisbanner_h)
        loandiagnosisbanner_h.click()
        time.sleep(2)

    # 내대출 진입
    def loan_data_api(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        try:
            # POST 요청
            response = requests.get(url, headers=headers, json=data, verify=False)
            # 응답 상태 코드 확인
            result = response.json()
            print(result)
            if 'list' in result and len(result['list']) > 0:
                first_product_name = result['list'][0]['productName']
                self.info.loans_data.append(first_product_name)
            print(self.info.loans_data)
            loans_data_a = "".join(map(str, self.info.loans_data))
            print(loans_data_a)
            if 'list' in result and len(result['list']) > 0:
                first_product_name_a = result['list'][0]['interestRate']
                self.info.loans_data_b.append(first_product_name_a)
            print(self.info.loans_data_b)
            loans_data_c = "".join(map(str, self.info.loans_data_b))
            print(loans_data_c)

        except Exception as e:
            print("요청 실패:", str(e))
    def loan_Banner(self):
        loan_banner = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loan_banner)
        loan_banner.click()
        time.sleep(2)
    def loan_A(self):
        self.info.loans_data.clear()
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": ''.join(usertoken)
                   }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        # POST 요청
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        print(result)
        if 'list' in result and len(result['list']) > 0:
            first_product_name = result['list'][0]['productName']
            self.info.loans_data.append(first_product_name)
        data_result = "".join(map(str, self.info.loans_data))
        print(data_result)
        loan = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '"+data_result+"')]")
        loan.click()
        time.sleep(2)
    def loan_B(self):
        self.info.loans_data.clear()
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": ''.join(usertoken)
                   }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        # POST 요청
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        print(result)
        if 'list' in result and len(result['list']) > 1:
            first_product_name = result['list'][1]['productName']
            self.info.loans_data.append(first_product_name)
        data_result = "".join(map(str, self.info.loans_data))
        print(data_result)
        loan = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '"+data_result+"')]")
        loan.click()
        time.sleep(2)

    # 내 현금자산 배너
    def cash_Assets_Banner(self):
        cash_assets_banner = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner)
        cash_assets_banner.click()
        time.sleep(2)
    def cash_Assets_Banner_A(self):
        cash_assets_banner_a = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner_a)
        cash_assets_banner_a.click()
        time.sleep(2)
    def cash_Assets_Banner_B(self):
        cash_assets_banner_b = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner_b)
        cash_assets_banner_b.click()
        time.sleep(2)

    # 상환예정 배너
    def notification_Enabled_On(self):
        notification_enabled_on = WebDriver.driver.find_element(MobileBy.XPATH, self.home.notification_enabled_on)
        notification_enabled_on.click()
        time.sleep(2)
    def notification_Enabled_Off(self):
        notification_enabled_off = WebDriver.driver.find_element(MobileBy.XPATH, self.home.notification_enabled_off)
        notification_enabled_off.click()
        time.sleep(2)

    # 오토리스 배너
    def Lease_Contract_Banner(self):
        lease_contract_banner = WebDriver.driver.find_element(MobileBy.XPATH, self.home.lease_contract_banner)
        lease_contract_banner.click()
        time.sleep(7)

    # 자동차 대출 배너
    def auto_Loan_Banner(self):
        auto_loan_banner = WebDriver.driver.find_element(MobileBy.XPATH, self.home.auto_loan_banner)
        auto_loan_banner.click()
        time.sleep(2)

