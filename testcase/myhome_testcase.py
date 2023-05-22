import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.result import Result_MyHome
from pages.mainlocator import etc
from pages.mainlocator.etc import Etc
from pages.mainlocator.home import Home
from pages.basemethod.base import basemethod
from testscript.myhome_testscript.myhome import MyHome


class MyHome_Testcase(unittest.TestCase):

    # 마이홈 비교대출 배너 테스트
    def test_ComPariSonLoan(self):
        driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        etc = Etc()
        results = []
        try:
            myhome_loans_Result_a = WebDriver.driver.find_element(MobileBy.XPATH, home.myhome_loans_Result_a)
            self.assertEqual(myhome_loans_Result_a.text, "대출 한도 조회 📌")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            try:
                myhome_loans_Result_b = WebDriver.driver.find_element(MobileBy.XPATH, home.myhome_loans_Result_b)
                self.assertEqual(myhome_loans_Result_b.text, "대출 알아보기")
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception as e:
                print("비교대출 배너 노출_a 에러 발생 : {}".format(str(e)))
                results.append("Error")

        try:
            loans_a = WebDriver.driver.find_element(MobileBy.XPATH, home.loans_a)
            self.assertEqual(loans_a.text, "내 대출 한도 한번에 조회하기")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            try:
                loans_b = WebDriver.driver.find_element(MobileBy.XPATH, home.loans_b)
                self.assertEqual(loans_b.text, "내게 맞는 더 좋은 대출 찾기")
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except :
                try:
                    loans_c = WebDriver.driver.find_element(MobileBy.XPATH, home.loans_c)
                    self.assertEqual(loans_c.text, "다른 방법 알아보기")
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except :
                    try:
                        loans_d = WebDriver.driver.find_element(MobileBy.XPATH, home.loans_d)
                        self.assertEqual(loans_d.text, "나에게 딱 맞는 대출 찾기")
                        results.append("PASS")
                    except AssertionError:
                        results.append("FAIL")
                    except :
                        try:
                            loans_e = WebDriver.driver.find_element(MobileBy.XPATH, home.loans_e)
                            self.assertEqual(loans_e.text, "대출 이어서 진행하기")
                            results.append("PASS")
                        except AssertionError:
                            results.append("FAIL")
                        except Exception as e:
                            print("비교대출 배너 노출_b 에러 발생 : {}".format(str(e)))

        if all(result == "PASS" for result in results):
            print("비교대출 배너 노출 : PASS")
            result_myhome.reports.append("비교대출 배너 노출 : *PASS*")
        else:
            print("비교대출 배너 노출 : FAIL")
            result_myhome.reports.append("비교대출 배너 노출 : *FAIL*")

        try:
            myhome.comPariSonLoan_In_a()
        except :
            try:
                myhome.comPariSonLoan_In_b()
            except:
                try:
                    myhome.comPariSonLoan_In_c()
                except:
                    try:
                        myhome.comPariSonLoan_In_d()
                    except :
                        try:
                            myhome.comPariSonLoan_In_e()
                        except Exception as e:
                            print("비교대출 배너 진입 에러 발생 : {}".format(str(e)))

        time.sleep(4)
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_a)
            self.assertEqual(Result_A.text,"오늘의 내 최저금리 알아보기")
            print("비교 대출 배너 진입 : PASS")
            result_myhome.reports.append("비교 대출 배너 진입 : *PASS*")
        except AssertionError:
            print("비교 대출 배너 진입 : FAIL")
            result_myhome.reports.append("비교 대출 배너 진입 : *FAIL*")
        except :
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_b)
                self.assertIn("오늘입금" , Result_B.text)
                print("비교 대출 배너 진입 : PASS")
                result_myhome.reports.append("비교 대출 배너 진입 : *PASS*")
            except AssertionError:
                print("비교 대출 배너 진입 : FAIL")
                result_myhome.reports.append("비교 대출 배너 진입 : *FAIL*")
            except Exception as e:
                print("비교 대출 배너 진입 에러 발생 : {}".format(str(e)))
                result_myhome.reports.append("비교 대출 배너 진입 : *Error*")
        time.sleep(2)
        base.android_Back()


if __name__ == '__main__':
    unittest.main()