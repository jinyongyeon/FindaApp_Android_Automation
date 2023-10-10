import time
import os
import concurrent.futures

appium_script_path = "/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/pages/basemethod/appiumrunner.py"
os.system(f"/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/venv/bin/python {appium_script_path} &")
time.sleep(10)


import unittest
from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan, Result_refinancing_loan, \
    Result_seting
from pages.basemethod.slackreports import SlackWebHook
from testcase.testcase_loan import AutoLoanTestcase, LoanComparisonTestcase
from testcase.testcase_login import LoginTestCase, JoinTestCase
from testcase.testcase_more import MoreTestcase_A
from testcase.testcase_more import MoreTestcase_B
from testcase.testcase_more import MoreTestcase_C
from testcase.testcase_myhome import MyHome_Testcase
from testcase.testcase_seting import Seting_Testcase



class test_start():



    # print(SlackWebHook.test_start_slack_webhook("AOS 자동화 테스트 시작"))
    result_myhome = Result_MyHome()
    result_more = Result_More()
    result_seting = Result_seting()
    result_join = Result_Join()
    result_auto_loan = Result_loan()

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
    # unittest.TextTestRunner().run(suite)

    result_myhome = '\n\n'.join(str(i) for i in result_myhome.reports)
    print(SlackWebHook.my_home_send_slack_webhook(result_myhome))

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

    result_more = '\n\n'.join(str(i) for i in result_more.reports)
    print(SlackWebHook.more_send_slack_webhook(result_more))

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
    # unittest.TextTestRunner().run(suite_d)

    result_set = '\n\n'.join(str(i) for i in result_seting.reports)
    print(SlackWebHook.seting_slack_webhook(result_set))

    suite_b = unittest.TestSuite()
    suite_b.addTest(LoginTestCase('test_log_out'))
    suite_b.addTest(JoinTestCase('test_message_certification'))
    suite_b.addTest(JoinTestCase('test_enter_personal_information'))
    suite_b.addTest(JoinTestCase('test_membership_terms_and_conditions'))
    suite_b.addTest(JoinTestCase('test_certification_number'))
    suite_b.addTest(JoinTestCase('test_join'))
    suite_b.addTest(LoginTestCase('test_withdraw'))
    # unittest.TextTestRunner().run(suite_b)

    result_join = '\n\n'.join(str(i) for i in result_join.reports)
    print(SlackWebHook.join_send_slack_webhook(result_join))

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
    # unittest.TextTestRunner().run(suite_c)

    result_auto_loan = '\n\n'.join(str(i) for i in result_auto_loan.reports)
    print(SlackWebHook.auto_loan_send_slack_webhook(result_auto_loan))