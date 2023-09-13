import time
import unittest

import requests
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.result import Result_MyHome
from pages.mainlocator import etc
from pages.mainlocator.etc import Etc
from pages.mainlocator.home import Home
from pages.basemethod.base import basemethod
from testscript.more_testscript.see_more import More
from testscript.more_testscript.seting import Seting
from testscript.myhome_testscript.myhome import MyHome


class MyHome_Testcase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("더보기 TestCase_A 시작")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("더보기 TestCase_A완료")
    #
    #
    # def setUp(self):
    #     base = basemethod()
    #     base.scroll(1)
    #     base.scroll(0.93)
    #
    def tearDown(self):
        base = basemethod()
        base.android_back()
        time.sleep(1)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 마이홈 비교대출 배너 테스트
    def test_comparison_loan(self):
        # driver = WebDriver.setUp()
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
            base.save_screenshot('비교대출배너노출_fail')

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
        time.sleep(10)
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_a)
            self.assertIn("오늘 내가 받을", Result_A.text)
            print("비교 대출 배너 진입 : PASS")
            result_myhome.reports.append("비교 대출 배너 진입 : *PASS*")
        except AssertionError:
            print("비교 대출 배너 진입 : FAIL")
            result_myhome.reports.append("비교 대출 배너 진입 : *FAIL*")
            base.save_screenshot('비교대출배너진입_fail')
        except :
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_b)
                self.assertIn("오늘입금" , Result_B.text)
                print("비교 대출 배너 진입 : PASS")
                result_myhome.reports.append("비교 대출 배너 진입 : *PASS*")
            except AssertionError:
                print("비교 대출 배너 진입 : FAIL")
                result_myhome.reports.append("비교 대출 배너 진입 : *FAIL*")
                base.save_screenshot('비교대출배너진입_fail')
            except Exception as e:
                print("비교 대출 배너 진입 에러 발생 : {}".format(str(e)))
                result_myhome.reports.append("비교 대출 배너 진입 : *Error*")
                base.save_screenshot('비교대출배너진입_error')
        time.sleep(2)
        base.android_back()

    # 마이홈 대출 진단 배너 테스트
    def test_loan_diagnosis_banner(self):
        # driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        base.scroll(0.04)
        verification_list_a = [("지금 도전하세요", home.loandiagnosisbanner_a),
                             ("챌린지", home.loandiagnosisbanner_aa)]
        verification_list_b = [("늘어난 대출이자에 힘드신가요?", home.loandiagnosisbanner_b),
                             ("클릭 한번에 대출 관리 시작하기", home.loandiagnosisbanner_bb)]
        verification_list_c = [("레벨업! 대환 챌린지", home.loandiagnosisbanner_g),
                             ("챌린지", home.loandiagnosisbanner_gg)]
        try:
            for text, xpath in verification_list_a:
                try:
                    result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result_a.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
            myhome.loanDiagnosisBanner_A()
        except :
            try:
                for text, xpath in verification_list_b:
                    try:
                        result_b = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                        self.assertIn(text, result_b.text)
                        results.append("PASS")
                    except AssertionError:
                        results.append("FAIL")
                myhome.loanDiagnosisBanner_B()
            except :
                try:
                    for text, xpath in verification_list_c:
                        try:
                            result_c = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                            self.assertIn(text, result_c.text)
                            results.append("PASS")
                        except AssertionError:
                            results.append("FAIL")
                    myhome.loanDiagnosisBanner_G()
                except:
                    try:
                        result_c = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_c)
                        self.assertIn("한도조회 누적 달성 1회", result_c.text)
                        results.append("PASS")
                        myhome.loanDiagnosisBanner_C()
                    except AssertionError:
                        results.append("FAIL")
                    except Exception:
                        try:
                            result_d = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_d)
                            self.assertIn("한도조회 누적 달성 2회", result_d.text)
                            results.append("PASS")
                            myhome.loanDiagnosisBanner_D()
                        except AssertionError:
                            results.append("FAIL")
                        except Exception:
                            try:
                                result_e = WebDriver.driver.find_element(MobileBy.XPATH, home.loandiagnosisbanner_e)
                                self.assertIn("한도조회 누적 달성 3회", result_e.text)
                                results.append("PASS")
                                myhome.loanDiagnosisBanner_E()
                            except AssertionError:
                                results.append("FAIL")
                            except Exception:
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
            base.save_screenshot('대출진단배너노출_fail')
        time.sleep(10)
        try:
            result_A = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_a)
            self.assertIn("내 대출 계좌 연결하기", result_A.text)
            print("대출진단 배너 진입 : PASS")
            result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
        except AssertionError:
            print("대출진단 배너 진입 : FAIL")
            result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
            base.save_screenshot('대출진단배너진입_fail')
        except Exception:
            try:
                result_B = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_b)
                self.assertIn("챌린지 시작", result_B.text)
                print("대출진단 배너 진입 : PASS")
                result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
            except AssertionError:
                print("대출진단 배너 진입 : FAIL")
                result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                base.save_screenshot('대출진단배너진입_fail')
            except Exception:
                try:
                    result_C = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge)
                    self.assertIn("대환 챌린지", result_C.text)
                    print("대출진단 배너 진입 : PASS")
                    result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                except AssertionError:
                    print("대출진단 배너 진입 : FAIL")
                    result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                    base.save_screenshot('대출진단배너진입_fail')
                except Exception:
                    try:
                        result_D = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_a)
                        self.assertIn("챌린지를 시작하면 이자를\n연 최대 331만원 아낄 수 있어요!", result_D.text)
                        print("대출진단 배너 진입 : PASS")
                        result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                    except AssertionError:
                        print("대출진단 배너 진입 : FAIL")
                        result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                        base.save_screenshot('대출진단배너진입_fail')
                    except Exception:
                        try:
                            result_E = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_b)
                            self.assertIn("당신은 Lv.1 될성부른 꿈나무", result_E.text)
                            print("대출진단 배너 진입 : PASS")
                            result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                        except AssertionError:
                            print("대출진단 배너 진입 : FAIL")
                            result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                            base.save_screenshot('대출진단배너진입_fail')
                        except Exception:
                            try:
                                result_F = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                         home.refinance_loan_challenge_c)
                                self.assertIn("당신은 Lv.2 성실한 우등생", result_F.text)
                                print("대출진단 배너 진입 : PASS")
                                result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                            except AssertionError:
                                print("대출진단 배너 진입 : FAIL")
                                result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                                base.save_screenshot('대출진단배너진입_fail')
                            except Exception:
                                try:
                                    result_G = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                             home.refinance_loan_challenge_d)
                                    self.assertIn("당신은 Lv.3 만랩 마스터", result_G.text)
                                    print("대출진단 배너 진입 : PASS")
                                    result_myhome.reports.append("대출진단 배너 진입 : *PASS*")
                                except AssertionError:
                                    print("대출진단 배너 진입 : FAIL")
                                    result_myhome.reports.append("대출진단 배너 진입 : *FAIL*")
                                    base.save_screenshot('대출진단배너진입_fail')
                                except Exception as e:
                                    print("대출진단 배너 진입 에러 발생 : {}".format(str(e)))
                                    results.append("Error")
                                    base.save_screenshot('대출진단배너진입_error')
        base.android_back()

    # 마이홈 내 대출 배너 테스트
    def test_loan_banner(self):
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        etc = Etc()
        more = More()
        info = InFo()
        seting = Seting()
        results = []
        results_a = []
        more.etc_in()
        seting.seting_in()
        base.scroll(2)
        base.user_id_get()
        base.user_token_get()
        base.android_back()
        base.android_back()
        url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(info.usertoken)
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
            info.loans_data.append(first_product_name)
        loans_data_a = "".join(map(str, info.loans_data))
        if 'list' in result and len(result['list']) > 0:
            first_product_name_a = result['list'][0]['interestRate']
            info.loans_data_b.append(first_product_name_a)
        loans_data_c = "".join(map(str, info.loans_data_b))
        print(loans_data_a)
        print(loans_data_c)

        base.scroll(0.6)
        verification_list = [(loans_data_a, "//*[contains(@text, '"+loans_data_a+"')]"),
                             (""+loans_data_c+"%", "//*[contains(@text, '"+loans_data_c+"%')]")]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertEqual(result_a.text, text)
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
            base.save_screenshot('내대출배너노출_fail')

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
            base.save_screenshot('내대출배너진입_fail')
        base.android_back()
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

    # 마이홈 내 현금 자산 배너 테스트
    def test_cash_assets_banner(self):
        # driver = WebDriver.setUp()
        myhome = MyHome()
        info = InFo()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        base.scroll(1)
        time.sleep(2)
        verification_list = [("내 현금자산", home.cash_assets_banner),
                             ("입출금", home.cash_assets_banner_a),
                             ("예적금", home.cash_assets_banner_b)]
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
            base.save_screenshot('내현금자산배너노출_fail')
        myhome.cash_Assets_Banner()
        try:
            result_b = WebDriver.driver.find_element(MobileBy.XPATH, home.cash_assets_banner_result)
            self.assertIn(""+info.name+"님의 현금자산은", result_b.text)
            print("내 현금자산 배너 진입_a : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_a : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_a : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_a : *FAIL*")
            base.save_screenshot('내현금자산배너진입_a_fail')
        except Exception as e:
            print("내 현금자산 배너 진입_a 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("내 현금자산 배너 진입_a : Error")
            base.save_screenshot('내현금자산배너진입_a_error')
        base.android_back()
        url = "https://service-api.finda.co.kr/ams/v1/checking"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(info.usertoken)
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
            info.loans_data_c.append(first_product_name)
        data_result = "".join(map(str, info.loans_data_c))
        print(data_result)
        myhome.cash_Assets_Banner_A()
        try:
            result_c = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text = "'+data_result+'"]')
            self.assertEqual(result_c.text , data_result)
            print("내 현금자산 배너 진입_b : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_b : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_b : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_b : *FAIL*")
            base.save_screenshot('내현금자산배너진입_b_fail')
        except Exception as e:
            print("내 현금자산 배너 진입_b 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("내 현금자산 배너 진입_b : Error")
            base.save_screenshot('내현금자산배너진입_b_error')
        base.android_back()
        url = "https://service-api.finda.co.kr/ams/v1/deposit-and-savings"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": ''.join(info.usertoken)
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
            info.loans_data_d.append(first_product_name)
        data_result_a = "".join(map(str, info.loans_data_d))
        print(data_result_a)
        myhome.cash_Assets_Banner_B()
        try:
            result_d = WebDriver.driver.find_element(MobileBy.XPATH, '//*[@text = "'+data_result_a+'"]')
            self.assertEqual(result_d.text, data_result_a)
            print("내 현금자산 배너 진입_c : PASS")
            result_myhome.reports.append("내 현금자산 배너 진입_c : *PASS*")
        except AssertionError:
            print("내 현금자산 배너 진입_c : FAIL")
            result_myhome.reports.append("내 현금자산 배너 진입_c : *FAIL*")
            base.save_screenshot('내현금자산배너진입_c_fail')
        except Exception as e:
            print("내 현금자산 배너 진입_c 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("내 현금자산 배너 진입_c : Error")
            base.save_screenshot('내현금자산배너진입_c_error')
        base.android_back()

    # 마이홈 상환예정 배너 테스트
    def test_repayment_schedule_banner(self):
        myhome = MyHome()
        home = Home()
        more = More()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        base.scroll(1)
        base.scroll(0.6)
        verification_list = [("상환 예정", home.repayment_schedule_banner),
                             ("알림 받기", home.notification_enabled_on)]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, result_a.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception as e:
                print("상환 예정 배너 노출 에러 발생 : {}".format(str(e)))
                results.append("Error")
        print(results)
        if all(result == "PASS" for result in results):
            print("상환 예정 배너 노출 : PASS")
            result_myhome.reports.append("상환 예정 배너 노출 : *PASS*")
        else:
            print("상환 예정 배너 노출 : FAIL")
            result_myhome.reports.append("상환 예정 배너 노출 : *FAIL*")
            base.save_screenshot('상환예정배너노출_fail')

        myhome.notification_Enabled_On()
        try:
            result_b = WebDriver.driver.find_element(MobileBy.XPATH, home.notification_enabled_off)
            self.assertIn("알림받는중", result_b.text)
            print("상환 예정 배너 > 알림 받기 On 동작 : PASS")
            result_myhome.reports.append("상환 예정 배너 > 알림 받기 On 동작 : *PASS*")
        except AssertionError:
            print("상환 예정 배너 > 알림 받기 On 동작 : FAIL")
            result_myhome.reports.append("상환 예정 배너 > 알림 받기 On 동작 : *FAIL*")
            base.save_screenshot('상환예정배너>알림받기On동작_fail')
        except Exception as e:
            print("상환 예정 배너 > 알림 받기 On 동작 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("Error")
            base.save_screenshot('상환예정배너>알림받기On동작_error')
        myhome.notification_Enabled_Off()
        try:
            result_c = WebDriver.driver.find_element(MobileBy.XPATH, home.notification_enabled_on)
            self.assertIn("알림 받기", result_c.text)
            print("상환 예정 배너 > 알림 받기 Off 동작 : PASS")
            result_myhome.reports.append("상환 예정 배너 > 알림 받기 Off 동작 : *PASS*")
        except AssertionError:
            print("상환 예정 배너 > 알림 받기 Off 동작 : FAIL")
            result_myhome.reports.append("상환 예정 배너 > 알림 받기 Off 동작 : *FAIL*")
            base.save_screenshot('상환예정배너>알림받기Off동작_fail')
        except Exception as e:
            print("상환 예정 배너 > 알림 받기 Off 동작 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("Error")
            base.save_screenshot('상환예정배너>알림받기Off동작_error')

        try:
            myhome.loan_A()
        except:
            myhome.loan_B()
        try:
            more.check()
        except:
            pass
        try:
            result_d = WebDriver.driver.find_element(MobileBy.XPATH, home.repayment_schedule)
            self.assertIn("이번달 총 상환액", result_d.text)
            print("상환 예정 배너 진입 : PASS")
            result_myhome.reports.append("상환 예정 배너 진입 : *PASS*")
        except AssertionError:
            print("상환 예정 배너 진입 : FAIL")
            result_myhome.reports.append("상환 예정 배너 진입 : *FAIL*")
            base.save_screenshot('상환예정배너진입_fail')
        except Exception as e:
            print("상환 예정 배너 진입 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("Error")
            base.save_screenshot('상환예정배너진입_error')
        base.android_back()

    # 마이홈 오토리스 배너 테스트
    def test_lease_contract_banner(self):
        # driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        etc = Etc()
        result_myhome = Result_MyHome()
        base = basemethod()
        # results = []
        base.scroll(1)
        base.scroll(2)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, home.lease_contract_banner)
            self.assertEqual(Result_a.text, "장기렌트·리스")
            print("장기렌트 리스 배너 노출 : PASS")
            result_myhome.reports.append("장기렌트 리스 배너 노출 : *PASS*")
        except AssertionError:
            print("장기렌트 리스 배너 노출 : FAIL")
            result_myhome.reports.append("장기렌트 리스 배너 노출 : *FAIL*")
            base.save_screenshot('장기렌트리스배너노출_fail')
        except Exception as e:
            print("장기렌트 리스 배너 노출 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("장기렌트 리스 배너 노출 : *Error*")
            base.save_screenshot('장기렌트리스배너노출_error')
        myhome.Lease_Contract_Banner()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.lease_rent_result)
            self.assertEqual(Result.text, "리스렌트")
            print("장기렌트 리스 배너 진입 : PASS")
            result_myhome.reports.append("장기렌트 리스 배너 진입 : *PASS*")
        except AssertionError:
            print("장기렌트 리스 배너 진입 : FAIL")
            result_myhome.reports.append("장기렌트 리스 배너 진입 : *FAIL*")
            base.save_screenshot('장기렌트리스배너진입_fail')
        except Exception as e:
            print("장기렌트 리스 배너 진입 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("장기렌트 리스 배너 진입 : *Error*")
            base.save_screenshot('장기렌트리스배너진입_error')
        base.android_back()

    # 마이홈 자동차 대출 배너 테스차
    def test_auto_loan_banner(self):
        # driver = WebDriver.setUp()
        myhome = MyHome()
        home = Home()
        etc = Etc()
        info = InFo()
        result_myhome = Result_MyHome()
        base = basemethod()
        base.scroll(1)
        base.scroll(2)
        # results = []
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, home.auto_loan_banner)
            self.assertEqual(Result_a.text, "차 구매 대출")
            print("차 구매 대출 배너 노출 : PASS")
            result_myhome.reports.append("차 구매 대출 배너 노출 : *PASS*")
        except AssertionError:
            print("차 구매 대출 배너 노출 : FAIL")
            result_myhome.reports.append("차 구매 대출 배너 노출 : *FAIL*")
            base.save_screenshot('차구매대출배너노출_fail')
        except Exception as e:
            print("차 구매 대출 배너 노출 에러 발생 : {}".format(str(e)))
            result_myhome.reports.append("차 구매 대출 배너 노출 : *Error*")
            base.save_screenshot('차구매대출배너노출_error')

        myhome.auto_Loan_Banner()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_a)
            self.assertEqual(Result_A.text,"1분만에 내 한도 알아보기")
            print("차 구매 대출 배너 진입 : PASS")
            result_myhome.reports.append("차 구매 대출 배너 진입 : *PASS*")
        except AssertionError:
            print("차 구매 대출 배너 진입 : FAIL")
            result_myhome.reports.append("차 구매 대출 배너 진입 : *FAIL*")
            base.save_screenshot('차구매대출배너진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_b)
                self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result_B.text)
                print("차 구매 대출 배너 진입 : PASS")
                result_myhome.reports.append("차 구매 대출 배너 진입 : *PASS*")
            except AssertionError:
                print("차 구매 대출 배너 진입 : FAIL")
                result_myhome.reports.append("차 구매 대출 배너 진입 : *FAIL*")
                base.save_screenshot('차구매대출배너진입_fail')
            except Exception as e:
                print("차 구매 대출 배너 진입 에러 발생 : {}".format(str(e)))
                result_myhome.reports.append("차 구매 대출 배너 진입 : *Error*")
                base.save_screenshot('차구매대출배너진입_error')
        base.android_back()

class hometest_Testcase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("더보기 TestCase_A 시작")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("더보기 TestCase_A완료")
    #
    #
    # def setUp(self):
    #     base = basemethod()
    #     base.scroll(1)
    #     base.scroll(0.93)
    #
    # def tearDown(self):
    #     base = basemethod()
    #     base.android_back()
    #     time.sleep(1)
    #     base.scroll_up(0.8)
    #     base.scroll_up(0.8)
    #     base.scroll_up(0.8)

    # 마이홈 비교대출 배너 테스트
    def test_test(self):
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        etc = Etc()
        more = More()
        info = InFo()
        seting = Seting()
        results = []
        results_a = []
        more.etc_in()
        seting.seting_in()
        base.scroll(2)
        base.user_id_get()
        base.user_token_get()
        base.android_back()
        base.android_back()
        url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans"
        # 요청 헤더 설정 (필요에 따라 사용)
        headers = { "Content-Type" : "application/json",
                    "X-Auth-Token": ''.join(info.usertoken)
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
            info.loans_data.append(first_product_name)
        print(info.loans_data)
        loans_data_a = "".join(map(str, info.loans_data))
        print(loans_data_a)
        if 'list' in result and len(result['list']) > 0:
            first_product_name_a = result['list'][0]['interestRate']
            info.loans_data_b.append(first_product_name_a)
        print(info.loans_data_b)
        loans_data_c = "".join(map(str, info.loans_data_b))
        print(loans_data_c)

        print(loans_data_a)
        print(loans_data_c)

        base.scroll(0.6)
        verification_list = [(loans_data_a, "//*[contains(@text, '"+loans_data_a+"')]"),
                             (""+loans_data_c+"%", "//*[contains(@text, '"+loans_data_c+"%')]")]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertEqual(result_a.text, text)
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
            base.save_screenshot('내대출배너노출_fail')

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
            base.save_screenshot('내대출배너진입_fail')
        base.android_back()








if __name__ == '__main__':
    unittest.main()