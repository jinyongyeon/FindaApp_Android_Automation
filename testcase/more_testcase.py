import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc
from pages.basemethod.result import Result_More
from testscript.more_testscript.see_more import More
from pages.basemethod.base import basemethod



class MoreTestcase_A(unittest.TestCase):

    # 더보기 진입 테스트
    def test_Check_More_Tab(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        moreresult = Result_More()
        more.etcIn()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.etc_Result)
            self.assertEqual(Result.text, "더보기")
            print("더보기 탭 진입 : PASS")
            moreresult.reports.append("더보기 탭 진입 : *PASS*")
        except AssertionError:
            print("더보기 탭 진입 : FAIL")
            moreresult.reports.append("더보기 탭 진입 : *FAIL*")
            WebDriver.tearDown()
        except :
            pass

    # 내대출 진입 테스트
    def test_Myloan_In(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        more.myLoan()
        morereports = Result_More()
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
            except:
                pass

        print(results)
        if all(result == "PASS" for result in results):
            print("내 대출 진입 : PASS")
            morereports.reports.append("내 대출 진입 : *PASS*")
        else:
            print("내 대출 진입 : FAIL")
            morereports.reports.append("내 대출 진입 : *FAIL*")
        more.myLoanBack()

    # 채팅문의 진입 테스트
    def test_ChatTing(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        more.chatTing()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.chatting_Result)
            self.assertIn("채널톡 이용중",Result.text)
            print("채널톡 진입 : PASS")
            morereports.reports.append("채널톡 진입 : *PASS*")
        except AssertionError:
            print("채널톡 진입 : FAIL")
            morereports.reports.append("채널톡 진입 : *FAIL*")
            WebDriver.tearDown()
        except :
            pass
        more.chatTingExit()

    # 자주묻는 질문 진입 및 상세 페이지 노출 테스트
    def test_Qna(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        more.qnA()
        morereports = Result_More()
        results = []
        verification_list = [("정말 이 조건 그대로 대출 가능한가요?", etc.qna_a),
                             ("신청하면 대출금은 언제 입금이 되나요?", etc.qna_b),
                             ("대출 조건은 언제까지 유효한가요?", etc.qna_c),
                             ("대출을 알아보는 것으로, 불이익이 있나요?", etc.qna_d),
                             ("신용조회가 여러 건 발생했다고 하는데 무슨 일인가요?", etc.qna_e)]
        for text, xpath in verification_list:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, xpath)
                self.assertIn(text, Result.text)
                results.append("PASS")
            except AssertionError:
                results.append("FAIL")
            except:
                pass
        print(results)
        if all(result == "PASS" for result in results):
            print("자주 묻는 질문 진입 : PASS")
            morereports.reports.append("자주 묻는 질문 진입 : *PASS*")
        else:
            print("자주 묻는 질문 진입 : FAIL")
            morereports.reports.append("자주 묻는 질문 진입 : *FAIL*")

        more.qna_Click_A()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_Result_a)
            self.assertIn("네, 가능합니다. 고객님께서 입력해주신 정보의 정확도 등에 따라 금융사 최종심사에 일부 차이가 발생할 수 있지만, 정확한 정보 입력 후 공동인증서를 연동하여 조회하셨다면 실제 심사결과에 부합하는 조건을 받아보실 수 있습니다.",Result_A.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            pass
        more.qna_Click_B()
        try:
            Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_Result_b)
            self.assertIn("대출이 확정된 후 대출금이 입금되기까지는 금융사마다 차이가 존재합니다. 빠르게 처리가 이루어지는 경우 입금까지 5분이내에 입금이 이루어지며, 고객과의 전화통화 이후 대출이 진행되는 경우에는 몇 시간에서 1~2영업일 가량 소요되기도 합니다. 일반적으로는 금융사의 영업일/영업시간 내에만 입금이 진행되지만, 주말/공휴일을 포함하여 24시간 대출금 입금이 가능한 금융사 또한 존재합니다.",Result_B.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            pass
        more.qna_Click_C()
        try:
            Result_C = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_Result_c)
            self.assertIn("조회하신 대출 조건은 조회 당일 자정까지만 유효하며, 다음날 조회 시 조건이 달라질 수 있습니다. 매일 조금씩 조건이 달라지는만큼, 대출이 필요한 시기에 맞춰 한도조회를 다시 진행해 주시면 가장 정확한 조건을 확인하실 수 있습니다.",Result_C.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            pass
        more.qna_Click_D()
        try:
            Result_D = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_Result_d)
            self.assertIn("대출조회는 신용점수에 전혀 영향을 미치지 않습니다. 2011년 10월, 금융위원회는 대출조회가 신용점수에 불이익을 주지 않도록 정책을 변경하였습니다. 또한, 핀다는 단 1건의 신용조회로 60개 이상 금융사의 금융상품 중 고객님께 맞는 상품을 안내해 드리고 있으니 걱정없이 대출상품을 알아 볼 수 있습니다. * 단, 단기간 너무 많은 조회를 할 경우 ‘대출사기’로 의심되어 대출이 거절될 수 있습니다. * 핀다를 통한 한도조회는 주 2~3회가 적합합니다.",Result_D.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            pass
        more.qna_Click_E()
        try:
            Result_E = WebDriver.driver.find_element(MobileBy.XPATH, etc.qna_Result_e)
            self.assertIn("걱정하지 마세요. 핀다에서는 여러 금융사의 상품을 조회해도, 단 1건의 신용조회로 처리됩니다. 신용평가회사에 따라 내역 조회 시, 여러 건으로 표기가 되기도 하지만 실제 신용조회기록에 반영되는 것은 ‘핀다’ 플랫폼 코드 1건만이 반영됩니다. 또한, 신용조회는 신용점수에 영향을 주지 않으니 안심하고 핀다를 이용하세요!",Result_E.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except :
            pass
        print(results)
        if all(result == "PASS" for result in results):
            print("자주 묻는 질문 상세 항목 노출 : PASS")
            morereports.reports.append("자주 묻는 질문 상세 항목 노출 : *PASS*")
        else:
            print("자주 묻는 질문 상세 항목 노출 : FAIL")
            morereports.reports.append("자주 묻는 질문 상세 항목 노출 : *FAIL*")
        more.qna_Click_E()
        more.qnaBack()

    # 대출 갈아타기 사전신청 테스트
    def test_Refinancing_Loan_Advance_Application(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.refinancing_Loan_Advance_Application()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_advance_application_Result_a)
            self.assertEqual(Result_A.text,"출시되면 알림 받기")
            print("대출 갈아타기 사전신청 진입 : PASS")
            morereports.reports.append("대출 갈아타기 사전신청 진입 : *PASS*")
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_advance_application_Result_b)
                self.assertEqual(Result_B.text,"사전신청 완료")
                print("대출 갈아타기 사전신청 진입 : PASS")
                morereports.reports.append("대출 갈아타기 사전신청 진입 : *PASS*")
            except AssertionError:
                print("대출 갈아타기 사전신청 진입 : FAIL")
                morereports.reports.append("대출 갈아타기 사전신청 진입 : *FAIL*")
                WebDriver.tearDown()
            except:
                try:
                    Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_advance_application_Result_a)
                    self.assertEqual(Result_A.text, "출시되면 알림 받기")
                    print("대출 갈아타기 사전신청 진입 : PASS")
                    morereports.reports.append("대출 갈아타기 사전신청 진입 : *PASS*")
                except Exception:
                    try:
                        Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_advance_application_Result_b)
                        self.assertEqual(Result_B.text, "사전신청 완료")
                        print("대출 갈아타기 사전신청 진입 : PASS")
                        morereports.reports.append("대출 갈아타기 사전신청 진입 : *PASS*")
                    except AssertionError:
                        print("대출 갈아타기 사전신청 진입 : FAIL")
                        morereports.reports.append("대출 갈아타기 사전신청 진입 : *FAIL*")
                        WebDriver.tearDown()
                    # except:
                    #     pass
                except NoSuchElementException:
                    try:
                        Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_advance_application_Result_b)
                        self.assertEqual(Result_B.text, "사전신청 완료")
                        print("대출 갈아타기 사전신청 진입 : PASS")
                        morereports.reports.append("대출 갈아타기 사전신청 진입 : *PASS*")
                    except AssertionError:
                        print("대출 갈아타기 사전신청 진입 : FAIL")
                        morereports.reports.append("대출 갈아타기 사전신청 진입 : *FAIL*")
                        WebDriver.tearDown()
                except AssertionError:
                    print("대출 갈아타기 사전신청 진입 : FAIL")
                    morereports.reports.append("대출 갈아타기 사전신청 진입 : *FAIL*")
                    WebDriver.tearDown()

        try:
            base.android_Back()
        except:
            base.android_Back()

    # 대출 한 번에 비교 진입 테스트
    def test_ComPariSonLoan(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.comPariSonLoan()

        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_a)
            self.assertEqual(Result_A.text,"오늘의 내 최저금리 알아보기")
            print("대출 한 번에 비교 진입 : PASS")
            morereports.reports.append("대출 한 번에 비교 진입 : *PASS*")
        except AssertionError:
            print("대출 한 번에 비교 진입 : FAIL")
            morereports.reports.append("대출 한 번에 비교 진입 : *FAIL*")
        except :
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.comparison_loan_Result_b)
                self.assertIn("오늘입금" , Result_B.text)
                print("대출 한 번에 비교 진입 : PASS")
                morereports.reports.append("대출 한 번에 비교 진입 : *PASS*")
            except AssertionError:
                print("대출 한 번에 비교 진입 : FAIL")
                morereports.reports.append("대출 한 번에 비교 진입 : *FAIL*")
            except Exception as e:
                print("대출 한 번에 비교 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("대출 한 번에 비교 진입 : *Error*")

        base.android_Back()

    # 자동차 구매 대출 진입 테스트
    def test_AutoLoan(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        info = InFo()
        base = basemethod()
        morereports = Result_More()
        more.autoLoan()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_a)
            self.assertEqual(Result_A.text,"1분만에 내 한도 알아보기")
            print("자동차 구매 대출 진입 : PASS")
            morereports.reports.append("자동차 구매 대출 진입 : *PASS*")
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.auto_loan_Result_b)
                self.assertIn(''+info.name+'님의\n가장 좋은 대출 조건이에요.', Result_B.text)
                print("자동차 구매 대출 진입 : PASS")
                morereports.reports.append("자동차 구매 대출 진입 : *PASS*")
            except AssertionError:
                print("자동차 구매 대출 진입 : FAIL")
                morereports.reports.append("자동차 구매 대출 진입 : *FAIL*")
            except Exception as e :
                print("자동차 구매 대출 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("자동차 구매 대출 진입 진입 : *Error*")
        except AssertionError:
            print("자동차 구매 대출 진입 : FAIL")
            morereports.reports.append("자동차 구매 대출 진입 : *FAIL*")

        base.android_Back()

    # 전월세 추천 진입 테스트
    def test_CharTer(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.charTer()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_Result_a)
            self.assertEqual(Result_A.text,"전월세대출 맞춤추천")
            print("전월세 추천 진입 : PASS")
            morereports.reports.append("전월세 추천 진입 : *PASS*")
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_Result_b)
                self.assertEqual(Result_B.text,"1:1 맞춤형 전월세대출 가이드")
                print("전월세 추천 진입 : PASS")
                morereports.reports.append("전월세 추천 진입 : *PASS*")
            except AssertionError:
                print("전월세 추천 진입 : FAIL")
                morereports.reports.append("전월세 추천 진입 : *FAIL*")
                WebDriver.tearDown()
            # except:
            #     pass
        except NoSuchElementException:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_Result_b)
                self.assertEqual(Result_B.text, "1:1 맞춤형 전월세대출 가이드")
                print("전월세 추천 진입 : PASS")
                morereports.reports.append("전월세 추천 진입 : *PASS*")
            except AssertionError:
                print("전월세 추천 진입 : FAIL")
                morereports.reports.append("전월세 추천 진입 : *FAIL*")
                WebDriver.tearDown()
        except AssertionError:
            print("전월세 추천 진입 : FAIL")
            morereports.reports.append("전월세 추천 진입 : *FAIL*")
            WebDriver.tearDown()

        try:
            more.charTerBack()
        except:
            base.android_Back()

    # 30일 대출 챌린지 진입 테스트
    def test_Change_Loan(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.change_Loan()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.change_loan_Result_a)
            self.assertEqual(Result_A.text,"매주 한도조회하면 내 레벨도 함께 높아져요")
            print("30일 대출 챌린지 진입 : PASS")
            morereports.reports.append("30일 대출 챌린지 진입 : *PASS*")
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.change_loan_Result_b)
                self.assertEqual(Result_B.text,"30일 대환 챌린지 Beta")
                print("30일 대출 챌린지 진입 : PASS")
                morereports.reports.append("30일 대출 챌린지 진입 : *PASS*")
            except AssertionError:
                print("30일 대출 챌린지 진입 : FAIL")
                morereports.reports.append("30일 대출 챌린지 진입 : *FAIL*")
                WebDriver.tearDown()
            # except:
            #     pass
        except NoSuchElementException:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.change_loan_Result_b)
                self.assertEqual(Result_B.text, "30일 대환 챌린지 Beta")
                print("30일 대출 챌린지 진입 : PASS")
                morereports.reports.append("30일 대출 챌린지 진입 : *PASS*")
            except AssertionError:
                print("30일 대출 챌린지 진입 : FAIL")
                morereports.reports.append("30일 대출 챌린지 진입 : *FAIL*")
                WebDriver.tearDown()
        except AssertionError:
            print("30일 대출 챌린지 진입 : FAIL")
            morereports.reports.append("30일 대출 챌린지 진입 : *FAIL*")
            WebDriver.tearDown()
        try:
            more.change_Loan_Back()
        except:
            base.android_Back()

    # 내대출_B 진입 테스트
    def test_Myloan_B(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        more.myLoan_B()
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
                WebDriver.tearDown()
            except:
                pass

        print(results)
        if all(result == "PASS" for result in results):
            print("내 대출_B 진입 : PASS")
            morereports.reports.append("내 대출_B 진입 : *PASS*")
        else:
            print("내 대출_B 진입 : FAIL")
            morereports.reports.append("내 대출_B 진입 : *FAIL*")
        # try:
        #     Result_a = driver.find_element(MobileBy.XPATH, etc.myloan_Result_a)
        # except:
        #     results.append("FAIL")
        # else:
        #     if Result_a.text == "내 현금흐름":
        #         results.append("PASS")
        #     else:
        #         results.append("FAIL")
        #
        # try:
        #     Result_b = driver.find_element(MobileBy.XPATH, etc.myloan_Result_b)
        # except:
        #     results.append("FAIL")
        # else:
        #     if Result_b.text == "대출":
        #         results.append("PASS")
        #     else:
        #         results.append("FAIL")
        #
        # try:
        #     Result_c = driver.find_element(MobileBy.XPATH, etc.myloan_Result_c)
        # except:
        #     results.append("FAIL")
        # else:
        #     if Result_c.text == "입출금":
        #         results.append("PASS")
        #     else:
        #         results.append("FAIL")
        #
        # try:
        #     Result_d = driver.find_element(MobileBy.XPATH, etc.myloan_Result_d)
        # except:
        #     results.append("FAIL")
        # else:
        #     if Result_d.text == "예적금":
        #         results.append("PASS")
        #     else:
        #         results.append("FAIL")
        #
        # if "FAIL" not in results:
        #     print("내 대출 진입 : PASS")
        # else:
        #     print("내 대출 진입 : FAIL")
        more.myLoanBack()

    # 상환일정 진입 테스트
    def test_Amortization_Schedule(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        base = basemethod()
        base.scroll(0.1)
        time.sleep(2)
        more.amortization_Schedule()
        try:
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.amortization_schedule_a)
            self.assertEqual(Result_A.text,"이번달 총 상환액")
            print("상환일정 진입 : PASS")
            morereports.reports.append("상환일정 진입 : *PASS*")
        except Exception:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.amortization_schedule_b)
                self.assertEqual(Result_B.text,"상환 일정이 없습니다.")
                print("상환일정 진입 : PASS")
                morereports.reports.append("상환일정 진입 : *PASS*")
            except AssertionError:
                print("상환일정 진입 : FAIL")
                morereports.reports.append("상환일정 진입 : *FAIL*")
                WebDriver.tearDown()
            # except:
            #     pass
        except NoSuchElementException:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.amortization_schedule_b)
                self.assertEqual(Result_B.text, "상환 일정이 없습니다.")
                print("상환일정 진입 : PASS")
                morereports.reports.append("상환일정 진입 : *PASS*")
            except AssertionError:
                print("상환일정 진입 : FAIL")
                morereports.reports.append("상환일정 진입 : *FAIL*")
                WebDriver.tearDown()
        except AssertionError:
            print("상환일정 진입 : FAIL")
            morereports.reports.append("상환일정 진입 : *FAIL*")
            WebDriver.tearDown()
        more.amortization_Schedule_back()


