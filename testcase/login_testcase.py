import time
import unittest

from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.basemethod.result import Result_Join
from pages.mainlocator.main import Main
from testscript.login_testscript.logincase import JoIn
from testscript.more_testscript.see_more import More
from testscript.more_testscript.seting import Seting

class JoInTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("더보기 TestCase_A 시작")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("더보기 TestCase_A완료")
    #
    #
    def setUp(self):
        join = JoIn()
        join.appStart()

    def tearDown(self):
        join = JoIn()
        join.appQuit()



    #MO인증 테스트
    def test_Message_Certification(self):
        main = Main()
        join = JoIn()
        # driver = WebDriver.setUp()
        result_join = Result_Join()
        base = basemethod()
        # join.appStart()
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.mo_Result)
            self.assertEqual(Result.text, '이름 입력')
            print("MO인증 결과 : PASS")
            result_join.reports.append("MO인증 결과 : *PASS*")
        except AssertionError:
            print("MO인증 결과 : FAIL")
            result_join.reports.append("MO인증 결과 : *FAIL*")
            base.save_screenshot('MO인증결과_fail')
        except Exception:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, main.mo_Result)
                self.assertEqual(Result.text, '이름 입력')
                print("MO인증 결과 : PASS")
                result_join.reports.append("MO인증 결과 : *PASS*")
            except AssertionError:
                print("MO인증 결과 : FAIL")
                result_join.reports.append("MO인증 결과 : *FAIL*")
                base.save_screenshot('MO인증결과_fail')
            except Exception as e:
                print("MO인증 에러 발생 : {}".format(str(e)))
                result_join.reports.append("MO인증 결과 : *Error*")
                base.save_screenshot('MO인증결과_error')
    #유심내용 자동입력 테스트
    def test_Enter_Personal_Information(self):
        main = Main()
        join = JoIn()
        # driver = WebDriver.setUp()
        result_join = Result_Join()
        base = basemethod()
        info = InFo()
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        join.enter_Personal_Information()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.phone_number_Result)
            self.assertEqual(Result.text,info.phone_number)
            print("유심내용 자동입력 결과 : PASS")
            result_join.reports.append("유심내용 자동입력 결과 : *PASS*")
        except AssertionError:
            print("유심내용 자동입력 결과 : FAIL")
            result_join.reports.append("유심내용 자동입력 결과 : *FAIL*")
            base.save_screenshot('유심내용자동입력결과_fail')
        except Exception as e:
            print("유심내용 자동입력 에러 발생 : {}".format(str(e)))
            result_join.reports.append("유심내용 자동입력 결과 : *Error*")
            base.save_screenshot('유심내용자동입력결과_error')

    #회원가입 약관 동의 진입 테스트
    def test_Membership_Terms_And_Conditions(self):
        main = Main()
        join = JoIn()
        # driver = WebDriver.setUp()
        result_join = Result_Join()
        base = basemethod()
        results = []
        results_a = []
        results_b = []
        results_c = []
        results_d = []
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        join.enter_Personal_Information()
        join.join_Next()
        verification_list = [("핀다 필수 항목 모두 동의", main.membership_terms_and_conditions_a_Result),
                             ("제휴사 필수 항목 모두 동의", main.membership_terms_and_conditions_b_Result),
                             ("본인인증 필수 항목 모두 동의", main.membership_terms_and_conditions_c_Result),
                             ("마케팅 정보 수신 동의 (선택)", main.membership_terms_and_conditions_d_Result)]

        for text, xpath in verification_list:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, Result.text)
                results_a.append("PASS")
            except AssertionError:
                results_a.append("FAIL")
            except Exception:
                results_a.append("Error")

        if all(result == "PASS" for result in results_a):
            print("회원가입 약관 노출 결과 : PASS")
            results.append("PASS")
        else:
            print("회원가입 약관 노출 결과 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출결과_fail')

        join.membership_Terms_And_Conditions_A()
        verification_list_a = [("서비스 이용약관 동의", main.membership_terms_and_conditions_aa),
                             ("개인정보 제3자 제공 동의", main.membership_terms_and_conditions_ab),
                             ("개인정보 수집 및 이용 동의", main.membership_terms_and_conditions_ac)]

        for text, xpath in verification_list_a:
            try:
                Result_a = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, Result_a.text)
                results_b.append("PASS")
            except AssertionError:
                results_b.append("FAIL")
            except Exception:
                results_b.append("Error")

        if all(result == "PASS" for result in results_b):
            print("회원가입 약관 노출_1 : PASS")
            results.append("PASS")
        else:
            print("회원가입 약관 노출_1 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_1_fail')

        join.membership_Terms_And_Conditions_Aa()

        try:
            Result_aa = WebDriver.driver.find_element(MobileBy.XPATH, main.membership_terms_and_conditions_aa_Result)
            self.assertIn("서비스 이용약관", Result_aa.text)
            print("회원가입 약관 진입_aa : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_aa : FAIL")
            base.save_screenshot('회원가입약관진입_aa_fail')
        except Exception as e:
            print("회원가입 약관 진입_aa 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_aa_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_Ab()

        try:
            Result_ab = WebDriver.driver.find_element(MobileBy.XPATH, main.membership_terms_and_conditions_ab_Result)
            self.assertIn("개인정보_제3자_제공_동의", Result_ab.text)
            print("회원가입 약관 진입_ab : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_ab : FAIL")
            base.save_screenshot('회원가입약관진입_ab_fail')
        except Exception as e:
            print("회원가입 약관 진입_ab 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ab_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_Ac()

        try:
            Result_ac = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_ac_Result)
            self.assertIn("개인정보 수집 및 이용 동의", Result_ac.text)
            print("회원가입 약관 진입_ac : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_ac : FAIL")
            base.save_screenshot('회원가입약관진입_ac_fail')
        except Exception as e:
            print("회원가입 약관 진입_ac 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ac_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_A()
        time.sleep(1)
        join.membership_Terms_And_Conditions_B()
        verification_list_b = [("KCB 신용조회 서비스 이용 약관 동의", main.membership_terms_and_conditions_ba),
                             ("개인(신용)정보 수집∙이용 동의(KCB)", main.membership_terms_and_conditions_bb),
                             ("개인(신용)정보 제3자 제공 동의(KCB)", main.membership_terms_and_conditions_bc)]

        for text, xpath in verification_list_b:
            try:
                Result_b = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, Result_b.text)
                results_c.append("PASS")
            except AssertionError:
                results_c.append("FAIL")
            except Exception:
                results_c.append("Error")

        if all(result == "PASS" for result in results_c):
            print("회원가입 약관 노출_2 : PASS")
            results.append("PASS")
        else:
            print("회원가입 약관 노출_2 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_2_fail')

        join.membership_Terms_And_Conditions_Ba()

        try:
            Result_ba = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_ba_Result)
            self.assertIn("KCB 올크레딧 이용약관", Result_ba.text)
            print("회원가입 약관 진입_ba : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_ba : FAIL")
            base.save_screenshot('회원가입약관진입_ba_fail')
        except Exception as e:
            print("회원가입 약관 진입_ba 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ba_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_Bb()

        try:
            Result_bb = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_bb_Result)
            self.assertIn("개인(신용)정보_수집∙이용_동의(KCB)", Result_bb.text)
            print("회원가입 약관 진입_bb : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_bb : FAIL")
            base.save_screenshot('회원가입약관진입_bb_fail')
        except Exception as e:
            print("회원가입 약관 진입_bb 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_bb_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_Bc()

        try:
            Result_bc = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_bc_Result)
            self.assertIn("개인(신용)정보_제3자_제공_동의(KCB)", Result_bc.text)
            print("회원가입 약관 진입_bc : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_bc : FAIL")
            base.save_screenshot('회원가입약관진입_bc_fail')
        except Exception as e:
            print("회원가입 약관 진입_bc 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_bc_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_B()
        time.sleep(2)
        join.membership_Terms_And_Conditions_C()
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
                Result_c = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, Result_c.text)
                results_d.append("PASS")
            except AssertionError:
                results_d.append("FAIL")
            except Exception:
                results_d.append("Error")

        if all(result == "PASS" for result in results_d):
            print("회원가입 약관 노출_3 : PASS")
            results.append("PASS")
        else:
            print("회원가입 약관 노출_3 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_3_fail')

        join.membership_Terms_And_Conditions_ca()

        try:
            Result_ca = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_ca_Result)
            self.assertIn("통신사 이용약관", Result_ca.text)
            print("회원가입 약관 진입_ca : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_ca : FAIL")
            base.save_screenshot('회원가입약관진입_ca_fail')
        except Exception as e:
            print("회원가입 약관 진입_ca 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ca_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_cb()

        try:
            Result_cb = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_cb_Result)
            self.assertIn("고유식별정보처리 동의", Result_cb.text)
            print("회원가입 약관 진입_cb : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_cb : FAIL")
            base.save_screenshot('회원가입약관진입_cb_fail')
        except Exception as e:
            print("회원가입 약관 진입_cb 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cb_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_cc()
        try:
            Result_cc = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_cc_Result)
            self.assertIn("개인정보 제3자 제공 동의", Result_cc.text)
            print("회원가입 약관 진입_cc : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_cc : FAIL")
            base.save_screenshot('회원가입약관진입_cc_fail')
        except Exception as e:
            print("회원가입 약관 진입_cc 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cc_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_cd()

        try:
            Result_cd = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_cd_Result)
            self.assertIn("개인정보 수집/이용/취급 위탁동의", Result_cd.text)
            print("회원가입 약관 진입_cd : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_cd : FAIL")
            base.save_screenshot('회원가입약관진입_cd_fail')
        except Exception as e:
            print("회원가입 약관 진입_cd 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_cd_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_ce()

        try:
            Result_ce = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_ce_Result)
            self.assertIn("본인확인서비스 이용약관", Result_ce.text)
            print("회원가입 약관 진입_ce : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_ce : FAIL")
            base.save_screenshot('회원가입약관진입_ce_fail')
        except Exception as e:
            print("회원가입 약관 진입_ce 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_ce_error')

        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_C_A()
        time.sleep(1)
        join.membership_Terms_And_Conditions_D()
        try:
            Result_d = WebDriver.driver.find_element(MobileBy.XPATH, main.membership_terms_and_conditions_da)
            self.assertIn("마케팅 정보 수신 동의", Result_d.text)
            print("회원가입 약관 노출_4 : PASS")
            results.append("PASS")
        except AssertionError:
            print("회원가입 약관 노출_4 : FAIL")
            results.append("FAIL")
            base.save_screenshot('회원가입약관노출_4_fail')
        except Exception as e:
            print("회원가입 약관 노출_4 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관노출_4_error')


        join.membership_Terms_And_Conditions_da()

        try:
            Result_da = WebDriver.driver.find_element(MobileBy.XPATH,
                                                      main.membership_terms_and_conditions_da_Result)
            self.assertIn("마케팅 정보 수신동의", Result_da.text)
            print("회원가입 약관 진입_da : PASS")
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            print("회원가입 약관 진입_da : FAIL")
            base.save_screenshot('회원가입약관진입_da_fail')
        except Exception as e:
            print("회원가입 약관 진입_da 에러 발생 : {}".format(str(e)))
            results.append("Error")
            base.save_screenshot('회원가입약관진입_da_error')
        time.sleep(3)
        base.android_Back()
        time.sleep(3)
        join.membership_Terms_And_Conditions_D()
        if all(result == "PASS" for result in results):
            print("회원가입 약관 목록 노출 및 진입 결과 : PASS")
            result_join.reports.append("회원가입 약관 목록 노출 및 진입 결과 : *PASS*")
        else:
            print("회원가입 약관 목록 노출 및 진입 결과 : FAIL")
            result_join.reports.append("회원가입 약관 목록 노출 및 진입 결과 : *FAIL*")

    #인증번호 수신 및 자동입력, 재요청 테스트
    def test_Certification_Number(self):
        main = Main()
        join = JoIn()
        # driver = WebDriver.setUp()
        result_join = Result_Join()
        base = basemethod()
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        join.enter_Personal_Information()
        join.join_Next()
        time.sleep(2)
        join.membership_Terms_And_Conditions_All()
        time.sleep(5)
        join.join_Next()
        time.sleep(3)
        # join.join_Next()
        # time.sleep(3)
        # join.join_Mms()
        # base.android_Back()
        # base.android_Back()
        # base.android_Back()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.pincode_in_Result)
            self.assertEqual(Result.text, "사용할 비밀번호를 입력해주세요")
            print("회원가입 인증번호 자동입력 결과 : PASS")
            result_join.reports.append("회원가입 인증번호 자동입력 결과 : *PASS*")
        except AssertionError:
            print("회원가입 인증번호 자동입력 결과 : FAIL")
            result_join.reports.append("회원가입 인증번호 자동입력 결과 : *FAIL*")
            base.save_screenshot('회원가입인증번호자동입력결과_fail')
        except Exception as e:
            print("회원가입 인증번호 자동입력 에러 발생 : {}".format(str(e)))
            result_join.reports.append("회원가입 인증번호 자동입력 결과 : *Error*")
            base.save_screenshot('회원가입인증번호자동입력결과_error')

        base.android_Back()
        time.sleep(3)
        join.re_Request_Verification_Code()
        join.join_Next()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.pincode_in_Result)
            self.assertEqual(Result.text, "사용할 비밀번호를 입력해주세요")
            print("회원가입 인증번호 재요청 : PASS")
            result_join.reports.append("회원가입 인증번호 재요청 : *PASS*")
        except AssertionError:
            print("회원가입 인증번호 재요청 : FAIL")
            result_join.reports.append("회원가입 인증번호 재요청 : *FAIL*")
            base.save_screenshot('회원가입인증번호재요청_fail')
        except Exception as e:
            print("회원가입 인증번호 재요청 에러 발생 : {}".format(str(e)))
            result_join.reports.append("회원가입 인증번호 재요청 : *Error*")
            base.save_screenshot('회원가입인증번호재요청_error')

    #핀코드 등록 및 회원가입 테스트
    def test_Join(self):
        main = Main()
        join = JoIn()
        # driver = WebDriver.setUp()
        base = basemethod()
        info = InFo()
        result_join = Result_Join()
        result_join = Result_Join()
        base = basemethod()
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        join.enter_Personal_Information()
        join.join_Next()
        time.sleep(2)
        join.membership_Terms_And_Conditions_All()
        time.sleep(5)
        join.join_Next()
        time.sleep(3)
        join.use_Fingerprint()
        join.pinCode()
        join.pinCode()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.login_result)
            self.assertEqual(Result.text, ''+info.name+'님 안녕하세요')
            print("회원가입 결과 : PASS")
            result_join.reports.append("회원가입 결과 : *PASS*")
        except AssertionError:
            print("회원가입 결과 : FAIL")
            result_join.reports.append("회원가입 결과 : *FAIL*")
            base.save_screenshot('회원가입결과_fail')
        except Exception as e:
            print("회원가입 에러 발생 : {}".format(str(e)))
            result_join.reports.append("회원가입 결과 : *Error*")
            base.save_screenshot('회원가입결과_error')

class LoginTestCase(unittest.TestCase):

    # 핀코드 로그인 테스트
    def test_Check_In(self):
        main = Main()
        join = JoIn()
        result_join = Result_Join()
        # driver = WebDriver.setUp()
        base = basemethod()
        info = InFo()
        join.appStart()
        # join.appQuit()
        join.pinCode()
        time.sleep(3)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.login_result)
            self.assertEqual(Result.text, ''+info.name+'님 안녕하세요')
            print("로그인 : PASS")
            result_join.reports.append("로그인 결과 : *PASS*")
        except AssertionError:
            print("로그인 : FAIL")
            result_join.reports.append("로그인 결과 : *FAIL*")
            base.save_screenshot('로그인결과_fail')
        except Exception as e:
            print("로그인 에러 발생 : {}".format(str(e)))
            result_join.reports.append("로그인 : Error")
            base.save_screenshot('로그인결과_error')

    #로그아웃
    def test_LogOut(self):
        main = Main()
        join = JoIn()
        seting = Seting()
        # driver = WebDriver.setUp()
        base = basemethod()
        info = InFo()
        result_join = Result_Join()
        seting.setingIn()
        base.scroll(2)
        join.logOut()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.logout_Result)
            self.assertEqual(Result.text, '안심하세요. 개인정보 보호 중')
            print("로그아웃 결과 : PASS")
            result_join.reports.append("로그아웃 결과 : *PASS*")
        except AssertionError:
            print("로그아웃 결과 : FAIL")
            result_join.reports.append("로그아웃 결과 : *FAIL*")
            base.save_screenshot('로그아웃결과_fail')
        except Exception as e:
            print("로그아웃 에러 발생 : {}".format(str(e)))
            result_join.reports.append("로그아웃 결과 : *Error*")
            base.save_screenshot('로그아웃결과_error')

    #회원탈퇴
    def test_Withdraw(self):
        main = Main()
        join = JoIn()
        seting = Seting()
        # driver = WebDriver.setUp()
        base = basemethod()
        info = InFo()
        result_join = Result_Join()
        more = More()
        join.appStart()
        join.pinCode()
        more.etcIn()
        seting.setingIn()
        base.scroll(2)
        join.withdrawal()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, main.withdraw_Result)
            self.assertEqual(Result.text, '원내비')
            print("탈퇴하기 결과 : PASS")
            result_join.reports.append("탈퇴하기 결과 : *PASS*")
        except AssertionError:
            print("탈퇴하기 결과 : FAIL")
            result_join.reports.append("탈퇴하기 결과 : *FAIL*")
            base.save_screenshot('탈퇴하기결과_fail')
        except Exception as e:
            print("탈퇴하기 에러 발생 : {}".format(str(e)))
            result_join.reports.append("탈퇴하기 결과 : *Error*")
            base.save_screenshot('탈퇴하기결과_error')
        time.sleep(5)
        join.appStart()
        join.start_Onboarding()
        join.malicious_App_Search()
        join.message_Certification()
        join.enter_Personal_Information()
        join.join_Next()
        join.membership_Terms_And_Conditions_All()
        time.sleep(6)
        join.join_Next()
        join.use_Fingerprint()
        join.pinCode()
        time.sleep(1)
        join.pinCode()


if __name__ == '__main__':
    unittest.main()