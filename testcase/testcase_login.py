import time
import unittest
import logging
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.basemethod.result import Result_Join
from pages.mainlocator.main import Main
from testscript.login_testscript.logincase import JoIn
from testscript.more_testscript.see_more import More
from testscript.more_testscript.seting import Seting

class JoinTestCase(unittest.TestCase):


    def setUp(self):
        join = JoIn()
        join.app_start()

    def tearDown(self):
        join = JoIn()
        join.app_quit()

    # MO인증 테스트
    def test_message_certification(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        logging.info("MO인증 테스트 테스트 시작")
        join.app_quit()
        join.app_start()
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.mo_Result))
            logging.info("MO인증 결과 : PASS")
            result_join.reports.append("MO인증 결과 : *PASS*")
            print("MO인증 결과 : PASS")
        except TimeoutError:
            logging.info("MO인증 결과_요소확인필요 : FAIL")
            result_join.reports.append("MO인증 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('MO인증결과_fail')
            print("MO인증 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"MO인증 에러 발생 : {e}")
            result_join.reports.append("MO인증 결과 : *Error*")
            base.save_screenshot('MO인증결과_error')
            print(f"MO인증 에러 발생 : {e}")
        logging.info("MO인증 테스트 테스트 종료")

    # 유심내용 자동입력 테스트
    def test_enter_personal_information(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        logging.info("유심내용 자동입력 테스트 시작")
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.phone_number_Result))
            logging.info("유심내용 자동입력 결과 : PASS")
            result_join.reports.append("유심내용 자동입력 결과 : *PASS*")
            print("유심내용 자동입력 결과 : PASS")
        except TimeoutError:
            logging.info("유심내용 자동입력 결과_요소확인필요 : FAIL")
            result_join.reports.append("유심내용 자동입력 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('유심내용자동입력결과_fail')
            print("유심내용 자동입력 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"유심내용 자동입력 에러 발생 : {e}")
            result_join.reports.append("유심내용 자동입력 결과 : *Error*")
            base.save_screenshot('유심내용자동입력결과_error')
            print(f"유심내용 자동입력 에러 발생 : {e}")
        logging.info("유심내용 자동입력 테스트 종료")

    # 회원가입 약관 동의 진입 테스트
    def test_membership_terms_and_conditions(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        results = []
        results_a = []
        results_b = []
        results_c = []
        results_d = []
        logging.info("회원가입 약관 동의 진입 테스트 시작")
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        join.join_next()
        verification_list = [("핀다 필수 항목 모두 동의", main.membership_terms_and_conditions_a_Result),
                             ("제휴사 필수 항목 모두 동의", main.membership_terms_and_conditions_b_Result),
                             ("본인인증 필수 항목 모두 동의", main.membership_terms_and_conditions_c_Result),
                             ("마케팅 정보 수신 동의 (선택)", main.membership_terms_and_conditions_d_Result)]
        for text, xpath in verification_list:
            try:
                Result = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, Result.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
            except TimeoutError:
                results_a.append("FAIL")
            except Exception:
                results_a.append("Error")
        if all(result == "PASS" for result in results_a):
            logging.info("회원가입 약관 노출 결과 : PASS")
            results.append("PASS")
        else:
            logging.info("회원가입 약관 노출 결과 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출결과_fail')
        join.membership_terms_and_conditions_a()
        verification_list_a = [("서비스 이용약관 동의", main.membership_terms_and_conditions_aa),
                             ("개인정보 제3자 제공 동의", main.membership_terms_and_conditions_ab),
                             ("개인정보 수집 및 이용 동의", main.membership_terms_and_conditions_ac)]
        for text, xpath in verification_list_a:
            try:
                Result_a = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, Result_a.text)
                results_b.append("PASS")
            except AssertionError:
                results_b.append("FAIL")
            except TimeoutError:
                results_b.append("FAIL")
            except Exception:
                results_b.append("Error")
        if all(result == "PASS" for result in results_b):
            logging.info("회원가입 약관 노출_1 : PASS")
            results.append("PASS")
        else:
            logging.info("회원가입 약관 노출_1 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_1_fail')
        try:
            join.membership_terms_and_conditions_aa()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_aa_Result))
            logging.info("회원가입 약관 진입_aa : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_aa_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_aa_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_aa 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_aa_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_ab()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_ab_Result))
            logging.info("회원가입 약관 진입_ab : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_ab_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_ab_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_ab 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ab_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_ac()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_ac_Result))
            logging.info("회원가입 약관 진입_ac : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_ac_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_ac_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_ac 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ac_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        join.membership_terms_and_conditions_a()
        time.sleep(1)
        join.membership_terms_and_conditions_b()
        verification_list_b = [("KCB 신용조회 서비스 이용 약관 동의", main.membership_terms_and_conditions_ba),
                             ("개인(신용)정보 수집∙이용 동의(KCB)", main.membership_terms_and_conditions_bb),
                             ("개인(신용)정보 제3자 제공 동의(KCB)", main.membership_terms_and_conditions_bc)]
        for text, xpath in verification_list_b:
            try:
                Result_b = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, Result_b.text)
                results_c.append("PASS")
            except AssertionError:
                results_c.append("FAIL")
            except TimeoutError:
                results_c.append("FAIL")
            except Exception:
                results_c.append("Error")
        if all(result == "PASS" for result in results_c):
            logging.info("회원가입 약관 노출_2 : PASS")
            results.append("PASS")
        else:
            logging.info("회원가입 약관 노출_2 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_2_fail')
        try:
            join.membership_terms_and_conditions_ba()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_ba_Result))
            logging.info("회원가입 약관 진입_ba : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_ba_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_ba_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_ba 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ba_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_bb()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_bb_Result))
            logging.info("회원가입 약관 진입_bb : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_bb_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_bb_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_bb 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_bb_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_bc()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_bc_Result))
            logging.info("회원가입 약관 진입_bc : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_bc_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_bc_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_bc 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_bc_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        join.membership_terms_and_conditions_b()
        time.sleep(2)
        join.membership_terms_and_conditions_c()
        time.sleep(3)
        base.scroll(0.1)
        time.sleep(4)
        verification_list_c = [("통신사 이용 약관", main.membership_terms_and_conditions_ca),
                               ("고유식별정보처리 동의", main.membership_terms_and_conditions_cb),
                               ("개인정보 제3자 동의 (KT, LGU+ 알뜰폰)", main.membership_terms_and_conditions_cc),
                               ("개인정보취급동의", main.membership_terms_and_conditions_cd),
                               ("본인확인서비스 이용약관", main.membership_terms_and_conditions_ce)]
        for text, xpath in verification_list_c:
            try:
                Result_c = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, Result_c.text)
                results_d.append("PASS")
            except AssertionError:
                results_d.append("FAIL")
            except TimeoutError:
                results_d.append("FAIL")
            except Exception:
                results_d.append("Error")
        if all(result == "PASS" for result in results_d):
            logging.info("회원가입 약관 노출_3 : PASS")
            results.append("PASS")
        else:
            logging.info("회원가입 약관 노출_3 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_3_fail')
        try:
            join.membership_terms_and_conditions_ca()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_ca_Result))
            logging.info("회원가입 약관 진입_ca : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_ca_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_ca_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_ca 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ca_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_cb()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_cb_Result))
            logging.info("회원가입 약관 진입_cb : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_cb_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_cb_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_cb 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cb_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_cc()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_cc_Result))
            logging.info("회원가입 약관 진입_cc : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_cc_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_cc_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_cc 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cc_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_cd()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_cd_Result))
            logging.info("회원가입 약관 진입_cd : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_cd_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_cd_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_cd 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cd_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        try:
            join.membership_terms_and_conditions_ce()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_ce_Result))
            logging.info("회원가입 약관 진입_ce : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_ce_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_ce_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_ce 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ce_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        join.membership_terms_and_conditions_c_a()
        time.sleep(1)
        join.membership_terms_and_conditions_d()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_da))
            logging.info("회원가입 약관 노출_4 : PASS")
            results.append("PASS")
        except TimeoutError:
            logging.info("회원가입 약관 노출_4_요소확인필요 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_4_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 노출_4 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관노출_4_error')
        try:
            join.membership_terms_and_conditions_da()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.membership_terms_and_conditions_da_Result))
            logging.info("회원가입 약관 진입_da : PASS")
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            logging.info("회원가입 약관 진입_da_요소확인필요 : FAIL")
            base.save_screenshot('회원가입약관진입_da_fail')
        except Exception as e:
            logging.warning(f"회원가입 약관 진입_da 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('회원가입약관진입_da_error')
        time.sleep(3)
        base.android_back()
        time.sleep(3)
        join.membership_terms_and_conditions_d()
        if all(result == "PASS" for result in results):
            logging.info("회원가입 약관 목록 노출 및 진입 결과 : PASS")
            result_join.reports.append("회원가입 약관 목록 노출 및 진입 결과 : *PASS*")
            print("회원가입 약관 목록 노출 및 진입 결과 : PASS")
        else:
            logging.info("회원가입 약관 목록 노출 및 진입 결과 : FAIL")
            result_join.reports.append("회원가입 약관 목록 노출 및 진입 결과 : *FAIL*")
            print("회원가입 약관 목록 노출 및 진입 결과 : FAIL")
        logging.info("회원가입 약관 동의 진입 테스트 종료")

    # 인증번호 수신 및 자동입력, 재요청 테스트
    def test_certification_number(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        logging.info("인증번호 수신 및 자동입력, 재요청 테스트 시작")
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        join.join_next()
        time.sleep(2)
        join.membership_terms_and_conditions_all()
        time.sleep(5)
        join.join_next()
        time.sleep(3)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.pincode_in_Result))
            logging.info("회원가입 인증번호 자동입력 결과 : PASS")
            result_join.reports.append("회원가입 인증번호 자동입력 결과 : *PASS*")
            print("회원가입 인증번호 자동입력 결과 : PASS")
        except TimeoutError:
            logging.info("회원가입 인증번호 자동입력 결과_요소확인필요 : FAIL")
            result_join.reports.append("회원가입 인증번호 자동입력 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('회원가입인증번호자동입력결과_fail')
            print("회원가입 인증번호 자동입력 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"회원가입 인증번호 자동입력 에러 발생 : {e}")
            result_join.reports.append("회원가입 인증번호 자동입력 결과 : *Error*")
            base.save_screenshot('회원가입인증번호자동입력결과_error')
            print(f"회원가입 인증번호 자동입력 에러 발생 : {e}")
        base.android_back()
        time.sleep(3)
        join.re_request_verification_code()
        join.join_next()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.pincode_in_Result))
            logging.info("회원가입 인증번호 재요청 : PASS")
            result_join.reports.append("회원가입 인증번호 재요청 : *PASS*")
            print("회원가입 인증번호 재요청 : PASS")
        except TimeoutError:
            logging.info("회원가입 인증번호 재요청_요소확인필요 : FAIL")
            result_join.reports.append("회원가입 인증번호 재요청_요소확인필요 : *FAIL*")
            base.save_screenshot('회원가입인증번호재요청_fail')
            print("회원가입 인증번호 재요청_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"회원가입 인증번호 재요청 에러 발생 : {e}")
            result_join.reports.append("회원가입 인증번호 재요청 : *Error*")
            base.save_screenshot('회원가입인증번호재요청_error')
            print(f"회원가입 인증번호 재요청 에러 발생 : {e}")
        logging.info("인증번호 수신 및 자동입력, 재요청 테스트 종료")

    # 핀코드 등록 및 회원가입 테스트
    def test_join(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        logging.info("핀코드 등록 및 회원가입 테스트 시작")
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        join.join_next()
        time.sleep(2)
        join.membership_terms_and_conditions_all()
        time.sleep(5)
        join.join_next()
        time.sleep(3)
        join.use_fingerprint()
        join.pin_code()
        join.pin_code()
        try:
            WebDriverWait(WebDriver.driver, 70).until(EC.visibility_of_element_located(main.login_result))
            logging.info("회원가입 결과 : PASS")
            result_join.reports.append("회원가입 결과 : *PASS*")
            print("회원가입 결과 : PASS")
        except TimeoutError:
            logging.info("회원가입 결과_요소확인필요 : FAIL")
            result_join.reports.append("회원가입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('회원가입결과_fail')
            print("회원가입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"회원가입 에러 발생 : {e}")
            result_join.reports.append("회원가입 결과 : *Error*")
            base.save_screenshot('회원가입결과_error')
            print(f"회원가입 에러 발생 : {e}")
        logging.info("핀코드 등록 및 회원가입 테스트 종료")

class LoginTestCase(unittest.TestCase):

    # 핀코드 로그인 테스트
    def test_check_in(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        base = basemethod()
        logging.info("핀코드 로그인 테스트 시작")
        join.app_start()
        join.pin_code()
        time.sleep(3)
        try:
            WebDriverWait(WebDriver.driver, 70).until(EC.visibility_of_element_located(main.login_result))
            logging.info("로그인 : PASS")
            result_join.reports.append("로그인 결과 : *PASS*")
            print("로그인 : PASS")
        except TimeoutError:
            logging.info("로그인_요소확인필요 : FAIL")
            result_join.reports.append("로그인 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('로그인결과_fail')
            print("로그인_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"로그인 에러 발생 : {e}")
            result_join.reports.append("로그인 : Error")
            base.save_screenshot('로그인결과_error')
            print(f"로그인 에러 발생 : {e}")
        logging.info("핀코드 로그인 테스트 종료")

    #로그아웃
    def test_log_out(self):
        main = Main()
        join = JoIn()
        seting = Seting()
        base = basemethod()
        more = More()
        result_join = Result_Join()
        logging.info("로그아웃 테스트 시작")
        more.etc_in()
        seting.seting_in()
        base.scroll(2)
        join.log_out()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.logout_Result))
            logging.info("로그아웃 결과 : PASS")
            result_join.reports.append("로그아웃 결과 : *PASS*")
            print("로그아웃 결과 : PASS")
        except TimeoutError:
            logging.info("로그아웃 결과_요소확인필요 : FAIL")
            result_join.reports.append("로그아웃 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('로그아웃결과_fail')
            print("로그아웃 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"로그아웃 에러 발생 : {e}")
            result_join.reports.append("로그아웃 결과 : *Error*")
            base.save_screenshot('로그아웃결과_error')
            print(f"로그아웃 에러 발생 : {e}")
        logging.info("로그아웃 테스트 종료")

    #회원탈퇴
    def test_withdraw(self):
        main = Main()
        join = JoIn()
        seting = Seting()
        base = basemethod()
        result_join = Result_Join()
        more = More()
        logging.info("회원탈퇴 테스트 시작")
        join.app_start()
        join.pin_code()
        more.etc_in()
        seting.seting_in()
        base.scroll(2)
        join.withdrawal()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(main.withdraw_Result))
            logging.info("탈퇴하기 결과 : PASS")
            result_join.reports.append("탈퇴하기 결과 : *PASS*")
            print("탈퇴하기 결과 : PASS")
        except TimeoutError:
            logging.info("탈퇴하기 결과_요소확인필요 : FAIL")
            result_join.reports.append("탈퇴하기 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('탈퇴하기결과_fail')
            print("탈퇴하기 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"탈퇴하기 에러 발생 : {e}")
            result_join.reports.append("탈퇴하기 결과 : *Error*")
            base.save_screenshot('탈퇴하기결과_error')
            print(f"탈퇴하기 에러 발생 : {e}")
        time.sleep(5)
        join.app_start()
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        join.join_next()
        join.membership_terms_and_conditions_all()
        time.sleep(6)
        join.join_next()
        join.use_fingerprint()
        join.pin_code()
        time.sleep(1)
        join.pin_code()
        logging.info("회원탈퇴 테스트 시작")

    #회원가입 자동화
    def test_auto_join(self):
        join = JoIn()
        join.app_start()
        join.start_onboarding()
        join.malicious_app_search()
        join.message_certification()
        join.enter_personal_information()
        join.join_next()
        join.membership_terms_and_conditions_all()
        time.sleep(6)
        join.join_next()
        join.use_fingerprint()
        join.pin_code()
        time.sleep(1)
        join.pin_code()

if __name__ == '__main__':
    unittest.main()