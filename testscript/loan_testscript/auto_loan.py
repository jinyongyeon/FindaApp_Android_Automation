import time
from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait

from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.mainlocator.loan import Loan


class Auto_Loan:

    # 초기화
    def __init__(self):
        self.loan = Loan()

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