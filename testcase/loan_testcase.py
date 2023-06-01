import time
import unittest

from appium.webdriver.common.mobileby import MobileBy
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.result import Result_loan
from pages.mainlocator.loan import Loan
from testscript.loan_testscript.auto_loan import Auto_Loan
from pages.basemethod.base import basemethod
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

    # 설정 > 내정보 수정 테스트
    def test_Auto_Loan_New_NewCar(self):
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

    def test_Auto_Loan_New_UsedCar(self):
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
            loanresult.reports.append("오토론 인증번호 자동입력 : FAIL")
            base.save_screenshot('오토론인증번호자동입력_fail')
        except Exception as e:
            print("오토론 인증번호 자동입력 에러 발생 : {}".format(str(e)))
            loanresult.reports.append("오토론 인증번호 자동입력 : Error")
            base.save_screenshot('오토론인증번호자동입력_error')
        base.android_Back()
        base.android_Back()
        base.android_Back()


    def test_Auto_Loan_existing_NewCar(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.autoLoan_Terms_Of_Use()

    def test_Auto_Loan_existing_UsedCar(self):
        loan = Loan()
        base = basemethod()
        loanresult = Result_loan()
        autoloan = Auto_Loan()
        myhome = MyHome()
        myhome.auto_Loan_Banner()
        autoloan.autoLoan_Terms_Of_Use()


if __name__ == '__main__':
    unittest.main()