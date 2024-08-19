import logging
import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More
from pages.mainlocator.home import Home
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod





class MoreTestcase_A(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("더보기 테스트 시작")

    @classmethod
    def tearDownClass(cls):
        logging.info("더보기 테스트 종료")

    def setUp(self):
        more = More()
        more.etc_in()

    def tearDown(self):
        base = basemethod()
        more = More()
        base.android_back()
        base.android_back()
        time.sleep(1)
        more.etc_in()
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        # base.scroll_up(0.8)
        more.more_top()

    # 더보기 진입 테스트
    def test_check_more_tab(self):
        more = More()
        base = basemethod()
        etc = Etc()
        moreresult = Result_More()
        logging.info("더보기 진입 테스트 시작")
        more.etc_in()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.etc_result))
            logging.info("더보기 탭 진입 : PASS")
            moreresult.reports.append("더보기 탭 진입 : *PASS*")
            print("더보기 탭 진입 : PASS")
        except TimeoutError:
            logging.info("더보기 탭 진입_요소 확인 필요 : FAIL")
            moreresult.reports.append("더보기 탭 진입_요소 확인 필요 : *FAIL*")
            base.save_screenshot('더보기탭진입_fail')
            print("더보기 탭 진입_요소 확인 필요 : FAIL")
        except Exception as e:
            logging.warning(f"더보기 탭 진입 에러 발생 : {e}")
            moreresult.reports.append("더보기 탭 진입 : *Error*")
            base.save_screenshot('더보기탭진입_error')
            print(f"더보기 탭 진입 에러 발생 : {e}")
        logging.info("더보기 진입 테스트 시작")

    # 내대출 진입 테스트
    def test_myloan_in(self):
        base = basemethod()
        more = More()
        etc = Etc()
        more.my_loan()
        moreresult = Result_More()
        results = []
        logging.info("내대출 진입 테스트 시작")
        verification_list = [("카드", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
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
            logging.info("내 대출 진입 : PASS")
            moreresult.reports.append("내 대출 진입 : *PASS*")
            print("내 대출 진입 : PASS")
        else:
            logging.info("내 대출 진입 : FAIL")
            moreresult.reports.append("내 대출 진입 : *FAIL*")
            base.save_screenshot('내대출진입_fail')
            print("내 대출 진입 : FAIL")
        more.my_loan_back()
        logging.info("내대출 진입 테스트 종료")

    # 채팅문의 진입 테스트
    def test_chat_ting(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("채팅문의 진입 테스트 시작")
        more.chatting()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.chatting_result))
            logging.info("채널톡 진입 : PASS")
            moreresult.reports.append("채널톡 진입 : *PASS*")
            print("채널톡 진입 : PASS")
        except TimeoutError:
            logging.info("채널톡 진입 : FAIL")
            moreresult.reports.append("채널톡 진입 : *FAIL*")
            base.save_screenshot('채널톡진입_fail')
            print("채널톡 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"채널톡 진입 에러 발생 : {e}")
            moreresult.reports.append("채널톡 진입 : *Error*")
            base.save_screenshot('채널톡진입_error')
            print(f"채널톡 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("채팅문의 진입 테스트 종료")

    # 자주묻는 질문 진입 및 상세 페이지 노출 테스트
    def test_qna(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        results = []
        logging.info("자주묻는 질문 진입 및 상세 페이지 노출 테스트 시작")
        more.qna()
        verification_list = [("정말 이 조건 그대로 대출 가능한가요?", etc.qna_a),
                             ("신청하면 대출금은 언제 입금이 되나요?", etc.qna_b),
                             # ("대출 조건은 언제까지 유효한가요?", etc.qna_c),    # 항목 삭제됨
                             ("대출을 알아보는 것으로, 불이익이 있나요?", etc.qna_d),
                             ("신용조회가 여러 건 발생했다고 하는데 무슨 일인가요?", etc.qna_e)]
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
            logging.info("자주 묻는 질문 진입 : PASS")
            moreresult.reports.append("자주 묻는 질문 진입 : *PASS*")
        else:
            logging.info("자주 묻는 질문 진입 : FAIL")
            moreresult.reports.append("자주 묻는 질문 진입 : *FAIL*")
            base.save_screenshot('자주묻는질문진입_fail')
        more.qna_click_a()
        more.qna_click_a()
        more.qna_click_a()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_result_a))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_A_fail')
        except Exception as e:
            logging.warning(f"자주묻는질문진입_A 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_A_error')
        more.qna_click_b()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.qna_result_b))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_B_fail')
        except Exception as e:
            logging.warning(f"자주묻는질문진입_B 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_B_error')
        # more.qna_click_c()
        # try:
        #     WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.qna_result_c))
        #     results.append("PASS")
        # except TimeoutError:
        #     results.append("FAIL")
        #     base.save_screenshot('자주묻는질문진입_C_fail')
        # except Exception as e:
        #     logging.warning(f"자주묻는질문진입_C 에러 발생 : {e}")
        #     results.append("Error")
        #     base.save_screenshot('자주묻는질문진입_C_error')
        more.qna_click_d()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.qna_result_d))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_D_fail')
        except Exception as e:
            logging.warning(f"자주묻는질문진입_D 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_D_error')
        more.qna_click_e()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.qna_result_e))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('자주묻는질문진입_E_fail')
        except Exception as e:
            logging.warning(f"자주묻는질문진입_E 에러 발생 : {e}")
            results.append("Error")
            base.save_screenshot('자주묻는질문진입_E_error')
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("자주 묻는 질문 상세 항목 노출 : PASS")
            moreresult.reports.append("자주 묻는 질문 상세 항목 노출 : *PASS*")
            print("자주 묻는 질문 상세 항목 노출 : PASS")
        else:
            logging.info("자주 묻는 질문 상세 항목 노출 : FAIL")
            moreresult.reports.append("자주 묻는 질문 상세 항목 노출 : *FAIL*")
            print("자주 묻는 질문 상세 항목 노출 : FAIL")
        more.qna_click_e()
        base.android_back()
        logging.info("자주묻는 질문 진입 및 상세 페이지 노출 테스트 종료")

    # 대출 갈아타기 테스트
    def test_refinancing_loan(self):
        # driver = WebDriver.setUpCalss()
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("대출 갈아타기 테스트 시작")
        more.transfer_loan()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.transfer_loan_result_a))
            logging.info("대출 갈아타기 진입 : PASS")
            moreresult.reports.append("대출 갈아타기 진입 : *PASS*")
            print("대출 갈아타기 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.transfer_loan_result_b))
                logging.info("대출 갈아타기 진입 : PASS")
                moreresult.reports.append("대출 갈아타기 진입 : *PASS*")
                print("대출 갈아타기 진입 : PASS")
            except TimeoutError:
                logging.info("대출 갈아타기 진입_요소 확인필요 : FAIL")
                moreresult.reports.append("대출 갈아타기 진입_요소 확인필요 : *FAIL*")
                base.save_screenshot('대출갈아타기진입_fail')
                print("대출 갈아타기 진입_요소 확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"대출 갈아타기 사전신청 진입 에러 발생 : {e}")
                moreresult.reports.append("대출 갈아타기 진입 : *Error*")
                base.save_screenshot('대출갈아타기진입_error')
                print(f"대출 갈아타기 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("대출 갈아타기 테스트 종료")

    # 대출 한 번에 비교 진입 테스트
    def test_comparison_loan(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("대출 한 번에 비교 진입 테스트 시작")
        more.comparison_loan()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.comparison_loan_Result_a))
            logging.info("대출 한 번에 비교 진입 : PASS")
            moreresult.reports.append("대출 한 번에 비교 진입 : *PASS*")
            print("대출 한 번에 비교 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.comparison_loan_Result_b))
                logging.info("대출 한 번에 비교 진입 : PASS")
                moreresult.reports.append("대출 한 번에 비교 진입 : *PASS*")
                print("대출 한 번에 비교 진입 : PASS")
            except TimeoutError:
                logging.info("대출 한 번에 비교 진입_요소 확인필요 : FAIL")
                moreresult.reports.append("대출 한 번에 비교 진입_요소 확인필요 : *FAIL*")
                base.save_screenshot('대출한번에비교진입_fail')
                print("대출 한 번에 비교 진입_요소 확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"대출 한 번에 비교 진입 에러 발생 : {e}")
                moreresult.reports.append("대출 한 번에 비교 진입 : *Error*")
                base.save_screenshot('대출한번에비교진입_error')
                print(f"대출 한 번에 비교 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("대출 한 번에 비교 진입 테스트 종료")

    # 자동차 구매 대출 진입 테스트
    def test_auto_loan(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("자동차 구매 대출 진입 테스트 시작")
        more.auto_loan()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.auto_loan_Result_a))
            logging.info("자동차 구매 대출 진입 : PASS")
            moreresult.reports.append("자동차 구매 대출 진입 : *PASS*")
            print("자동차 구매 대출 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.auto_loan_Result_b))
                logging.info("자동차 구매 대출 진입 : PASS")
                moreresult.reports.append("자동차 구매 대출 진입 : *PASS*")
                print("자동차 구매 대출 진입 : PASS")
            except TimeoutError:
                logging.info("자동차 구매 대출 진입_요소 확인필요 : FAIL")
                moreresult.reports.append("자동차 구매 대출 진입_요소 확인필요 : *FAIL*")
                base.save_screenshot('자동차구매대출진입_fail')
                print("자동차 구매 대출 진입_요소 확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"자동차 구매 대출 진입 에러 발생 : {e}")
                moreresult.reports.append("자동차 구매 대출 진입 : *Error*")
                base.save_screenshot('자동차구매대출진입_error')
                print(f"자동차 구매 대출 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("자동차 구매 대출 진입 테스트 종료")

    # 전월세 추천 진입 테스트
    def test_charter(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("전월세 추천 진입 테스트 시작")
        more.charter()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.charter_Result_a))
            logging.info("전월세 추천 진입 : PASS")
            moreresult.reports.append("전월세 추천 진입 : *PASS*")
            print("전월세 추천 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.charter_Result_b))
                logging.info("전월세 추천 진입 : PASS")
                moreresult.reports.append("전월세 추천 진입 : *PASS*")
                print("전월세 추천 진입 : PASS")
            except TimeoutError:
                logging.info("전월세 추천 진입_요소 확인필요 : FAIL")
                moreresult.reports.append("전월세 추천 진입_요소 확인필요 : *FAIL*")
                base.save_screenshot('전월세추천진입_fail')
                print("전월세 추천 진입_요소 확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"전월세 추천 진입 에러 발생 : {e}")
                moreresult.reports.append("전월세 추천 진입 : *Error*")
                base.save_screenshot('전월세추천진입_error')
                print(f"전월세 추천 진입 에러 발생 : {e}")
        try:
            more.charter_back()
        except:
            base.android_back()
        logging.info("전월세 추천 진입 테스트 종료")

    # 대환 챌린지 진입 테스트
    def test_change_loan(self):
        more = More()
        home = Home()
        base = basemethod()
        moreresult = Result_More()
        logging.info("대환 챌린지 진입 테스트 시작")
        more.change_loan()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinanceloanfirstvisit_a))
            logging.info("대출 챌린지 진입 : PASS")
            moreresult.reports.append("대출 챌린지 진입 : *PASS*")
            print("대출 챌린지 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinanceloanfirstvisit_b))
                logging.info("대출 챌린지 진입 : PASS")
                moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                print("대출 챌린지 진입 : PASS")
            except Exception:
                try:
                    WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinance_loan_challenge))
                    logging.info("대출 챌린지 진입 : PASS")
                    moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                    print("대출 챌린지 진입 : PASS")
                except Exception:
                    try:
                        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinance_loan_challenge_a))
                        logging.info("대출 챌린지 진입 : PASS")
                        moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                        print("대출 챌린지 진입 : PASS")
                    except Exception:
                        try:
                            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinance_loan_challenge_b))
                            logging.info("대출 챌린지 진입 : PASS")
                            moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                            print("대출 챌린지 진입 : PASS")
                        except Exception:
                            try:
                                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinance_loan_challenge_c))
                                logging.info("대출 챌린지 진입 : PASS")
                                moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                                print("대출 챌린지 진입 : PASS")
                            except Exception:
                                try:
                                    WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(home.refinance_loan_challenge_d))
                                    logging.info("대출 챌린지 진입 : PASS")
                                    moreresult.reports.append("대출 챌린지 진입 : *PASS*")
                                    print("대출 챌린지 진입 : PASS")
                                except TimeoutError:
                                    logging.info("대출진단 배너 진입_요소 확인필요 : FAIL")
                                    moreresult.reports.append("대출 챌린지 진입_요소 확인필요 : *FAIL*")
                                    base.save_screenshot('대출챌린지진입_fail')
                                    print("대출진단 배너 진입_요소 확인필요 : FAIL")
                                except Exception as e:
                                    logging.warning(f"대출 챌린지 진입 에러 발생 : {e}")
                                    moreresult.reports.append("대출 챌린지 진입 진입 : *Error*")
                                    base.save_screenshot('대출챌린지진입_error')
                                    print(f"대출 챌린지 진입 에러 발생 : {e}")
        try:
            more.change_loan_back()
        except:
            base.android_back()
        logging.info("대환 챌린지 진입 테스트 종료")

    # 내자산 진입 테스트
    def test_my_loan_b(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("내자산 진입 테스트 시작")
        more.my_loan_b()
        results = []
        verification_list = [("카드", etc.myloan_Result_a),
                             ("대출", etc.myloan_Result_b),
                             ("입출금", etc.myloan_Result_c),
                             ("예적금", etc.myloan_Result_d)]
        for text, xpath in verification_list:
            try:
                result = WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(xpath))
                self.assertIn(text, result.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except Exception :
                results.append("Error")
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("내 자산 진입 : PASS")
            moreresult.reports.append("내 자산 진입 : *PASS*")
            print("내 자산 진입 : PASS")
        else:
            logging.info("내 자산 진입 : FAIL")
            moreresult.reports.append("내 자산 진입 : *FAIL*")
            base.save_screenshot('내자산진입_fail')
            print("내 자산 진입 : FAIL")
        more.my_loan_back()
        logging.info("내 자산 진입 테스트 종료")

    # 상환일정 진입 테스트
    def test_amortization_schedule(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("상환일정 진입 테스트 시작")
        more.amortization_schedule()
        try:
            more.check()
        except:
            pass
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.amortization_schedule_a))
            logging.info("상환일정 진입 : PASS")
            moreresult.reports.append("상환일정 진입 : *PASS*")
            print("상환일정 진입 : PASS")
        except TimeoutError:
            logging.info("상환일정 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("상환일정 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('상환일정진입_fail')
            print("상환일정 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"상환일정 진입 에러 발생 : {e}")
            moreresult.reports.append("상환일정 진입 진입 : *Error*")
            base.save_screenshot('상환일정진입_error')
            print(f"상환일정 진입 에러 발생 : {e}")
        try:
            more.amortization_schedule_back()
        except:
            base.android_back()
        logging.info("상환일정 진입 테스트 종료")

    # 정부 전자문서지갑 진입 테스트
    def test_electronic_wallet(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("정부 전자문서지갑 진입 테스트 시작")
        more.electronic_wallet()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.electronic_wallet))
            logging.info("정부 전자문서지갑 진입 : PASS")
            moreresult.reports.append("정부 전자문서지갑 진입 : *PASS*")
            print("정부 전자문서지갑 진입 : PASS")
        except TimeoutError:
            logging.info("정부 전자문서지갑 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("정부 전자문서지갑 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('정부 전자문서지갑진입_fail')
            print("정부 전자문서지갑 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"정부 전자문서지갑 진입 에러 발생 : {e}")
            moreresult.reports.append("정부 전자문서지갑 진입 진입 : *Error*")
            base.save_screenshot('정부 전자문서지갑진입_error')
            print(f"정부 전자문서지갑 진입 에러 발생 : {e}")
        try:
            more.check()
        except:
            base.android_back()
        logging.info("정부 전자문서지갑 진입 테스트 종료")

#
# class MoreTestcase_B(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         logging.info("더보기 테스트_B 시작")
#
#     @classmethod
#     def tearDownClass(cls):
#         logging.info("더보기 테스트_B 종료")
#
#     def setUp(self):
#         base = basemethod()
#
#     def tearDown(self):
#         base = basemethod()
#         more = More()
#         base.android_back()
#         base.android_back()
#         time.sleep(1)
#         more.etc_in()
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)

    # 신용점수 진입 테스트
    def test_credit_score(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("신용점수 진입 테스트 시작")
        time.sleep(1)
        more.credit_score()
        try:
            time.sleep(5)
            more.exit()
        except:
            pass
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_score_Result))
            logging.info("신용점수 진입 : PASS")
            moreresult.reports.append("신용점수 진입 : *PASS*")
            print("신용점수 진입 : PASS")
        except TimeoutError:
            logging.info("신용점수 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("신용점수 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('신용점수진입_fail')
            print("신용점수 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"신용점수 진입 에러 발생 : {e}")
            moreresult.reports.append("신용점수 진입 : *Error*")
            base.save_screenshot('신용점수진입_error')
            print(f"신용점수 진입 에러 발생 : {e}")
        try:
            more.credit_score_back()
        except:
            base.android_back()
        logging.info("신용점수 진입 테스트 종료")

    # 신용점수 올리기 진입 테스트
    def test_improve_credit_score(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("신용점수 올리기 진입 테스트 시작")
        more.improve_credit_score()
        time.sleep(10)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.improve_credit_score_Result_a))
            logging.info("신용점수 올리기 진입 : PASS")
            moreresult.reports.append("신용점수 올리기 진입 : *PASS*")
            print("신용점수 올리기 진입 : PASS")
        except Exception:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.improve_credit_score_Result_b))
                logging.info("신용점수 올리기 진입 : PASS")
                moreresult.reports.append("신용점수 올리기 진입 : *PASS*")
                print("신용점수 올리기 진입 : PASS")
            except TimeoutError:
                logging.info("신용점수 올리기 진입_요소 확인필요 : FAIL")
                moreresult.reports.append("신용점수 올리기 진입_요소 확인필요 : *FAIL*")
                base.save_screenshot('신용점수올리기진입_fail')
                print("신용점수 올리기 진입_요소 확인필요 : FAIL")
            except Exception as e:
                logging.warning(f"신용점수 올리기 진입 에러 발생 : {e}")
                moreresult.reports.append("신용점수 올리기 진입 : *Error*")
                base.save_screenshot('신용점수올리기진입_error')
                print(f"신용점수 올리기 진입 에러 발생 : {e}")
        # more.improve_Credit_Score_Back()
        base.android_back()
        logging.info("신용점수 올리기 진입 테스트 종료")

    # 신용점수 상승 전략 진입 테스트
    def test_credit_analysis(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("신용점수 상승 전략 진입 테스트 시작")
        more.credit_analysis()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_analysis_Result))
            logging.info("신용점수 상승 전략 진입 : PASS")
            moreresult.reports.append("신용점수 상승 전략 진입 : *PASS*")
            print("신용점수 상승 전략 진입 : PASS")
        except TimeoutError:
            logging.info("신용점수 상승 전략 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("신용점수 상승 전략 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('신용점수상승전략진입_fail')
            print("신용점수 상승 전략 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"신용점수 상승 전략 진입 에러 발생 : {e}")
            moreresult.reports.append("신용점수 상승 전략 진입 : *Error*")
            base.save_screenshot('신용점수상승전략진입_error')
            print(f"신용점수 상승 전략 진입 에러 발생 : {e}")
        # more.credit_Analysis_Back()
        base.android_back()
        logging.info("신용점수 상승 전략 진입 테스트 종료")

    # 신용관리 > 신용점수 히스토리 진입 테스트
    def test_credit_history(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("신용관리 > 신용점수 히스토리 진입 테스트 시작")
        more.credit_history()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_history_Result))
            logging.info("신용점수 히스토리 진입 : PASS")
            moreresult.reports.append("신용점수 히스트리 진입 : *PASS*")
            print("신용점수 히스토리 진입 : PASS")
        except TimeoutError:
            logging.info("신용점수 히스트리 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("신용점수 히스트리 진입_요소 확인필요 : *FAIL")
            base.save_screenshot('신용점수히스트리진입_fail')
            print("신용점수 히스트리 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"신용점수 히스트리 진입 에러 발생 : {e}")
            moreresult.reports.append("신용점수 히스트리 진입 : *Error*")
            base.save_screenshot('신용점수히스트리진입_error')
            print(f"신용점수 히스트리 진입 에러 발생 : {e}")
        # more.credit_History_Back()
        base.android_back()
        logging.info("신용관리 > 신용점수 히스토리 진입 테스트 종료")

    # 개인사업자 신용관리 진입 테스트
    def test_private_business_credit_management(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("개인사업자 신용관리 진입 테스트 시작")
        time.sleep(1)
        more.private_business_credit_management()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_score_Result))
            logging.info("개인사업자 신용관리 진입 : PASS")
            moreresult.reports.append("개인사업자 신용관리 진입 : *PASS*")
            print("개인사업자 신용관리 진입 : PASS")
        except TimeoutError:
            logging.info("개인사업자 신용관리 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("개인사업자 신용관리 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('개인사업자용관리진입_fail')
            print("개인사업자 신용관리 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"개인사업자 신용관리 진입 에러 발생 : {e}")
            moreresult.reports.append("개인사업자 신용관리 진입 : *Error*")
            base.save_screenshot('개인사업자용관리진입_error')
            print(f"개인사업자 신용관리 진입 에러 발생 : {e}")
        try:
            more.credit_score_back()
        except:
            base.android_back()
        logging.info("개인사업자 신용관리 진입 테스트 종료")

    # 신용퀴즈 어워즈 진입 테스트
    def test_credit_quiz_awards(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("신용퀴즈 어워즈 진입 테스트 시작")
        more.credit_quiz_awards()
        time.sleep(10)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.credit_quiz_awards_result))
            logging.info("신용퀴즈 어워즈 진입 : PASS")
            moreresult.reports.append("신용퀴즈 어워즈 진입 : *PASS*")
            print("신용퀴즈 어워즈 진입 : PASS")
        except TimeoutError:
            logging.info("신용퀴즈 어워즈 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("신용퀴즈 어워즈 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('신용퀴즈어워즈진입_fail')
            print("신용퀴즈 어워즈 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"신용퀴즈 어워즈 진입 에러 발생 : {e}")
            moreresult.reports.append("신용퀴즈 어워즈 진입 : *Error*")
            base.save_screenshot('신용퀴즈어워즈진입_error')
            print(f"신용퀴즈 어워즈 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("신용퀴즈 어워즈 진입 테스트 종료")

    # 연체 기록 삭제하기 진입 테스트
    def test_delete_delinquent_records(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("연체 기록 삭제하기 진입 테스트 시작")
        more.delete_delinquent_records()
        time.sleep(10)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.delete_delinquent_records_result))
            logging.info("연체 기록 삭제하기 진입 : PASS")
            moreresult.reports.append("연체 기록 삭제하기 진입 : *PASS*")
            print("연체 기록 삭제하기 진입 : PASS")
        except TimeoutError:
            logging.info("연체 기록 삭제하기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("연체 기록 삭제하기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('연체 기록 삭제하기진입_fail')
            print("연체 기록 삭제하기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"연체 기록 삭제하기 진입 에러 발생 : {e}")
            moreresult.reports.append("연체 기록 삭제하기 진입 : *Error*")
            base.save_screenshot('연체 기록 삭제하기진입_error')
            print(f"연체 기록 삭제하기 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("연체 기록 삭제하기 진입 테스트 종료")

    # 계산기 > 여윳돈 계산기 진입 테스트
    def test_extra_money(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 여윳돈 계산기 진입 테스트 시작")
        more.extra_money()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.extra_money_Result))
            logging.info("여윳돈 계산기 진입 : PASS")
            moreresult.reports.append("여윳돈 계산기 진입 : *PASS*")
            print("여윳돈 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("여윳돈 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("여윳돈 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('여윳돈계산기진입_fail')
            print("여윳돈 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"여윳돈 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("여윳돈 계산기 진입 : *Error*")
            base.save_screenshot('여윳돈계산기진입_error')
            print(f"여윳돈 계산기 진입 에러 발생 : {e}")
        try:
            more.extra_money_back()
        except:
            base.android_back()
        logging.info("계산기 > 여윳돈 계산기 진입 테스트 종료")

    # 계산기 > DSR 계산기 진입 테스트
    def test_dsr(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > DSR 계산기 진입 테스트 시작")
        more.dsr()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.dsr_Result))
            logging.info("DSR 계산기 진입 : PASS")
            moreresult.reports.append("DSR 계산기 진입 : *PASS*")
            print("DSR 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("DSR 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("DSR 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('DSR계산기진입_fail')
            print("DSR 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"DSR 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("DSR 계산기 진입 : *Error*")
            base.save_screenshot('DSR계산기진입_error')
            print(f"DSR 계산기 진입 에러 발생 : {e}")
        try:
            more.dsr_back()
        except:
            base.android_back()
        logging.info("계산기 > DSR 계산기 진입 테스트 종료")

    # 계산기 > 대출이자 계산기 진입 테스트
    def test_interest(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 대출이자 계산기 진입 테스트 시작")
        more.interest()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.interest_Result))
            logging.info("대출이자 계산기 진입 : PASS")
            moreresult.reports.append("대출이자 계산기 진입 : *PASS*")
            print("대출이자 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("대출이자 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("대출이자 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('대출이자계산기진입_fail')
            print("대출이자 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"대출이자 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("대출이자 계산기 진입 : *Error*")
            base.save_screenshot('대출이자계산기진입_error')
            print(f"대출이자 계산기 진입 에러 발생 : {e}")
        try:
            more.interest_back()
        except:
            base.android_back()
        logging.info("계산기 > 대출이자 계산기 진입 테스트 종료")

    def test_get_myownhouse(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 내 집 마련 대출한도 계산기 진입 테스트 시작")
        more.get_myownhouse()
        more.get_myownhouse_next()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.get_myownhouse_result))
            logging.info("계산기 > 내 집 마련 대출한도 계산기 : PASS")
            moreresult.reports.append("계산기 > 내 집 마련 대출한도 계산기 : *PASS*")
            print("계산기 > 내 집 마련 대출한도 계산기 : PASS")
        except TimeoutError:
            logging.info("계산기 > 내 집 마련 대출한도 계산기_요소 확인필요 : FAIL")
            moreresult.reports.append("계산기 > 내 집 마련 대출한도 계산기_요소 확인필요 : *FAIL*")
            base.save_screenshot('계산기 > 내 집 마련 대출한도 계산기_fail')
            print("계산기 > 내 집 마련 대출한도 계산기_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"계산기 > 내 집 마련 대출한도 계산기 에러 발생 : {e}")
            moreresult.reports.append("계산기 > 내 집 마련 대출한도 계산기 : *Error*")
            base.save_screenshot('계산기 > 내 집 마련 대출한도 계산기_error')
            print(f"계산기 > 내 집 마련 대출한도 계산기 에러 발생 : {e}")
        base.android_back()
        base.android_back()
        logging.info("계산기 > 내 집 마련 대출한도 계산기 진입 테스트 종료")

    # 계산기 > 연말정산 계산기 진입 테스트
    def test_year_end_settlement(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 연말정산 계산기 진입 테스트 시작")
        more.year_end_settlement()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.year_end_settlement_Result))
            logging.info("연말정산 계산기 진입 : PASS")
            moreresult.reports.append("연말정산 계산기 진입 : *PASS*")
            print("연말정산 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("연말정산 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("연말정산 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('연말정산계산기진입_fail')
            print("연말정산 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"연말정산 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("연말정산 계산기 진입 : *Error*")
            base.save_screenshot('연말정산계산기진입_error')
            print(f"연말정산 계산기 진입 에러 발생 : {e}")
        try:
            more.year_end_settlement_back()
        except:
            base.android_back()
        logging.info("계산기 > 연말정산 계산기 진입 테스트 종료")

    # 계산기 > 전세 vs 월세 계산기 진입 테스트
    def test_charter_vs_monthly_rent(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 전세 vs 월세 계산기 진입 테스트 시작")
        more.charter_vs_monthly_rent()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.charter_vs_monthly_rent_Result))
            logging.info("전세 vs 월세 계산기 진입 : PASS")
            moreresult.reports.append("전세 vs 월세 계산기 진입 : *PASS*")
            print("전세 vs 월세 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("전세 vs 월세 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("전세 vs 월세 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('전세vs월세계산기진입_fail')
            print("전세 vs 월세 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"전세 vs 월세 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("전세 vs 월세 계산기 진입 : *Error*")
            base.save_screenshot('전세vs월세계산기진입_error')
            print(f"전세 vs 월세 계산기 진입 에러 발생 : {e}")
        try:
            more.charter_vs_monthly_rent_back()
        except:
            base.android_back()
        logging.info("계산기 > 전세 vs 월세 계산기 진입 테스트 종료")

    # 계산기 > 대출 갈아타기 계산기 진입 테스트
    def test_refinancing_loan_calculate(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("계산기 > 대출 갈아타기 계산기 진입 테스트 시작")
        more.refinancing_loan()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.refinancing_loan_Result))
            logging.info("대출 갈아타기 계산기 진입 : PASS")
            moreresult.reports.append("대출 갈아타기 계산기 진입 : *PASS*")
            print("대출 갈아타기 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("대출 갈아타기 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("대출 갈아타기 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('대출갈아타기계산기진입_fail')
            print("대출 갈아타기 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"대출 갈아타기 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("대출 갈아타기 계산기 진입 : *Error*")
            base.save_screenshot('대출갈아타기계산기진입_error')
            print(f"대출 갈아타기 계산기 진입 에러 발생 : {e}")
        try:
            more.refinancing_loan_back()
        except:
            base.android_back()
        logging.info("계산기 > 대출 갈아타기 계산기 진입 테스트 종료")

    # 청년도약계좌 계산기 진입 테스트
    def test_youth_leap_account(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("청년도약계좌 계산기 진입 테스트 시작")
        more.youth_leap_account()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.youth_leap_account_result))
            logging.info("청년도약계좌 계산기 진입 : PASS")
            moreresult.reports.append("청년도약계좌 계산기 진입 : *PASS*")
            print("청년도약계좌 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("청년도약계좌 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("청년도약계좌 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('청년도약계좌계산기진입_fail')
            print("청년도약계좌 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"청년도약계좌 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("청년도약계좌 계산기 진입 : *Error*")
            base.save_screenshot('청년도약계좌계산기진입_error')
            print(f"청년도약계좌 계산기 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("청년도약계좌 계산기 진입 테스트 종료")

    # 자동차 할부 계산기 진입 테스트
    def test_car_installment_calculator(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("자동차 할부 계산기 진입 테스트 시작")
        more.car_installment_calculator()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.car_installment_calculator_result))
            logging.info("자동차 할부 계산기 진입 : PASS")
            moreresult.reports.append("자동차 할부 계산기 진입 : *PASS*")
            print("자동차 할부 계산기 진입 : PASS")
        except TimeoutError:
            logging.info("자동차 할부 계산기 진입_요소 확인필요 : FAIL")
            moreresult.reports.append("자동차 할부 계산기 진입_요소 확인필요 : *FAIL*")
            base.save_screenshot('자동차할부계산기진입_fail')
            print("자동차 할부 계산기 진입_요소 확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"자동차 할부 계산기 진입 에러 발생 : {e}")
            moreresult.reports.append("자동차 할부 계산기 진입 : *Error*")
            base.save_screenshot('자동차할부계산기진입_error')
            print(f"자동차 할부 계산기 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("자동차 할부 계산기 진입 테스트 종료")
#
# class MoreTestcase_C(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         logging.info("더보기 테스트_C 시작")
#
#     @classmethod
#     def tearDownClass(cls):
#         logging.info("더보기 테스트_C 종료")
#
#     def setUp(self):
#         base = basemethod()
#
#     def tearDown(self):
#         base = basemethod()
#         more = More()
#         base.android_back()
#         base.android_back()
#         time.sleep(1)
#         more.etc_in()
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)
#         base.scroll_up(0.8)

    # 장기렌트 리스 진입 테스트
    def test_lease_rent(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("장기렌트 리스 진입 테스트 시작")
        more.lease_rent()
        time.sleep(3)
        base.save_screenshot('장기렌트리스진입_스크린샷')
        logging.info("장기렌트 리스 진입 : 스크린샷으로 검증 대체")
        moreresult.reports.append("장기렌트 리스 진입 : *스크린샷으로 검증 대체*")
        print("장기렌트 리스 진입 : 스크린샷으로 검증 대체")
        base.android_back()
        logging.info("장기렌트 리스 진입 테스트 종료")

    # 두낫콜 약관 리스트 진입 테스트
    def test_do_not_call_terms_of_use(self):
        more = More()
        etc = Etc()
        base = basemethod()
        logging.info("두낫콜 약관 리스트 진입 테스트 시작")
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
                             ("[금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)", etc.do_not_call_c_b)]
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
            logging.info("두낫콜 약관 노출 : PASS")
            moreresult.reports.append("두낫콜 약관 노출 : *PASS*")
        else:
            logging.info("두낫콜 약관 노출 : FAIL")
            moreresult.reports.append("두낫콜 약관 노출 : *FAIL*")
            base.save_screenshot('두낫콜약관노출_fail')

        more.terms_of_use_aa()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_a_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Aa_요소확인필요_fail')
            print("두낫콜약관진입_Aa_요소 확인필요_fail")
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Aa_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_ab()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_a_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ab_요소 확인필요_fail')
            print("두낫콜약관진입_Ab_요소 확인필요_fail")
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ab_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_ac()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_a_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ac_요소확인필요_fail')
            print('두낫콜약관진입_Ac_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ac_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_ba()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_b_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ba_요소확인필요_fail')
            print('두낫콜약관진입_Ba_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ba_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_bb()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_b_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bb_요소확인필요_fail')
            print('두낫콜약관진입_Bb_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bb_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_bc()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_b_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bc_요소확인필요_fail')
            print('두낫콜약관진입_Bc_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bc_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_bd()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_b_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Bd_요소확인필요_fail')
            print('두낫콜약관진입_Bd_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Bd_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_ca()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_c_a_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Ca_요소확인필요_fail')
            print('두낫콜약관진입_Ca_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Ca_error')
        more.terms_of_use_webview_exit()
        more.terms_of_use_cb()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_c_b_Result))
            results.append("PASS")
        except TimeoutError:
            results.append("FAIL")
            base.save_screenshot('두낫콜약관진입_Cb_요소확인필요_fail')
            print('두낫콜약관진입_Cb_요소확인필요_fail')
        except Exception:
            results.append("Error")
            base.save_screenshot('두낫콜약관진입_Cb_error')
        more.terms_of_use_webview_exit()
        # more.terms_of_use_cc()
        # try:
        #     WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.do_not_call_c_c_Result))
        #     results.append("PASS")
        # except TimeoutError:
        #     results.append("FAIL")
        #     base.save_screenshot('두낫콜약관진입_Cc_요소확인필요_fail')
        #     print('두낫콜약관진입_Cc_요소확인필요_fail')
        # except Exception:
        #     results.append("Error")
        #     base.save_screenshot('두낫콜약관진입_Cc_error')
        # more.terms_of_use_webview_exit()
        logging.info(results)
        if all(result == "PASS" for result in results):
            logging.info("두낫콜 약관 페이지 진입 노출 : PASS")
            moreresult.reports.append("두낫콜 약관 페이지 진입 노출 : *PASS*")
            print("두낫콜 약관 페이지 진입 노출 : PASS")
        else:
            logging.info("두낫콜 약관 페이지 진입 노출 : FAIL")
            moreresult.reports.append("두낫콜 약관 페이지 진입 노출 : *FAIL*")
            print("두낫콜 약관 페이지 진입 노출 : FAIL")
        more.do_not_call_back()
        logging.info("두낫콜 약관 리스트 진입 테스트 종료")

    # 대출금 갚아주는 보험 진입 테스트
    def test_insurance(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("대출금 갚아주는 보험 진입 테스트 시작")
        more.insurance()
        time.sleep(2)
        more.insurance_web()
        time.sleep(15)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.insurance_Result))
            logging.info("대출금 갚아주는 보험 진입 : PASS")
            moreresult.reports.append("대출금 갚아주는 보험 진입 : *PASS*")
            print("대출금 갚아주는 보험 진입 : PASS")
        except TimeoutError:
            logging.info("대출금 갚아주는 보험 진입_요소확인필요 : FAIL")
            moreresult.reports.append("대출금 갚아주는 보험 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('대출금갚아주는보험진입_fail')
            print("대출금 갚아주는 보험 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"대출금 갚아주는 보험 진입 에러 발생 : {e}")
            moreresult.reports.append("대출금 갚아주는 보험 진입 : *Error*")
            base.save_screenshot('대출금갚아주는보험진입_error')
            print(f"대출금 갚아주는 보험 진입 에러 발생 : {e}")
        base.android_back()
        base.android_back()
        logging.info("대출금 갚아주는 보험 진입 테스트 종료")

    # 예적금 비교 진입 테스트
    def test_deposit_and_savings(self):
        more = More()
        etc = Etc()
        moreresult = Result_More()
        base = basemethod()
        logging.info("예적금 비교 진입 테스트 시작")
        more.deposit_and_savings()
        time.sleep(10)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.deposit_and_savings_Result))
            logging.info("예적금 비교 진입 : PASS")
            moreresult.reports.append("예적금 비교 진입 : *PASS*")
            print("예적금 비교 진입 : PASS")
        except TimeoutError:
            logging.info("예적금 비교 진입_요소확인필요 : FAIL")
            moreresult.reports.append("예적금 비교 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('예적금비교진입_fail')
            print("예적금 비교 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"예적금 비교 진입 에러 발생 : {e}")
            moreresult.reports.append("예적금 비교 진입 : *Error*")
            base.save_screenshot('예적금비교진입_error')
            print(f"예적금 비교 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("예적금 비교 진입 테스트 종료")

    # 핀다 포스트 진입 테스트
    def test_finda_post(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("핀다 포스트 진입 테스트 시작")
        more.finda_post()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.finda_post_Result))
            logging.info("핀다 포스트 진입 : PASS")
            moreresult.reports.append("핀다 포스트 진입 : *PASS*")
            print("핀다 포스트 진입 : PASS")
        except TimeoutError:
            logging.info("핀다 포스트 진입_요소확인필요 : FAIL")
            moreresult.reports.append("핀다 포스트 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('핀다포스트진입_fail')
            print("핀다 포스트 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"핀다 포스트 진입 에러 발생 : {e}")
            moreresult.reports.append("핀다 포스트 진입 : *Error*")
            base.save_screenshot('핀다포스트진입_error')
            print(f"핀다 포스트 진입 에러 발생 : {e}")
        try:
            more.finda_post_back()
        except:
            base.android_back()
        logging.info("핀다 포스트 진입 테스트 종료")

    # 내 폰 지키미 진입 테스트
    def test_my_phorn(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("내 폰 지키미 진입 테스트 시작")
        more.my_phorn()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.my_phorn_Result))
            logging.info("내 폰 지키미 진입 : PASS")
            moreresult.reports.append("내 폰 지키미 진입 : *PASS*")
            print("내 폰 지키미 진입 : PASS")
        except TimeoutError:
            logging.info("내 폰 지키미 진입_요소확인필요 : FAIL")
            moreresult.reports.append("내 폰 지키미 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('내폰지키미진입_fail')
            print("내 폰 지키미 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"내 폰 지키미 진입 에러 발생 : {e}")
            moreresult.reports.append("내 폰 지키미 진입 : *Error*")
            base.save_screenshot('내폰지키미진입_error')
            print(f"내 폰 지키미 진입 에러 발생 : {e}")
        try:
            more.my_phorn_back()
        except:
            base.android_back()
        logging.info("내 폰 지키미 진입 테스트 종료")

    # 이벤트 진입 테스트
    def test_event(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("이벤트 진입 테스트 시작")
        more.event()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.event_Result))
            logging.info("돈되는 혜택 진입 : PASS")
            moreresult.reports.append("돈되는 혜택 진입 : *PASS*")
            print("돈되는 혜택 진입 : PASS")
        except TimeoutError:
            logging.info("돈되는 혜택 진입_요소확인필요 : FAIL")
            moreresult.reports.append("돈되는 혜택 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('돈되는혜택진입_fail')
            print("돈되는 혜택 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"돈되는 혜택 진입 에러 발생 : {e}")
            moreresult.reports.append("돈되는 혜택 진입 : *Error*")
            base.save_screenshot('돈되는혜택진입_error')
            print(f"돈되는 혜택 진입 에러 발생 : {e}")
        try:
            more.event_back()
        except:
            base.android_back()
        logging.info("이벤트 진입 테스트 종료")

    # 공지사항 진입 테스트
    def test_notice(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("공지사항 진입 테스트 시작")
        more.notice()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.notice_Result))
            logging.info("공지사항 진입 : PASS")
            moreresult.reports.append("공지사항 진입 : *PASS*")
            print("공지사항 진입 : PASS")
        except TimeoutError:
            logging.info("공지사항 진입_요소확인필요 : FAIL")
            moreresult.reports.append("공지사항 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('공지사항진입_fail')
            print("공지사항 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"공지사항 진입 에러 발생 : {e}")
            moreresult.reports.append("공지사항 진입 : *Error*")
            base.save_screenshot('공지사항진입_error')
            print(f"공지사항 진입 에러 발생 : {e}")
        time.sleep(2)
        more.notice_in()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.notice_in_Result))
            logging.info("공지사항 상세 진입 : PASS")
            moreresult.reports.append("공지사항 상세 진입 : *PASS*")
            print("공지사항 상세 진입 : PASS")
        except TimeoutError:
            logging.info("공지사항 상세 진입_요소확인필요 : FAIL")
            moreresult.reports.append("공지사항 상세 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('공지사항상세진입_fail')
            print("공지사항 상세 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"공지사항 상세 진입 에러 발생 : {e}")
            moreresult.reports.append("공지사항 상세 진입 : *Error*")
            base.save_screenshot('공지사항상세진입_error')
            print(f"공지사항 상세 진입 에러 발생 : {e}")
        more.notice_in_back()
        more.notice_back()
        logging.info("공지사항 진입 테스트 종료")

    # 대출 후기 진입 테스트
    def test_loan_reviews(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("대출 후기 진입 테스트 시작")
        more.loan_reviews()
        time.sleep(5)
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.loan_reviews_Result))
            logging.info("대출 후기 진입 : PASS")
            moreresult.reports.append("대출 후기 진입 : *PASS*")
            print("대출 후기 진입 : PASS")
        except TimeoutError:
            logging.info("대출 후기 진입_요소확인필요 : FAIL")
            moreresult.reports.append("대출 후기 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('대출후기진입_fail')
            print("대출 후기 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"대출 후기 진입 에러 발생 : {e}")
            moreresult.reports.append("대출 후기 진입 : *Error*")
            base.save_screenshot('대출후기진입_error')
            print(f"대출 후기 진입 에러 발생 : {e}")
        try:
            more.loan_reviews_back()
        except:
            base.android_back()
        logging.info("대출 후기 진입 테스트 종료")

    # 최근 알림 진입 테스트
    def test_alarm(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("최근 알림 진입 테스트 시작")
        more.alarm()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.alarm_Result))
            logging.info("최근 알림 진입 : PASS")
            moreresult.reports.append("최근 알림 진입 : *PASS*")
            print("최근 알림 진입 : PASS")
        except TimeoutError:
            logging.info("최근 알림 진입_요소확인필요 : FAIL")
            moreresult.reports.append("최근 알림 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('최근알림진입_fail')
            print("최근 알림 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"최근 알림 진입 에러 발생 : {e}")
            moreresult.reports.append("최근 알림 진입 : *Error*")
            base.save_screenshot('최근알림진입_error')
            print(f"최근 알림 진입 에러 발생 : {e}")
        more.alarm_back()
        logging.info("최근 알림 진입 테스트 종료")

    # 포인트 진입 테스트
    def test_point(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("포인트 진입 테스트 시작")
        more.point()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.point))
            logging.info("포인트 진입 : PASS")
            moreresult.reports.append("포인트 진입 : *PASS*")
            print("포인트 진입 : PASS")
        except TimeoutError:
            logging.info("포인트 진입_요소확인필요 : FAIL")
            moreresult.reports.append("포인트 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('포인트진입_fail')
            print("포인트 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"포인트 진입 에러 발생 : {e}")
            moreresult.reports.append("포인트 진입 : *Error*")
            base.save_screenshot('포인트진입_error')
            print(f"포인트 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("포인트 진입 테스트 종료")

    # 출석체크 진입 테스트
    def test_checkin(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("출석체크 진입 테스트 시작")
        more.checkin()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.checkin))
            logging.info("출석체크 진입 : PASS")
            moreresult.reports.append("출석체크 진입 : *PASS*")
            print("출석체크 진입 : PASS")
        except TimeoutError:
            logging.info("출석체크 진입_요소확인필요 : FAIL")
            moreresult.reports.append("출석체크 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('출석체크진입_fail')
            print("출석체크 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"출석체크 진입 에러 발생 : {e}")
            moreresult.reports.append("출석체크 진입 : *Error*")
            base.save_screenshot('출석체크진입_error')
            print(f"출석체크 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("출석체크 진입 테스트 종료")

    # 물가예측 시즌1 테스트
    def test_price_forecast_season_1(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("물가예측 시즌 1 진입 테스트 시작")
        more.priceforecast()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.priceforecast_result))
            logging.info("물가예측 시즌1 진입 : PASS")
            moreresult.reports.append("물가예측 시즌1 진입 : *PASS*")
            print("물가예측 시즌1 진입 : PASS")
        except TimeoutError:
            logging.info("물가예측 시즌1 진입_요소확인필요 : FAIL")
            moreresult.reports.append("물가예측 시즌1 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('물가예측시즌1진입_fail')
            print("물가예측 시즌1 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"물가예측 시즌1 진입 에러 발생 : {e}")
            moreresult.reports.append("물가예측 시즌1 진입 : *Error*")
            base.save_screenshot('물가예측 시즌1진입_error')
            print(f"물가예측 시즌1 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("물가예측 시즌1 진입 테스트 종료")

    # 물가예측 참여내역 테스트
    def test_priceforecast_history(self):
        more = More()
        etc = Etc()
        base = basemethod()
        moreresult = Result_More()
        logging.info("물가예측 참여내역 진입 테스트 시작")
        more.priceforecast_history()
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(etc.priceforecast_history_result))
            logging.info("물가예측 참여내역 진입 : PASS")
            moreresult.reports.append("물가예측 참여내역 진입 : *PASS*")
            print("물가예측 참여내역 진입 : PASS")
        except TimeoutError:
            logging.info("물가예측 참여내역 진입_요소확인필요 : FAIL")
            moreresult.reports.append("물가예측 참여내역 진입_요소확인필요 : *FAIL*")
            base.save_screenshot('물가예측참여내역진입_fail')
            print("물가예측 참여내역 진입_요소확인필요 : FAIL")
        except Exception as e:
            logging.warning(f"물가예측 참여내역 진입 에러 발생 : {e}")
            moreresult.reports.append("물가예측 참여내역 진입 : *Error*")
            base.save_screenshot('물가예측 참여내역진입_error')
            print(f"물가예측 참여내역 진입 에러 발생 : {e}")
        base.android_back()
        logging.info("물가예측 참여내역 진입 테스트 종료")

if __name__ == '__main__':
    unittest.main()