class MoreTestcase_B(unittest.TestCase):


    # 신용점수 진입 테스트
    def test_Credit_Score(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        base = basemethod()
        base.scroll(0.93)
        time.sleep(1)

        try:
            more.credit_Score()
            time.sleep(10)
            print("신용점수 진입 : PASS")
            morereports.reports.append("신용점수 진입 : *PASS*")
        except :
            print("신용점수 진입 : FAIL")
            morereports.reports.append("신용점수 진입 : *FAIL*")


        # try:
        #     Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_score_Result)
        #     self.assertEqual("내 신용점수", Result.text)
        #     print("신용점수 진입 : PASS")
        #     morereports.reports.append("신용점수 진입 : *PASS*")
        # except AssertionError:
        #     print("신용점수 진입 : FAIL")
        #     morereports.reports.append("신용점수 진입 : *FAIL*")
        # except Exception as e:
        #     print("신용점수 진입 에러 발생 : {}".format(str(e)))
        #     morereports.reports.append("신용점수 진입 : *Error*")

        try:
            more.credit_Score_Back()
        except:
            base.android_Back()


    # 신용점수 올리기 진입 테스트
    def test_Improve_Credit_Score(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.improve_Credit_Score()
        time.sleep(10)
        try:
            # Result_A = driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_a)
            Result_A = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_a)
            self.assertEqual(Result_A.text,"신용점수 올리고\n대출이자 낮춰봐요")
            print("신용점수 올리기 진입 : PASS")
            morereports.reports.append("신용점수 올리기 진입 : *PASS*")
        except Exception:
            try:
                # Result_A = driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_a)
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_b)
                self.assertEqual(Result_B.text, "최근 6개월내 신용점수 올리기를\n이용했어요")
                print("신용점수 올리기 진입 : PASS")
                morereports.reports.append("신용점수 올리기 진입 : *PASS*")
            except AssertionError:
                print("신용점수 올리기 진입 : FAIL")
                morereports.reports.append("신용점수 올리기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("신용점수 올리기 진입 에러 발생_1 : {}".format(str(e)))
                morereports.reports.append("신용점수 올리기 진입 : *Error*")
            # except:
            #     pass
        except NoSuchElementException:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_b)
                self.assertEqual(Result_B.text, "최근 6개월내 신용점수 올리기를\n이용했어요")
                print("신용점수 올리기 진입입 : PASS")
                morereports.reports.append("신용점수 올리기 진입 : *PASS*")
            except AssertionError:
                print("신용점수 올리기 진입 : FAIL")
                morereports.reports.append("신용점수 올리기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("신용점수 올리기 진입 에러 발생_2 : {}".format(str(e)))
                morereports.reports.append("신용점수 올리기 진입 : *Error*2")
        except AssertionError:
            try:
                Result_B = WebDriver.driver.find_element(MobileBy.XPATH, etc.improve_credit_score_Result_b)
                self.assertEqual(Result_B.text, "최근 6개월내 신용점수 올리기를\n이용했어요")
                print("신용점수 올리기 진입입 : PASS")
                morereports.reports.append("신용점수 올리기 진입 : *PASS*")
            except AssertionError:
                print("신용점수 올리기 진입 : FAIL")
                morereports.reports.append("신용점수 올리기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("신용점수 올리기 진입 에러 발생_3 : {}".format(str(e)))
                morereports.reports.append("신용점수 올리기 진입 : *Error*3")
        # more.improve_Credit_Score_Back()
        base.android_Back()

    # 신용점수 상승 전략 진입 테스트
    def test_Credit_Analysis(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.credit_Analysis()
        time.sleep(10)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_analysis_Result)
            self.assertEqual(Result.text, "신용점수 상승 전략")
            print("신용점수 상승 전략 진입 : PASS")
            morereports.reports.append("신용점수 상승 전략 진입 : *PASS*")
        except AssertionError:
            print("신용점수 상승 전략 진입 : FAIL")
            morereports.reports.append("신용점수 상승 전략 진입 : *FAIL*")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_analysis_Result)
                self.assertEqual(Result.text, "신용점수 상승 전략")
                print("신용점수 상승 전략 진입 : PASS")
                morereports.reports.append("신용점수 상승 전략 진입 : *PASS*")
            except AssertionError:
                print("신용점수 상승 전략 진입 : FAIL")
                morereports.reports.append("신용점수 상승 전략 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("신용점수 상승 전략 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("신용점수 상승 전략 진입 : *Error*")
                WebDriver.tearDown()
        # more.credit_Analysis_Back()
        base.android_Back()

    # 신용관리 > 신용점수 히스트리 진입 테스트
    def test_Credit_History(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        # appview = driver.contexts[0]
        # webview = driver.contexts[1]
        more.credit_History()
        time.sleep(10)
        # driver.switch_to.context(webview)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_history_Result)
            self.assertEqual(Result.text, "신용점수 히스토리")
            print("신용점수 히스트리 진입 : PASS")
            morereports.reports.append("신용점수 히스트리 진입 : *PASS*")
        except AssertionError:
            print("신용점수 히스트리 진입 : FAIL")
            morereports.reports.append("신용점수 히스트리 진입 : *FAIL")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.credit_history_Result)
                self.assertEqual(Result.text, "신용점수 히스토리")
                print("신용점수 히스트리 진입 : PASS")
                morereports.reports.append("신용점수 히스트리 진입 : *PASS*")
            except AssertionError:
                print("신용점수 히스트리 진입 : FAIL")
                morereports.reports.append("신용점수 히스트리 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("신용점수 히스트리 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("신용점수 히스트리 진입 : *Error*")
        # more.credit_History_Back()
        # driver.switch_to.context(appview)
        base.android_Back()

    # 계산기 > 여윳돈 계산기 진입 테스트
    def test_Extra_Money(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.extra_Money()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.extra_money_Result)
            self.assertEqual(Result.text, "상환할 여윳돈이 생기셨나요?")
            print("여윳돈 계산기 진입 : PASS")
            morereports.reports.append("여윳돈 계산기 진입 : *PASS*")
        except AssertionError:
            print("여윳돈 계산기 진입 : FAIL")
            morereports.reports.append("여윳돈 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.extra_money_Result)
                self.assertEqual(Result.text, "상환할 여윳돈이 생기셨나요?")
                print("여윳돈 계산기 진입 : PASS")
                morereports.reports.append("여윳돈 계산기 진입 : *PASS*")
            except AssertionError:
                print("여윳돈 계산기 진입 : FAIL")
                morereports.reports.append("여윳돈 계산기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("여윳돈 계산기 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("여윳돈 계산기 진입 : *Error*")

        try:
            more.extra_Money_Back()
        except:
            base.android_Back()

    # 계산기 > DSR 계산기 진입 테스트
    def test_Dsr(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.dsR()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.dsr_Result)
            self.assertEqual(Result.text, "DSR 계산기")
            print("DSR 계산기 진입 : PASS")
            morereports.reports.append("DSR 계산기 진입 : *PASS*")
        except AssertionError:
            print("DSR 계산기 진입 : FAIL")
            morereports.reports.append("DSR 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.dsr_Result)
                self.assertEqual(Result.text, "DSR 계산기")
                print("DSR 계산기 진입 : PASS")
                morereports.reports.append("DSR 계산기 진입 : *PASS*")
            except AssertionError:
                print("DSR 계산기 진입 : FAIL")
                morereports.reports.append("DSR 계산기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("DSR 계산기 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("DSR 계산기 진입 : *Error*")
        try:
            more.dsr_Back()
        except:
            base.android_Back()

    # 계산기 > 대출이자 계산기 진입 테스트
    def test_Interest(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.interest()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.interest_Result)
            self.assertEqual(Result.text, "대출이자 계산기")
            print("대출이자 계산기 진입 : PASS")
            morereports.reports.append("대출이자 계산기 진입 : *PASS*")
        except AssertionError:
            print("대출이자 계산기 진입 : FAIL")
            morereports.reports.append("대출이자 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.interest_Result)
                self.assertEqual(Result.text, "대출이자 계산기")
                print("대출이자 계산기 진입 : PASS")
                morereports.reports.append("대출이자 계산기 진입 : *PASS*")
            except AssertionError:
                print("대출이자 계산기 진입 : FAIL")
                morereports.reports.append("대출이자 계산기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("대출이자 계산기 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("대출이자 계산기 진입 : *Error*")
        try:
            more.interest_Back()
        except:
            base.android_Back()

    # 계산기 > 연말정산 계산기 진입 테스트
    def test_Year_End_Settlement(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.year_End_Settlement()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.year_end_settlement_Result)
            self.assertEqual(Result.text, "카드 및 현금 소비액 소득공제")
            print("연말정산 계산기 진입 : PASS")
            morereports.reports.append("연말정산 계산기 진입 : *PASS*")
        except AssertionError:
            print("연말정산 계산기 진입 : FAIL")
            morereports.reports.append("연말정산 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.year_end_settlement_Result)
                self.assertEqual(Result.text, "카드 및 현금 소비액 소득공제")
                print("연말정산 계산기 진입 : PASS")
                morereports.reports.append("연말정산 계산기 진입 : *PASS*")
            except AssertionError:
                print("연말정산 계산기 진입 : FAIL")
                morereports.reports.append("연말정산 계산기 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("연말정산 계산기 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("연말정산 계산기 진입 : *Error*")
                WebDriver.tearDown()

        try:
            more.year_End_Settlement_Back()
        except:
            base.android_Back()

    # 계산기 > 전세 vs 월세 계산기 진입 테스트
    def test_Charter_Vs_Monthly_Rent(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.charter_Vs_Monthly_Rent()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.charter_vs_monthly_rent_Result)
            self.assertEqual(Result.text, "전세 vs 월세 계산기")
            print("전세 vs 월세 계산기 진입 : PASS")
            morereports.reports.append("전세 vs 월세 계산기 진입 : *PASS*")
        except AssertionError:
            print("전세 vs 월세 계산기 진입 : FAIL")
            morereports.reports.append("전세 vs 월세 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except Exception as e:
            print("전세 vs 월세 계산기 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("전세 vs 월세 계산기 진입 : *Error*")
        except :
            WebDriver.tearDown()
        try:
            more.charter_Vs_Monthly_Rent_Back()
        except:
            base.android_Back()

    # 계산기 > 대출 갈아타기 계산기 진입 테스트
    def test_Refinancing_Loan(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.refinancing_Loan()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.refinancing_loan_Result)
            self.assertIn("대출 갈아타기 계산기" , Result.text)
            print("대출 갈아타기 계산기 진입 : PASS")
            morereports.reports.append("대출 갈아타기 계산기 진입 : *PASS*")
        except AssertionError:
            print("대출 갈아타기 계산기 진입 : FAIL")
            morereports.reports.append("대출 갈아타기 계산기 진입 : *FAIL*")
            WebDriver.tearDown()
        except Exception as e:
            print("대출 갈아타기 계산기 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("대출 갈아타기 계산기 진입 : *Error*")
        except:
            WebDriver.tearDown()
        try:
            more.refinancing_Loan_Back()
        except:
            base.android_Back()

class MoreTestcase_C(unittest.TestCase):

    # 장기렌트 리스 진입 테스트
    def test_Lease_Rent(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        base = basemethod()
        base.scroll(0.93)
        time.sleep(1)
        more.lease_Rent()
        time.sleep(10)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.lease_rent_Result)
            self.assertEqual(Result.text, "리스렌트")
            print("장기렌트 리스 진입 : PASS")
            morereports.reports.append("장기렌트 리스 진입 : *PASS*")
        except AssertionError:
            print("장기렌트 리스 진입 : FAIL")
            morereports.reports.append("장기렌트 리스 진입 : *FAIL*")
            WebDriver.tearDown()
        except Exception as e:
            print("장기렌트 리스 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("장기렌트 리스 진입 : *Error*")

        base.android_Back()

    # 두낫콜 약관 리스트 진입 테스트
    def test_Do_Not_Call_Terms_Of_Use(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        more.do_Not_Call()
        more.do_Net_Call_Cta()
        more.terms_Of_Use_A()
        more.terms_Of_Use_B()
        more.terms_Of_Use_C()
        morereports = Result_More()
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
                results.append("FAIL")
                WebDriver.tearDown()

        print(results)
        if all(result == "PASS" for result in results):
            print("두낫콜 약관 노출 : PASS")
            morereports.reports.append("두낫콜 약관 노출 : *PASS*")
        else:
            print("두낫콜 약관 노출 : FAIL")
            morereports.reports.append("두낫콜 약관 노출 : *FAIL*")

        more.terms_Of_Use_Aa()
        try:
            Result_a_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_a.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Ab()
        try:
            Result_a_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_b.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Ac()
        try:
            Result_a_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_a_Result)
            self.assertIn("두낫콜 본인확인",Result_a_c.text)
            results.append("PASS")
        except AssertionError:
            results.append("FAIL")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Ba()
        try:
            Result_b_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_a.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Bb()
        try:
            Result_b_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_b.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Bc()
        try:
            Result_b_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_c.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Bd()
        try:
            Result_b_d = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_b_Result)
            self.assertIn("사이트에 연결할 수 없음",Result_b_d.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Ca()
        try:
            Result_c_a = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_a.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Cb()
        try:
            Result_c_b = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_b.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        more.terms_Of_Use_Cc()
        try:
            Result_c_c = WebDriver.driver.find_element(MobileBy.XPATH, etc.do_not_call_c_Result)
            self.assertIn("페이지를 찾을 수 없습니다",Result_c_c.text)
            results.append("FAIL")
        except AssertionError:
            results.append("PASS")
        except Exception:
            results.append("PASS")
        more.terms_Of_Use_Webview_Exit()

        print(results)
        if all(result == "PASS" for result in results):
            print("두낫콜 약관 페이지 진입 노출 : PASS")
            morereports.reports.append("두낫콜 약관 페이지 진입 노출 : *PASS*")
        else:
            print("두낫콜 약관 페이지 진입 노출 : FAIL")
            morereports.reports.append("두낫콜 약관 페이지 진입 노출 : *FAIL*")
        more.do_Not_Call_Back()

    # 대출금 갚아주는 보험 진입 테스트
    def test_Insurance(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.insurance()
        time.sleep(15)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.insurance_Result)
            self.assertEqual(Result.text,"BNP파리바 카디프생명")
            print("대출금 갚아주는 보험 진입 : PASS")
            morereports.reports.append("대출금 갚아주는 보험 진입 : *PASS*")
        except AssertionError:
            print("대출금 갚아주는 보험 진입 : FAIL")
            morereports.reports.append("대출금 갚아주는 보험 진입 : *FAIL*")
            WebDriver.tearDown()
        except :
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.insurance_Result)
                self.assertEqual(Result.text, "BNP파리바 카디프생명")
                print("대출금 갚아주는 보험 진입 : PASS")
                morereports.reports.append("대출금 갚아주는 보험 진입 : *PASS*")
            except AssertionError:
                print("대출금 갚아주는 보험 진입 : FAIL")
                morereports.reports.append("대출금 갚아주는 보험 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("대출금 갚아주는 보험 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("대출금 갚아주는 보험 진입 : *Error*")
                WebDriver.tearDown()
        base.android_Back()

    # 예적금 비교 진입 테스트
    def test_Deposit_And_Savings(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        base = basemethod()
        more.deposit_And_Savings()
        time.sleep(10)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.deposit_and_savings_Result)
            self.assertEqual(Result.text,"예적금 비교")
            print("예적금 비교 진입 : PASS")
            morereports.reports.append("예적금 비교 진입 : *PASS*")
        except AssertionError:
            print("예적금 비교 진입 : FAIL")
            morereports.reports.append("예적금 비교 진입 : *FAIL*")
        except:
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.deposit_and_savings_Result)
                self.assertEqual(Result.text, "예적금 비교")
                print("예적금 비교 진입 : PASS")
                morereports.reports.append("예적금 비교 진입 : *PASS*")
            except AssertionError:
                print("예적금 비교 진입 : FAIL")
                morereports.reports.append("예적금 비교 진입 : *FAIL*")
                WebDriver.tearDown()
            except Exception as e:
                print("예적금 비교 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("예적금 비교 진입 : *Error*")
                WebDriver.tearDown()
        base.android_Back()


    # 핀다 포스트 진입 테스트
    def test_Finda_Post(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.finda_Post()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.finda_post_Result)
            self.assertEqual(Result.text,"핀다포스트")
            print("핀다 포스트 진입 : PASS")
            morereports.reports.append("핀다 포스트 진입 : *PASS*")
        except AssertionError:
            print("핀다 포스트 진입 : FAIL")
            morereports.reports.append("핀다 포스트 진입 : *FAIL*")
        except :
            try:
                Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.finda_post_Result)
                self.assertEqual(Result.text, "핀다포스트")
                print("핀다 포스트 진입 : PASS")
                morereports.reports.append("핀다 포스트 진입 : *PASS*")
            except AssertionError:
                print("핀다 포스트 진입 : FAIL")
                morereports.reports.append("핀다 포스트 진입 : *FAIL*")
            except Exception as e:
                print("핀다 포스트 진입 에러 발생 : {}".format(str(e)))
                morereports.reports.append("핀다 포스트 진입 : *Error*")

        try:
            more.finda_Post_Back()
        except:
            base.android_Back()


    # 내 폰 지키미 진입 테스트
    def test_My_Phorn(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.my_Phorn()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.my_phorn_Result)
            self.assertEqual(Result.text,"내 폰 보호하기")
            print("내 폰 지키미 진입 : PASS")
            morereports.reports.append("내 폰 지키미 진입 : *PASS*")
        except AssertionError:
            print("내 폰 지키미 진입 : FAIL")
            morereports.reports.append("내 폰 지키미 진입 : *FAIL*")
        except Exception as e:
            print("내 폰 지키미 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("내 폰 지키미 진입 : *Error*")
        except :
            WebDriver.tearDown()

        try:
            more.my_Phorn_Back()
        except:
            base.android_Back()

    # 이벤트 진입 테스트
    def test_Event(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        base = basemethod()
        morereports = Result_More()
        more.event()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.event_Result)
            self.assertEqual(Result.text,"진행 중인 이벤트")
            print("이벤트 진입 : PASS")
            morereports.reports.append("이벤트 진입 : *PASS*")
        except AssertionError:
            print("이벤트 진입 : FAIL")
            morereports.reports.append("이벤트 진입 : *FAIL*")
        except Exception as e:
            print("이벤트 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("이벤트 진입 : *Error*")
        except :
            WebDriver.tearDown()
        try:
            more.event_Back()
        except:
            base.android_Back()

    # 공지사항 진입 테스트
    def test_Notice(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        more.notice()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.notice_Result)
            self.assertEqual(Result.text,"공지사항")
            print("공지사항 진입 : PASS")
            morereports.reports.append("공지사항 진입 : *PASS*")
        except AssertionError:
            print("공지사항 진입 : FAIL")
            morereports.reports.append("공지사항 진입 : *FAIL*")
        except Exception as e:
            print("공지사항 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("공지사항 진입 : *Error*")
        except :
            WebDriver.tearDown()
        time.sleep(2)

        more.notice_In()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.notice_in_Result)
            self.assertEqual(Result.text,"안녕하세요 핀다입니다.")
            print("공지사항 상세 진입 : PASS")
            morereports.reports.append("공지사항 상세 진입 : *PASS*")
        except AssertionError:
            print("공지사항 상세 진입 : FAIL")
            morereports.reports.append("공지사항 상세 진입 : *FAIL*")
        except Exception as e:
            print("공지사항 상세 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("공지사항 상세 진입 : *Error*")
        except :
            WebDriver.tearDown()
        more.notice_In_Back()
        more.notice_Back()

    # 대출 후기 진입 테스트
    def test_loan_Reviews(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        more.loan_Reviews()
        time.sleep(15)
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.loan_reviews_Result)
            self.assertIn("핀다 신용대출 신청 서비스로\n대출받으신 고객님들의 후기입니다.", Result.text)
            print("대출 후기 진입 : PASS")
            morereports.reports.append("대출 후기 진입 : *PASS*")
        except AssertionError:
            print("대출 후기 진입 : FAIL")
            morereports.reports.append("대출 후기 진입 : *FAIL*")
            WebDriver.tearDown()
        except Exception as e:
            print("대출 후기 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("대출 후기 진입 : *Error*")
            WebDriver.tearDown()
        except :
            WebDriver.tearDown()
        more.loan_Reviews_Back()

    # 최근 알림 진입 테스트
    def test_Alarm(self):
        driver = WebDriver.setUp()
        more = More()
        etc = Etc()
        morereports = Result_More()
        more.alarm()
        try:
            Result = WebDriver.driver.find_element(MobileBy.XPATH, etc.alarm_Result)
            self.assertEqual(Result.text,"최근 알림")
            print("최근 알림 진입 : PASS")
            morereports.reports.append("최근 알림 진입 : *PASS*")
        except AssertionError:
            print("최근 알림 진입 : FAIL")
            morereports.reports.append("최근 알림 진입 : *FAIL*")
            WebDriver.tearDown()
        except Exception as e:
            print("최근 알림 진입 에러 발생 : {}".format(str(e)))
            morereports.reports.append("최근 알림 진입 : *Error*")
            WebDriver.tearDown()
        except :
            WebDriver.tearDown()
        more.alarm_Back()


if __name__ == '__main__':
    unittest.main()