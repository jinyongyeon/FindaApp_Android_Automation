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
        suite.addTest(MyHome_Testcase('test_credit_score'))
        suite.addTest(MyHome_Testcase('test_myhome_myloan'))
        suite.addTest(MyHome_Testcase('test_financial_life_in'))
        unittest.TextTestRunner().run(suite)
        result_myhome = '\n\n'.join(str(i) for i in resultmyhome.reports)
        print(result_myhome)
        print(SlackWebHook.my_home_send_slack_webhook(result_myhome))

    def testmore(self):
        resultmore = Result_More()
        suite = unittest.TestSuite()
        suite.addTest(MoreTestcase_A('test_check_more_tab'))
        suite.addTest(MoreTestcase_A('test_myloan_in'))
        suite.addTest(MoreTestcase_A('test_chat_ting'))
        suite.addTest(MoreTestcase_A('test_qna'))
        suite.addTest(MoreTestcase_A('test_refinancing_loan'))
        suite.addTest(MoreTestcase_A('test_comparison_loan'))
        suite.addTest(MoreTestcase_A('test_auto_loan'))
        suite.addTest(MoreTestcase_A('test_charter'))
        # suite.addTest(MoreTestcase_A('test_change_loan'))    # 대환 첼린지 삭제됨
        suite.addTest(MoreTestcase_A('test_my_loan_b'))
        suite.addTest(MoreTestcase_A('test_amortization_schedule'))
        suite.addTest(MoreTestcase_A('test_electronic_wallet'))
        suite.addTest(MoreTestcase_A('test_credit_score'))
        suite.addTest(MoreTestcase_A('test_improve_credit_score'))
        suite.addTest(MoreTestcase_A('test_credit_analysis'))
        suite.addTest(MoreTestcase_A('test_credit_history'))
        suite.addTest(MoreTestcase_A('test_private_business_credit_management'))
        # suite.addTest(MoreTestcase_A('test_credit_quiz_awards'))    # 핀다퀴즈 삭제됨
        # suite.addTest(MoreTestcase_A('test_delete_delinquent_records')) # 연체 기록 삭제하기 삭제됨
        suite.addTest(MoreTestcase_A('test_extra_money'))
        suite.addTest(MoreTestcase_A('test_dsr'))
        suite.addTest(MoreTestcase_A('test_interest'))
        suite.addTest(MoreTestcase_A('test_year_end_settlement'))
        suite.addTest(MoreTestcase_A('test_charter_vs_monthly_rent'))
        suite.addTest(MoreTestcase_A('test_refinancing_loan_calculate'))
        suite.addTest(MoreTestcase_A('test_youth_leap_account'))
        suite.addTest(MoreTestcase_A('test_car_installment_calculator'))
        suite.addTest(MoreTestcase_A('test_lease_rent'))
        suite.addTest(MoreTestcase_A('test_do_not_call_terms_of_use'))
        suite.addTest(MoreTestcase_A('test_insurance'))
        suite.addTest(MoreTestcase_A('test_deposit_and_savings'))
        suite.addTest(MoreTestcase_A('test_finda_post'))
        suite.addTest(MoreTestcase_A('test_my_phorn'))
        suite.addTest(MoreTestcase_A('test_notice'))
        suite.addTest(MoreTestcase_A('test_alarm'))
        suite.addTest(MoreTestcase_A('test_point'))
        suite.addTest(MoreTestcase_A('test_checkin'))
        # suite.addTest(MoreTestcase_A('test_price_forecast_season_1'))     # 물가예측 시즌1 삭제됨
        suite.addTest(MoreTestcase_A('test_priceforecast_history'))
        # suite.addTest(MoreTestcase_A('test_event'))     # 이벤트 삭제됨
        suite.addTest(MoreTestcase_A('test_loan_reviews'))
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
        # suite.addTest(JoinTestCase('test_message_certification'))
        # suite.addTest(JoinTestCase('test_membership_terms_and_conditions'))
        # suite.addTest(JoinTestCase('test_certification_number'))
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
    # test.testmyhome() # 코드 개선완료
    # test.testautoloan()
    test.testmore() # 코드 개선완료
    test.testseting() # 코드개선 완료
    test.testjoin() # 코드개선 완료
    # test.testloan()
