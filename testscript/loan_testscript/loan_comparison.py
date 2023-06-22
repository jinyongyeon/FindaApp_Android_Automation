import time

import requests
from appium.webdriver.common.mobileby import MobileBy


from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.loan import Loan


class ComparisonLoan:

    def __init__(self):
        self.loan = Loan()
        self.info = InFo()

    # 다음 버튼
    def next_Loan(self):
        next_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.next_loan)
        next_loan.click()

    # 확인 버튼
    def check_Loan(self):
        check_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check_loan)
        check_loan.click()


            # 비교대출 온보딩 페이지에서 대출 목정페이지로 진입
    def loan_In(self):
        loan_in = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_in)
        loan_in.click()

    # 생활비 선택 및 대출 희망금액 입력
    def living_Expenses(self):
        living_expenses = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.living_expenses)
        living_expenses.click()
        loan_amount = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_amount)
        loan_amount.click()
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)

    #비교대출 약관
    def loan_Terms_And_Conditions_A(self):
        loan_terms_and_conditions_A = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_A)
        loan_terms_and_conditions_A.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Aa(self):
        loan_terms_and_conditions_Aa = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Aa)
        loan_terms_and_conditions_Aa.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ab(self):
        loan_terms_and_conditions_Ab = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ab)
        loan_terms_and_conditions_Ab.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ac(self):
        loan_terms_and_conditions_Ac = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ac)
        loan_terms_and_conditions_Ac.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ad(self):
        loan_terms_and_conditions_Ad = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ad)
        loan_terms_and_conditions_Ad.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ae(self):
        loan_terms_and_conditions_Ae = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ae)
        loan_terms_and_conditions_Ae.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_B(self):
        loan_terms_and_conditions_B = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_B)
        loan_terms_and_conditions_B.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Ba(self):
        loan_terms_and_conditions_Ba = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ba)
        loan_terms_and_conditions_Ba.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bb(self):
        loan_terms_and_conditions_Bb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bb)
        loan_terms_and_conditions_Bb.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bc(self):
        loan_terms_and_conditions_Bc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bc)
        loan_terms_and_conditions_Bc.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bd(self):
        loan_terms_and_conditions_Bd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bd)
        loan_terms_and_conditions_Bd.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Be(self):
        loan_terms_and_conditions_Be = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Be)
        loan_terms_and_conditions_Be.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bf(self):
        loan_terms_and_conditions_Bf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bf)
        loan_terms_and_conditions_Bf.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_C(self):
        loan_terms_and_conditions_C = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_C)
        loan_terms_and_conditions_C.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Ca(self):
        loan_terms_and_conditions_Ca = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ca)
        loan_terms_and_conditions_Ca.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cb(self):
        loan_terms_and_conditions_Cb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cb)
        loan_terms_and_conditions_Cb.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cc(self):
        loan_terms_and_conditions_Cc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cc)
        loan_terms_and_conditions_Cc.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cd(self):
        loan_terms_and_conditions_Cd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cd)
        loan_terms_and_conditions_Cd.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ce(self):
        loan_terms_and_conditions_Ce = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ce)
        loan_terms_and_conditions_Ce.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cf(self):
        loan_terms_and_conditions_Cf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cf)
        loan_terms_and_conditions_Cf.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cg(self):
        loan_terms_and_conditions_Cg = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cg)
        loan_terms_and_conditions_Cg.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ch(self):
        loan_terms_and_conditions_Ch = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ch)
        loan_terms_and_conditions_Ch.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ci(self):
        loan_terms_and_conditions_Ci = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ci)
        loan_terms_and_conditions_Ci.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cj(self):
        loan_terms_and_conditions_Cj = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cj)
        loan_terms_and_conditions_Cj.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ck(self):
        loan_terms_and_conditions_Ck = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ck)
        loan_terms_and_conditions_Ck.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cl(self):
        loan_terms_and_conditions_Cl = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cl)
        loan_terms_and_conditions_Cl.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cm(self):
        loan_terms_and_conditions_Cm = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cm)
        loan_terms_and_conditions_Cm.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_D(self):
        loan_terms_and_conditions_D = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_D)
        loan_terms_and_conditions_D.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Da(self):
        loan_terms_and_conditions_Da = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Da)
        loan_terms_and_conditions_Da.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_All(self):
        loan_terms_and_conditions_all = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_all)
        loan_terms_and_conditions_all.click()
        time.sleep(2)

    def comparison_Loan_Verification_Resend(self):
        comparison_loan_verification_resend = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.comparison_loan_verification_resend)
        comparison_loan_verification_resend.click()
        time.sleep(2)

    def rrn_Fail_Input(self):
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)

    def rrn_Pass_Input(self):
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
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