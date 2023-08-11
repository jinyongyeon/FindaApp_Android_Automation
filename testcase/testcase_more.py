import time
import unittest

from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More
from pages.mainlocator.home import Home
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod





class MoreTestcase_A(unittest.TestCase):

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
        more = More()
        more.etc_in()

    def tearDown(self):
        base = basemethod()
        more = More()
        base.android_back()
        time.sleep(1)
        more.etc_in()
        base.scroll_up(0.8)

    # 더보기 진입 테스트
    def test_check_more_tab(self):
        more = More()
        base = basemethod()
        etc = Etc()
        moreresult = Result_More()
        more.etc_in()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.etc_result)
            self.assertEqual(Result.text, "더보기")
            print("더보기 탭 진입 : PASS")
            moreresult.reports.append("더보기 탭 진입 : *PASS*")
        except AssertionError:
            print("더보기 탭 진입 : FAIL")
            moreresult.reports.append("더보기 탭 진입 : *FAIL*")
            base.save_screenshot('더보기탭진입_fail')
        except Exception as e:
            print("더보기 탭 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("더보기 탭 진입 : *Error*")
            base.save_screenshot('더보기탭진입_error')

    # 내대출 진입 테스트
    def test_myloan_in(self):
        # driver = WebDriver.setUpCalss()
        base = basemethod()
        more = More()
        etc = Etc()
        more.my_loan()
        moreresult = Result_More()
        results = []
        verification_list = [("내 현금흐름", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
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
            print("내 대출 진입 : PASS")
            moreresult.reports.append("내 대출 진입 : *PASS*")
        else:
            print("내 대출 진입 : FAIL")
            moreresult.reports.append("내 대출 진입 : *FAIL*")
            base.save_screenshot('내대출진입_fail')

        more.my_loan_back()

    # 채팅문의 진입 테스트
    def test_chat_ting(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.chatting()
        try:
            result = WebDriver.driver.find_element(MobileBy.XPATH, etc.chatting_result)
            self.assertEqual(result.text, "채널톡 이용중")
            print("채널톡 진입 : PASS")
            moreresult.reports.append("채널톡 진입 : *PASS*")
        except AssertionError:
            print("채널톡 진입 : FAIL")
            moreresult.reports.append("채널톡 진입 : *FAIL*")
            base.save_screenshot('채널톡진입_fail')
        except Exception as e:
            print("채널톡 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("채널톡 진입 : *Error*")
            base.save_screenshot('채널톡진입_error')
        base.android_back()

    # 자주묻는 질문 진입 및 상세 페이지 노출 테스트
    def test_qna(self):
        more = More()
        etc = Etc()
        base = basemethod()
        more.qna()
        moreresult = Result_More()
        results = []
        verification_list = [("정말 이 조건 그대로 대출 가능한가요?", etc.qna_a),
                             ("신청하면 대출금은 언제 입금이 되나요?", etc.qna_b),
                             ("대출 조건은 언제까지 유효한가요?", etc.qna_c),
                             ("대출을 알아보는 것으로, 불이익이 있나요?", etc.qna_d),
                             ("신용조회가 여러 건 발생했다고 하는데 무슨 일인가요?", etc.qna_e)]
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
            print("자주 묻는 질문 진입 : PASS")
            moreresult.reports.append("자주 묻는 질문 진입 : *PASS*")
        else:
            print("자주 묻는 질문 진입 : FAIL")
            moreresult.reports.append("자주 묻는 질문 진입 : *FAIL*")
            base.save_screenshot('자주묻는질문진입_fail')

        more.qna_click_a()
        try:
            result_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_result_a)
            self.assertIn("고객님께서 입력해주신 정보의 정확도", result_a.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_A_fail')
        except Exception as e:
            print("{}".format(str(e)))
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_A_error')
        more.qna_click_b()
        try:
            result_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_result_b)
            self.assertIn("대출이 확정된 후 대출금이 입금되기까지는", result_b.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_B_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_B_error')
        more.qna_click_c()
        try:
            result_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_result_c)
            self.assertIn("조회하신 대출 조건은 조회 당일 자정까지만 유효하며,", result_c.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_C_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_C_error')
        more.qna_click_d()
        try:
            result_d = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_result_d)
            self.assertIn("대출조회는 신용점수에 전혀 영향을 미치지 않습니다.", result_d.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_D_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_D_error')
        more.qna_click_e()
        try:
            result_e = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_result_e)
            self.assertIn("걱정하지 마세요. 핀다에서는 여러 금융사의 상품을", result_e.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_E_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_E_error')
        print(results)
        if all(result == "PASS" for result in results):
            print("자주 묻는 질문 상세 항목 노출 : PASS")
            moreresult.reports.append("자주 묻는 질문 상세 항목 노출 : *PASS*")
        else:
            print("자주 묻는 질문 상세 항목 노출 : FAIL")
            moreresult.reports.append("자주 묻는 질문 상세 항목 노출 : *FAIL*")
        more.qna_click_e()
        base.android_back()

    # 대출 갈아타기 테스트
    def test_refinancing_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.transfer_loan()
        try:
            result_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.transfer_loan_result_a)
            self.assertEqual(result_a.text,"대출 갈아타러 가기")
            print("대출 갈아타기 진입 : PASS")
            moreresult.reports.append("대출 갈아타기 진입 : *PASS*")
        except AssertionError:
            print("대출 갈아타기 진입 : FAIL")
            moreresult.reports.append("대출 갈아타기 진입 : *FAIL*")
            base.save_screenshot('대출갈아타기진입_fail')
        except Exception:
            try:
                result_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.transfer_loan_result_b)
                self.assertEqual(result_b.text,"매월 부담되는 이자를\n지금 바로 줄이고 싶다면?")
                print("대출 갈아타기 진입 : PASS")
                moreresult.reports.append("대출 갈아타기 진입 : *PASS*")
            except AssertionError:
                print("대출 갈아타기 진입 : FAIL")
                moreresult.reports.append("대출 갈아타기 진입 : *FAIL*")
                base.save_screenshot('대출갈아타기진입_fail')
            except Exception as e:
                print("대출 갈아타기 사전신청 진입 에러 발생 : {}".format(str(e)))
                moreresult.reports.append("대출 갈아타기 진입 : *Error*")
                base.save_screenshot('대출갈아타기진입_error')
        base.android_back()

    # 대출 한 번에 비교 진입 테스트
    def test_comparison_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.comparison_loan()

        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_a)
            self.assertEqual(Result_A.text,"오늘의 내 최저금리 알아보기")
            print("대출 한 번에 비교 진입 : PASS")
            moreresult.reports.append("대출 한 번에 비교 진입 : *PASS*")
        except AssertionError:
            print("대출 한 번에 비교 진입 : FAIL")
            moreresult.reports.append("대출 한 번에 비교 진입 : *FAIL*")
            base.save_screenshot('대출한번에비교진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_b)
                self.assertIn("오늘입금" , Result_B.text)
                print("대출 한 번에 비교 진입 : PASS")
                moreresult.reports.append("대출 한 번에 비교 진입 : *PASS*")
            except AssertionError:
                print("대출 한 번에 비교 진입 : FAIL")
                moreresult.reports.append("대출 한 번에 비교 진입 : *FAIL*")
                base.save_screenshot('대출한번에비교진입_fail')
            except Exception as e:
                print("대출 한 번에 비교 진입 에러 발생 : {}".format(str(e)))
                moreresult.reports.append("대출 한 번에 비교 진입 : *Error*")
                base.save_screenshot('대출한번에비교진입_error')

        base.android_back()

    # 자동차 구매 대출 진입 테스트
    def test_auto_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        info = InFo()
        base = basemethod()
        moreresult = Result_More()
        more.auto_loan()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_a)
            self.assertEqual(Result_A.text,"1분만에 내 한도 알아보기")
            print("자동차 구매 대출 진입 : PASS")
            moreresult.reports.append("자동차 구매 대출 진입 : *PASS*")
        except AssertionError:
            print("자동차 구매 대출 진입 : FAIL")
            moreresult.reports.append("자동차 구매 대출 진입 : *FAIL*")
            base.save_screenshot('자동차구매대출진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_b)
                self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result_B.text)
                print("자동차 구매 대출 진입 : PASS")
                moreresult.reports.append("자동차 구매 대출 진입 : *PASS*")
            except AssertionError:
                print("자동차 구매 대출 진입 : FAIL")
                moreresult.reports.append("자동차 구매 대출 진입 : *FAIL*")
                base.save_screenshot('자동차구매대출진입_fail')
            except Exception as e:
                print("자동차 구매 대출 진입 에러 발생 : {}".format(str(e)))
                moreresult.reports.append("자동차 구매 대출 진입 : *Error*")
                base.save_screenshot('자동차구매대출진입_error')

        base.android_back()

    # 전월세 추천 진입 테스트
    def test_charter(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.charter()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_Result_a)
            self.assertEqual(Result_A.text,"전월세대출 맞춤추천")
            print("전월세 추천 진입 : PASS")
            moreresult.reports.append("전월세 추천 진입 : *PASS*")
        except AssertionError:
            print("전월세 추천 진입 : FAIL")
            moreresult.reports.append("전월세 추천 진입 : *FAIL*")
            base.save_screenshot('전월세추천진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_Result_b)
                self.assertEqual(Result_B.text,"1:1 맞춤형\n전월세대출 가이드")
                print("전월세 추천 진입 : PASS")
                moreresult.reports.append("전월세 추천 진입 : *PASS*")
            except AssertionError:
                print("전월세 추천 진입 : FAIL")
                moreresult.reports.append("전월세 추천 진입 : *FAIL*")
                base.save_screenshot('전월세추천진입_fail')
            except Exception as e:
                print("전월세 추천 진입 에러 발생 : {}".format(str(e)))
                moreresult.reports.append("전월세 추천 진입 : *Error*")
                base.save_screenshot('전월세추천진입_error')
        try:
            more.charter_back()
        except:
            base.android_back()

    # 대출 챌린지 진입 테스트
    def test_change_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        home = Home()
        base = basemethod()
        moreresult = Result_More()
        more.change_loan()
        try:
            result_A = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_a)
            self.assertIn("내 대출 계좌 연결하기", result_A.text)
            print("대출 챌린지 진입 : PASS")
            moreresult.reports.append("대출 챌린지 진입 : *PASS*")
        except AssertionError:
            print("대출 챌린지 진입 : FAIL")
            moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
            base.save_screenshot('대출챌린지진입_fail')
        except Exception:
            try:
                result_B = WebDriver.driver.find_element(MobileBy.XPATH, home.refinanceloanfirstvisit_b)
                self.assertIn("챌린지 시작하기", result_B.text)
                print("대출 챌린지 진입 : PASS")
                moreresult.reports.append("대출 챌린지 진입 : *PASS*")
            except AssertionError:
                print("대출 챌린지 진입 : FAIL")
                moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                base.save_screenshot('대출챌린지진입_fail')
            except Exception:
                try:
                    result_C = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge)
                    self.assertIn("대환 챌린지", result_C.text)
                    print("대출 챌린지 진입 : PASS")
                    moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                except AssertionError:
                    print("대출 챌린지 진입 : FAIL")
                    moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                    base.save_screenshot('대출챌린지진입_fail')
                except Exception:
                    try:
                        result_D = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_a)
                        self.assertIn("챌린지를 시작하면 이자를\n연 최대 331만원 아낄 수 있어요!", result_D.text)
                        print("대출 챌린지 진입 : PASS")
                        moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                    except AssertionError:
                        print("대출 챌린지 진입 : FAIL")
                        moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                        base.save_screenshot('대출챌린지진입_fail')
                    except Exception:
                        try:
                            result_E = WebDriver.driver.find_element(MobileBy.XPATH, home.refinance_loan_challenge_b)
                            self.assertIn("당신은 Lv.1 될성부른 꿈나무", result_E.text)
                            print("대출 챌린지 진입 : PASS")
                            moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                        except AssertionError:
                            print("대출 챌린지 진입 : FAIL")
                            moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                            base.save_screenshot('대출챌린지진입_fail')
                        except Exception:
                            try:
                                result_F = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                         home.refinance_loan_challenge_c)
                                self.assertIn("당신은 Lv.2 성실한 우등생", result_F.text)
                                print("대출 챌린지 진입 : PASS")
                                moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                            except AssertionError:
                                print("대출진단 배너 진입 : FAIL")
                                moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                                base.save_screenshot('대출챌린지진입_fail')
                            except Exception:
                                try:
                                    result_G = WebDriver.driver.find_element(MobileBy.XPATH,
                                                                             home.refinance_loan_challenge_d)
                                    self.assertIn("당신은 Lv.3 만랩 마스터", result_G.text)
                                    print("대출 챌린지 진입 : PASS")
                                    moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                                except AssertionError:
                                    print("대출진단 배너 진입 : FAIL")
                                    moreresult.reports.append("대출 챌린지 진입 : *FAIL*")
                                    base.save_screenshot('대출챌린지진입_fail')
                                except Exception as e:
                                    print("대출 챌린지 진입 에러 발생 : {}".format(str(e)))
                                    moreresult.reports.append("대출 챌린지 진입 진입 : *Error*")
                                    base.save_screenshot('대출챌린지진입_error')
        try:
            more.change_loan_back()
        except:
            base.android_back()

    # 내대출_B 진입 테스트
    def test_my_loan_b(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        more.my_loan_b()
        results = []
        verification_list = [("내 현금흐름", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
        for text, xpath in verification_list:
            try:
                result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, result.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception :
                results.append("Error")

        print(results)
        if all(result == "PASS" for result in results):
            print("내 대출_B 진입 : PASS")
            moreresult.reports.append("내 대출_B 진입 : *PASS*")
        else:
            print("내 대출_B 진입 : FAIL")
            moreresult.reports.append("내 대출_B 진입 : *FAIL*")
            base.save_screenshot('내대출_B진입_fail')

        more.my_loan_back()

    # 상환일정 진입 테스트
    def test_amortization_schedule(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        base.scroll(0.1)
        time.sleep(2)
        more.amortization_schedule()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.amortization_schedule_a)
            self.assertEqual(Result_A.text,"이번달 총 상환액")
            print("상환일정 진입 : PASS")
            moreresult.reports.append("상환일정 진입 : *PASS*")
        except AssertionError:
            print("상환일정 진입 : FAIL")
            moreresult.reports.append("상환일정 진입 : *FAIL*")
            base.save_screenshot('상환일정진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.amortization_schedule_b)
                self.assertEqual(Result_B.text,"상환 일정이 없습니다.")
                print("상환일정 진입 : PASS")
                moreresult.reports.append("상환일정 진입 : *PASS*")
            except AssertionError:
                print("상환일정 진입 : FAIL")
                moreresult.reports.append("상환일정 진입 : *FAIL*")
                base.save_screenshot('상환일정진입_fail')
            except Exception as e:
                print("상환일정 진입 에러 발생 : {}".format(str(e)))
                moreresult.reports.append("상환일정 진입 진입 : *Error*")
                base.save_screenshot('상환일정진입_error')

        more.amortization_schedule_back()

class MoreTestcase_B(unittest.TestCase):

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
        base = basemethod()
        base.scroll(1)

    def tearDown(self):
        base = basemethod()
        more = More()
        base.android_back()
        time.sleep(1)
        more.etc_in()
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 신용점수 진입 테스트
    def test_credit_score(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        time.sleep(1)
        more.credit_score()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_score_Result)
            self.assertEqual("신용관리", Result.text)
            print("신용점수 진입 : PASS")
            moreresult.reports.append("신용점수 진입 : *PASS*")
        except AssertionError:
            print("신용점수 진입 : FAIL")
            moreresult.reports.append("신용점수 진입 : *FAIL*")
            base.save_screenshot('신용점수진입_fail')
        except Exception as e:
            print("신용점수 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("신용점수 진입 : *Error*")
            base.save_screenshot('신용점수진입_error')

        try:
            more.credit_score_back()
        except:
            base.android_back()

    # 신용점수 올리기 진입 테스트
    def test_improve_credit_score(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.improve_credit_score()
        time.sleep(10)
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_a)
            self.assertEqual(Result_A.text,"신용점수 올리고\n대출이자 낮춰봐요")
            print("신용점수 올리기 진입 : PASS")
            moreresult.reports.append("신용점수 올리기 진입 : *PASS*")
        except AssertionError:
            print("신용점수 올리기 진입 : FAIL")
            moreresult.reports.append("신용점수 올리기 진입 : *FAIL*")
            base.save_screenshot('신용점수올리기진입_fail')
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_b)
                self.assertEqual(Result_B.text, "최근 6개월내 신용점수 올리기를\n이용했어요")
                print("신용점수 올리기 진입 : PASS")
                moreresult.reports.append("신용점수 올리기 진입 : *PASS*")
            except AssertionError:
                print("신용점수 올리기 진입 : FAIL")
                moreresult.reports.append("신용점수 올리기 진입 : *FAIL*")
                base.save_screenshot('신용점수올리기진입_fail')
            except Exception as e:
                print("신용점수 올리기 진입 에러 발생_1 : {}".format(str(e)))
                moreresult.reports.append("신용점수 올리기 진입 : *Error*")
                base.save_screenshot('신용점수올리기진입_error')
        # more.improve_Credit_Score_Back()
        base.android_back()

    # 신용점수 상승 전략 진입 테스트
    def test_credit_analysis(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.credit_analysis()
        # time.sleep(10)
        try:
            Result_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_analysis_Result)
            self.assertEqual(Result_a.text, "신용점수 상승 전략")
            print("신용점수 상승 전략 진입 : PASS")
            moreresult.reports.append("신용점수 상승 전략 진입 : *PASS*")
        except AssertionError:
            print("신용점수 상승 전략 진입 : FAIL")
            moreresult.reports.append("신용점수 상승 전략 진입 : *FAIL*")
            base.save_screenshot('신용점수상승전략진입_fail')
        except Exception as e:
            print("신용점수 상승 전략 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("신용점수 상승 전략 진입 : *Error*")
            base.save_screenshot('신용점수상승전략진입_error')

        # more.credit_Analysis_Back()
        base.android_back()

    # 신용관리 > 신용점수 히스토리 진입 테스트
    def test_credit_history(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.credit_history()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_history_Result)
            self.assertIn("신용점수 히스토리", Result.text)
            print("신용점수 히스토리 진입 : PASS")
            moreresult.reports.append("신용점수 히스트리 진입 : *PASS*")
        except AssertionError:
            print("신용점수 히스트리 진입 : FAIL")
            moreresult.reports.append("신용점수 히스트리 진입 : *FAIL")
            base.save_screenshot('신용점수히스트리진입_fail')
        except Exception as e:
            print("신용점수 히스트리 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("신용점수 히스트리 진입 : *Error*")
            base.save_screenshot('신용점수히스트리진입_error')
        # more.credit_History_Back()
        base.android_back()

    # 개인사업자 신용관리 진입 테스트
    def test_private_business_credit_management(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        time.sleep(1)
        more.private_business_credit_management()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_score_Result)
            self.assertEqual("신용관리", Result.text)
            print("개인사업자 신용관리 진입 : PASS")
            moreresult.reports.append("개인사업자 신용관리 진입 : *PASS*")
        except AssertionError:
            print("개인사업자 신용관리 진입 : FAIL")
            moreresult.reports.append("개인사업자 신용관리 진입 : *FAIL*")
            base.save_screenshot('개인사업자용관리진입_fail')
        except Exception as e:
            print("개인사업자 신용관리 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("개인사업자 신용관리 진입 : *Error*")
            base.save_screenshot('개인사업자용관리진입_error')
        try:
            more.credit_score_back()
        except:
            base.android_back()

    # 계산기 > 여윳돈 계산기 진입 테스트
    def test_extra_money(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.extra_money()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.extra_money_Result)
            self.assertEqual(Result.text, "상환할 여윳돈이 생기셨나요?")
            print("여윳돈 계산기 진입 : PASS")
            moreresult.reports.append("여윳돈 계산기 진입 : *PASS*")
        except AssertionError:
            print("여윳돈 계산기 진입 : FAIL")
            moreresult.reports.append("여윳돈 계산기 진입 : *FAIL*")
            base.save_screenshot('여윳돈계산기진입_fail')
        except Exception as e:
            print("여윳돈 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("여윳돈 계산기 진입 : *Error*")
            base.save_screenshot('여윳돈계산기진입_error')

        try:
            more.extra_money_back()
        except:
            base.android_back()

    # 계산기 > DSR 계산기 진입 테스트
    def test_dsr(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.dsr()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.dsr_Result)
            self.assertEqual(Result.text, "DSR 계산기")
            print("DSR 계산기 진입 : PASS")
            moreresult.reports.append("DSR 계산기 진입 : *PASS*")
        except AssertionError:
            print("DSR 계산기 진입 : FAIL")
            moreresult.reports.append("DSR 계산기 진입 : *FAIL*")
            base.save_screenshot('DSR계산기진입_fail')
        except Exception as e:
            print("DSR 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("DSR 계산기 진입 : *Error*")
            base.save_screenshot('DSR계산기진입_error')

        try:
            more.dsr_back()
        except:
            base.android_back()

    # 계산기 > 대출이자 계산기 진입 테스트
    def test_interest(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.interest()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.interest_Result)
            self.assertEqual(Result.text, "대출이자 계산기")
            print("대출이자 계산기 진입 : PASS")
            moreresult.reports.append("대출이자 계산기 진입 : *PASS*")
        except AssertionError:
            print("대출이자 계산기 진입 : FAIL")
            moreresult.reports.append("대출이자 계산기 진입 : *FAIL*")
            base.save_screenshot('대출이자계산기진입_fail')

        except Exception as e:
            print("대출이자 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("대출이자 계산기 진입 : *Error*")
            base.save_screenshot('대출이자계산기진입_error')

        try:
            more.interest_back()
        except:
            base.android_back()

    # 계산기 > 연말정산 계산기 진입 테스트
    def test_year_end_settlement(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.year_end_settlement()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.year_end_settlement_Result)
            self.assertEqual(Result.text, "카드 및 현금 소비액 소득공제")
            print("연말정산 계산기 진입 : PASS")
            moreresult.reports.append("연말정산 계산기 진입 : *PASS*")
        except AssertionError:
            print("연말정산 계산기 진입 : FAIL")
            moreresult.reports.append("연말정산 계산기 진입 : *FAIL*")
            base.save_screenshot('연말정산계산기진입_fail')
        except Exception as e:
            print("연말정산 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("연말정산 계산기 진입 : *Error*")
            base.save_screenshot('연말정산계산기진입_error')

        try:
            more.year_end_settlement_back()
        except:
            base.android_back()

    # 계산기 > 전세 vs 월세 계산기 진입 테스트
    def test_charter_vs_monthly_rent(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.charter_vs_monthly_rent()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_vs_monthly_rent_Result)
            self.assertEqual(Result.text, "전세 vs 월세 계산기")
            print("전세 vs 월세 계산기 진입 : PASS")
            moreresult.reports.append("전세 vs 월세 계산기 진입 : *PASS*")
        except AssertionError:
            print("전세 vs 월세 계산기 진입 : FAIL")
            moreresult.reports.append("전세 vs 월세 계산기 진입 : *FAIL*")
            base.save_screenshot('전세vs월세계산기진입_fail')
        except Exception as e:
            print("전세 vs 월세 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("전세 vs 월세 계산기 진입 : *Error*")
            base.save_screenshot('전세vs월세계산기진입_error')
        try:
            more.charter_vs_monthly_rent_back()
        except:
            base.android_back()

    # 계산기 > 대출 갈아타기 계산기 진입 테스트
    def test_refinancing_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        base.scroll(0.1)
        more.refinancing_loan()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_Result)
            self.assertIn("대출 갈아타기 계산기" , Result.text)
            print("대출 갈아타기 계산기 진입 : PASS")
            moreresult.reports.append("대출 갈아타기 계산기 진입 : *PASS*")
        except AssertionError:
            print("대출 갈아타기 계산기 진입 : FAIL")
            moreresult.reports.append("대출 갈아타기 계산기 진입 : *FAIL*")
            base.save_screenshot('대출갈아타기계산기진입_fail')
        except Exception as e:
            print("대출 갈아타기 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("대출 갈아타기 계산기 진입 : *Error*")
            base.save_screenshot('대출갈아타기계산기진입_error')

        try:
            more.refinancing_loan_back()
        except:
            base.android_back()

    # 청년도약계좌 계산기 진입 테스트
    def test_youth_leap_account(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        base.scroll(0.15)
        more.youth_leap_account()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.youth_leap_account_result)
            self.assertIn("청년도약계좌 계산기" , Result.text)
            print("청년도약계좌 계산기 진입 : PASS")
            moreresult.reports.append("청년도약계좌 계산기 진입 : *PASS*")
        except AssertionError:
            print("청년도약계좌 계산기 진입 : FAIL")
            moreresult.reports.append("청년도약계좌 계산기 진입 : *FAIL*")
            base.save_screenshot('청년도약계좌계산기진입_fail')
        except Exception as e:
            print("청년도약계좌 계산기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("청년도약계좌 계산기 진입 : *Error*")
            base.save_screenshot('청년도약계좌계산기진입_error')
        base.android_back()

class MoreTestcase_C(unittest.TestCase):

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
        base = basemethod()
        base.scroll(1)
        base.scroll(1.05)

    def tearDown(self):
        base = basemethod()
        more = More()
        base.android_back()
        time.sleep(1)
        more.etc_in()
        base.scroll_up(0.8)
        base.scroll_up(0.8)
        base.scroll_up(0.8)

    # 장기렌트 리스 진입 테스트
    def test_lease_rent(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        more.lease_rent()
        time.sleep(3)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.lease_rent_result)
            self.assertEqual(Result.text, "리스렌트")
            print("장기렌트 리스 진입 : PASS")
            moreresult.reports.append("장기렌트 리스 진입 : *PASS*")
        except AssertionError:
            print("장기렌트 리스 진입 : FAIL")
            moreresult.reports.append("장기렌트 리스 진입 : *FAIL*")
            base.save_screenshot('장기렌트리스진입_fail')
        except Exception as e:
            print("장기렌트 리스 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("장기렌트 리스 진입 : *Error*")
            base.save_screenshot('장기렌트리스진입_error')

        base.android_back()

    # 두낫콜 약관 리스트 진입 테스트
    def test_do_not_call_terms_of_use(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        more.do_not_call()
        more.do_net_call_cta()
        more.terms_of_use_a()
        more.terms_of_use_b()
        more.terms_of_use_c()
        moreresult = Result_More()
        results = []
        verification_list = [("연락중지청구(Do-not-call) 서비스 이용약관", etc.do_not_call_a_a),
                             ("개인정보 수집·이용에 대한 동의", etc.do_not_call_a_b),
                             ("개인정보처리방침", etc.do_not_call_a_c),
                             ("개인정보이용동의", etc.do_not_call_b_a),
                             ("고유식별정보처리동의", etc.do_not_call_b_b),
                             ("서비스이용약관동의", etc.do_not_call_b_c),
                             ("통신사이용약관동의", etc.do_not_call_b_d),
                             ("[금융스팸차단하기] 서비스 이용 약관", etc.do_not_call_c_a),
                             ("[금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)", etc.do_not_call_c_b),
                             ("[금융스팸차단하기] 개인(신용)정보 제3자 제공 동의(필수)", etc.do_not_call_c_c)]

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
            print("두낫콜 약관 노출 : PASS")
            moreresult.reports.append("두낫콜 약관 노출 : *PASS*")
        else:
            print("두낫콜 약관 노출 : FAIL")
            moreresult.reports.append("두낫콜 약관 노출 : *FAIL*")
            base.save_screenshot('두낫콜약관노출_fail')

        more.terms_of_use_aa()
        try:
            Result_a_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_a.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Aa_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Aa_error')
        more.terms_of_use_webview_exit()

        more.terms_of_use_ab()
        try:
            Result_a_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_b.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ab_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ab_error')

        more.terms_of_use_webview_exit()

        more.terms_of_use_ac()
        try:
            Result_a_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_c.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ac_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ac_error')

        more.terms_of_use_webview_exit()

        more.terms_of_use_ba()
        try:
            Result_b_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_a.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ba_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ba_error')
        except Exception:
            results.append("PASS")

        more.terms_of_use_webview_exit()

        more.terms_of_use_bb()
        try:
            Result_b_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_b.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bb_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bb_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        more.terms_of_use_bc()
        try:
            Result_b_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_c.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bc_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bc_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        more.terms_of_use_bd()
        try:
            Result_b_d = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_d.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bd_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bd_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        more.terms_of_use_ca()
        try:
            Result_c_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_a.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ca_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ca_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        more.terms_of_use_cb()
        try:
            Result_c_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_b.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Cb_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Cb_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        more.terms_of_use_cc()
        try:
            Result_c_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_c.text)
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Cc_fail')
        except AssertionError:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Cc_error')
        except Exception:
            results.append("PASS")
        more.terms_of_use_webview_exit()

        print(results)
        if all(result == "PASS" for result in results):
            print("두낫콜 약관 페이지 진입 노출 : PASS")
            moreresult.reports.append("두낫콜 약관 페이지 진입 노출 : *PASS*")
        else:
            print("두낫콜 약관 페이지 진입 노출 : FAIL")
            moreresult.reports.append("두낫콜 약관 페이지 진입 노출 : *FAIL*")
        more.do_not_call_back()

    # 대출금 갚아주는 보험 진입 테스트
    def test_insurance(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.insurance()
        time.sleep(2)
        more.insurance_web()
        time.sleep(15)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.insurance_Result)
            self.assertIn("BNP파리바 카디프생명", Result.text)
            print("대출금 갚아주는 보험 진입 : PASS")
            moreresult.reports.append("대출금 갚아주는 보험 진입 : *PASS*")
        except AssertionError:
            print("대출금 갚아주는 보험 진입 : FAIL")
            moreresult.reports.append("대출금 갚아주는 보험 진입 : *FAIL*")
            base.save_screenshot('대출금갚아주는보험진입_fail')
        except Exception as e:
            print("대출금 갚아주는 보험 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("대출금 갚아주는 보험 진입 : *Error*")
            base.save_screenshot('대출금갚아주는보험진입_error')
        base.android_back()
        base.android_back()

    # 예적금 비교 진입 테스트
    def test_deposit_and_savings(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        more.deposit_and_savings()
        time.sleep(10)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.deposit_and_savings_Result)
            self.assertEqual(Result.text,"예적금 비교")
            print("예적금 비교 진입 : PASS")
            moreresult.reports.append("예적금 비교 진입 : *PASS*")
        except AssertionError:
            print("예적금 비교 진입 : FAIL")
            moreresult.reports.append("예적금 비교 진입 : *FAIL*")
            base.save_screenshot('예적금비교진입_fail')
        except Exception as e:
            print("예적금 비교 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("예적금 비교 진입 : *Error*")
            base.save_screenshot('예적금비교진입_error')

        base.android_back()

    # 핀다 포스트 진입 테스트
    def test_finda_post(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.finda_post()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.finda_post_Result)
            self.assertEqual(Result.text,"핀다포스트")
            print("핀다 포스트 진입 : PASS")
            moreresult.reports.append("핀다 포스트 진입 : *PASS*")
        except AssertionError:
            print("핀다 포스트 진입 : FAIL")
            moreresult.reports.append("핀다 포스트 진입 : *FAIL*")
            base.save_screenshot('핀다포스트진입_fail')
        except Exception as e:
            print("핀다 포스트 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("핀다 포스트 진입 : *Error*")
            base.save_screenshot('핀다포스트진입_error')

        try:
            more.finda_post_back()
        except:
            base.android_back()

    # 내 폰 지키미 진입 테스트
    def test_my_phorn(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.my_phorn()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.my_phorn_Result)
            self.assertEqual(Result.text,"내 폰 보호하기")
            print("내 폰 지키미 진입 : PASS")
            moreresult.reports.append("내 폰 지키미 진입 : *PASS*")
        except AssertionError:
            print("내 폰 지키미 진입 : FAIL")
            moreresult.reports.append("내 폰 지키미 진입 : *FAIL*")
            base.save_screenshot('내폰지키미진입_fail')
        except Exception as e:
            print("내 폰 지키미 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("내 폰 지키미 진입 : *Error*")
            base.save_screenshot('내폰지키미진입_error')

        try:
            more.my_phorn_back()
        except:
            base.android_back()

    # 이벤트 진입 테스트
    def test_event(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.event()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.event_Result)
            self.assertEqual(Result.text,"돈되는 혜택")
            print("돈되는 혜택 진입 : PASS")
            moreresult.reports.append("돈되는 혜택 진입 : *PASS*")
        except AssertionError:
            print("돈되는 혜택 진입 : FAIL")
            moreresult.reports.append("돈되는 혜택 진입 : *FAIL*")
            base.save_screenshot('돈되는혜택진입_fail')
        except Exception as e:
            print("돈되는 혜택 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("돈되는 혜택 진입 : *Error*")
            base.save_screenshot('돈되는혜택진입_error')

        try:
            more.event_back()
        except:
            base.android_back()

    # 공지사항 진입 테스트
    def test_notice(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.notice()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.notice_Result)
            self.assertEqual(Result.text,"공지사항")
            print("공지사항 진입 : PASS")
            moreresult.reports.append("공지사항 진입 : *PASS*")
        except AssertionError:
            print("공지사항 진입 : FAIL")
            moreresult.reports.append("공지사항 진입 : *FAIL*")
            base.save_screenshot('공지사항진입_fail')
        except Exception as e:
            print("공지사항 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("공지사항 진입 : *Error*")
            base.save_screenshot('공지사항진입_error')
        time.sleep(2)
        more.notice_in()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.notice_in_Result)
            self.assertEqual(Result.text,"안녕하세요 핀다입니다.")
            print("공지사항 상세 진입 : PASS")
            moreresult.reports.append("공지사항 상세 진입 : *PASS*")
        except AssertionError:
            print("공지사항 상세 진입 : FAIL")
            moreresult.reports.append("공지사항 상세 진입 : *FAIL*")
            base.save_screenshot('공지사항상세진입_fail')
        except Exception as e:
            print("공지사항 상세 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("공지사항 상세 진입 : *Error*")
            base.save_screenshot('공지사항상세진입_error')
        more.notice_in_back()
        more.notice_back()

    # 대출 후기 진입 테스트
    def test_loan_reviews(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.loan_reviews()
        time.sleep(15)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.loan_reviews_Result)
            self.assertIn("대출받으신 고객님들의 후기입니다.", Result.text)
            print("대출 후기 진입 : PASS")
            moreresult.reports.append("대출 후기 진입 : *PASS*")
        except AssertionError:
            print("대출 후기 진입 : FAIL")
            moreresult.reports.append("대출 후기 진입 : *FAIL*")
            base.save_screenshot('대출후기진입_fail')
        except Exception as e:
            print("대출 후기 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("대출 후기 진입 : *Error*")
            base.save_screenshot('대출후기진입_error')
        more.loan_reviews_back()

    # 최근 알림 진입 테스트
    def test_alarm(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        more.alarm()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.alarm_Result)
            self.assertEqual(Result.text,"최근 알림")
            print("최근 알림 진입 : PASS")
            moreresult.reports.append("최근 알림 진입 : *PASS*")
        except AssertionError:
            print("최근 알림 진입 : FAIL")
            moreresult.reports.append("최근 알림 진입 : *FAIL*")
            base.save_screenshot('최근알림진입_fail')
        except Exception as e:
            print("최근 알림 진입 에러 발생 : {}".format(str(e)))
            moreresult.reports.append("최근 알림 진입 : *Error*")
            base.save_screenshot('최근알림진입_error')
        more.alarm_back()

if __name__ == '__main__':
    unittest.main()