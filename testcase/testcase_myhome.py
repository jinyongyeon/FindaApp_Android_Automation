import logging
import time
import unittest
import pickle
from datetime import datetime

import requests
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.result import Result_MyHome
from pages.mainlocator.etc import Etc
from pages.mainlocator.home import Home
from pages.basemethod.base import basemethod
from testscript.more_testscript.see_more import More
from testscript.more_testscript.seting import Seting
from testscript.myhome_testscript.myhome import MyHome


class MyHome_Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("마이홈 테스트 시작")

    @classmethod
    def tearDownClass(cls):
        logging.info("마이홈 테스트 종료")

    def tearDown(self):
        base = basemethod()
        base.android_back()
        time.sleep(1)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 마이홈 상단 메뉴 영역 노출 및 진입 테스트
    def test_myhome_menu(self):
        myhome = MyHome()
        home = Home()
        result_myhome = Result_MyHome()
        base = basemethod()
        results = []
        logging.info("마이홈 상단 퀵 메뉴 영역 노출 및 진입 테스트 시작")
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_a))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_b))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_c))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_d))
            myhome.menu_right_to_left_a()
            myhome.menu_right_to_left_b()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_e))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_f))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.quick_menu_g))
            logging.info("마이홈 상단 퀵 메뉴 영역 노출 : PASS")
            result_myhome.reports.append("마이홈 상단 퀵 메뉴 영역 노출 : *PASS*")
            print("마이홈 상단 퀵 메뉴 영역 노출 : PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 영역 노출 : FAIL_요소 확인 필요")
            result_myhome.reports.append("마이홈 상단 퀵 메뉴 영역 노출_요소 확인 필요 : *FAIL*")
            base.save_screenshot('마이홈 상단 퀵 메뉴 영역 노출_fail')
            print("마이홈 상단 퀵 메뉴 영역 노출 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 메뉴 퀵 영역 노출 에러 발생 : {e}")
            result_myhome.reports.append("마이홈 상단 퀵 메뉴 영역 노출 : *Error*")
            base.save_screenshot('마이홈 상단 퀵 메뉴 영역 노출_error')
            print(f"마이홈 상단 퀵 메뉴 영역 노출 에러 발생 : {e}")
        myhome.menu_left_to_right_b()
        myhome.menu_left_to_right_a()
        try:
            myhome.menu_loan()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_a))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 대출받기 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_대출받기_fail')
            print("마이홈 상단 퀵 메뉴_대출받기 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_대출받기 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_대출받기_error')
            print(f"마이홈 상단 퀵 메뉴_대출받기 에러 발생 : {e}")
        base.android_back()
        try:
            myhome.menu_refinance_loan()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_b))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 대출 갈아타기 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_대출갈아타기_fail')
            print("마이홈 상단 퀵 메뉴_대출갈아타기 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_대출갈아타기 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_대출갈아타기_error')
            print(f"마이홈 상단 퀵 메뉴_대출갈아타기 에러 발생 : {e}")
        base.android_back()
        try:
            myhome.menu_business_loan()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_c))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 사업자대출 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_사업자대출_fail')
            print("마이홈 상단 퀵 메뉴_사업자대출 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_사업자대출 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_사업자대출_error')
            print(f"마이홈 상단 퀵 메뉴_사업자대출 에러 발생 : {e}")
        base.android_back()
        try:
            myhome.menu_home_equity_loan()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_d))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 주택담보대출 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_주택담보대출_fail')
            print("마이홈 상단 퀵 메뉴_주택담보대출 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_주택담보대출 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_주택담보대출_error')
            print(f"마이홈 상단 퀵 메뉴_주택담보대출 에러 발생 : {e}")
        base.android_back()
        myhome.menu_right_to_left_a()
        myhome.menu_right_to_left_b()
        try:
            myhome.menu_charter()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_e))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 전세대출 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_전세대출_fail')
            print("마이홈 상단 퀵 메뉴_전세대출 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_전세대출 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_전세대출_error')
            print(f"마이홈 상단 퀵 메뉴_전세대출 에러 발생 : {e}")
        base.android_back()
        try:
            myhome.menu_car_loan()
            time.sleep(4)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.result_quick_menu_f))
            results.append("PASS")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 차구매대출 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_차구매대출_fail')
            print("마이홈 상단 퀵 메뉴_차구매대출 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_차구매대출 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_차구매대출_error')
            print(f"마이홈 상단 퀵 메뉴_차구매대출 에러 발생 : {e}")
        base.android_back()
        try:
            myhome.menu_auto_lease()
            time.sleep(4)
            base.save_screenshot("마이홈 상단 퀵 메뉴 오토리스_캡처본으로 검증 대체")
        except TimeoutError:
            logging.info("마이홈 상단 퀵 메뉴 오토리스 진입실패 : FAIL_요소 확인 필요")
            results.append("FAIL")
            base.save_screenshot('마이홈 상단 퀵 메뉴_오토리스_fail')
            print("마이홈 상단 퀵 메뉴_오토리스 : FAIL_요소 확인 필요")
        except Exception as e:
            logging.warning(f"마이홈 상단 퀵 메뉴_오토리스 에러 발생 : {e}")
            results.append("ERROR")
            base.save_screenshot('마이홈 상단 퀵 메뉴_오토리스_error')
            print(f"마이홈 상단 퀵 메뉴_오토리스 에러 발생 : {e}")
        base.android_back()
        myhome.menu_left_to_right_b()
        myhome.menu_left_to_right_a()
        logging.info(results)
        print(results)
        if all(result == "PASS" for result in results):
            print("마이홈 퀵메뉴 진입 결과 : PASS")
            logging.info("마이홈 퀵메뉴 진입 결과 : PASS")
            result_myhome.reports.append("마이홈 퀵 메뉴 진입 결과 : *PASS*")
        else:
            print("마이홈 퀵 메뉴 진입 결과 : FAIL")
            logging.info("마이홈 퀵 메뉴 진입 결과 : FAIL")
            result_myhome.reports.append("마이홈 퀵 메뉴 진입 결과 : *FAIL*")
            base.save_screenshot('마이홈 퀵 메뉴 진입 결과_fail')
        logging.info("마이홈 상단 퀵 메뉴 영역 노출 및 진입 테스트 종료")

    # 마이홈 금융생활 선택 후 자산목록 진입 테스트
    def test_financial_life_in(self):
        myhome = MyHome()
        result_myhome = Result_MyHome()
        base = basemethod()
        etc = Etc()
        results = []
        results_a = []
        logging.info("마이홈 금융생활 선택 후 자산목록 진입 테스트 시작")
        myhome.loan_Banner()
        verification_list_a = [("카드", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
        for text, xpath in verification_list_a:
            try:
                result_b = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, result_b.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
            except TimeoutError:
                results_a.append("FAIL")
            except Exception as e:
                logging.warning(f"금융생활 선택 후 자산목록 진입 에러 발생 : {e}")
                results.append("Error")
        base.android_back()
        logging.info(results_a)
        if all(result == "PASS" for result in results_a):
            logging.info("금융생활 선택 후 자산목록 진입 : PASS")
            result_myhome.reports.append("금융생활 선택 후 자산목록 진입 : *PASS*")
            print("금융생활 선택 후 자산목록 진입 : PASS")
        else:
            logging.info("금융생활 선택 후 자산목록 진입 : FAIL")
            result_myhome.reports.append("금융생활 선택 후 자산목록 진입 : *FAIL*")
            base.save_screenshot('금융생활 선택 후 자산목록 진입_fail')
            print("금융생활 선택 후 자산목록 진입 : FAIL")
        base.android_back()
        logging.info("마이홈 금융생활 선택 후 자산목록 진입 테스트 종료")

    # 마이홈 금융생활 출금 일정 노출 및 진입 테스트
    def test_myhome_repayment_schedule(self):
        myhome = MyHome()
        result_myhome = Result_MyHome()
        base = basemethod()
        more = More()
        seting = Seting()
        logging.info("마이홈 금융생활 출금 일정 노출 테스트 시작")
        more.etc_in()
        seting.seting_in()
        base.scroll(2)
        base.user_id_get()
        base.user_token_get()
        base.android_back()
        base.android_back()
        results = []
        try:
            myhome.home_loan_data_api_a()
            base.android_back()
            results.append("PASS")
        except:
            base.android_back()
            results.append("FAIL")
        try:
            myhome.home_loan_data_api_b()
            base.android_back()
            results.append("PASS")
        except:
            base.android_back()
            results.append("FAIL")
        print(results)
        if all(result == "PASS" for result in results):
            logging.info("금융생활 출금일정 노출 결과 : PASS")
            result_myhome.reports.append("금융생활 출금일정 노출 결과 : *PASS*")
            print("금융생활 출금일정 노출 결과 : PASS")
        else:
            logging.info("금융생활 출금일정 노출 결과 : FAIL")
            result_myhome.reports.append("금융생활 출금일정 노출 결과 : *FAIL*")
            base.save_screenshot('금융생활 출금일정 노출 결과_fail')
            print("내 대출 진입 : FAIL")
        logging.info("마이홈 금융생활 출금 일정 노출 테스트 종료")

    # 마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 테스트
    def test_myhome_cash(self):
        myhome = MyHome()
        result_myhome = Result_MyHome()
        base = basemethod()
        more = More()
        seting = Seting()
        logging.info("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 테스트 시작")
        # more.etc_in()
        # seting.seting_in()
        # base.scroll(2)
        # base.user_id_get()
        # base.user_token_get()
        # base.android_back()
        # base.android_back()
        try:
            myhome.home_cash()
            base.android_back()
            logging.info("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : PASS")
            result_myhome.reports.append("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : *PASS*")
            print("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : PASS")
        except:
            base.android_back()
            logging.info("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : FAIL")
            result_myhome.reports.append("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : *FAIL*")
            base.save_screenshot('마이홈 금융생활 쓸 수 있는 현금 노출 및 진입_fail')
            print("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 : FAIL")
        logging.info("마이홈 금융생활 쓸 수 있는 현금 노출 및 진입 테스트 종료")

    # 마이홈 금융생활 카드 사용금액 노출 및 진입 테스트
    def test_myhome_card(self):
        myhome = MyHome()
        result_myhome = Result_MyHome()
        base = basemethod()
        more = More()
        seting = Seting()
        logging.info("마이홈 금융생활 카드 사용금액 노출 및 진입 테스트 시작")
        # more.etc_in()
        # seting.seting_in()
        # base.scroll(2)
        # base.user_id_get()
        # base.user_token_get()
        # base.android_back()
        # base.android_back()
        try:
            myhome.home_card()
            current_date = datetime.now()
            current_month = current_date.month
            card_result = MobileBy.XPATH, f"//*[contains(@text, '{current_month}월 사용금액')]"
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(card_result))
            base.android_back()
            logging.info("마이홈 금융생활 카드 사용금액 노출 및 진입 : PASS")
            result_myhome.reports.append("마이홈 금융생활 카드 사용금액 노출 및 진입 : *PASS*")
            print("마이홈 금융생활 카드 사용금액 노출 및 진입 : PASS")
        except:
            base.android_back()
            logging.info("마이홈 금융생활 카드 사용금액 노출 및 진입 : FAIL")
            result_myhome.reports.append("마이홈 금융생활 카드 사용금액 노출 및 진입 : *FAIL*")
            base.save_screenshot('마이홈 금융생활 카드 사용금액 노출 및 진입_fail')
            print("마이홈 금융생활 카드 사용금액 노출 및 진입 : FAIL")
        logging.info("마이홈 금융생활 카드 사용금액 노출 및 진입 테스트 종료")

    # 마이홈 금융생활 영역 대출 노출 및 진입 테스트(삭제)
    def test_myhome_myloan(self):
        result_myhome = Result_MyHome()
        base = basemethod()
        home = Home()
        info = InFo()
        results = []
        logging.info("마이홈 금융생활 영역 대출 노출 테스트 시작")
        # more.etc_in()
        # seting.seting_in()
        # base.scroll(2)
        # base.user_id_get()
        # base.user_token_get()
        base.android_back()
        base.android_back()
        with open('usertoken.pickle', 'rb') as f:
            usertoken = pickle.load(f)
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
            logging.info(result)
            if 'list' in result and len(result['list']) > 0:
                first_product_name = result['list'][0]['productName']
                info.loans_data.append(first_product_name)
            loans_data = "".join(map(str, info.loans_data))
            logging.info(loans_data)
            print(loans_data)
        except Exception as e:
            logging.error(f"loans_data 요청실패 : {e}")
        verification_list = [(loans_data, "//*[contains(@text, '"+loans_data+"')]")]
        for text, xpath in verification_list:
            try:
                result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertEqual(result_a.text, text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception as e:
                logging.warning(f"내 대출 노출 에러 발생 : {e}")
                results.append("Error")
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("내 대출 노출 : PASS")
            result_myhome.reports.append("내 대출 노출 : *PASS*")
        else:
            logging.info("내 대출 노출 : FAIL")
            result_myhome.reports.append("내 대출 노출 : *FAIL*")
            base.save_screenshot('내대출노출_fail')
        try:
            WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '"+loans_data+"')]").click()
            time.sleep(2)
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.loan_a))
            print("금융생활 > 대출 상세 진입 : PASS")
            logging.info("금융생활 > 대출 상세 진입 : PASS")
            result_myhome.reports.append("금융생활 > 대출 상세 진입 : *PASS*")
        except TimeoutError:
            print("금융생활 > 대출 상세 진입 : FAIL_요소 확인 필요")
            logging.info("금융생활 > 대출 상세 진입 : FAIL_요소 확인 필요")
            result_myhome.reports.append("금융생활 > 대출 상세 진입_요소 확인 필요 : *FAIL*")
            base.save_screenshot('금융생활 > 대출 상세 진입_FAIL')
        except Exception as e:
            print(f"금융생활 > 대출 상세 진입 에러 발생 : {e}")
            logging.warning(f"금융생활 > 대출 상세 진입 에러 발생 : {e}")
            result_myhome.reports.append("금융생활 > 대출 상세 진입 : *Error*")
            base.save_screenshot('금융생활 > 대출 상세 진입_error')
        base.android_back()
        logging.info("마이홈 금융생활 영역 대출 노출 테스트 종료")

    # 마이홈 신용점수 진입 후 신용점수 노출 테스트
    def test_credit_score(self):
        myhome = MyHome()
        result_myhome = Result_MyHome()
        base = basemethod()
        more = More()
        info = InFo()
        seting = Seting()
        logging.info("마이홈 신용점수 진입 후 신용점수 노출 테스트 시작")
        # more.etc_in()
        # seting.seting_in()
        # base.scroll(2)
        # base.user_id_get()
        # base.user_token_get()
        # base.android_back()
        # base.android_back()
        # myhome.credit_score_get()
        myhome.credit_score()
        try:
            time.sleep(5)
            more.exit()
        except:
            pass
        try:
            credit_score = "".join(map(str, info.credit_score))
            print(credit_score)
            WebDriver.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '"+credit_score+"')]")
            print("마이홈 신용점수 진입 후 신용점수 노출결과 : PASS")
            logging.info("마이홈 신용점수 진입 후 신용점수 노출결과 : PASS")
            result_myhome.reports.append("마이홈 신용점수 진입 후 신용점수 노출 결과 : *PASS*")
        except TimeoutError:
            print("마이홈 신용점수 진입 후 신용점수 노출 결과_요소 확인 필요 : FAIL")
            logging.info("마이홈 신용점수 진입 후 신용점수 노출 결과_요소 확인 필요 : FAIL")
            result_myhome.reports.append("마이홈 신용점수 진입  후 신용점수 노출 결과_요소 확인 필요 : *FAIL*")
            base.save_screenshot('마이홈 신용점수 진입  후 신용점수 노출_fail')
        except Exception as e:
            print(f"마이홈 신용점수 진입 후 신용점수 노출 결과 에러 발생 : {e}")
            logging.warning(f"마이홈 신용점수 진입 후 신용점수 노출 결과 에러 발생 : {e}")
            result_myhome.reports.append("마이홈 신용점수 진입  후 신용점수 노출 결과 : *Error*")
            base.save_screenshot('마이홈 신용점수 진입  후 신용점수 노출_error')
        try:
            more.credit_score_back()
        except:
            base.android_back()
        base.android_back()
        logging.info("마이홈 신용점수 진입 후 신용점수 노출 테스트 종료")

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
        current_date = datetime.now()
        current_month = current_date.month

        print(f"{current_month}test")









if __name__ == '__main__':
    unittest.main()