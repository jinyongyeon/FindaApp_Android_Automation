import time
import unittest
import logging

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More, Result_seting
from testscript.login_testscript.logincase import JoIn
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod
from testscript.more_testscript.seting import Seting


class Seting_Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("설정 페이지 테스트 시작")

    @classmethod
    def tearDownClass(cls):
        logging.info("설정 페이지 테스트 종료")

    def setUp(self):
        more = More()
        set = Seting()
        more.etc_in()
        set.seting_in()

    def tearDown(self):
        base = basemethod()
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()

    # 설정 > 내정보 수정 테스트
    def test_my_info(self):
        set = Seting()
        etc = Etc()
        join = JoIn()
        info = InFo()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 내정보 수정 테스트 시작")
        set.myinfo()
        results = []
        verification_list = [("내 정보 확인", etc.myinfo_result_a),
                             (info.phone_number, etc.myinfo_result_b),
                             (info.news_agency, etc.myinfo_result_c),
                             (info.name, etc.myinfo_result_d)]
        for text, xpath in verification_list:
            try:
                result = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, result.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception:
                results.append("Error")
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("설정 > 내 정보 진입 결과 : PASS")
            setingresult.reports.append("설정 > 내 정보 진입 결과 : *PASS*")
        else:
            logging.info("설정 > 내 정보 진입 결과 : FAIL")
            setingresult.reports.append("설정 > 내 정보 진입 결과 : *FAIL*")
            base.save_screenshot('내정보진입_fail')
        set.myinfo_edit()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.myinfo_result))
            logging.info("설정 > 내정보 수정 결과 : PASS")
            setingresult.reports.append("설정 > 내정보 수정 결과 : *PASS*")
            print("설정 > 내정보 수정 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 내정보 수정 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 내정보 수정 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('내정보수정_fail')
            print("설정 > 내정보 수정 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 내정보 수정 에러 발생 : {e}")
            setingresult.reports.append("설정 > 내정보 수정 결과 : *Error*")
            base.save_screenshot('내정보수정_error')
            print(f"설정 > 내정보 수정 에러 발생 : {e}")
        time.sleep(5)
        join.start_onboarding()
        join.malicious_app_search()
        join.enter_personal_information()
        join.message_certification()
        join.join_next()
        join.membership_terms_and_conditions_all()
        time.sleep(6)
        join.join_next()
        join.use_fingerprint()
        join.pin_code()
        time.sleep(1)
        join.pin_code()
        logging.info("설정 > 내정보 수정 테스트 종료")

    # 설정 > 알림 설정 테스트
    def test_notification_settings(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 알림설정 테스트 시작")
        set.notification_settings()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.notification_settings_result))
            logging.info("설정 > 알림설정 결과 : PASS")
            setingresult.reports.append("설정 > 알림설정 결과 : *PASS*")
            print("설정 > 알림설정 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 알림설정 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 알림설정 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('알림설정결과_fail')
            print("설정 > 알림설정 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 알림설정 결과 에러 발생 : {e}")
            setingresult.reports.append("설정 > 알림설정 결과 : *Error*")
            base.save_screenshot('알림설정결과_error')
            print(f"설정 > 알림설정 결과 에러 발생 : {e}")
        logging.info("설정 > 알림설정 테스트 종료")

    # 설정 > 비밀번호 변경 테스트
    def test_change_password(self):
        set = Seting()
        etc = Etc()
        join = JoIn()
        base = basemethod()
        setingresult = Result_seting()
        results = []
        logging.info("설정 > 비밀번호 변경 테스트 시작")
        set.change_password()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.changepassword_a))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('비밀번호변경_a_fail')
        except Exception as e:
            logging.warning(f"설정 > 비밀번호 변경_a 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('비밀번호변경_a_error')
        join.pin_code()
        time.sleep(3)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.changepassword_b))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('비밀번호변경_b_fail')
        except Exception as e:
            logging.warning(f"설정 > 비밀번호 변경_b 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('비밀번호변경_b_error')
        join.pin_code()
        time.sleep(3)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.changepassword_c))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('비밀번호변경_c_fail')
        except Exception as e:
            logging.warning(f"설정 > 비밀번호 변경_c 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('비밀번호변경_c_error')
        join.pin_code()
        time.sleep(3)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.changepassword))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('비밀번호변경_fail')
        except Exception as e:
            logging.warning(f"설정 > 비밀번호 변경 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('비밀번호변경_error')
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("설정 > 비밀번호 변경 결과 : PASS")
            setingresult.reports.append("설정 > 비밀번호 변경 결과 : *PASS*")
            print("설정 > 비밀번호 변경 결과 : PASS")
        else:
            logging.info("설정 > 비밀번호 변경 결과 : FAIL")
            setingresult.reports.append("설정 > 비밀번호 변경 결과 : *FAIL*")
            print("설정 > 비밀번호 변경 결과 : FAIL")
        logging.info("설정 > 비밀번호 변경 테스트 종료")

    # 설정 > 개인신용정보 이용/제공 내역 조회 테스트
    def test_credit_information_history(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        join = JoIn()
        setingresult = Result_seting()
        logging.info("설정 > 개인신용정보 이용/제공 내역 조회 진입 테스트 시작")
        set.credit_information_history()
        join.pin_code()
        time.sleep(10)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_information_history_result))
            logging.info("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과 : PASS")
            setingresult.reports.append("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과 : *PASS*")
            print("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('개인신용정보 이용/제공 내역 조회 진입_fail')
            print("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 개인신용정보 이용/제공 내역 조회 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 개인신용정보 이용/제공 내역 조회 진입 결과 : *Error*")
            base.save_screenshot('개인신용정보 이용/제공 내역 조회 진입_error')
            print(f"설정 > 개인신용정보 이용/제공 내역 조회 진입 에러 발생 : {e}")
        logging.info("설정 > 개인신용정보 이용/제공 내역 조회 진입 테스트 종료")

    # 설정 > 금융정보 관리(마이데이터) 진입 테스트
    def test_seting_mydata(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 금융정보 관리(마이데이터) 진입 테스트 시작")
        set.seting_mtdata()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_mtdata_result_a))
            logging.info("설정 > 금융 정보 관리(마이데이터) 진입 결과 : PASS")
            setingresult.reports.append("설정 > 금융 정보 관리(마이데이터) 진입 결과 : *PASS*")
            print("설정 > 금융 정보 관리(마이데이터) 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('금융정보관리진입_fail')
            print("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : FAIL")
        except Exception :
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_mtdata_result_b))
                logging.info("설정 > 금융 정보 관리(마이데이터) 진입 결과 : PASS")
                setingresult.reports.append("설정 > 금융 정보 관리(마이데이터) 진입 결과 : *PASS*")
                print("설정 > 금융 정보 관리(마이데이터) 진입 결과 : PASS")
            except TimeoutError:
                logging.info("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : FAIL")
                setingresult.reports.append("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : *FAIL*")
                base.save_screenshot('금융정보관리진입_fail')
                print("설정 > 금융 정보 관리(마이데이터) 진입 결과_요소확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"설정 > 금융 정보 관리(마이데이터) 진입 에러 발생 : {e}")
                setingresult.reports.append("설정 > 금융 정보 관리(마이데이터) 진입 결과 : *Error*")
                base.save_screenshot('금융정보관리진입_error')
                print(f"설정 > 금융 정보 관리(마이데이터) 진입 에러 발생 : {e}")
        logging.info("설정 > 금융정보 관리(마이데이터) 진입 테스트 종료")

    # 설정 > 이용역관 진입 테스트
    def test_seting_terms_of_use(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 이용역관 진입 테스트 시작")
        set.seting_terms_of_use()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_terms_of_use_result))
            logging.info("설정 > 이용약관 진입 결과 : PASS")
            setingresult.reports.append("설정 > 이용약관 진입 결과 : *PASS*")
            print("설정 > 이용약관 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 이용약관 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 이용약관 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('이용약관진입_fail')
            print("설정 > 이용약관 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 이용약관 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 이용약관 진입 결과 : *Error*")
            base.save_screenshot('이용약관진입_error')
            print(f"설정 > 이용약관 진입 에러 발생 : {e}")
        logging.info("설정 > 이용역관 진입 테스트 종료")

    # 설정 > 개인정보 처리방침 진입 테스트
    def test_seting_privacy_policy(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 개인정보 처리방침 진입 테스트 시작")
        set.seting_privacy_policy()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_privacy_policy_result))
            logging.info("설정 > 개인정보 처리방침 진입 결과 : PASS")
            setingresult.reports.append("설정 > 개인정보 처리방침 진입 결과 : *PASS*")
            print("설정 > 개인정보 처리방침 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 개인정보 처리방침 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 개인정보 처리방침 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('개인정보처리방침진입_fail')
            print("설정 > 개인정보 처리방침 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 개인정보 처리방침 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 개인정보 처리방침 진입 결과 : *Error*")
            base.save_screenshot('개인정보처리방침진입_error')
            print(f"설정 > 개인정보 처리방침 진입 에러 발생 : {e}")
        logging.info("설정 > 개인정보 처리방침 진입 테스트 종료")

    # 설정 > 마이데이터 서비스 이용약관 진입 테스트
    def test_seting_mydata_service_terms_of_use(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 마이데이터 서비스 이용약관 진입 테스트 시작")
        set.seting_mydata_service_terms_of_use()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_mydata_service_terms_of_use_result))
            logging.info("설정 > 마이데이터 서비스 이용약관 진입 결과 : PASS")
            setingresult.reports.append("설정 > 마이데이터 서비스 이용약관 진입 결과 : *PASS*")
            print("설정 > 마이데이터 서비스 이용약관 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 마이데이터 서비스 이용약관 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 마이데이터 서비스 이용약관 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('마이데이터서비스이용약관진입_fail')
            print("설정 > 마이데이터 서비스 이용약관 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 마이데이터 서비스 이용약관 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 마이데이터 서비스 이용약관 진입 결과 : *Error*")
            base.save_screenshot('마이데이터서비스이용약관진입_error')
            print(f"설정 > 마이데이터 서비스 이용약관 진입 에러 발생 : {e}")
        logging.info("설정 > 마이데이터 서비스 이용약관 진입 테스트 종료")

    # 설정 > 금융소비자보호 고지사항 진입 테스트
    def test_financial_consumer_protection_notice(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 금융소비자보호 고지사항 진입 테스트 시작")
        base.scroll(0.4)
        set.financial_consumer_protection_notice()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.financial_consumer_protection_notice_result))
            logging.info("설정 > 금융소비자보호 고지사항 진입 결과 : PASS")
            setingresult.reports.append("설정 > 금융소비자보호 고지사항 진입 결과 : *PASS*")
            print("설정 > 금융소비자보호 고지사항 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 금융소비자보호 고지사항 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 금융소비자보호 고지사항 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('금융소비자보호고지사항진입_fail')
            print("설정 > 금융소비자보호 고지사항 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 금융소비자보호 고지사항 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 금융소비자보호 고지사항 진입 결과 : *Error*")
            base.save_screenshot('금융소비자보호고지사항진입_error')
            print(f"설정 > 금융소비자보호 고지사항 진입 에러 발생 : {e}")
        logging.info("설정 > 금융소비자보호 고지사항 진입 테스트 종료")

    # 설정 > 버전 정보 진입 테스트
    def test_seting_version(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 버전 정보 진입 테스트 시작")
        base.scroll(0.4)
        set.seting_version()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.seting_version_result))
            logging.info("설정 > 버전 정보 진입 결과 : PASS")
            setingresult.reports.append("설정 > 버전 정보 진입 결과 : *PASS*")
            print("설정 > 버전 정보 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 버전 정보 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 버전 정보 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('버전정보진입_fail')
            print("설정 > 버전 정보 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 버전 정보 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 버전 정보 진입 결과 : *Error*")
            base.save_screenshot('버전정보진입_error')
            print(f"설정 > 버전 정보 진입 에러 발생 : {e}")
        logging.info("설정 > 버전 정보 진입 테스트 종료")

    # 설정 > 오픈소스 라이선스 진입 테스트
    def test_open_source_license(self):
        set = Seting()
        etc = Etc()
        base = basemethod()
        setingresult = Result_seting()
        logging.info("설정 > 오픈소스 라이선스 진입 테스트 시작")
        base.scroll(0.4)
        set.open_source_license()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.open_source_license_result))
            logging.info("설정 > 오픈소스 라이선스 진입 결과 : PASS")
            setingresult.reports.append("설정 > 오픈소스 라이선스 진입 결과 : *PASS*")
            print("설정 > 오픈소스 라이선스 진입 결과 : PASS")
        except TimeoutError:
            logging.info("설정 > 오픈소스 라이선스 진입 결과_요소확인필요 : FAIL")
            setingresult.reports.append("설정 > 오픈소스 라이선스 진입 결과_요소확인필요 : *FAIL*")
            base.save_screenshot('오픈소스라이선스진입_fail')
            print("설정 > 오픈소스 라이선스 진입 결과_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"설정 > 오픈소스 라이선스 진입 에러 발생 : {e}")
            setingresult.reports.append("설정 > 오픈소스 라이선스 진입 결과 : *Error*")
            base.save_screenshot('오픈소스라이선스진입_error')
            print(f"설정 > 오픈소스 라이선스 진입 에러 발생 : {e}")
        logging.info("설정 > 오픈소스 라이선스 진입 테스트 종료")

if __name__ == '__main__':
    unittest.main()