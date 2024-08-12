import logging
import time
import pickle

from selenium.webdriver.support import expected_conditions as EC
import requests
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

from config.info import InFo
from pages.basemethod.base import basemethod
from pages.mainlocator.home import Home
from drivers.aos_webdrivers import WebDriver


class MyHome:
    def __init__(self):
        self.home = Home()
        self.info = InFo()
        self.base = basemethod()

    # 마이홈 메뉴바 왼쪽으로 스크롤
    def menu_right_to_left(self):
        action = TouchAction(WebDriver.driver)
        action_a = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '대출갈아타기')]")
        action_b = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '대출받기')]")
        action.press(action_a).move_to(action_b).release()
        return action.perform()

    # 마이홈 메뉴바 오른쪽으로 스크롤
    def menu_left_to_right(self):
        action = TouchAction(WebDriver.driver)
        action_a = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '대출갈아타기')]")
        action_b = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '차 구매대출')]")
        action.press(action_a).move_to(action_b).release()
        return action.perform()

    def menu_loan(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_a)).click()
        time.sleep(2)

    def menu_refinance_loan(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_b)).click()
        time.sleep(2)

    def menu_business_loan(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_c)).click()
        time.sleep(2)

    def menu_home_equity_loan(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_d)).click()
        time.sleep(2)

    def menu_car_loan(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_e)).click()
        time.sleep(2)

    def menu_auto_lease(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.quick_menu_f)).click()
        time.sleep(2)

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

    def comPariSonLoan_In_f(self):
        loans = WebDriver.driver.find_element(MobileBy.XPATH, self.home.loans_f)
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

    # 신용점수 가져오기
    def credit_score_get(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        url = "https://service-api.finda.co.kr/pf/v2/personalcredit/kcb-data"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {"Content-Type": "application/json",
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
            logging.info(result)
            credit_score = result["creditSummary"]["creditScore"]
            self.info.credit_score.append(credit_score)
            logging.info(credit_score)
            print(credit_score)
        except Exception as e:
            logging.error(f"credit_score 요청실패 : {e}")
            print(f"credit_score 요청실패 : {e}")


    # 신용점수 진입
    def credit_score(self):
        a = 3
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(
                    EC.visibility_of_element_located(self.home.credit_score)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 상환 일정 노출 확인
    def home_loan_data_api_a(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/ams/v1/home/assets-info"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        logging.info(result)
        print(result)

        assetType_A = []
        loan_A = []
        loan_B = []

        if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
            assetType = result['data']['repayPlanInfo'][0]['assetList'][0]['assetType']
            assetType_A.append(assetType)
        assetType_b = "".join(map(str, assetType_A))
        print(assetType_b)
        if assetType_b == "LOAN":
            if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
                loanname = result['data']['repayPlanInfo'][0]['assetList'][0]['productName']
                loan_A.append(loanname)
                print(loan_A)
                loanname_A = "".join(map(str, loan_A))
                loan = MobileBy.XPATH, "//*[contains(@text, '"+loanname_A+"')]"
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))
        else:
            if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
                loanname = result['data']['repayPlanInfo'][0]['assetList'][0]['orgName']
                loan_B.append(loanname)
                print(loan_B)
                loanname_B = "".join(map(str, loan_B))
                loan = MobileBy.XPATH, "//*[contains(@text, '"+loanname_B+"')]"
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))

    def home_loan_data_api_b(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/ams/v1/home/assets-info"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": ''.join(usertoken)
                   }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        logging.info(result)
        print(result)

        assetType_A = []
        loan_A = []
        loan_B = []

        if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
            try:
                assetType = result['data']['repayPlanInfo'][0]['assetList'][1]['assetType']
                assetType_A.append(assetType)
                assetType_b = "".join(map(str, assetType_A))
                print(assetType_b)
                if assetType_b == "LOAN":
                    if 'data' in result and len(result['repayPlanInfo']) > 0:
                        loanname = result['data']['repayPlanInfo'][0]['assetList'][1]['productName']
                        loan_A.append(loanname)
                        print(loan_A)
                        loanname_A = "".join(map(str, loan_A))
                        loan = MobileBy.XPATH, "//*[contains(@text, '" + loanname_A + "')]"
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))
                else:
                    if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
                        loanname = result['data']['repayPlanInfo'][0]['assetList'][1]['orgName']
                        loan_B.append(loanname)
                        print(loan_B)
                        loanname_B = "".join(map(str, loan_B))
                        loan = MobileBy.XPATH, "//*[contains(@text, '" + loanname_B + "')]"
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))
            except:
                assetType = result['data']['repayPlanInfo'][1]['assetList'][0]['assetType']
                assetType_A.append(assetType)
                assetType_b = "".join(map(str, assetType_A))
                print(assetType_b)
                if assetType_b == "LOAN":
                    if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
                        loanname = result['data']['repayPlanInfo'][1]['assetList'][0]['productName']
                        loan_A.append(loanname)
                        print(loan_A)
                        loanname_A = "".join(map(str, loan_A))
                        loan = MobileBy.XPATH, "//*[contains(@text, '"+loanname_A+"')]"
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))
                else:
                    if 'data' in result and 'repayPlanInfo' in result['data'] and len(result['data']['repayPlanInfo']) > 0:
                        loanname = result['data']['repayPlanInfo'][1]['assetList'][0]['orgName']
                        loan_B.append(loanname)
                        print(loan_B)
                        loanname_B = "".join(map(str, loan_B))
                        loan = MobileBy.XPATH, "//*[contains(@text, '"+loanname_B+"')]"
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan)).click()
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(loan))

    # 마이홈 금융생활 쓸 수 있는 현금 노출 및 진입
    def home_cash(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/ams/v1/home/assets-info"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        logging.info(result)
        print(result)
        cash = []
        if 'data' in result and 'totalCheckingAccountBalanceAmount' in result['data']:
            data_cash = result['data']['totalCheckingAccountBalanceAmount']
            cash.append(data_cash)
            print(cash)
        data_cash_a = "".join(map(str, cash))
        all_cash = f"{int(data_cash_a):,}원"
        print(all_cash)
        c = MobileBy.XPATH, "//*[contains(@text, '"+all_cash+"')]"
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(c)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")
        time.sleep(4)
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(c))

    # 마이홈 금융생활 카드 사용금액 노출 및 진입
    def home_card(self):
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
        # API 엔드포인트 URL
        url = "https://service-api.finda.co.kr/ams/v1/home/assets-info"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(usertoken)
                    }
        # 요청 본문 데이터 (필요에 따라 사용)
        data = {
        }
        response = requests.get(url, headers=headers, json=data, verify=False)
        # 응답 상태 코드 확인
        result = response.json()
        logging.info(result)
        print(result)
        card = []
        if 'data' in result and 'totalCardPayAmount' in result['data']:
            data_card = result['data']['totalCardPayAmount']
            card.append(data_card)
            print(card)
        data_card_a = "".join(map(str, card))
        all_card = f"{int(data_card_a):,}원"
        print(all_card)
        c = MobileBy.XPATH, "//*[contains(@text, '"+all_card+"')]"
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(c)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")
        time.sleep(4)

    def loan_Banner(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.loan_banner)).click()
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
        logging.info(result)
        if 'list' in result and len(result['list']) > 0:
            first_product_name = result['list'][0]['productName']
            self.info.loans_data.append(first_product_name)
        data_result = "".join(map(str, self.info.loans_data))
        logging.info(data_result)
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
        try:
        # POST 요청
            response = requests.get(url, headers=headers, json=data, verify=False)
            # 응답 상태 코드 확인
            result = response.json()
            logging.info(result)
            if 'list' in result and len(result['list']) > 1:
                first_product_name = result['list'][1]['productName']
                self.info.loans_data.append(first_product_name)
            data_result = "".join(map(str, self.info.loans_data))
            logging.info(data_result)
            loan = WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '"+data_result+"')]")
            loan.click()
        except Exception as e:
            logging.error(f"loan_B 요청 실패 : {e}")
        time.sleep(2)

    # 내 현금자산 배너
    def cash_Assets_Banner(self):
        try:
            cash_assets_banner = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner)
            cash_assets_banner.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"cash_Assets_Banner : {e}")
    def cash_Assets_Banner_A(self):
        try:
            cash_assets_banner_a = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner_a)
            cash_assets_banner_a.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"cash_Assets_Banner_A : {e}")
    def cash_Assets_Banner_B(self):
        try:
            cash_assets_banner_b = WebDriver.driver.find_element(MobileBy.XPATH, self.home.cash_assets_banner_b)
            cash_assets_banner_b.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"cash_Assets_Banner_B : {e}")

    # 상환예정 배너
    def notification_Enabled_On(self):
        try:
            notification_enabled_on = WebDriver.driver.find_element(MobileBy.XPATH, self.home.notification_enabled_on)
            notification_enabled_on.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"notification_Enabled_On : {e}")
    def notification_Enabled_Off(self):
        try:
            notification_enabled_off = WebDriver.driver.find_element(MobileBy.XPATH, self.home.notification_enabled_off)
            notification_enabled_off.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"notification_Enabled_Off")

    # 오토리스 배너
    def Lease_Contract_Banner(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.lease_contract_banner)).click()
        time.sleep(7)


    # 자동차 대출 배너
    def auto_Loan_Banner(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.home.auto_loan_banner)).click()
        time.sleep(2)