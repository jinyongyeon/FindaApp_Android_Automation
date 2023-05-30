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

    def test_LoanDiagnosisBanner(self):
        driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        verification_list_a = [("30일 안에 대출 갈아타기\n지금 도전하세요", home.loandiagnosisbanner_a),
                             ("챌린지 시작하기", home.loandiagnosisbanner_aa)]
        verification_list_b = [("늘어난 대출이자에\n힘드신가요?", home.loandiagnosisbanner_b),
                             ("클릭 한번에 대출 관리 시작하기", home.loandiagnosisbanner_bb)]
        try:
            for text, xpath in verification_list_a:
                try:
                    result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result_a.text)
                    results.append("PASS")
                    myhome.loanDiagnosisBanner_A()
                except AssertionError:
                    results.append("FAIL")
        except:
            try:
                for text, xpath in verification_list_b:
                    try:
                        result_b = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                        self.assertIn(text, result_b.text)
                        results.append("PASS")
                        myhome.loanDiagnosisBanner_B()
                    except AssertionError:
                        results.append("FAIL")
            except:
                try:
                    result_c = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_c)
                    self.assertIn("한도조회 누적 달성 1회", result_c.text)
                    results.append("PASS")
                    myhome.loanDiagnosisBanner_C()
                except AssertionError:
                    results.append("FAIL")
                except:
                    try:
                        result_d = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_d)
                        self.assertIn("한도조회 누적 달성 2회", result_d.text)
                        results.append("PASS")
                        myhome.loanDiagnosisBanner_D()
                    except AssertionError:
                        results.append("FAIL")
                    except:
                        try:
                            result_e = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_e)
                            self.assertIn("한도조회 누적 달성 3회", result_e.text)
                            results.append("PASS")
                            myhome.loanDiagnosisBanner_E()
                        except AssertionError:
                            results.append("FAIL")
                        except:
                            try:
                                result_f = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_f)
                                self.assertIn("한도조회 누적 달성 4회", result_f.text)
                                results.append("PASS")
                                myhome.loanDiagnosisBanner_F()
                            except AssertionError:
                                results.append("FAIL")
                            except Exception as e:
                                print("대출진단 배너 노출 에러 발생 : {}".format(str(e)))
                                results.append("Error")
        print(results)
        if all(result == "PASS" for result in results):
            print("대출진단 배너 노출 : PASS")
            result_myhome.reports.append("대출진단 배너 노출 : *PASS*")
        else:
            print("대출진단 배너 노출 : FAIL")
            result_myhome.reports.append("대출진단 배너 노출 : *FAIL*")

        try:
            result_A = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_a)
            self.assertIn("내 대출 계좌 연결하기", result_A.text)
            print("대출진단 배너 진입 : PASS")
            result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
        except AssertionError:
            print("대출진단 배너 진입 : FAIL")
            result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
        except:
            try:
                result_B = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_b)
                self.assertIn("챌린지 시작하기", result_B.text)
                print("대출진단 배너 진입 : PASS")
                result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
            except AssertionError:
                print("대출진단 배너 진입 : FAIL")
                result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
            except:
                try:
                    result_C = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge)
                    self.assertIn("30일 대환 챌린지", result_C.text)
                    print("대출진단 배너 진입 : PASS")
                    result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                except AssertionError:
                    print("대출진단 배너 진입 : FAIL")
                    result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                except:
                    try:
                        result_D = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_a)
                        self.assertIn("챌린지를 시작하면 이자를\n연 최대 331만원 아낄 수 있어요!", result_D.text)
                        print("대출진단 배너 진입 : PASS")
                        result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                    except AssertionError:
                        print("대출진단 배너 진입 : FAIL")
                        result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                    except:
                        try:
                            result_E = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_b)
                            self.assertIn("당신은 Lv.1 될성부른 꿈나무", result_E.text)
                            print("대출진단 배너 진입 : PASS")
                            result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                        except AssertionError:
                            print("대출진단 배너 진입 : FAIL")
                            result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                        except:
                            try:
                                result_F = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                         home.refinance_loan_challenge_c)
                                self.assertIn("당신은 Lv.2 성실한 우등생", result_F.text)
                                print("대출진단 배너 진입 : PASS")
                                result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                            except AssertionError:
                                print("대출진단 배너 진입 : FAIL")
                                result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                            except:
                                try:
                                    result_G = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                             home.refinance_loan_challenge_d)
                                    self.assertIn("당신은 Lv.3 만랩 마스터", result_G.text)
                                    print("대출진단 배너 진입 : PASS")
                                    result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                                except AssertionError:
                                    print("대출진단 배너 진입 : FAIL")
                                    result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                                except Exception as e:
                                    print("대출진단 배너 진입 에러 발생 : {}".format(str(e)))
                                    results.append("Error")
        base.android_Back()

    def test_Loan_Banner(self):
        driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        etc = Etc()
        results = []
        results_a = []
        base.scroll(0.4)
        verification_list = [("내 대출 2", home.loan_banner),
                             ("주택도시기금 청년취업(창업) 전세자금대출", home.loan_a),
                             ("1.3%", home.loan_aa),
                             ("주택도시기금 버팀목전세자금(신혼가구)", home.loan_b),
                             ("2.1%", home.loan_bb)]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, result_a.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception as e:
                print("내 대출 배너 노출 에러 발생 : {}".format(str(e)))
                results.append("Error")
        print(results)
        if all(result == "PASS" for result in results):
            print("내 대출 배너 노출 : PASS")
            result_myhome.reports.append("내 대출 배너 노출 : *PASS*")
        else:
            print("내 대출 배너 노출 : FAIL")
            result_myhome.reports.append("내 대출 배너 노출 : *FAIL*")

        myhome.loan_Banner()
        verification_list_a = [("내 현금흐름", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
        for text, xpath in verification_list_a:
            try:
                result_b = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, result_b.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
            except Exception as e:
                print("내 대출 배너 진입 에러 발생 : {}".format(str(e)))
                results.append("Error")
        print(results_a)
        if all(result == "PASS" for result in results_a):
            print("내 대출 배너 진입 : PASS")
            result_myhome.reports.append("내 대출 배너 진입 : *PASS*")
        else:
            print("내 대출 배너 진입 : FAIL")
            result_myhome.reports.append("내 대출 배너 진입 : *FAIL*")
        base.android_Back()
        # myhome.loan_A
        # try:
        #     result_c = WebDriver.driver.find_element(MobileBy.XPATH, home.loan_a)
        #     self.assertIn("주택도시기금 청년취업(창업) 전세자금대출", result_c.text)
        #     print("내 대출 배너 > 대출 상세_a 진입 : PASS")
        #     result_myhome.reports.append("내 대출 배너 > 대출 상세_a 진입 : *PASS*")
        # except AssertionError:
        #     print("내 대출 배너 > 대출 상세_a 진입 : FAIL")
        #     result_myhome.reports.append("내 대출 배너 > 대출 상세_a 진입 : *FAIL*")
        # except Exception as e:
        #     print("내 대출 배너 > 대출 상세_a 진입 에러 발생 : {}".format(str(e)))
        #     results.append("Error")
        # base.android_Back()
        # time.sleep(2)
        #
        # myhome.loan_B
        # try:
        #     result_d = WebDriver.driver.find_element(MobileBy.XPATH, home.loan_a)
        #     self.assertIn("주택도시기금 버팀목전세자금(신혼가구)", result_d.text)
        #     print("내 대출 배너 > 대출 상세_b 진입 : PASS")
        #     result_myhome.reports.append("내 대출 배너 > 대출 상세_b 진입 : *PASS*")
        # except AssertionError:
        #     print("내 대출 배너 > 대출 상세_b 진입 : FAIL")
        #     result_myhome.reports.append("내 대출 배너 > 대출 상세_b 진입 : *FAIL*")
        # except Exception as e:
        #     print("내 대출 배너 > 대출 상세_b 진입 에러 발생 : {}".format(str(e)))
        #     results.append("Error")
        # base.android_Back()


    def test_Cash_Assets_Banner(self):
        driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        # base.scroll(0.6)
        time.sleep(2)
        verification_list = [("내 현금자산 3", home.cash_assets_banner),
                             ("입출금 2", home.cash_assets_banner_a),
                             ("예적금 1", home.cash_assets_banner_b)]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, result_a.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception as e:
                print("내 현금자산 배너 노출 에러 발생 : {}".format(str(e)))
                results.append("Error")
        print(results)
        if all(result == "PASS" for result in results):
            print("내 현금자산 배너 노출 : PASS")
            result_myhome.reports.append("내 현금자산 배너 노출 : *PASS*")
        else:
            print("내 현금자산 배너 노출 : FAIL")
            result_myhome.reports.append("내 현금자산 배너 노출 : *FAIL*")

        myhome.cash_Assets_Banner()
        try:
            result_b = WebDriver.driver.find_element(MobileBy.XPATH, home.cash_assets_banner_result)
            self.assertIn("진용연님의 현금자산은", result_b.text)
            print("내 현금자산 배너 진입_a : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_a : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_a : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_a : *FAIL*")
        except Exception as e:
            print("내 현금자산 배너 진입_a 에러 발생 : {}".format(str(e)))
            result_myhome.results.append("내 현금자산 배너 진입_a : Error")
        base.android_Back()
        myhome.cash_Assets_Banner_A()
        try:
            result_c = WebDriver.driver.find_element(MobileBy.XPATH, home.cash_assets_banner_a_result)
            self.assertIn("저축예금", result_c.text)
            print("내 현금자산 배너 진입_b : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_b : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_b : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_b : *FAIL*")
        except Exception as e:
            print("내 현금자산 배너 진입_b 에러 발생 : {}".format(str(e)))
            result_myhome.results.append("내 현금자산 배너 진입_b : Error")
        base.android_Back()
        myhome.cash_Assets_Banner_B()
        try:
            result_d = WebDriver.driver.find_element(MobileBy.XPATH, home.cash_assets_banner_b_result)
            self.assertIn("청년 우대형 주택청약종합저축", result_d.text)
            print("내 현금자산 배너 진입_c : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_c : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_c : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_c : *FAIL*")
        except Exception as e:
            print("내 현금자산 배너 진입_c 에러 발생 : {}".format(str(e)))
            result_myhome.results.append("내 현금자산 배너 진입_c : Error")
        base.android_Back()



if __name__ == '__main__':
    unittest.main()