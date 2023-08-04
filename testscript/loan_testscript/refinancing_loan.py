import time


from appium.webdriver.common.mobileby import MobileBy


from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.loan import Loan


class RefinancingLoan:

    def __init__(self):
        self.loan = Loan()
        self.info = InFo()

    def loan_re_view_bottomsheet(self):
        loan_re_view_bottomsheet = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_re_view_bottomsheet)
        loan_re_view_bottomsheet.click()
        time.sleep(3)

    # 대출 목적 > 대환대출 선택
    def refinancing_loan(self):
        refinancing_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.refinancing_loan)
        refinancing_loan.click()
        time.sleep(2)

    # 대출 갈아타기 선택
    def refinancing_loan_transfer(self):
        refinancing_loan_transfer = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.refinancing_loan_transfer)
        refinancing_loan_transfer.click()
        time.sleep(10)

    # 미입력 정보 입력
    def please_enter(self):
        please_enter = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.please_enter)
        please_enter.click()
        time.sleep(10)

    # 직장이 없어요 선택
    def no_job(self):
        no_job = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.no_job)
        no_job.click()
        time.sleep(2)
        auto_loan_terms_check = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_check)
        auto_loan_terms_check.click()
        time.sleep(3)

    # 소유 차량이 없어요
    def no_car(self):
        no_car = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.no_car)
        no_car.click()
        time.sleep(2)
        auto_loan_terms_check = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_terms_check)
        auto_loan_terms_check.click()
        time.sleep(3)

    # 내 최대 한도 확인하기
    def check_max_limit(self):
        check_max_limit = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check_max_limit)
        check_max_limit.click()
        time.sleep(2)

    # 대환대출 약관 전체 동의 선택
    def refinancing_loan_full_terms(self):
        full_terms = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.full_terms)
        full_terms.click()
        time.sleep(2)
        check_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check_loan)
        check_loan.click()
        time.sleep(2)
