import time
import unittest

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


class Auto_Loan_Testcase(unittest.TestCase):

    def setUp(self):
        base = basemethod()
        base.scroll(2)
        base.scroll(2)
        base.scroll(2)

    def tearDown(self):
        base = basemethod()
        base.android_Back()
        base.android_Back()
        time.sleep(1)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 오토론 약관 테스트
    def test_Auto_Loan_New_NewCar_Terms(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.autoLoan_Terms_Of_Use()
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
        autoloan.auto_Loan_Terms_A_Unfold()
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

        autoloan.auto_Loan_Terms_Aa()
        time.sleep(6)
        try:
            Result_ba = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_aa_r)
            self.assertIn("통신사 이용약관", Result_ba.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관Aa진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관Aa진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Ab()
        time.sleep(6)
        try:
            Result_bb = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ab_r)
            self.assertIn("개인정보 수집/이용/취급 위탁동의", Result_bb.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관Ab진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관Ab진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Ac()
        time.sleep(6)
        try:
            Result_bc = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ac_r)
            self.assertIn("고유식별정보처리 동의", Result_bc.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관Ac진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관Ac진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Ad()
        time.sleep(6)
        try:
            Result_bd = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ad_r)
            self.assertIn("본인확인서비스 이용약관", Result_bd.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관Ad진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관Ad진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Ae()
        time.sleep(6)
        try:
            Result_be = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ae_r)
            self.assertIn("개인정보 제3자 제공 동의", Result_be.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관Ae진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관Ae진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_A_Unfold()
        autoloan.auto_Loan_Terms_B_Unfold()
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

        autoloan.auto_Loan_Terms_Ba()
        time.sleep(6)
        try:
            Result_ca = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ba_r)
            self.assertIn("서비스 이용 약관 [오토론]", Result_ca.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관ba진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관ba진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Bb()
        time.sleep(6)
        try:
            Result_cb = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_bb_r)
            self.assertIn("핀다 개인(신용)정보 수집이용제공 동의[오토론]", Result_cb.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관bb진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관bb진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_B_Unfold()
        autoloan.auto_Loan_Terms_C_Unfold()
        base.scroll(0.15)
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
        autoloan.auto_Loan_Terms_Ca()
        time.sleep(6)
        try:
            Result_da = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ca_r)
            self.assertIn("금융기관 개인(신용)정보 수집이용제공 동의[오토론]", Result_da.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관ca진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관ca진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Cb()
        time.sleep(6)
        try:
            Result_db = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cb_r)
            self.assertIn("개인(신용)정보 조회 동의서[오토론]", Result_db.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관cb진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관cb진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Cc()
        time.sleep(6)
        try:
            Result_dc = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cc_r)
            self.assertIn("개인(신용)정보 수집 이용 제공 동의서[오토론]", Result_dc.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관cc진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관cc진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Cd()
        time.sleep(6)
        try:
            Result_dd = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cd_r)
            self.assertIn("개인(신용)정보 수집이용제공동의서[가계여신 금융 거래][오토론]", Result_dd.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관cd진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관cd진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Ce()
        time.sleep(6)
        try:
            Result_de = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_ce_r)
            self.assertIn("계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[오토론]", Result_de.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관ce진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관ce진입_error')
        base.android_Back()
        time.sleep(3)
        autoloan.auto_Loan_Terms_Cf()
        time.sleep(6)
        try:
            Result_df = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_terms_cf_r)
            self.assertIn("개인정보 제 3자 제공 동의서[OPENAPI][오토론]", Result_df.text)
            results_a.append("PASS")
        except AssertionError:
            results_a.append("FAIL")
            base.save_screenshot('자동차대출약관cf진입_fail')
        except Exception:
            results_a.append("Error")
            base.save_screenshot('자동차대출약관cf진입_error')
        base.android_Back()
        time.sleep(3)
        print(results)
        if all(result == "PASS" for result in results):
            print("자동차 대출 약관 노출 : PASS")
            loanresult.reports.append("자동차 대출 약관 노출 : *PASS*")
        else:
            print("자동차 대출 약관 노출 : FAIL")
            loanresult.reports.append("자동차 대출 약관 노출 : *FAIL*")
            base.save_screenshot('자동차대출약관노출_fail')
        base.android_Back()

    # 오토론 인증번호 자동입력 테스트
    def test_Auto_Loan_New_NewCar_Certification_Number(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.autoLoan_Terms_Of_Use()
        autoloan.auto_Loan_Terms_All()
        autoloan.auto_Loan_Terms_Check()
        autoloan.auto_Loan_Terms_Next()
        autoloan.auto_Loan_Terms_Next()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_certification_number)
            self.assertIn("주민등록번호 뒷자리 입력", Result.text)
            print("오토론 인증번호 자동입력 : PASS")
            loanresult.reports.append("오토론 인증번호 자동입력 : PASS")
        except AssertionError:
            print("오토론 인증번호 자동입력 : FAIL")
            loanresult.reports.append("오토론 인증번호 자동입력 : FAIL")
            base.save_screenshot('오토론인증번호자동입력_fail')
        except Exception as e:
            print("오토론 인증번호 자동입력 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("오토론 인증번호 자동입력 : Error")
            base.save_screenshot('오토론인증번호자동입력_error')
        base.android_Back()
        base.android_Back()
        base.android_Back()

    # 오토론 신차 신규 대출 조회 테스트
    def test_Auto_Loan_New(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        info = InFo()
        myhome.auto_Loan_Banner()
        autoloan.autoLoan_Terms_Of_Use()
        autoloan.auto_Loan_Terms_All()
        autoloan.auto_Loan_Terms_Check()
        autoloan.auto_Loan_Terms_Next()
        time.sleep(4)
        autoloan.auto_Loan_Terms_Next()
        autoloan.auto_Loan_Rrn()
        autoloan.auto_Loan_Terms_Next()
        autoloan.auto_Loan_Annual_Income()
        autoloan.auto_Loan_Terms_Next()
        autoloan.auto_Loan_New()
        autoloan.auto_Loan_Newcar()
        autoloan.auto_Loan_Terms_Check()
        autoloan.auto_Loan_Terms_Check()
        time.sleep(60)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
            self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result.text)
            print("오토론 신차 신규 대출 조회(조회성공) : PASS")
            loanresult.reports.append("오토론 신차 신규 대출 조회(조회성공) : PASS")
        except AssertionError:
            print("오토론 신차 신규 대출 조회(조회성공) : FAIL")
            loanresult.reports.append("오토론 신차 신규 대출 조회(조회성공) : FAIL")
            base.save_screenshot('오토론신차신규대출조회_fail')
        except :
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                print("오토론 신차 신규 대출 조회(부결) : PASS")
                loanresult.reports.append("오토론 신차 신규 대출 조회(부결) : PASS")
            except AssertionError:
                print("오토론 신차 신규 대출 조회(부결) : FAIL")
                loanresult.reports.append("오토론 신차 신규 대출 조회(부결) : FAIL")
                base.save_screenshot('오토론신차신규대출조회_fail')
            except Exception as e:
                print("오토론 신차 신규 대출 조회 에러 발생 : {}".format(str(e)))
                loanresult.reports.append("오토론 신차 신규 대출 조회 : Error")
                base.save_screenshot('오토론신차신규대출조회_error')
        base.android_Back()

    # 오토론 대출 상세 진입
    def test_Auto_Loan_Detail(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.auto_Loan_Detail()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_detail_result)
            self.assertIn("조회결과", Result.text)
            print("오토론 대출 상세 진입 : PASS")
            loanresult.reports.append("오토론 대출 상세 진입 : PASS")
        except AssertionError:
            print("오토론 대출 상세 진입 : FAIL")
            loanresult.reports.append("오토론 대출 상세 진입 : FAIL")
            base.save_screenshot('오토론대출상세진입_fail')
        except Exception as e:
            print("오토론 대출 상세 진입 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("오토론 대출 상세 진입 : Error")
            base.save_screenshot('오토론대출상세진입_error')
        base.android_Back()

    # 오토론 대출 신청하기 및 홈페이지 진입
    def test_Auto_Loan_Application(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.auto_Loan_Detail()
        autoloan.auto_Loan_Application()
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
        print(results)
        if all(result == "PASS" for result in results):
            print("오토론 대출 신청 : PASS")
            loanresult.reports.append("오토론 대출 신청 : *PASS*")
        else:
            print("오토론 대출 신청 : FAIL")
            loanresult.reports.append("오토론 대출 신청 : *FAIL*")
            base.save_screenshot('오토론대출신청_fail')
        time.sleep(2)
        autoloan.auto_Loan_Terms_Next()
        time.sleep(5)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_url_r)
            self.assertIn("하나은행 X 핀다", Result_a.text)
            print("오토론 대출 신청 하나은행 홈페이지 진입 : PASS")
            loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : PASS")
        except AssertionError:
            print("오토론 대출 신청 하나은행 홈페이지 진입 : FAIL")
            loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : FAIL")
            base.save_screenshot('오토론대출신청_하나은행홈페이지진입_fail')
        except Exception as e:
            print("오토론 대출 신청 하나은행 홈페이지 진입 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("오토론 대출 신청 하나은행 홈페이지 진입 : Error")
            base.save_screenshot('오토론대출신청_하나은행홈페이지진입_error')
        base.android_Back()
        base.android_Back()
        autoloan.auto_Loan_Application_Exit()
        base.android_Back()
        base.android_Back()

    # 오토론 중고차 신규 대출 조회 테스트
    def test_Auto_Loan_New_UsedCar(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        join = JoIn()
        more = More()
        seting = Seting()
        join.join_Mms_delete()
        time.sleep(3)
        more.etcIn()
        seting.setingIn()
        base.scroll(2)
        base.user_Id_Get()
        base.user_Token_Get()
        base.user_TxSeqNo_Get()
        join.join_Mms()
        base.user_idToken_Get()
        autoloan.auto_Loan_New_UsedCar()
        base.android_Back()
        base.android_Back()
        base.scroll(2)
        myhome.auto_Loan_Banner()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
            self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
            print("오토론 중고차 신규 대출 조회 : PASS")
            loanresult.reports.append("오토론 중고차 신규 대출 조회(조회성공) : PASS")
        except AssertionError:
            print("오토론 중고차 신규 대출 조회(조회성공) : FAIL")
            loanresult.reports.append("오토론 중고차 신규 대출 조회(조회성공) : FAIL")
            base.save_screenshot('오토론중고차신규대출조회_fail')
        except Exception:
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                print("오토론 중고차 신규 대출 조회 : PASS")
                loanresult.reports.append("오토론 중고차 신규 대출 조회(부결) : PASS")
            except AssertionError:
                print("오토론 중고차 신규 대출 조회(부결) : FAIL")
                loanresult.reports.append("오토론 중고차 신규 대출 조회(부결) : FAIL")
                base.save_screenshot('오토론중고차신규대출조회_fail')
            except Exception as e:
                print("오토론 중고차 신규 대출 조회 에러 발생 : {}".format(str(e)))
                loanresult.reports.append("오토론 중고차 신규 대출 조회 : Error")
                base.save_screenshot('오토론중고차신규대출조회_error')
        base.android_Back()

    # 오토론 신차 대환 대출 조회 테스트
    def test_Auto_Loan_existing_NewCar(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        autoloan.auto_Loan_existing_NewCar()
        myhome.auto_Loan_Banner()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
            self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
            print("오토론 신차 대환 대출 조회 : PASS")
            loanresult.reports.append("오토론 신차 대환 대출 조회(조회성공) : PASS")
        except AssertionError:
            print("오토론 신차 대환 대출 조회(조회성공) : FAIL")
            loanresult.reports.append("오토론 신차 대환 대출 조회(조회성공) : FAIL")
            base.save_screenshot('오토론신차대환대출조회_fail')
        except :
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                print("오토론 신차 대환 대출 조회 : PASS")
                loanresult.reports.append("오토론 신차 대환 대출 조회(부결) : PASS")
            except AssertionError:
                print("오토론 신차 대환 대출 조회(부결) : FAIL")
                loanresult.reports.append("오토론 신차 대환 대출 조회(부결) : FAIL")
                base.save_screenshot('오토론신차대환대출조회_fail')
            except Exception as e:
                print("오토론 신차 대환 대출 조회 에러 발생 : {}".format(str(e)))
                loanresult.reports.append("오토론 신차 대환 대출 조회 : Error")
                base.save_screenshot('오토론신차대환대출조회_error')
        base.android_Back()

    # 오토론 중고차 대환 대출 조회 테스트
    def test_Auto_Loan_existing_UsedCar(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        info = InFo()
        myhome = MyHome()
        autoloan.auto_Loan_existing_UsedCar()
        myhome.auto_Loan_Banner()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result)
            self.assertIn(""+info.name+"님의\n가장 좋은 대출 조건이에요.", Result.text)
            print("오토론 중고차 대환 대출 조회 : PASS")
            loanresult.reports.append("오토론 중고차 대환 대출 조회(조회성공) : PASS")
        except AssertionError:
            print("오토론 중고차 대환 대출 조회(조회성공) : FAIL")
            loanresult.reports.append("오토론 중고차 대환 대출 조회(조회성공) : FAIL")
            base.save_screenshot('오토론중고차대환대출조회_fail')
        except :
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.auto_loan_result_a)
                self.assertIn("아쉽게도\n신청이 어려워요", Result_a.text)
                print("오토론 중고차 대환 대출 조회 : PASS")
                loanresult.reports.append("오토론 중고차 대환 대출 조회(부결) : PASS")
            except AssertionError:
                print("오토론 중고차 대환 대출 조회(부결) : FAIL")
                loanresult.reports.append("오토론 중고차 대환 대출 조회(부결) : FAIL")
                base.save_screenshot('오토론중고차대환대출조회_fail')
            except Exception as e:
                print("오토론 중고차 대환 대출 조회 에러 발생 : {}".format(str(e)))
                loanresult.reports.append("오토론 중고차 대환 대출 조회 : Error")
                base.save_screenshot('오토론중고차대환대출조회_error')
        base.android_Back()

class Loan_Comparison_Testcase(unittest.TestCase):

    def setUp(self):
        base = basemethod()
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    def tearDown(self):
        base = basemethod()
        base.android_Back()
        base.android_Back()
        base.android_Back()



    # 비교대출 약관 페이지 진입 테스트
    def test_loan_Terms_And_Conditions(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
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
        comparisonloan.loan_In()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        results = []
        results_a = []
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
        print(results)
        if all(result == "PASS" for result in results):
            print("비교대출 약관 노출 : PASS")
            loanresult.reports.append("비교대출 약관 노출 : *PASS*")
        else:
            print("비교대출 약관 노출 : FAIL")
            loanresult.reports.append("비교대출 약관 노출 : *FAIL*")
            base.save_screenshot('비교대출약관노출_fail')
        comparisonloan.loan_Terms_And_Conditions_A()
        try:
            comparisonloan.loan_Terms_And_Conditions_Aa()
            Result_Aa = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Aa_result)
            self.assertEqual(Result_Aa.text, "통신사 이용약관")
            print("비교대출 약관 Aa 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Aa 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Aa_fail')
        except Exception as e:
            print("비교대출 약관 Aa 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Aa_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ab()
            Result_Ab = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ab_result)
            self.assertEqual(Result_Ab.text, "개인정보 수집/이용/취급 위탁동의")
            print("비교대출 약관 Ab 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ab 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ab_fail')
        except Exception as e:
            print("비교대출 약관 Ab 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ab_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ac()
            Result_Ac = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ac_result)
            self.assertEqual(Result_Ac.text, "고유식별정보처리 동의")
            print("비교대출 약관 Ac 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ac 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ac_fail')
        except Exception as e:
            print("비교대출 약관 Ac 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ac_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ad()
            Result_Ad = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ad_result)
            self.assertEqual(Result_Ad.text, "KCB휴대폰 본인확인 이용약관")
            print("비교대출 약관 Ad 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ad 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ad_fail')
        except Exception as e:
            print("비교대출 약관 Ad 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ad_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ae()
            Result_Ae = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ae_result)
            self.assertEqual(Result_Ae.text, "개인정보 제3자 제공 동의")
            print("비교대출 약관 Ae 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ae 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ae_fail')
        except Exception as e:
            print("비교대출 약관 Ae 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ae_error')
        base.android_Back()
        comparisonloan.loan_Terms_And_Conditions_A()
        comparisonloan.loan_Terms_And_Conditions_B()
        base.scroll(0.065)
        try:
            comparisonloan.loan_Terms_And_Conditions_Ba()
            Result_Ba = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ba_result)
            self.assertEqual(Result_Ba.text, "개인(신용)정보 수집·이용·제공 동의서(FINDA)")
            print("비교대출 약관 Ba 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ba 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ba_fail')
        except Exception as e:
            print("비교대출 약관 Ba 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ba_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Bb()
            Result_Bb = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bb_result)
            self.assertEqual(Result_Bb.text, "서비스 이용 약관 [대출비교]")
            print("비교대출 약관 Bb 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Bb 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Bb_fail')
        except Exception as e:
            print("비교대출 약관 Bb 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Bb_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Bc()
            Result_Bc = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bc_result)
            self.assertEqual(Result_Bc.text, "[간편인증] 서비스 이용 약관 동의")
            print("비교대출 약관 Bc 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Bc 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Bc_fail')
        except Exception as e:
            print("비교대출 약관 Bc 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Bc_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Bd()
            Result_Bd = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bd_result)
            self.assertEqual(Result_Bd.text, "[간편인증] 개인정보 이용 동의")
            print("비교대출 약관 Bd 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Bd 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Bd_fail')
        except Exception as e:
            print("비교대출 약관 Bd 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Bd_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Be()
            Result_Be = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Be_result)
            self.assertEqual(Result_Be.text, "[간편인증] 제3자 정보제공 동의")
            print("비교대출 약관 Be 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Be 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Be_fail')
        except Exception as e:
            print("비교대출 약관 Be 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Be_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Bf()
            Result_Bf = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Bf_result)
            self.assertEqual(Result_Bf.text, "[간편인증] 고유식별번호처리 동의")
            print("비교대출 약관 Bf 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Bf 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Bf_fail')
        except Exception as e:
            print("비교대출 약관 Bf 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Bf_error')
        base.android_Back()
        comparisonloan.loan_Terms_And_Conditions_B()
        comparisonloan.loan_Terms_And_Conditions_C()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ca()
            Result_Ca = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ca_result)
            self.assertEqual(Result_Ca.text, "개인(신용)정보 수집·이용·제공 동의서(금융기관 용)")
            print("비교대출 약관 Ca 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ca 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ca_fail')
        except Exception as e:
            print("비교대출 약관 Ca 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ca_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cb()
            Result_Cb = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cb_result)
            self.assertEqual(Result_Cb.text, "개인(신용)정보 수집·이용·제공·조회 동의서(금융기관 용)")
            print("비교대출 약관 Cb 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cb 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cb_fail')
        except Exception as e:
            print("비교대출 약관 Cb 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cb_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cc()
            Result_Cc = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cc_result)
            self.assertEqual(Result_Cc.text, "고유식별정보 수집·이용·제공·조회 동의서")
            print("비교대출 약관 Cc 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cc 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cc_fail')
        except Exception as e:
            print("비교대출 약관 Cc 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cc_error')
        base.android_Back()
        base.scroll(0.25)
        try:
            comparisonloan.loan_Terms_And_Conditions_Cd()
            Result_Cd = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cd_result)
            self.assertEqual(Result_Cd.text, "개인(신용)정보 조회 동의서(서민금융진흥원)")
            print("비교대출 약관 Cd 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cd 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cd_fail')
        except Exception as e:
            print("비교대출 약관 Cd 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cd_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ce()
            Result_Ce = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ce_result)
            self.assertEqual(Result_Ce.text, "개인정보 수집·이용·제공 동의서(서민금융진흥원)")
            print("비교대출 약관 Ce 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ce 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ce_fail')
        except Exception as e:
            print("비교대출 약관 Ce 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ce_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cf()
            Result_Cf = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cf_result)
            self.assertEqual(Result_Cf.text, "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[비교대출]")
            print("비교대출 약관 Cf 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cf 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cf_fail')
        except Exception as e:
            print("비교대출 약관 Cf 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cf_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cg()
            Result_Cg = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cg_result)
            self.assertEqual(Result_Cg.text, "개인(신용)정보 제3자 제공 동의서 [토스뱅크][비교대출]")
            print("비교대출 약관 Cg 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cg 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cg_fail')
        except Exception as e:
            print("비교대출 약관 Cg 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cg_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ch()
            Result_Ch = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ch_result)
            self.assertEqual(Result_Ch.text, "개인(신용)정보 제3자 제공 동의서 [중소기업중앙회][비교대출]")
            print("비교대출 약관 Ch 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ch 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ch_fail')
        except Exception as e:
            print("비교대출 약관 Ch 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ch_error')
        base.android_Back()
        base.scroll(0.25)
        try:
            comparisonloan.loan_Terms_And_Conditions_Ci()
            Result_Ci = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ci_result)
            self.assertEqual(Result_Ci.text, "개인(신용)정보 제3자 제공 동의서 [OPENAPI][비교대출]")
            print("비교대출 약관 Ci 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ci 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ci_fail')
        except Exception as e:
            print("비교대출 약관 Ci 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ci_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cj()
            Result_Cj = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cj_result)
            self.assertEqual(Result_Cj.text, "개인(신용)정보 수집 이용 제공 조회 동의서 [서민금융진흥원][비교대출]")
            print("비교대출 약관 Cj 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cj 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cj_fail')
        except Exception as e:
            print("비교대출 약관 Cj 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cj_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Ck()
            Result_Ck = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Ck_result)
            self.assertEqual(Result_Ck.text, "개인(신용)정보 제 3자 제공 조회 동의서 [대안정보이용][비교대출]")
            print("비교대출 약관 Ck 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Ck 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Ck_fail')
        except Exception as e:
            print("비교대출 약관 Ck 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Ck_error')
        base.android_Back()
        try:
            comparisonloan.loan_Terms_And_Conditions_Cl()
            Result_Cl = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cl_result)
            self.assertEqual(Result_Cl.text, "고유식별정보 수집∙이용 동의서[KCB대안신용평가모델]")
            print("비교대출 약관 Cl 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cl 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cl_fail')
        except Exception as e:
            print("비교대출 약관 Cl 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cl_error')
        base.android_Back()
        base.scroll(0.25)
        try:
            comparisonloan.loan_Terms_And_Conditions_Cm()
            Result_Cm = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Cm_result)
            self.assertEqual(Result_Cm.text, "개인(신용)정보 이용 및 제3자 제공 동의서[KCB대안신용평가모델]")
            print("비교대출 약관 Cm 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Cm 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Cm_fail')
        except Exception as e:
            print("비교대출 약관 Cm 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Cm_error')
        base.android_Back()
        comparisonloan.loan_Terms_And_Conditions_D()
        try:
            comparisonloan.loan_Terms_And_Conditions_Da()
            Result_Da = WebDriver.driver.find_element(MobileBy.XPATH, loan.loan_terms_and_conditions_Da_result)
            self.assertEqual(Result_Da.text, "개인정보 제3자 제공 동의(대출안심플랜)")
            print("비교대출 약관 Da 진입 : PASS")
            results_a.append("PASS")
        except AssertionError:
            print("비교대출 약관 Da 진입 : FAIL")
            results_a.append("FAIL")
            base.save_screenshot('비교대출약관Da_fail')
        except Exception as e:
            print("비교대출 약관 Da 진입 에러 발생 : {}".format(str(e)))
            results_a.append("Error")
            base.save_screenshot('비교대출약관Da_error')
        base.android_Back()
        print(results_a)
        if all(result == "PASS" for result in results_a):
            print("비교대출 약관 진입 결과 : PASS")
            loanresult.reports.append("비교대출 약관 진입 결과 : *PASS*")
        else:
            print("비교대출 약관 진입 결과 : FAIL")
            loanresult.reports.append("비교대출 약관 진입 결과 : *FAIL*")

        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()

    # 비교대출 인증번호 자동 입력 및 재전송 테스트
    def test_loan_Comparison_Verification_Code(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
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
        comparisonloan.loan_In()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        comparisonloan.loan_Terms_And_Conditions_All()
        comparisonloan.check_Loan()
        time.sleep(5)
        comparisonloan.next_Loan()
        time.sleep(5)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.comparison_loan_verification_result)
            self.assertEqual(Result_a.text, "주민등록번호 뒷자리 입력")
            print("비교대출 인증번호 자동입력 결과 : PASS")
            loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *PASS*")
        except AssertionError:
            print("비교대출 인증번호 자동입력 결과 : FAIL")
            loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *FAIL*")
            base.save_screenshot('비교대출인증번호자동입력_fail')
        except Exception as e:
            print("비교대출 인증번호 자동입력 결과 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("비교대출 인증번호 자동입력 결과 : *Error*")
            base.save_screenshot('비교대출인증번호자동입력_error')
        base.android_Back()
        base.android_Back()
        comparisonloan.comparison_Loan_Verification_Resend()
        time.sleep(5)
        comparisonloan.next_Loan()
        time.sleep(5)
        try:
            Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.comparison_loan_verification_result)
            self.assertEqual(Result_b.text, "주민등록번호 뒷자리 입력")
            print("비교대출 인증번호 재요청 결과 : PASS")
            loanresult.reports.append("비교대출 인증번호 재요청 결과 : *PASS*")
        except AssertionError:
            print("비교대출 인증번호 재요청 결과 : FAIL")
            loanresult.reports.append("비교대출 인증번호 재요청 결과 : *FAIL*")
            base.save_screenshot('비교대출인증번호재요청_fail')
        except Exception as e:
            print("비교대출 인증번호 재요청 결과 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("비교대출 인증번호 재요청 결과 : *Error*")
            base.save_screenshot('비교대출인증번호재요청_error')
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()

    # 비교대출 주민번호 적합서 검사 테스트
    def test_rrn_Validation_Check(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        results = []
        comparisonloan = ComparisonLoan()
        time.sleep(3)
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
        comparisonloan.loan_In()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        comparisonloan.loan_Terms_And_Conditions_All()
        comparisonloan.check_Loan()
        time.sleep(5)
        comparisonloan.next_Loan()
        comparisonloan.rrn_Fail_Input()
        comparisonloan.next_Loan()
        time.sleep(3)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.rrn_validation_fail_result)
            self.assertEqual(Result_a.text, "주민등록번호를 다시 한 번 확인해주세요.")
            print("비교대출 주민등록번호 적합성 실패 결과 : PASS")
            results.append("PASS")
        except AssertionError:
            print("비교대출 주민등록번호 적합성 실패 결과 : FAIL")
            results.append("FAIL")
            base.save_screenshot('비교대출주민번호적합성실패_fail')
        except Exception as e:
            print("비교대출 주민등록번호 적합성 실패 결과 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('비교대출주민번호적합성실패_error')
        comparisonloan.check_Loan()
        base.android_Back()
        comparisonloan.comparison_Loan_Verification_Resend()
        time.sleep(5)
        comparisonloan.next_Loan()
        time.sleep(3)
        comparisonloan.rrn_Pass_Input()
        comparisonloan.next_Loan()
        time.sleep(3)
        try:
            Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.rrn_validation_pass_result)
            self.assertEqual(Result_b.text, "소득 정보 입력")
            print("비교대출 주민등록번호 적합성 성공 결과 : PASS")
            results.append("PASS")
        except AssertionError:
            print("비교대출 주민등록번호 적합성 성공 결과 : FAIL")
            results.append("FAIL")
            base.save_screenshot('비교대출주민번호적합성성공_fail')
        except Exception as e:
            print("비교대출 주민등록번호 적합성 성공 결과 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('비교대출주민번호적합성성공_error')
        print(results)
        if all(result == "PASS" for result in results):
            print("비교대출 주민등록번호 적합성 검사 결과 : PASS")
            loanresult.reports.append("비교대출 주민등록번호 적합성 검사 결과 : *PASS*")
        else:
            print("비교대출 주민등록번호 적합성 검사 결과 : FAIL")
            loanresult.reports.append("비교대출 주민등록번호 적합성 검사 결과 : *FAIL*")
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()
        base.android_Back()

    # 비교대출 후담대 조회 및 열람 테스트 & 직장인대출 조회 > 인증서 없이 조회 테스트 & 안심번호 테스트
    def test_loan_Comparison_APT_Secured_Loan(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
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
        comparisonloan.loan_In()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        comparisonloan.loan_Terms_And_Conditions_All()
        comparisonloan.check_Loan()
        time.sleep(5)
        comparisonloan.next_Loan()
        comparisonloan.rrn_Pass_Input()
        comparisonloan.next_Loan()
        comparisonloan.office_Workers()
        comparisonloan.company_Name_Input()
        comparisonloan.search()
        base.scroll(1)
        comparisonloan.company_Number()
        comparisonloan.full_Time()
        comparisonloan.check_Loan()
        comparisonloan.workplace_Insurance()
        comparisonloan.annual_Income_Input()
        comparisonloan.check_Loan()
        comparisonloan.my_House_APT()
        comparisonloan.check_Loan()
        comparisonloan.address_Search()
        comparisonloan.check_Loan()
        comparisonloan.no_Certificate()
        time.sleep(3)
        verification_list = [("최저금리", loan.safe_number_result_a),
                             ("최대한도", loan.safe_number_result_b),
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
            print("안심번호 결과 : PASS")
            loanresult.reports.append("안심번호 결과 : *PASS*")
            print("직장인 대출 조회 (직장의료보험 선택) -인증서 사용안함 결과 : PASS")
            loanresult.reports.append("직장인 대출 조회 (직장의료보험 선택) -인증서 사용안함 결과 : *PASS*")
        else:
            print("안심번호 결과 : FAIL")
            loanresult.reports.append("안심번호 결과 : *FAIL*")
            print("직장인 대출 조회 (직장의료보험 선택) -인증서 사용안함 결과 : FAIL")
            loanresult.reports.append("직장인 대출 조회 (직장의료보험 선택) -인증서 사용안함 결과 : *FAIL*")
            base.save_screenshot('안심번호결과&직장인대출조회_인증서사용안함_fail')
        comparisonloan.type_Of_Loan()
        comparisonloan.secured_Loan()
        time.sleep(3)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, loan.secured_loan_result_a)
            self.assertEqual(Result_a.text, "아파트담보대출")
            print("비교대출 후담대 조회 및 열람 결과 : PASS")
            loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *PASS*")
        except AssertionError:
            print("비교대출 후담대 조회 및 열람 결과 : FAIL")
            loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *FAIL*")
            base.save_screenshot('비교대출후담대결과_fail')
        except Exception:
            try:
                Result_b = WebDriver.driver.find_element(MobileBy.XPATH, loan.secured_loan_result_b)
                self.assertEqual(Result_b.text, "주택담보대출")
                print("비교대출 후담대 조회 및 열람 결과 : PASS")
                loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *PASS*")
            except AssertionError:
                print("비교대출 후담대 조회 및 열람 결과 : FAIL")
                loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *FAIL*")
                base.save_screenshot('비교대출후담대결과_fail')
            except Exception as e:
                print("비교대출 후담대 조회 및 열람 결과 에러 발생 : {}".format(str(e)))
                loanresult.reports.append("비교대출 후담대 조회 및 열람 결과 : *Error*")
                base.save_screenshot('비교대출후담대결과_error')
        base.android_Back()
        base.android_Back()

    # 직장인 대출 조회  (지역의료보험 선택) 테스트
    def test_office_Worker_Loan_No_Certificate(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
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
        base.scroll(2)
        base.scroll(2)
        base.scroll(2)
        comparisonloan.lookup_Again()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        comparisonloan.loan_Terms_And_Conditions_All()
        comparisonloan.check_Loan()
        time.sleep(5)
        comparisonloan.next_Loan()
        comparisonloan.rrn_Pass_Input()
        comparisonloan.next_Loan()
        comparisonloan.office_Workers()
        comparisonloan.company_Name_Input()
        comparisonloan.search()
        base.scroll(1)
        comparisonloan.company_Number()
        comparisonloan.full_Time()
        comparisonloan.check_Loan()
        comparisonloan.region_Insurance()
        comparisonloan.annual_Income_Input()
        comparisonloan.check_Loan()
        comparisonloan.monthly_Rent()
        comparisonloan.check_Loan()
        time.sleep(100)
        verification_list = [("최저금리", loan.safe_number_result_a),
                             ("최대한도", loan.safe_number_result_b),
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
            print("직장인 대출 조회  (지역의료보험 선택) 결과 : PASS")
            loanresult.reports.append("직장인 대출 조회  (지역의료보험 선택) 결과 : *PASS*")
        else:
            print("직장인 대출 조회  (지역의료보험 선택) 결과 : FAIL")
            loanresult.reports.append("직장인 대출 조회  (지역의료보험 선택) 결과 : *FAIL*")
            base.save_screenshot('직장인대출조회(지역의료보험선택)_fail')
        base.android_Back()
        base.android_Back()

    # 직장인 외 대출 조회
    def test_Unemployed_Loan(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
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
        base.scroll(2)
        base.scroll(2)
        base.scroll(2)
        comparisonloan.lookup_Again()
        comparisonloan.living_Expenses()
        comparisonloan.next_Loan()
        comparisonloan.next_Loan()
        comparisonloan.loan_Terms_And_Conditions_All()
        comparisonloan.check_Loan()
        time.sleep(5)
        comparisonloan.next_Loan()
        comparisonloan.rrn_Pass_Input()
        comparisonloan.next_Loan()
        comparisonloan.unemployed()
        comparisonloan.check_Loan()
        comparisonloan.monthly_Rent()
        comparisonloan.check_Loan()
        time.sleep(100)
        verification_list = [("최저금리", loan.safe_number_result_a),
                             ("최대한도", loan.safe_number_result_b),
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
            print("직장인 외 대출 조회 결과 : PASS")
            loanresult.reports.append("직장인 외 대출 조회 결과 : *PASS*")
        else:
            print("직장인 외 대출 조회 결과 : FAIL")
            loanresult.reports.append("직장인 외 대출 조회 결과 : *FAIL*")
            base.save_screenshot('직장인외대출조회_fail')
        base.android_Back()
        base.android_Back()

    # 비교대출 내 자동차대출 선택 시 오토론 이동
    def test_Auto_Loan_In(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        info = InFo()
        etc = Etc()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        results = []
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
        base.scroll(2)
        base.scroll(2)
        base.scroll(2)
        comparisonloan.lookup_Again()
        time.sleep(3)
        comparisonloan.auto_Loan_In()
        time.sleep(3)
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_a)
            self.assertEqual(Result_A.text,"1분만에 내 한도 알아보기")
            print("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : PASS")
            loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *PASS*")
        except AssertionError:
            print("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : FAIL")
            loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *FAIL*")
            base.save_screenshot('자동차대출선택시오토론이동결과_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_b)
                self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result_B.text)
                print("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : PASS")
                loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *PASS*")
            except AssertionError:
                print("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : FAIL")
                loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *FAIL*")
                base.save_screenshot('자동차대출선택시오토론이동결과_fail')
            except Exception as e:
                print("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : {}".format(str(e)))
                loanresult.reports.append("비교대출 내 자동차대출 선택 시 오토론 이동 결과 : *Error*")
                base.save_screenshot('자동차대출선택시오토론이동결과_error')
        base.android_Back()
        base.android_Back()
        base.android_Back()



class test_Testcase(unittest.TestCase):

    def test_test(self):
        loan = Loan()
        base = basemethod()
        join = JoIn()
        more = More()
        seting = Seting()
        loanresult = Result_loan()
        myhome = MyHome()
        comparisonloan = ComparisonLoan()
        try:
            a = WebDriver.driver.find_element(MobileBy.XPATH,loan.a)
            self.assertIn("심의필",a.text)
            print("성공")
        except Exception as e:
            print("실패 : {}".format(str(e)))










if __name__ == '__main__':
    unittest.main()