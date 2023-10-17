import time
import unittest
import logging

from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.basemethod.result import Result_loan
from pages.mainlocator.etc import Etc
from pages.mainlocator.loan import Loan
from testscript.loan_testscript.auto_loan import Auto_Loan
from testscript.loan_testscript.loan_comparison import ComparisonLoan
from testscript.login_testscript.logincase import JoIn
from testscript.more_testscript.see_more import More
from testscript.more_testscript.seting import Seting
from testscript.myhome_testscript.myhome import MyHome


class AutoLoanTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("오토론 테스트 시작")

    @classmethod
    def tearDownClass(cls):
        logging.info("오토론 테스트 종료")

    def setUp(self):
        base = basemethod()
        base.scroll(2)
        base.scroll(2)
        base.scroll(2)

    def tearDown(self):
        base = basemethod()
        base.android_back()
        base.android_back()
        time.sleep(1)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 오토론 약관 테스트
    def test_auto_loan_new_new_car_terms(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        logging.info("오토론 약관 테스트 시작")
        try:
            myhome.auto_Loan_Banner()
            autoloan.auto_loan_terms_of_use()
            results = []
            results_a = []
            verification_list_a = [("본인인증 필수 항목 모두 동의", loan.auto_loan_terms_a),
                                   ("핀다 필수 항목 동의", loan.auto_loan_terms_b),
                                   ("금융기관 필수 항목 동의", loan.auto_loan_terms_c)]
            for text, xpath in verification_list_a:
                try:
                    Result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, Result_a.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            autoloan.auto_loan_terms_a_unfold()
            verification_list_b = [("통신사 이용 약관", loan.auto_loan_terms_aa),
                                   ("개인정보취급동의", loan.auto_loan_terms_ab),
                                   ("고유식별정보처리 동의", loan.auto_loan_terms_ac),
                                   ("본인확인서비스 이용약관", loan.auto_loan_terms_ad),
                                   ("개인정보 제3자 동의 (KT, LGU+ 알뜰폰)", loan.auto_loan_terms_ae)]
            for text, xpath in verification_list_b:
                try:
                    Result_b = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, Result_b.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            try:
                autoloan.auto_loan_terms_aa()
                time.sleep(6)
                Result_ba = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_aa_r)
                self.assertIn("통신사 이용약관", Result_ba.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관Aa진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관Aa진입_error : {e}")
                base.save_screenshot('자동차대출약관Aa진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_ab()
                time.sleep(6)
                Result_bb = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ab_r)
                self.assertIn("개인정보 수집/이용/취급 위탁동의", Result_bb.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관Ab진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관Ab진입_error : {e}")
                base.save_screenshot('자동차대출약관Ab진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_ac()
                time.sleep(6)
                Result_bc = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ac_r)
                self.assertIn("고유식별정보처리 동의", Result_bc.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관Ac진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관Ac진입_error : {e}")
                base.save_screenshot('자동차대출약관Ac진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_ad()
                time.sleep(8)
                Result_bd = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ad_r)
                self.assertIn("본인확인서비스 이용약관", Result_bd.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관Ad진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관Ad진입_error : {e}")
                base.save_screenshot('자동차대출약관Ad진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_ae()
                time.sleep(6)
                Result_be = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ae_r)
                self.assertIn("개인정보 제3자 제공 동의", Result_be.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관Ae진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관Ae진입_error : {e}")
                base.save_screenshot('자동차대출약관Ae진입_error')
            base.android_back()
            time.sleep(3)
            autoloan.auto_loan_terms_a_unfold()
            autoloan.auto_loan_terms_b_unfold()
            verification_list_c = [("오토론 서비스 이용약관", loan.auto_loan_terms_ba),
                                   ("핀다 개인(신용)정보 수집이용제공 동의서", loan.auto_loan_terms_bb)]
            for text, xpath in verification_list_c:
                try:
                    Result_c = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, Result_c.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            try:
                autoloan.auto_loan_terms_ba()
                time.sleep(6)
                Result_ca = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ba_r)
                self.assertIn("서비스 이용 약관 [오토론]", Result_ca.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관ba진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관ba진입_error : {e}")
                base.save_screenshot('자동차대출약관ba진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_bb()
                time.sleep(6)
                Result_cb = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_bb_r)
                self.assertIn("핀다 개인(신용)정보 수집이용제공 동의[오토론]", Result_cb.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관bb진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관bb진입_erro : {e}r")
                base.save_screenshot('자동차대출약관bb진입_error')
            base.android_back()
            time.sleep(3)
            autoloan.auto_loan_terms_b_unfold()
            autoloan.auto_loan_terms_c_unfold()
            base.scroll(0.15)
            verification_list_c = [("금융기관 개인(신용)정보 수집이용제공 동의[오토론]", loan.auto_loan_terms_ca),
                                   ("개인(신용)정보 조회 동의서[오토론]", loan.auto_loan_terms_cb),
                                   ("개인(신용)정보 수집 이용 제공 동의서[오토론]", loan.auto_loan_terms_cc),
                                   ("개인(신용)정보 수집이용제공동의서[가계여신 금융 거래][오토론]", loan.auto_loan_terms_cd),
                                   ("계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용) [오토론]", loan.auto_loan_terms_ce),
                                   ("개인정보 제 3자 제공 동의서[OPENAPI][오토론]", loan.auto_loan_terms_cf)]
            for text, xpath in verification_list_c:
                try:
                    Result_c = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, Result_c.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            try:
                autoloan.auto_loan_terms_ca()
                time.sleep(6)
                Result_da = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ca_r)
                self.assertIn("금융기관 개인(신용)정보 수집이용제공 동의[오토론]", Result_da.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관ca진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관ca진입_error : {e}")
                base.save_screenshot('자동차대출약관ca진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_cb()
                time.sleep(6)
                Result_db = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cb_r)
                self.assertIn("개인(신용)정보 조회 동의서[오토론]", Result_db.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관cb진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관cb진입_error : {e}")
                base.save_screenshot('자동차대출약관cb진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_cc()
                time.sleep(6)
                Result_dc = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cc_r)
                self.assertIn("개인(신용)정보 수집 이용 제공 동의서[오토론]", Result_dc.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관cc진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관cc진입_error : {e}")
                base.save_screenshot('자동차대출약관cc진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_cd()
                time.sleep(6)
                Result_dd = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cd_r)
                self.assertIn("개인(신용)정보 수집이용제공동의서[가계여신 금융 거래][오토론]", Result_dd.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관cd진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관cd진입_error : {e}")
                base.save_screenshot('자동차대출약관cd진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_ce()
                time.sleep(6)
                Result_de = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ce_r)
                self.assertIn("계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[오토론]", Result_de.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관ce진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관ce진입_error : {e}")
                base.save_screenshot('자동차대출약관ce진입_error')
            base.android_back()
            time.sleep(3)
            try:
                autoloan.auto_loan_terms_cf()
                time.sleep(6)
                Result_df = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cf_r)
                self.assertIn("개인정보 제 3자 제공 동의서[OPENAPI][오토론]", Result_df.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
                base.save_screenshot('자동차대출약관cf진입_fail')
            except Exception as e:
                results_a.append("Error")
                logging.warning(f"자동차대출약관cf진입_error : {e}")
                base.save_screenshot('자동차대출약관cf진입_error')
            base.android_back()
            time.sleep(3)
            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("자동차 대출 약관 노출 : PASS")
                loanresult.reports.append("자동차 대출 약관 노출 : *PASS*")
            else:
                logging.info("자동차 대출 약관 노출 : FAIL")
                loanresult.reports.append("자동차 대출 약관 노출 : *FAIL*")
                base.save_screenshot('자동차대출약관노출_fail')
            logging.info(results_a)
            if all(result == "PASS" for result in results_a):
                logging.info("자동차 대출 약관 진입 결과 : PASS")
                loanresult.reports.append("자동차 대출 약관 진입 결과 : *PASS*")
            else:
                logging.info("자동차 대출 약관 진입 결과 : FAIL")
                loanresult.reports.append("자동차 대출 약관 진입 결과 : *FAIL*")
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 약관 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 약관 테스트 종료")

    # 오토론 인증번호 자동입력 테스트
    def test_auto_loan_new_new_car_certification_number(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        logging.info("오토론 인증번호 자동입력 테스트 시작")
        try:
            myhome.auto_Loan_Banner()
            autoloan.auto_loan_terms_of_use()
            autoloan.auto_loan_terms_all()
            autoloan.auto_loan_terms_check()
            autoloan.auto_loan_terms_next()
            time.sleep(4)
            autoloan.auto_loan_terms_next()
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_certification_number)
                self.assertIn("주민등록번호 뒷자리 입력", Result.text)
                logging.info("오토론 인증번호 자동입력 : PASS")
                loanresult.reports.append("오토론 인증번호 자동입력 : PASS")
            except AssertionError:
                logging.info("오토론 인증번호 자동입력 : FAIL")
                loanresult.reports.append("오토론 인증번호 자동입력 : FAIL")
                base.save_screenshot('오토론인증번호자동입력_fail')
            except Exception as e:
                logging.warning(f"오토론 인증번호 자동입력 결과 에러 발생 : {e}")
                loanresult.reports.append("오토론 인증번호 자동입력 : Error")
                base.save_screenshot('오토론인증번호자동입력_error')
            base.android_back()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 인증번호 자동입력 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 인증번호 자동입력 테스트 종료")

    # 오토론 신차 신규 대출 조회 테스트
    def test_auto_loan_new(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        info = InFo()
        logging.info("오토론 신차 신규 대출 조회 테스트 시작")
        try:
            myhome.auto_Loan_Banner()
            autoloan.auto_loan_terms_of_use()
            autoloan.auto_loan_terms_all()
            autoloan.auto_loan_terms_check()
            autoloan.auto_loan_terms_next()
            time.sleep(4)
            autoloan.auto_loan_terms_next()
            autoloan.auto_loan_rrn()
            autoloan.auto_loan_terms_next()
            autoloan.auto_loan_annual_income()
            autoloan.auto_loan_terms_next()
            autoloan.auto_loan_new()
            autoloan.auto_loan_newcar()
            autoloan.auto_loan_terms_check()
            autoloan.auto_loan_terms_check()
            time.sleep(60)
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
                self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result.text)
                logging.info("오토론 신차 신규 대출 조회(조회성공) : PASS")
                loanresult.reports.append("오토론 신차 신규 대출 조회(조회성공) : PASS")
            except AssertionError:
                logging.info("오토론 신차 신규 대출 조회(조회성공) : FAIL")
                loanresult.reports.append("오토론 신차 신규 대출 조회(조회성공) : FAIL")
                base.save_screenshot('오토론신차신규대출조회_fail')
            except :
                try:
                    Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                    self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                    logging.info("오토론 신차 신규 대출 조회(부결) : PASS")
                    loanresult.reports.append("오토론 신차 신규 대출 조회(부결) : PASS")
                except AssertionError:
                    logging.info("오토론 신차 신규 대출 조회(부결) : FAIL")
                    loanresult.reports.append("오토론 신차 신규 대출 조회(부결) : FAIL")
                    base.save_screenshot('오토론신차신규대출조회_fail')
                except Exception as e:
                    logging.warning(f"오토론 신차 신규 대출 조회 에러 발생 : {e}")
                    loanresult.reports.append("오토론 신차 신규 대출 조회 : Error")
                    base.save_screenshot('오토론신차신규대출조회_error')
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 신차 신규 대출 조회 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 신차 신규 대출 조회 테스트 종료")

    # 오토론 대출 상세 진입
    def test_auto_loan_detail(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        logging.info("오토론 대출 상세 진입 테스트 시작")
        try:
            myhome.auto_Loan_Banner()
            autoloan.auto_loan_detail()
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_detail_result)
                self.assertIn("조회결과", Result.text)
                logging.info("오토론 대출 상세 진입 : PASS")
                loanresult.reports.append("오토론 대출 상세 진입 : PASS")
            except AssertionError:
                logging.info("오토론 대출 상세 진입 : FAIL")
                loanresult.reports.append("오토론 대출 상세 진입 : FAIL")
                base.save_screenshot('오토론대출상세진입_fail')
            except Exception as e:
                logging.warning(f"오토론 대출 상세 진입 결과 에러 발생 : {e}")
                loanresult.reports.append("오토론 대출 상세 진입 : Error")
                base.save_screenshot('오토론대출상세진입_error')
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 대출 상세 진입 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 대출 상세 진입 테스트 종료")

    # 오토론 대출 신청하기 및 홈페이지 진입
    def test_auto_loan_application(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        logging.info("오토론 대출 신청하기 및 홈페이지 진입 테스트 시작")
        try:
            myhome.auto_Loan_Banner()
            autoloan.auto_loan_detail()
            autoloan.auto_loan_application()
            results = []
            verification_list = [("하나은행 홈페이지로\n이동할게요", loan.auto_loan_application_r_a),
                                 ("대출 신청", loan.auto_loan_application_r_b),
                                 ("서류 제출", loan.auto_loan_application_r_c),
                                 ("약정 및 입금", loan.auto_loan_application_r_d),
                                 ("출고 확인", loan.auto_loan_application_r_e),
                                 ("진행을 위해 이런 서류들이 필요해요!", loan.auto_loan_application_r_f)]
            for text, xpath in verification_list:
                try:
                    Result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, Result.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("오토론 대출 신청 : PASS")
                loanresult.reports.append("오토론 대출 신청 : *PASS*")
            else:
                logging.info("오토론 대출 신청 : FAIL")
                loanresult.reports.append("오토론 대출 신청 : *FAIL*")
                base.save_screenshot('오토론대출신청_fail')
            time.sleep(2)
            autoloan.auto_loan_terms_next()
            time.sleep(5)
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_url_r)
                self.assertIn("하나은행 X 핀다", Result_a.text)
                logging.info("오토론 대출 신청 하나은행 홈페이지 진입 : PASS")
                loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : PASS")
            except AssertionError:
                logging.info("오토론 대출 신청 하나은행 홈페이지 진입 : FAIL")
                loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : FAIL")
                base.save_screenshot('오토론대출신청_하나은행홈페이지진입_fail')
            except Exception as e:
                logging.warning(f"오토론 대출 신청 하나은행 홈페이지 진입 에러 발생 : {e}")
                loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : Error")
                base.save_screenshot('오토론대출신청_하나은행홈페이지진입_error')
            base.android_back()
            base.android_back()
            autoloan.auto_loan_application_exit()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 대출 신청하기 및 홈페이지 진입 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 대출 신청하기 및 홈페이지 진입 테스트 종료")

    # 오토론 중고차 신규 대출 조회 테스트
    def test_auto_loan_new_used_car(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        join = JoIn()
        more = More()
        seting = Seting()
        logging.info("오토론 중고차 신규 대출 조회 테스트 시작")
        try:
            info.user_id.clear()
            info.usertoken.clear()
            info.txseqno.clear()
            info.idtoken.clear()
            more.etc_in()
            seting.seting_in()
            base.scroll(2)
            base.user_id_get()
            base.user_token_get()
            base.user_txseqno_get()
            join.join_mms()
            base.user_idtoken_get()
            autoloan.auto_loan_new_used_car()
            base.android_back()
            base.android_back()
            base.scroll(2)
            myhome.auto_Loan_Banner()
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
                self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
                logging.info("오토론 중고차 신규 대출 조회 : PASS")
                loanresult.reports.append("오토론 중고차 신규 대출 조회(조회성공) : PASS")
            except AssertionError:
                logging.info("오토론 중고차 신규 대출 조회(조회성공) : FAIL")
                loanresult.reports.append("오토론 중고차 신규 대출 조회(조회성공) : FAIL")
                base.save_screenshot('오토론중고차신규대출조회_fail')
            except Exception:
                try:
                    Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                    self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                    logging.info("오토론 중고차 신규 대출 조회 : PASS")
                    loanresult.reports.append("오토론 중고차 신규 대출 조회(부결) : PASS")
                except AssertionError:
                    logging.info("오토론 중고차 신규 대출 조회(부결) : FAIL")
                    loanresult.reports.append("오토론 중고차 신규 대출 조회(부결) : FAIL")
                    base.save_screenshot('오토론중고차신규대출조회_fail')
                except Exception as e:
                    logging.warning(f"오토론 중고차 신규 대출 조회 에러 발생 : {e}")
                    loanresult.reports.append("오토론 중고차 신규 대출 조회 : Error")
                    base.save_screenshot('오토론중고차신규대출조회_error')
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 중고차 신규 대출 조회 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 중고차 신규 대출 조회 테스트 종료")

    # 오토론 신차 대환 대출 조회 테스트
    def test_auto_loan_existing_new_car(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        logging.info("오토론 신차 대환 대출 조회 테스트 시작")
        try:
            autoloan.auto_loan_existing_new_car()
            myhome.auto_Loan_Banner()
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
                self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
                logging.info("오토론 신차 대환 대출 조회 : PASS")
                loanresult.reports.append("오토론 신차 대환 대출 조회(조회성공) : PASS")
            except AssertionError:
                logging.info("오토론 신차 대환 대출 조회(조회성공) : FAIL")
                loanresult.reports.append("오토론 신차 대환 대출 조회(조회성공) : FAIL")
                base.save_screenshot('오토론신차대환대출조회_fail')
            except :
                try:
                    Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                    self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                    logging.info("오토론 신차 대환 대출 조회 : PASS")
                    loanresult.reports.append("오토론 신차 대환 대출 조회(부결) : PASS")
                except AssertionError:
                    logging.info("오토론 신차 대환 대출 조회(부결) : FAIL")
                    loanresult.reports.append("오토론 신차 대환 대출 조회(부결) : FAIL")
                    base.save_screenshot('오토론신차대환대출조회_fail')
                except Exception as e:
                    logging.warning(f"오토론 신차 대환 대출 조회 에러 발생 : {e}")
                    loanresult.reports.append("오토론 신차 대환 대출 조회 : Error")
                    base.save_screenshot('오토론신차대환대출조회_error')
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 신차 대환 대출 조회 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 신차 대환 대출 조회 테스트 종료")

    # 오토론 중고차 대환 대출 조회 테스트
    def test_auto_loan_existing_used_car(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        logging.info("오토론 중고차 대환 대출 조회 테스트 시작")
        try:
            autoloan.auto_loan_existing_used_car()
            myhome.auto_Loan_Banner()
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
                self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
                logging.info("오토론 중고차 대환 대출 조회 : PASS")
                loanresult.reports.append("오토론 중고차 대환 대출 조회(조회성공) : PASS")
            except AssertionError:
                logging.info("오토론 중고차 대환 대출 조회(조회성공) : FAIL")
                loanresult.reports.append("오토론 중고차 대환 대출 조회(조회성공) : FAIL")
                base.save_screenshot('오토론중고차대환대출조회_fail')
            except :
                try:
                    Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                    self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                    logging.info("오토론 중고차 대환 대출 조회 : PASS")
                    loanresult.reports.append("오토론 중고차 대환 대출 조회(부결) : PASS")
                except AssertionError:
                    logging.info("오토론 중고차 대환 대출 조회(부결) : FAIL")
                    loanresult.reports.append("오토론 중고차 대환 대출 조회(부결) : FAIL")
                    base.save_screenshot('오토론중고차대환대출조회_fail')
                except Exception as e:
                    logging.warning(f"오토론 중고차 대환 대출 조회 에러 발생 : {e}")
                    loanresult.reports.append("오토론 중고차 대환 대출 조회 : Error")
                    base.save_screenshot('오토론중고차대환대출조회_error')
            base.android_back()
        except Exception as e:
            logging.error(f"오토론 중고차 대환 대출 조회 테스트 진행 중 에러 발생 : {e}")
        logging.info("오토론 중고차 대환 대출 조회 테스트 종료")

class LoanComparisonTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("비교대출 테스트 시작")
    @classmethod
    def tearDownClass(cls):
        logging.info("비교대출 테스트 종료")
    def setUp(self):
        base = basemethod()
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    def tearDown(self):
        base = basemethod()
        base.android_back()
        base.android_back()
        base.android_back()

    # 비교대출 약관 페이지 진입 테스트
    def test_loan_terms_and_conditions(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        logging.info("비교대출 약관 페이지 진입 테스트 시작")
        try:
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
            base.scroll_up(0.2)
            comparisonloan.loan_in()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            results = []
            results_a = []
            time.sleep(4)
            verification_list = [("본인인증 필수 항목 모두 동의", loan.loan_terms_and_conditions_A_result),
                                 ("핀다 필수 항목 모두 동의", loan.loan_terms_and_conditions_B_result),
                                 ("금융기관 필수 항목 모두 동의", loan.loan_terms_and_conditions_C_result),
                                 ("서비스 이용 안내 수신 동의 (선택)", loan.loan_terms_and_conditions_D_result)]
            for text, xpath in verification_list:
                try:
                    result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("비교대출 약관 노출 : PASS")
                loanresult.reports.append("비교대출 약관 노출 : *PASS*")
            else:
                logging.info("비교대출 약관 노출 : FAIL")
                loanresult.reports.append("비교대출 약관 노출 : *FAIL*")
                base.save_screenshot('비교대출약관노출_fail')
            comparisonloan.loan_terms_and_conditions_a()
            try:
                comparisonloan.loan_terms_and_conditions_aa()
                Result_Aa = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Aa_result)
                self.assertEqual(Result_Aa.text, "통신사 이용약관")
                logging.info("비교대출 약관 Aa 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Aa 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Aa_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Aa 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Aa_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ab()
                Result_Ab = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ab_result)
                self.assertEqual(Result_Ab.text, "개인정보 수집/이용/취급 위탁동의")
                logging.info("비교대출 약관 Ab 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ab 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ab_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ab 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ab_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ac()
                Result_Ac = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ac_result)
                self.assertEqual(Result_Ac.text, "고유식별정보처리 동의")
                logging.info("비교대출 약관 Ac 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ac 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ac_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ac 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ac_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ad()
                Result_Ad = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ad_result)
                self.assertIn("KCB휴대폰 본인확인 이용약관", Result_Ad.text)
                logging.info("비교대출 약관 Ad 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ad 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ad_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ad 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ad_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ae()
                Result_Ae = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ae_result)
                self.assertEqual(Result_Ae.text, "개인정보 제3자 제공 동의")
                logging.info("비교대출 약관 Ae 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ae 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ae_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ae 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ae_error')
            base.android_back()
            comparisonloan.loan_terms_and_conditions_a()
            comparisonloan.loan_terms_and_conditions_b()
            base.scroll(0.065)
            try:
                comparisonloan.loan_terms_and_conditions_ba()
                Result_Ba = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ba_result)
                self.assertEqual(Result_Ba.text, "개인(신용)정보 수집·이용·제공 동의서(FINDA)")
                logging.info("비교대출 약관 Ba 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ba 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ba_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ba 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ba_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_bb()
                Result_Bb = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bb_result)
                self.assertEqual(Result_Bb.text, "서비스 이용 약관 [대출비교]")
                logging.info("비교대출 약관 Bb 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Bb 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Bb_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Bb 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Bb_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_bc()
                Result_Bc = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bc_result)
                self.assertEqual(Result_Bc.text, "[간편인증] 서비스 이용 약관 동의")
                logging.info("비교대출 약관 Bc 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Bc 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Bc_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Bc 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Bc_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_bd()
                Result_Bd = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bd_result)
                self.assertEqual(Result_Bd.text, "[간편인증] 개인정보 이용 동의")
                logging.info("비교대출 약관 Bd 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Bd 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Bd_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Bd 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Bd_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_be()
                Result_Be = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Be_result)
                self.assertEqual(Result_Be.text, "[간편인증] 제3자 정보제공 동의")
                logging.info("비교대출 약관 Be 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Be 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Be_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Be 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Be_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_bf()
                Result_Bf = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bf_result)
                self.assertEqual(Result_Bf.text, "[간편인증] 고유식별번호처리 동의")
                logging.info("비교대출 약관 Bf 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Bf 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Bf_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Bf 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Bf_error')
            base.android_back()
            comparisonloan.loan_terms_and_conditions_b()
            comparisonloan.loan_terms_and_conditions_c()
            try:
                comparisonloan.loan_terms_and_conditions_ca()
                Result_Ca = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ca_result)
                self.assertEqual(Result_Ca.text, "개인(신용)정보 수집·이용·제공 동의서(금융기관 용)")
                logging.info("비교대출 약관 Ca 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ca 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ca_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ca 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ca_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cb()
                Result_Cb = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cb_result)
                self.assertEqual(Result_Cb.text, "개인(신용)정보 수집·이용·제공·조회 동의서(금융기관 용)")
                logging.info("비교대출 약관 Cb 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cb 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cb_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cb 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cb_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cc()
                Result_Cc = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cc_result)
                self.assertEqual(Result_Cc.text, "고유식별정보 수집·이용·제공·조회 동의서")
                logging.info("비교대출 약관 Cc 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cc 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cc_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cc 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cc_error')
            base.android_back()
            base.scroll(0.25)
            try:
                comparisonloan.loan_terms_and_conditions_cd()
                Result_Cd = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cd_result)
                self.assertEqual(Result_Cd.text, "개인(신용)정보 조회 동의서(서민금융진흥원)")
                logging.info("비교대출 약관 Cd 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cd 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cd_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cd 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cd_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ce()
                Result_Ce = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ce_result)
                self.assertEqual(Result_Ce.text, "개인정보 수집·이용·제공 동의서(서민금융진흥원)")
                logging.info("비교대출 약관 Ce 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ce 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ce_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ce 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ce_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cf()
                Result_Cf = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cf_result)
                self.assertEqual(Result_Cf.text, "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[비교대출]")
                logging.info("비교대출 약관 Cf 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cf 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cf_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cf 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cf_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cg()
                Result_Cg = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cg_result)
                self.assertEqual(Result_Cg.text, "개인(신용)정보 제3자 제공 동의서 [토스뱅크][비교대출]")
                logging.info("비교대출 약관 Cg 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cg 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cg_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cg 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cg_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ch()
                Result_Ch = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ch_result)
                self.assertEqual(Result_Ch.text, "개인(신용)정보 제3자 제공 동의서 [중소기업중앙회][비교대출]")
                logging.info("비교대출 약관 Ch 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ch 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ch_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ch 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ch_error')
            base.android_back()
            base.scroll(0.25)
            try:
                comparisonloan.loan_terms_and_conditions_ci()
                Result_Ci = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ci_result)
                self.assertEqual(Result_Ci.text, "개인(신용)정보 제3자 제공 동의서 [OPENAPI][비교대출]")
                logging.info("비교대출 약관 Ci 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ci 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ci_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ci 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ci_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cj()
                Result_Cj = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cj_result)
                self.assertEqual(Result_Cj.text, "개인(신용)정보 수집 이용 제공 조회 동의서 [서민금융진흥원][비교대출]")
                logging.info("비교대출 약관 Cj 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cj 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cj_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cj 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cj_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ck()
                Result_Ck = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ck_result)
                self.assertEqual(Result_Ck.text, "개인(신용)정보 제 3자 제공 조회 동의서 [대안정보이용][비교대출]")
                logging.info("비교대출 약관 Ck 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ck 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ck_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ck 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ck_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cl()
                Result_Cl = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cl_result)
                self.assertEqual(Result_Cl.text, "[비교대출] 개인(신용)정보 수집∙이용 동의서(KCB대안신용평가모델)")
                logging.info("비교대출 약관 Cl 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cl 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cl_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cl 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cl_error')
            base.android_back()
            base.scroll(0.25)
            try:
                comparisonloan.loan_terms_and_conditions_cm()
                Result_Cm = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cm_result)
                self.assertEqual(Result_Cm.text, "[비교대출] 개인(신용)정보 이용 및 제3자 제공 동의서(KCB대안신용평가모델)")
                logging.info("비교대출 약관 Cm 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cm 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cm_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cm 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cm_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cn()
                Result_Cn = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cn_result)
                self.assertEqual(Result_Cn.text, "[비교대출] 개인(신용)정보 수집∙이용∙제공∙조회 동의서(케이뱅크)")
                logging.info("비교대출 약관 Cn 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cn 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cn_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cn 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cn_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_co()
                Result_Co = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Co_result)
                self.assertEqual(Result_Co.text, "[비교대출] 개인(신용)정보 수집∙이용∙제공 동의서(케이뱅크)")
                logging.info("비교대출 약관 Co 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Co 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Co_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Co 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Co_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cp()
                Result_Cp = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cp_result)
                self.assertEqual(Result_Cp.text, "[비교대출] 개인(신용)정보 수집∙이용 동의서(대안정보)")
                logging.info("비교대출 약관 Cp 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cp 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cp_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cp 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cp_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cq()
                Result_Cq = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cq_result)
                self.assertEqual(Result_Cq.text, "[비교대출] 개인(신용)정보 수집∙이용∙제공∙조회 동의서(대안정보)")
                logging.info("비교대출 약관 Cq 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cq 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cq_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cq 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cq_error')
            base.android_back()
            base.scroll(0.25)
            try:
                comparisonloan.loan_terms_and_conditions_cr()
                Result_Cr = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cr_result)
                self.assertEqual(Result_Cr.text, "[비교대출] 개인(신용)정보 제3자 제공 동의서(통신정보 신용평가반영)")
                logging.info("비교대출 약관 Cr 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cr 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cr_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cr 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cr_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cs()
                Result_Cs = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cs_result)
                self.assertEqual(Result_Cs.text, "[비교대출] 개인(신용)정보 제3자 제공 동의서(대안정보)")
                logging.info("비교대출 약관 Cs 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cs 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cs_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cs 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cs_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_ct()
                Result_Ct = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ct_result)
                self.assertEqual(Result_Ct.text, "[비교대출] 개인(신용)정보 수집∙이용∙제공 동의서(우리은행)")
                logging.info("비교대출 약관 Ct 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Ct 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Ct_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Ct 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Ct_error')
            base.android_back()
            base.scroll(0.25)
            try:
                comparisonloan.loan_terms_and_conditions_cu()
                Result_Cu = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cu_result)
                self.assertEqual(Result_Cu.text, "[비교대출] 개인(신용)정보 제3자 제공 동의서(우리은행)")
                logging.info("비교대출 약관 Cu 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cu 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cu_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cu 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cu_error')
            base.android_back()
            try:
                comparisonloan.loan_terms_and_conditions_cv()
                Result_Cv = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cv_result)
                self.assertEqual(Result_Cv.text, "[비교대출] 개인(신용)정보 수집∙이용∙제공∙조회 동의서(우리은행)")
                logging.info("비교대출 약관 Cv 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Cv 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Cv_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Cv 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Cv_error')
            base.android_back()
            comparisonloan.loan_terms_and_conditions_d()
            try:
                comparisonloan.loan_terms_and_conditions_da()
                Result_Da = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Da_result)
                self.assertEqual(Result_Da.text, "개인정보 제3자 제공 동의(대출안심플랜)")
                logging.info("비교대출 약관 Da 진입 : PASS")
                results_a.append("PASS")
            except AssertionError:
                logging.info("비교대출 약관 Da 진입 : FAIL")
                results_a.append("FAIL")
                base.save_screenshot('비교대출약관Da_fail')
            except Exception as e:
                logging.warning(f"비교대출 약관 Da 진입 에러 발생 : {e}")
                results_a.append("Error")
                base.save_screenshot('비교대출약관Da_error')
            base.android_back()
            logging.info(results_a)
            if all(result == "PASS" for result in results_a):
                logging.info("비교대출 약관 진입 결과 : PASS")
                loanresult.reports.append("비교대출 약관 진입 결과 : *PASS*")
            else:
                logging.info("비교대출 약관 진입 결과 : FAIL")
                loanresult.reports.append("비교대출 약관 진입 결과 : *FAIL*")
        except Exception as e:
            logging.error(f"비교대출 약관 페이지 진입 테스트 진행중 에러 발생 : {e}")
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()
        base.android_back()
        logging.info("비교대출 약관 페이지 진입 테스트 종료")

    # 비교대출 인증번호 자동 입력 및 재전송 테스트
    def test_loan_comparison_verification_code(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        logging.info("비교대출 인증번호 자동 입력 및 재전송 테스트 시작")
        try:
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
                                logging.error("비교대출 배너 진입 에러 발생 : {}".format(str(e)))
            base.scroll_up(0.2)
            comparisonloan.loan_in()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            comparisonloan.loan_terms_and_conditions_all()
            comparisonloan.check_loan()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(5)
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.comparison_loan_verification_result)
                self.assertEqual(Result_a.text, "주민등록번호 뒷자리 입력")
                logging.info("비교대출 인증번호 자동입력 결과 : PASS")
                loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *PASS*")
            except AssertionError:
                logging.info("비교대출 인증번호 자동입력 결과 : FAIL")
                loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *FAIL*")
                base.save_screenshot('비교대출인증번호자동입력_fail')
            except Exception as e:
                logging.warning(f"비교대출 인증번호 자동입력 결과 에러 발생 : {e}")
                loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *Error*")
                base.save_screenshot('비교대출인증번호자동입력_error')
            base.android_back()
            base.android_back()
            comparisonloan.comparison_loan_verification_resend()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(5)
            try:
                Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.comparison_loan_verification_result)
                self.assertEqual(Result_b.text, "주민등록번호 뒷자리 입력")
                logging.info("비교대출 인증번호 재요청 결과 : PASS")
                loanresult.reports.append("비교대출 인증번호 재요청 결과 : *PASS*")
            except AssertionError:
                logging.info("비교대출 인증번호 재요청 결과 : FAIL")
                loanresult.reports.append("비교대출 인증번호 재요청 결과 : *FAIL*")
                base.save_screenshot('비교대출인증번호재요청_fail')
            except Exception as e:
                logging.warning(f"비교대출 인증번호 재요청 결과 에러 발생 : {e}")
                loanresult.reports.append("비교대출 인증번호 재요청 결과 : *Error*")
                base.save_screenshot('비교대출인증번호재요청_error')
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 인증번호 자동 입력 및 재전송 테스트 진행중 에러 발생 : {e}")
        logging.info("비교대출 인증번호 자동 입력 및 재전송 테스트 종료")

    # 비교대출 주민번호 적합서 검사 테스트
    def test_rrn_validation_check(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        results = []
        comparisonloan = ComparisonLoan()
        logging.info("비교대출 주민번호 적합서 검사 테스트 시작")
        time.sleep(3)
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            base.scroll_up(0.2)
            comparisonloan.loan_in()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            comparisonloan.loan_terms_and_conditions_all()
            comparisonloan.check_loan()
            time.sleep(5)
            comparisonloan.next_loan()
            comparisonloan.rrn_fail_input()
            comparisonloan.next_loan()
            time.sleep(3)
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.rrn_validation_fail_result)
                self.assertEqual(Result_a.text, "주민등록번호를 다시 한 번 확인해주세요.")
                logging.info("비교대출 주민등록번호 적합성 실패 결과 : PASS")
                results.append("PASS")
            except AssertionError:
                logging.info("비교대출 주민등록번호 적합성 실패 결과 : FAIL")
                results.append("FAIL")
                base.save_screenshot('비교대출주민번호적합성실패_fail')
            except Exception as e:
                logging.warning(f"비교대출 주민등록번호 적합성 실패 결과 에러 발생 : {e}")
                results.append("Error")
                base.save_screenshot('비교대출주민번호적합성실패_error')
            comparisonloan.check_loan()
            base.android_back()
            comparisonloan.comparison_loan_verification_resend()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(3)
            comparisonloan.rrn_pass_input()
            comparisonloan.next_loan()
            time.sleep(3)
            try:
                Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.rrn_validation_pass_result)
                self.assertEqual(Result_b.text, "소득 정보 입력")
                logging.info("비교대출 주민등록번호 적합성 성공 결과 : PASS")
                results.append("PASS")
            except AssertionError:
                logging.info("비교대출 주민등록번호 적합성 성공 결과 : FAIL")
                results.append("FAIL")
                base.save_screenshot('비교대출주민번호적합성성공_fail')
            except Exception as e:
                logging.warning(f"비교대출 주민등록번호 적합성 성공 결과 에러 발생 : {e}")
                results.append("Error")
                base.save_screenshot('비교대출주민번호적합성성공_error')
            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("비교대출 주민등록번호 적합성 검사 결과 : PASS")
                loanresult.reports.append("비교대출 주민등록번호 적합성 검사 테스트 결과 : *PASS*")
            else:
                logging.info("비교대출 주민등록번호 적합성 검사 결과 : FAIL")
                loanresult.reports.append("비교대출 주민등록번호 적합성 검사 테스트 결과 : *FAIL*")
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 주민번호 적합서 검사 테스트 진행중 에러 발생 : {e}")
        logging.info("비교대출 주민번호 적합서 검사 테스트 종료")

    # 비교대출 후담대 조회 및 열람 테스트 & 직장인대출 조회 > 인증서 없이 조회 테스트 & 안심번호 테스트
    def test_loan_comparison_apt_secured_loan(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
        logging.info("비교대출 후담대 조회 및 열람 테스트 & 직장인대출 조회 > 인증서 없이 조회 테스트 & 안심번호 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            base.scroll_up(0.2)
            comparisonloan.loan_in()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            comparisonloan.loan_terms_and_conditions_all()
            comparisonloan.check_loan()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(3)
            comparisonloan.rrn_pass_input()
            comparisonloan.next_loan()
            comparisonloan.office_workers()
            comparisonloan.company_name_input()
            comparisonloan.search()
            base.scroll(1)
            comparisonloan.company_number()
            comparisonloan.full_time()
            comparisonloan.check_loan()
            comparisonloan.workplace_insurance()
            comparisonloan.annualincome_input()
            comparisonloan.check_loan()
            comparisonloan.my_house_apt()
            comparisonloan.check_loan()
            comparisonloan.address_search()
            # time.sleep(4)
            # comparisonloan.check_loan()
            comparisonloan.no_certificate()
            time.sleep(3)
            verification_list = [("최저금리", loan.safe_number_result_a),
                                 ("대출가능", loan.safe_number_result_b),
                                 ("오늘입금", loan.safe_number_result_c),
                                 ("계좌개설 없음", loan.safe_number_result_d),
                                 ("금리 낮은순", loan.safe_number_result_e)]
            for text, xpath in verification_list:
                try:
                    result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")

            print(results)
            if all(result == "PASS" for result in results):
                logging.info("안심번호 결과 : PASS")
                loanresult.reports.append("안심번호 결과 : *PASS*")
                logging.info("직장인 대출 조회 (직장의료보험 선택) - 인증서 사용안함 결과 : PASS")
                loanresult.reports.append("직장인 대출 조회 (직장의료보험 선택) - 인증서 사용안함 결과 : *PASS*")
            else:
                logging.info("안심번호 결과 : FAIL")
                loanresult.reports.append("안심번호 결과 : *FAIL*")
                logging.info("직장인 대출 조회 (직장의료보험 선택) - 인증서 사용안함 결과 : FAIL")
                loanresult.reports.append("직장인 대출 조회 (직장의료보험 선택) - 인증서 사용안함 결과 : *FAIL*")
                base.save_screenshot('안심번호결과&직장인대출조회_인증서사용안함_fail')
            comparisonloan.type_of_loan()
            comparisonloan.secured_loan()
            time.sleep(3)
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.secured_loan_result_a)
                self.assertEqual(Result_a.text, "아파트담보대출")
                logging.info("비교대출 후담대 조회 및 열람 결과 : PASS")
                loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *PASS*")
            except AssertionError:
                logging.infov("비교대출 후담대 조회 및 열람 결과 : FAIL")
                loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *FAIL*")
                base.save_screenshot('비교대출후담대결과_fail')
            except Exception:
                try:
                    Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.secured_loan_result_b)
                    self.assertEqual(Result_b.text, "주택담보대출")
                    logging.info("비교대출 후담대 조회 및 열람 결과 : PASS")
                    loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *PASS*")
                except AssertionError:
                    logging.info("비교대출 후담대 조회 및 열람 결과 : FAIL")
                    loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *FAIL*")
                    base.save_screenshot('비교대출후담대결과_fail')
                except Exception as e:
                    logging.warning(f"비교대출 후담대 조회 및 열람 결과 에러 발생 : {e}")
                    loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *Error*")
                    base.save_screenshot('비교대출후담대결과_error')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 후담대 조회 및 열람 테스트 & 직장인대출 조회 > 인증서 없이 조회 테스트 & 안심번호 테스트 진행중 에러 발생 :{e}")
        logging.info("비교대출 후담대 조회 및 열람 테스트 & 직장인대출 조회 > 인증서 없이 조회 테스트 & 안심번호 테스트 종료")

    # 오늘 입금 태그 확인 테스트
    def test_check_deposit_today(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        logging.info("오늘 입금 태그 확인 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            try:
                Result_A = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                self.assertEqual(Result_A.text, "오늘입금")
                logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
            except:
                try:
                    base.scroll(0.7)
                    time.sleep(3)
                    Result_B = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                    self.assertEqual(Result_B.text, "오늘입금")
                    logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                    loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
                except:
                    try:
                        base.scroll(0.7)
                        time.sleep(3)
                        Result_C = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                        self.assertEqual(Result_C.text, "오늘입금")
                        logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                        loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
                    except:
                        try:
                            base.scroll(0.7)
                            time.sleep(3)
                            Result_D = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                            self.assertEqual(Result_D.text, "오늘입금")
                            logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                            loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
                        except:
                            try:
                                base.scroll(0.7)
                                time.sleep(3)
                                Result_E = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                                self.assertEqual(Result_E.text, "오늘입금")
                                logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                                loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
                            except:
                                try:
                                    base.scroll(0.7)
                                    time.sleep(3)
                                    Result_F = WebDriver.driver.find_element(MobileBy.XPATH, loan.deposit_today)
                                    self.assertEqual(Result_F.text, "오늘입금")
                                    logging.info("비교대출 오늘입금 태그노출 결과 : PASS")
                                    loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *PASS*")
                                except AssertionError:
                                    logging.info("비교대출 오늘입금 태그노출 결과 : FAIL")
                                    loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *FAIL*")
                                    base.save_screenshot('비교대출오늘입금태그노출결과_fail')
                                except Exception as e:
                                    logging.warning(f"비교대출 오늘입금 태그노출 결과 : {e}")
                                    loanresult.reports.append("비교대출 오늘입금 태그노출 결과 : *Error*")
                                    base.save_screenshot('비교대출오늘입금태그노출결과_error')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"오늘 입금 태그 확인 테스트 진행 중 에러 발생 : {e}")
        logging.info("오늘 입금 태그 확인 테스트 시작")

    # 비교대출 > 대출 상세 페이지 진입 테스트
    def test_comparison_loan_detail(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        logging.info("비교대출 > 대출 상세 페이지 진입 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            try:
                financial_sector_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                financial_sector_a.click()
            except:
                try:
                    base.scroll(0.7)
                    time.sleep(3)
                    financial_sector_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                    financial_sector_b.click()
                except:
                    try:
                        base.scroll(0.7)
                        time.sleep(3)
                        financial_sector_c = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                        financial_sector_c.click()
                    except:
                        try:
                            base.scroll(0.7)
                            time.sleep(3)
                            financial_sector_d = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                            financial_sector_d.click()
                        except:
                            try:
                                base.scroll(0.7)
                                time.sleep(3)
                                financial_sector_e = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                financial_sector_e.click()
                            except:
                                try:
                                    base.scroll(0.7)
                                    time.sleep(3)
                                    financial_sector_f = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                    financial_sector_f.click()
                                except Exception as e:
                                    logging.error(f"비교대출 대출상세페이지 진입 실패 : {e}")
            try:
                time.sleep(4)
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.comparison_loan_detail)
                self.assertEqual(Result.text, "대출 신청하기")
                logging.info("비교대출 대출상세페이지 진입 결과 : PASS")
                loanresult.reports.append("비교대출 대출상세페이지 진입 결과 : *PASS*")
            except AssertionError:
                logging.info("비교대출 대출상세페이지 진입 결과 : FAIL")
                loanresult.reports.append("비교대출 대출상세페이지 진입 결과 : *FAIL*")
                base.save_screenshot('비교대출대출상세페이지진입결과_fail')
            except Exception as e:
                logging.warning(f"비교대출 대출상세페이지 진입 결과 : {e}")
                loanresult.reports.append("비교대출 대출상세페이지 진입 결과 : *Error*")
                base.save_screenshot('비교대출대출상세페이지진입결과_error')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 > 대출 상세 페이지 진입 테스트 진행중 에러 발생 : {e}")
        logging.info("비교대출 > 대출 상세 페이지 진입 테스트 종료")

    # 비교대출 > 대출 상세 페이지 > 심의필 노출 확인 테스트
    def test_comparison_loan_detail_certification(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        logging.info("비교대출 > 대출 상세 페이지 > 심의필 노출 확인 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            try:
                financial_sector_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                financial_sector_a.click()
            except:
                try:
                    base.scroll(0.7)
                    time.sleep(3)
                    financial_sector_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                    financial_sector_b.click()
                except:
                    try:
                        base.scroll(0.7)
                        time.sleep(3)
                        financial_sector_c = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                        financial_sector_c.click()
                    except:
                        try:
                            base.scroll(0.7)
                            time.sleep(3)
                            financial_sector_d = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                            financial_sector_d.click()
                        except:
                            try:
                                base.scroll(0.7)
                                time.sleep(3)
                                financial_sector_e = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                financial_sector_e.click()
                            except:
                                try:
                                    base.scroll(0.7)
                                    time.sleep(3)
                                    financial_sector_f = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                    financial_sector_f.click()
                                except Exception as e:
                                    logging.error(f"비교대출 대출상세페이지 진입 실패 : {e}")
            base.scroll(2)
            base.scroll(2)
            base.scroll(2)
            try:
                time.sleep(4)
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.certification_a)
                self.assertIn("심의필" , Result_a.text)
                logging.info("비교대출 대출상세페이지_심의필 노출 결과 : PASS")
                loanresult.reports.append("비교대출 대출상세페이지_심의필 노출 결과 : *PASS*")
            except:
                try:
                    time.sleep(4)
                    Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.certification_b)
                    self.assertIn("심사필", Result_b.text)
                    logging.info("비교대출 대출상세페이지_심의필 노출 결과 : PASS")
                    loanresult.reports.append("비교대출 대출상세페이지_심의필 노출 결과 : *PASS*")
                except AssertionError:
                    logging.info("비교대출 대출상세페이지_심의필 노출 결과 : FAIL")
                    loanresult.reports.append("비교대출 대출상세페이지_심의필 노출 결과 : *FAIL*")
                    base.save_screenshot('비교대출대출상세페이지_심의필노출결과_fail')
                except Exception as e:
                    logging.warning(f"비교대출 대출상세페이지_심의필 노출 결과 : {e}")
                    loanresult.reports.append("비교대출 대출상세페이지_심의필 노출 결과 : *Error*")
                    base.save_screenshot('비교대출대출상세페이지_심의필노출결과_error')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 > 대출 상세 페이지 > 심의필 노출 확인 테스트 진행 중 에러 발생 : {e}")
        logging.info("비교대출 > 대출 상세 페이지 > 심의필 노출 확인 테스트 종료")

    # 비교대출 대출신청하기 테스트
    def test_loan_application(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        logging.info("비교대출 대출신청하기 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            try:
                financial_sector_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                financial_sector_a.click()
            except:
                try:
                    base.scroll(0.7)
                    time.sleep(3)
                    financial_sector_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                    financial_sector_b.click()
                except:
                    try:
                        base.scroll(0.7)
                        time.sleep(3)
                        financial_sector_c = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                        financial_sector_c.click()
                    except:
                        try:
                            base.scroll(0.7)
                            time.sleep(3)
                            financial_sector_d = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                            financial_sector_d.click()
                        except:
                            try:
                                base.scroll(0.7)
                                time.sleep(3)
                                financial_sector_e = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                financial_sector_e.click()
                            except:
                                try:
                                    base.scroll(0.7)
                                    time.sleep(3)
                                    financial_sector_f = WebDriver.driver.find_element(MobileBy.XPATH, loan.financial_sector)
                                    financial_sector_f.click()
                                except Exception as e:
                                    logging.error(f"비교대출 대출상세페이지 진입 실패 : {e}")
            time.sleep(5)
            comparisonloan.loan_application()
            try:
                time.sleep(5)
                Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_application_result)
                self.assertEqual(Result.text , "안내사항")
                logging.info("비교대출 대출신청 결과 : PASS")
                loanresult.reports.append("비교대출 대출신청 결과 : *PASS*")
            except AssertionError:
                logging.info("비교대출 대출신청 결과 : FAIL")
                loanresult.reports.append("비교대출 대출신청 결과 : *FAIL*")
                base.save_screenshot('비교대출대출신청결과_fail')
            except Exception as e:
                logging.warning(f"비교대출 대출신청 결과 : {e}")
                loanresult.reports.append("비교대출 대출신청 결과 : *Error*")
                base.save_screenshot('비교대출대출신청결과_error')
            base.android_back()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 대출신청하기 테스트 진행중 에러 발생 : {e}")
        logging.info("비교대출 대출신청하기 테스트 종료")

    # 직장인 대출 조회  (지역의료보험 선택) 테스트
    def test_office_worker_loan_no_certificate(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
        logging.info("직장인 대출 조회  (지역의료보험 선택) 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            base.scroll(2)
            base.scroll(2)
            base.scroll(2)
            comparisonloan.lookup_again()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            comparisonloan.loan_terms_and_conditions_all()
            comparisonloan.check_loan()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(3)
            comparisonloan.rrn_pass_input()
            comparisonloan.next_loan()
            comparisonloan.office_workers()
            comparisonloan.company_name_input()
            comparisonloan.search()
            base.scroll(1)
            comparisonloan.company_number()
            comparisonloan.full_time()
            comparisonloan.check_loan()
            comparisonloan.region_insurance()
            comparisonloan.annualincome_input()
            comparisonloan.check_loan()
            comparisonloan.monthly_rent()
            comparisonloan.check_loan()
            time.sleep(100)
            verification_list = [("최저금리", loan.safe_number_result_a),
                                 ("대출가능", loan.safe_number_result_b),
                                 ("오늘입금", loan.safe_number_result_c),
                                 ("계좌개설 없음", loan.safe_number_result_d),
                                 ("금리 낮은순", loan.safe_number_result_e)]
            for text, xpath in verification_list:
                try:
                    result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")
            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("직장인 대출 조회  (지역의료보험 선택) 결과 : PASS")
                loanresult.reports.append("직장인 대출 조회  (지역의료보험 선택) 결과 : *PASS*")
            else:
                logging.info("직장인 대출 조회  (지역의료보험 선택) 결과 : FAIL")
                loanresult.reports.append("직장인 대출 조회  (지역의료보험 선택) 결과 : *FAIL*")
                base.save_screenshot('직장인대출조회(지역의료보험선택)_fail')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"직장인 대출 조회  (지역의료보험 선택) 테스트 진행중 에러 발생 : {e}")
        logging.info("직장인 대출 조회 (지역의료보험 선택) 테스트 종료")

    # 직장인 외 대출 조회 테스트
    def test_unemployed_loan(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
        logging.info("직장인 외 대출 조회 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            base.scroll(2)
            base.scroll(2)
            base.scroll(2)
            comparisonloan.lookup_again()
            comparisonloan.living_expenses()
            comparisonloan.next_loan()
            comparisonloan.next_loan()
            comparisonloan.loan_terms_and_conditions_all()
            comparisonloan.check_loan()
            time.sleep(5)
            comparisonloan.next_loan()
            time.sleep(3)
            comparisonloan.rrn_pass_input()
            comparisonloan.next_loan()
            comparisonloan.unemployed()
            comparisonloan.check_loan()
            comparisonloan.monthly_rent()
            comparisonloan.check_loan()
            time.sleep(100)
            verification_list = [("최저금리", loan.safe_number_result_a),
                                 ("대출가능", loan.safe_number_result_b),
                                 ("오늘입금", loan.safe_number_result_c),
                                 ("계좌개설 없음", loan.safe_number_result_d),
                                 ("금리 낮은순", loan.safe_number_result_e)]
            for text, xpath in verification_list:
                try:
                    result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                    self.assertIn(text, result.text)
                    results.append("PASS")
                except AssertionError:
                    results.append("FAIL")
                except Exception:
                    results.append("Error")

            logging.info(results)
            if all(result == "PASS" for result in results):
                logging.info("직장인 외 대출 조회 결과 : PASS")
                loanresult.reports.append("직장인 외 대출 조회 결과 : *PASS*")
            else:
                logging.info("직장인 외 대출 조회 결과 : FAIL")
                loanresult.reports.append("직장인 외 대출 조회 결과 : *FAIL*")
                base.save_screenshot('직장인외대출조회_fail')
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"직장인 외 대출 조회 테스트 진행중 에러 발생 : {e}")
        logging.info("직장인 외 대출 조회 테스트 종료")

    # 비교대출 내 자동차대출 선택 시 오토론 이동
    def test_auto_loan_in(self):
        base = basemethod()
        info = InFo()
        etc = Etc()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 테스트 시작")
        try:
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
                                logging.error(f"비교대출 배너 진입 에러 발생 : {e}")
            base.scroll(2)
            base.scroll(2)
            base.scroll(2)
            comparisonloan.lookup_again()
            time.sleep(3)
            comparisonloan.auto_loan_in()
            time.sleep(3)
            try:
                Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_a)
                self.assertEqual(Result_A.text,"1분만에 내 한도 알아보기")
                logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : PASS")
                loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *PASS*")
            except AssertionError:
                logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : FAIL")
                loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *FAIL*")
                base.save_screenshot('자동차대출선택시오토론이동결과_fail')
            except Exception:
                try:
                    Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_b)
                    self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result_B.text)
                    logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : PASS")
                    loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *PASS*")
                except AssertionError:
                    logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : FAIL")
                    loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *FAIL*")
                    base.save_screenshot('자동차대출선택시오토론이동결과_fail')
                except Exception as e:
                    logging.warning(f"비교대출 내 자동차대출 선택 시 오토론 이동 결과 : {e}")
                    loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *Error*")
                    base.save_screenshot('자동차대출선택시오토론이동결과_error')
            base.android_back()
            base.android_back()
            base.android_back()
        except Exception as e:
            logging.error(f"비교대출 내 자동차대출 선택 시 오토론 이동 테스트 진행중 에러 발생 : {e}")
        logging.info("비교대출 내 자동차대출 선택 시 오토론 이동 테스트 종료")


class test_Testcase(unittest.TestCase):

    def test_test(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        etc = Etc()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        autoloan = Auto_Loan()










if __name__ == '__main__':
    unittest.main()