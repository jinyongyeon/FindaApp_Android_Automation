# from multiprocessing import process
# import time
# import os
from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan, Result_seting
from pages.basemethod.slackreports import SlackWebHook
import unittest
import logging
import datetime
from testcase.testcase_loan import AutoLoanTestcase, LoanComparisonTestcase
from testcase.testcase_login import LoginTestCase, JoinTestCase
from testcase.testcase_more import MoreTestcase_A, MoreTestcase_B, MoreTestcase_C
from testcase.testcase_myhome import MyHome_Testcase
from testcase.testcase_seting import Seting_Testcase

# class appium:
#     def start_appium_server(self):
#         appium_command = "appium -a 127.0.0.1 -p 4723 -pa /wd/hub"
#         os.system(appium_command)
#         # appium_script_path = "/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/pages/basemethod/appiumrunner.py"
#         # os.system(f"/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/venv/bin/python {appium_script_path} &")
#
#     def kill_appium_server(self):
#         appium_command = "pkill -9 -f appium"
#         os.system(appium_command)

class test:

    def testsuite1(self):
        resultmyhome = Result_MyHome()
        suite = unittest.TestSuite()
        suite.addTest(LoginTestCase('test_check_in'))
        # Result_refinancing = Result_refinancing_loan()
        # Result_refinancing = '\n\n'.join(str(i) for i in Result_refinancing.reports)
        # print(SlackWebHook.refinancing_loan_send_slack_webhook(Result_refinancing))
        suite.addTest(MyHome_Testcase('test_comparison_loan'))
        suite.addTest(MyHome_Testcase('test_loan_diagnosis_banner'))
        suite.addTest(MyHome_Testcase('test_loan_banner'))
        suite.addTest(MyHome_Testcase('test_cash_assets_banner'))
        suite.addTest(MyHome_Testcase('test_repayment_schedule_banner'))
        suite.addTest(MyHome_Testcase('test_lease_contract_banner'))
        suite.addTest(MyHome_Testcase('test_auto_loan_banner'))
        unittest.TextTestRunner().run(suite)

        result_myhome = '\n\n'.join(str(i) for i in resultmyhome.reports)
        print(result_myhome)
        print(SlackWebHook.my_home_send_slack_webhook(result_myhome))

    def testsuite2(self):
        resultmore = Result_More()
        suite_a = unittest.TestSuite()
        suite_a.addTest(MoreTestcase_A('test_check_more_tab'))
        suite_a.addTest(MoreTestcase_A('test_myloan_in'))
        suite_a.addTest(MoreTestcase_A('test_chat_ting'))
        suite_a.addTest(MoreTestcase_A('test_qna'))
        suite_a.addTest(MoreTestcase_A('test_refinancing_loan'))
        suite_a.addTest(MoreTestcase_A('test_comparison_loan'))
        suite_a.addTest(MoreTestcase_A('test_auto_loan'))
        suite_a.addTest(MoreTestcase_A('test_charter'))
        suite_a.addTest(MoreTestcase_A('test_change_loan'))
        suite_a.addTest(MoreTestcase_A('test_my_loan_b'))
        suite_a.addTest(MoreTestcase_A('test_amortization_schedule'))
        suite_a.addTest(MoreTestcase_B('test_credit_score'))
        suite_a.addTest(MoreTestcase_B('test_improve_credit_score'))
        suite_a.addTest(MoreTestcase_B('test_credit_analysis'))
        suite_a.addTest(MoreTestcase_B('test_credit_history'))
        suite_a.addTest(MoreTestcase_B('test_private_business_credit_management'))
        suite_a.addTest(MoreTestcase_B('test_credit_quiz_awards'))
        suite_a.addTest(MoreTestcase_B('test_extra_money'))
        suite_a.addTest(MoreTestcase_B('test_dsr'))
        suite_a.addTest(MoreTestcase_B('test_interest'))
        suite_a.addTest(MoreTestcase_B('test_year_end_settlement'))
        suite_a.addTest(MoreTestcase_B('test_charter_vs_monthly_rent'))
        suite_a.addTest(MoreTestcase_B('test_refinancing_loan'))
        suite_a.addTest(MoreTestcase_B('test_youth_leap_account'))
        suite_a.addTest(MoreTestcase_B('test_car_installment_calculator'))
        suite_a.addTest(MoreTestcase_C('test_lease_rent'))
        suite_a.addTest(MoreTestcase_C('test_do_not_call_terms_of_use'))
        suite_a.addTest(MoreTestcase_C('test_insurance'))
        suite_a.addTest(MoreTestcase_C('test_deposit_and_savings'))
        suite_a.addTest(MoreTestcase_C('test_finda_post'))
        suite_a.addTest(MoreTestcase_C('test_my_phorn'))
        suite_a.addTest(MoreTestcase_C('test_event'))
        suite_a.addTest(MoreTestcase_C('test_notice'))
        suite_a.addTest(MoreTestcase_C('test_loan_reviews'))
        suite_a.addTest(MoreTestcase_C('test_alarm'))
        unittest.TextTestRunner().run(suite_a)

        result_more = '\n\n'.join(str(i) for i in resultmore.reports)
        print(result_more)
        print(SlackWebHook.more_send_slack_webhook(result_more))

    def testsuite3(self):
        resultseting = Result_seting()
        suite_d = unittest.TestSuite()
        suite_d.addTest(Seting_Testcase('test_my_info'))
        suite_d.addTest(Seting_Testcase('test_change_password'))
        suite_d.addTest(Seting_Testcase('test_seting_mydata'))
        suite_d.addTest(Seting_Testcase('test_seting_terms_of_use'))
        suite_d.addTest(Seting_Testcase('test_seting_privacy_policy'))
        suite_d.addTest(Seting_Testcase('test_seting_mydata_service_terms_of_use'))
        suite_d.addTest(Seting_Testcase('test_financial_consumer_protection_notice'))
        suite_d.addTest(Seting_Testcase('test_seting_version'))
        suite_d.addTest(Seting_Testcase('test_open_source_license'))
        unittest.TextTestRunner().run(suite_d)

        result_set = '\n\n'.join(str(i) for i in resultseting.reports)
        print(result_set)
        print(SlackWebHook.seting_slack_webhook(result_set))

    def testsuite4(self):
        resultjoin = Result_Join()
        suite_b = unittest.TestSuite()
        suite_b.addTest(LoginTestCase('test_log_out'))
        suite_b.addTest(JoinTestCase('test_message_certification'))
        suite_b.addTest(JoinTestCase('test_enter_personal_information'))
        suite_b.addTest(JoinTestCase('test_membership_terms_and_conditions'))
        suite_b.addTest(JoinTestCase('test_certification_number'))
        suite_b.addTest(JoinTestCase('test_join'))
        suite_b.addTest(LoginTestCase('test_withdraw'))
        unittest.TextTestRunner().run(suite_b)

        result_join = '\n\n'.join(str(i) for i in resultjoin.reports)
        print(result_join)
        print(SlackWebHook.join_send_slack_webhook(result_join))

    def testsuite5(self):
        resultautoloan = Result_loan()
        suite_c = unittest.TestSuite()
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_new_new_car_terms'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_new_new_car_certification_number'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_new'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_detail'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_application'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_new_used_car'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_existing_new_car'))
        suite_c.addTest(AutoLoanTestcase('test_auto_loan_existing_used_car'))
        suite_c.addTest(LoanComparisonTestcase('test_loan_terms_and_conditions'))
        suite_c.addTest(LoanComparisonTestcase('test_loan_comparison_verification_code'))
        suite_c.addTest(LoanComparisonTestcase('test_rrn_validation_check'))
        suite_c.addTest(LoanComparisonTestcase('test_loan_comparison_apt_secured_loan'))
        suite_c.addTest(LoanComparisonTestcase('test_check_deposit_today'))
        suite_c.addTest(LoanComparisonTestcase('test_comparison_loan_detail'))
        suite_c.addTest(LoanComparisonTestcase('test_comparison_loan_detail_certification'))
        suite_c.addTest(LoanComparisonTestcase('test_loan_application'))
        suite_c.addTest(LoanComparisonTestcase('test_office_worker_loan_no_certificate'))
        suite_c.addTest(LoanComparisonTestcase('test_unemployed_loan'))
        suite_c.addTest(LoanComparisonTestcase('test_auto_loan_in'))
        unittest.TextTestRunner().run(suite_c)

        result_auto_loan = '\n\n'.join(str(i) for i in resultautoloan.reports)
        print(result_auto_loan)
        print(SlackWebHook.auto_loan_send_slack_webhook(result_auto_loan))

if __name__ == '__main__':

#     appium_process = process(target = appium.start_appium_server)
#     appium_process.start()
#     time.sleep(10)
#
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.basicConfig(filename=f"apptestlog_{current_date}.log", level=logging.INFO)
    print(SlackWebHook.test_start_slack_webhook("AOS 자동화 테스트 시작\n"))
    logging.info("\n\n\n자동화 테스트 시작\n\n\n")
    test = test()

    test.testsuite1()
    test.testsuite2()
    test.testsuite3()
    test.testsuite4()
    test.testsuite5()

    # kill = process(target = kill_appium_server)
    # #
    # # test_case = [
    # a = multiprocessing.Process(target=test.testsuite1)
    # b = multiprocessing.Process(target=test.testsuite2)
    # c = multiprocessing.Process(target=test.testsuite3)
    # d = multiprocessing.Process(target=test.testsuite4)
    # e = multiprocessing.Process(target=test.testsuite5)
    # ]
    #
    # for process in test_case:
    #     process.start()
    #
    # for process in test_case:
    #     process.join()