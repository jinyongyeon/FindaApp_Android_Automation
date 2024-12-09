from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan, Result_seting
from pages.basemethod.slackreports import SlackWebHook
import unittest
import logging
import datetime
from testcase.testcase_loan import AutoLoanTestcase, LoanComparisonTestcase
from testcase.testcase_login import LoginTestCase, JoinTestCase
from testcase.testcase_more import MoreTestcase_A
from testcase.testcase_myhome import MyHome_Testcase
from testcase.testcase_seting import Seting_Testcase


class test:

    def testmyhome(self):
        resultmyhome = Result_MyHome()
        suite = unittest.TestSuite()
        suite.addTest(LoginTestCase('test_check_in'))
        suite.addTest(MyHome_Testcase('test_myhome_menu'))
        suite.addTest(MyHome_Testcase('test_financial_life_in'))
        suite.addTest(MyHome_Testcase('test_myhome_repayment_schedule'))
        suite.addTest(MyHome_Testcase('test_myhome_cash'))
        suite.addTest(MyHome_Testcase('test_myhome_card'))
        suite.addTest(MyHome_Testcase('test_credit_score'))
        unittest.TextTestRunner().run(suite)
        result_myhome = '\n\n'.join(str(i) for i in resultmyhome.reports)
        print(result_myhome)
        print(SlackWebHook.my_home_send_slack_webhook(result_myhome))

    def testmore(self):
        resultmore = Result_More()
        suite = unittest.TestSuite()
        suite.addTest(MoreTestcase_A('test_check_more_tab'))  # 더보기 진입
        suite.addTest(MoreTestcase_A('test_myloan_in'))  # 내 대출 진입
        suite.addTest(MoreTestcase_A('test_chat_ting'))  # 1:1채팅문의 진입
        suite.addTest(MoreTestcase_A('test_qna'))  # 자주 묻는 질문 진입
        suite.addTest(MoreTestcase_A('test_refinancing_loan')) # 대출 갈아타기
        suite.addTest(MoreTestcase_A('test_comparison_loan')) # 대출 한번에 비교
        suite.addTest(MoreTestcase_A('test_auto_loan')) # 자동차 구매 대출
        suite.addTest(MoreTestcase_A('test_charter')) #전월세 추천
        suite.addTest(MoreTestcase_A('test_loan_reviews')) # 대출 후기
        # suite.addTest(MoreTestcase_A('test_change_loan'))    # 대환 첼린지 삭제됨

        suite.addTest(MoreTestcase_A('test_business_loan')) # 사업자대출
        suite.addTest(MoreTestcase_A('test_KB_loan')) # KB사장님+
        suite.addTest(MoreTestcase_A('test_private_business_credit_management')) # 개인사업자 신용관리
        suite.addTest(MoreTestcase_A('test_analyze_commercial_area')) # 상권분석서비스

        suite.addTest(MoreTestcase_A('test_my_loan_b')) # 내 자산
        suite.addTest(MoreTestcase_A('test_amortization_schedule')) # 상환 일정
        suite.addTest(MoreTestcase_A('test_electronic_wallet')) # # 정부 전자지갑
        suite.addTest(MoreTestcase_A('test_credit_score')) # 신용점수
        suite.addTest(MoreTestcase_A('test_improve_credit_score')) # 신용점수 올리기
        suite.addTest(MoreTestcase_A('test_credit_analysis')) # #신용점수 상승 전략
        suite.addTest(MoreTestcase_A('test_credit_history')) # 신용점수 히스토리
        # suite.addTest(MoreTestcase_A('test_credit_quiz_awards'))    # 핀다퀴즈 삭제됨
        # suite.addTest(MoreTestcase_A('test_delete_delinquent_records')) # 연체 기록 삭제하기 삭제됨

        suite.addTest(MoreTestcase_A('test_extra_money')) #여윳돈 계산기
        suite.addTest(MoreTestcase_A('test_dsr')) # DSR계산기
        suite.addTest(MoreTestcase_A('test_interest')) # 대출이자 계산기
        suite.addTest(MoreTestcase_A('test_get_myownhouse')) # 내집 마련 계산기
        suite.addTest(MoreTestcase_A('test_year_end_settlement')) # 연말정산 계산기
        suite.addTest(MoreTestcase_A('test_charter_vs_monthly_rent')) # 전세 vs 월세 계산기
        suite.addTest(MoreTestcase_A('test_refinancing_loan_calculate')) # 대출 갈아타기 계산기
        suite.addTest(MoreTestcase_A('test_youth_leap_account')) # 청년도약계좌 계산기
        # suite.addTest(MoreTestcase_A('test_car_installment_calculator')) # 자동차 할부 계산기

        suite.addTest(MoreTestcase_A('test_lease_rent')) # 장기렌트 리스
        suite.addTest(MoreTestcase_A('test_do_not_call_terms_of_use')) #두낫콜
        suite.addTest(MoreTestcase_A('test_insurance')) # 대출금 갚아주는 보험
        suite.addTest(MoreTestcase_A('test_deposit_and_savings')) # 예적금 비교
        suite.addTest(MoreTestcase_A('test_finda_post')) #핀다 포스터
        suite.addTest(MoreTestcase_A('test_my_phorn')) # 내폰 지키미

        suite.addTest(MoreTestcase_A('test_notice')) # 공지사항
        suite.addTest(MoreTestcase_A('test_alarm')) # 최신 알림
        suite.addTest(MoreTestcase_A('test_point')) # 포인트
        suite.addTest(MoreTestcase_A('test_checkin')) # 출석체크
        # suite.addTest(MoreTestcase_A('test_price_forecast_season_1'))     # 물가예측 시즌1 삭제됨
        # suite.addTest(MoreTestcase_A('test_priceforecast_history')) # 물가예측 참여내역
        # suite.addTest(MoreTestcase_A('test_event'))     # 이벤트 삭제됨
        unittest.TextTestRunner().run(suite)
        result_more = '\n\n'.join(str(i) for i in resultmore.reports)
        print(result_more)
        print(SlackWebHook.more_send_slack_webhook(result_more))

    def testseting(self):
        resultseting = Result_seting()
        suite = unittest.TestSuite()
        suite.addTest(Seting_Testcase('test_my_info'))
        suite.addTest(Seting_Testcase('test_notification_settings'))
        suite.addTest(Seting_Testcase('test_change_password'))
        suite.addTest(Seting_Testcase('test_credit_information_history'))
        suite.addTest(Seting_Testcase('test_seting_mydata'))
        suite.addTest(Seting_Testcase('test_seting_terms_of_use'))
        suite.addTest(Seting_Testcase('test_seting_privacy_policy'))
        suite.addTest(Seting_Testcase('test_seting_mydata_service_terms_of_use'))
        suite.addTest(Seting_Testcase('test_financial_consumer_protection_notice'))
        suite.addTest(Seting_Testcase('test_seting_version'))
        suite.addTest(Seting_Testcase('test_open_source_license'))
        unittest.TextTestRunner().run(suite)
        result_set = '\n\n'.join(str(i) for i in resultseting.reports)
        print(result_set)
        print(SlackWebHook.seting_slack_webhook(result_set))

    def testjoin(self):
        resultjoin = Result_Join()
        suite = unittest.TestSuite()
        suite.addTest(LoginTestCase('test_log_out'))
        suite.addTest(JoinTestCase('test_message_certification'))
        # suite.addTest(JoinTestCase('test_membership_terms_and_conditions'))
        suite.addTest(JoinTestCase('test_certification_number'))
        suite.addTest(JoinTestCase('test_join'))
        suite.addTest(LoginTestCase('test_withdraw'))
        unittest.TextTestRunner().run(suite)
        result_join = '\n\n'.join(str(i) for i in resultjoin.reports)
        print(result_join)
        print(SlackWebHook.join_send_slack_webhook(result_join))

    def testautoloan(self):
        resultautoloan = Result_loan()
        suite = unittest.TestSuite()
        suite.addTest(AutoLoanTestcase('test_auto_loan_new'))
        suite.addTest(AutoLoanTestcase('test_auto_loan_detail'))
        suite.addTest(AutoLoanTestcase('test_auto_loan_application'))
        unittest.TextTestRunner().run(suite)
        result_auto_loan = '\n\n'.join(str(i) for i in resultautoloan.auto_reports)
        print(result_auto_loan)
        print(SlackWebHook.auto_loan_send_slack_webhook(result_auto_loan))

    def testloan(self):
        resultloan = Result_loan()
        suite = unittest.TestSuite()
        suite.addTest(LoanComparisonTestcase('test_loan_terms_and_conditions'))
        suite.addTest(LoanComparisonTestcase('test_loan_comparison_verification_code'))
        suite.addTest(LoanComparisonTestcase('test_rrn_validation_check'))
        suite.addTest(LoanComparisonTestcase('test_loan_comparison_apt_secured_loan'))
        suite.addTest(LoanComparisonTestcase('test_comparison_loan_detail'))
        # suite.addTest(LoanComparisonTestcase('test_comparison_loan_detail_certification')) # 웹뷰로 인하여 심의필 노출 테스트 불가능 메뉴얼로 대체
        suite.addTest(LoanComparisonTestcase('test_loan_application'))
        suite.addTest(LoanComparisonTestcase('test_office_worker_loan_no_certificate'))
        suite.addTest(LoanComparisonTestcase('test_carnomber'))
        suite.addTest(LoanComparisonTestcase('test_unemployed_loan'))
        suite.addTest(LoanComparisonTestcase('test_auto_loan_in'))
        unittest.TextTestRunner().run(suite)
        result_loan = '\n\n'.join(str(i) for i in resultloan.reports)
        print(result_loan)
        print(SlackWebHook.loan_send_slack_webhook(result_loan))

if __name__ == '__main__':
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.basicConfig(filename=f"apptestlog_{current_date}.log", level=logging.INFO)
    print(SlackWebHook.test_start_slack_webhook("AOS 자동화 테스트 시작\n"))
    logging.info("\n\n\n자동화 테스트 시작\n\n\n")
    test = test()
    test.testmyhome() # 코드 개선완료
    # test.testautoloan()
    test.testmore() # 코드 개선완료
    # test.testseting() # 수정 필요함
    # test.testjoin() # 코드개선 완료
    # test.testloan()


