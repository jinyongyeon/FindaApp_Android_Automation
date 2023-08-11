import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More, Result_loan, Result_refinancing_loan
from pages.mainlocator.loan import Loan
from testscript.loan_testscript.loan_comparison import ComparisonLoan
from testscript.loan_testscript.refinancing_loan import RefinancingLoan
from testscript.login_testscript.logincase import JoIn
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod
from testscript.more_testscript.seting import Seting
from testscript.myhome_testscript.myhome import MyHome


class Refinancing_Loan_Testcase(unittest.TestCase):

    # 대환대출 재한도 조회
    def test_refinancing_loan_mydata_connected(self):
        loan = Loan()
        base = basemethod()
        resultrefinancing = Result_refinancing_loan()
        refinancingloan = RefinancingLoan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        try:
            myhome.comPariSonLoan_In_a()
        except:
            try:
                myhome.comPariSonLoan_In_b()
            except:
                try:
                    myhome.comPariSonLoan_In_c()
                except:
                    try:
                        myhome.comPariSonLoan_In_d()
                    except:
                        try:
                            myhome.comPariSonLoan_In_e()
                        except Exception as e:
                            print("비교대출 배너 진입 에러 발생 : {}".format(str(e)))
        time.sleep(10)
        try:
            refinancingloan.refinancing_loan_transfer()
        except:
            try:
                refinancingloan.loan_re_view_bottomsheet()
                time.sleep(4)
                refinancingloan.refinancing_loan_transfer()
            except:
                try:
                    comparisonloan.loan_in()
                    time.sleep(4)
                    refinancingloan.refinancing_loan()
                except:
                    base.scroll(2)
                    base.scroll(2)
                    base.scroll(2)
                    comparisonloan.lookup_again()
        time.sleep(3)
        refinancingloan.refinancing_loan_transfer()
        try:
            refinancingloan.refinancing_loan_transfer()
            try:
                refinancingloan.please_enter()
                try:
                    refinancingloan.no_job()
                except:
                    refinancingloan.no_car()
            except :
                pass
            time.sleep(5)
            try:
                refinancingloan.please_enter()
                try:
                    refinancingloan.no_job()
                except:
                    refinancingloan.no_car()
            except :
                pass
            time.sleep(5)
            refinancingloan.check_max_limit()
            refinancingloan.refinancing_loan_full_terms()
            time.sleep(10)
            comparisonloan.next_loan()
            time.sleep(5)
            comparisonloan.rrn_pass_input()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(100)

            try:
                result = WebDriver.driver.find_element(MobileBy.XPATH, loan.refinancing_loan_result)
                self.assertIn("대환대출", result.text)
                print("대환 대출 재 한도 조회 결과 : PASS")
                resultrefinancing.reports.append("대환 대출 재 한도 조회 결과 : *PASS*")
            except AssertionError:
                print("대환 대출 재 한도 조회 결과 : FAIL")
                resultrefinancing.reports.append("대환 대출 재 한도 조회 결과 : *FAIL*")
                base.save_screenshot('대환대출재한도조회_fail')
            except Exception as e:
                print("대환 대출 재 한도 조회 결과 에러 발생 : {}".format(str(e)))
                resultrefinancing.reports.append("대환 대출 재 한도 조회 결과 : *Error*")
                base.save_screenshot('대환대출재한도조회_error')
        except:
            print("대환 대출 재 한도 조회 결과 : 재한도 조회 진행 실패")
            resultrefinancing.reports.append("대환 대출 재 한도 조회 결과 : *재한도 조회 진행 실패*")
        base.android_back()
        base.android_back()

if __name__ == '__main__':
    unittest.main()