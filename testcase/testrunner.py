from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan
from pages.basemethod.slackreports import SlackWebHook

import unittest

from testcase.testcase_loan import AutoLoanTestcase, LoanComparisonTestcase
from testcase.testcase_login import LoginTestCase, JoinTestCase
from testcase.testcase_more import MoreTestcase_A
from testcase.testcase_more import MoreTestcase_B
from testcase.testcase_more import MoreTestcase_C
from testcase.testcase_myhome import MyHome_Testcase

suite = unittest.TestSuite()

suite.addTest(LoginTestCase('test_check_in'))
suite.addTest(MyHome_Testcase('test_comparison_loan'))
suite.addTest(MyHome_Testcase('test_loan_diagnosis_banner'))
suite.addTest(MyHome_Testcase('test_loan_banner'))
suite.addTest(MyHome_Testcase('test_cash_assets_banner'))
suite.addTest(MyHome_Testcase('test_repayment_schedule_banner'))
suite.addTest(MyHome_Testcase('test_lease_contract_banner'))
suite.addTest(MyHome_Testcase('test_auto_loan_banner'))
suite.addTest(MoreTestcase_A('test_check_more_tab'))
suite.addTest(MoreTestcase_A('test_myloan_in'))
suite.addTest(MoreTestcase_A('test_chat_ting'))
suite.addTest(MoreTestcase_A('test_qna'))
suite.addTest(MoreTestcase_A('test_refinancing_loan'))
suite.addTest(MoreTestcase_A('test_comparison_loan'))
suite.addTest(MoreTestcase_A('test_auto_loan'))
suite.addTest(MoreTestcase_A('test_charter'))
suite.addTest(MoreTestcase_A('test_change_loan'))
suite.addTest(MoreTestcase_A('test_my_loan_b'))
suite.addTest(MoreTestcase_A('test_amortization_schedule'))
suite.addTest(MoreTestcase_B('test_credit_score'))
suite.addTest(MoreTestcase_B('test_improve_credit_score'))
suite.addTest(MoreTestcase_B('test_credit_analysis'))
suite.addTest(MoreTestcase_B('test_credit_history'))
suite.addTest(MoreTestcase_B('test_extra_money'))
suite.addTest(MoreTestcase_B('test_dsr'))
suite.addTest(MoreTestcase_B('test_interest'))
suite.addTest(MoreTestcase_B('test_year_end_settlement'))
suite.addTest(MoreTestcase_B('test_charter_vs_monthly_rent'))
suite.addTest(MoreTestcase_B('test_refinancing_loan'))
suite.addTest(MoreTestcase_C('test_lease_rent'))
suite.addTest(MoreTestcase_C('test_do_not_call_terms_of_use'))
suite.addTest(MoreTestcase_C('test_insurance'))
suite.addTest(MoreTestcase_C('test_deposit_and_savings'))
suite.addTest(MoreTestcase_C('test_finda_post'))
suite.addTest(MoreTestcase_C('test_my_phorn'))
suite.addTest(MoreTestcase_C('test_event'))
suite.addTest(MoreTestcase_C('test_notice'))
suite.addTest(MoreTestcase_C('test_loan_reviews'))
suite.addTest(MoreTestcase_C('test_alarm'))
suite.addTest(LoginTestCase('test_log_out'))
suite.addTest(JoinTestCase('test_message_certification'))
suite.addTest(JoinTestCase('test_enter_personal_information'))
suite.addTest(JoinTestCase('test_membership_terms_and_conditions'))
suite.addTest(JoinTestCase('test_certification_number'))
suite.addTest(JoinTestCase('test_join'))
suite.addTest(LoginTestCase('test_withdraw'))
suite.addTest(AutoLoanTestcase('test_auto_loan_new_new_car_terms'))
suite.addTest(AutoLoanTestcase('test_auto_loan_new_new_car_certification_number'))
suite.addTest(AutoLoanTestcase('test_auto_loan_new'))
suite.addTest(AutoLoanTestcase('test_auto_loan_detail'))
suite.addTest(AutoLoanTestcase('test_auto_loan_application'))
suite.addTest(AutoLoanTestcase('test_auto_loan_new_used_car'))
suite.addTest(AutoLoanTestcase('test_auto_loan_existing_new_car'))
suite.addTest(AutoLoanTestcase('test_auto_loan_existing_used_car'))
suite.addTest(LoanComparisonTestcase('test_loan_terms_and_conditions'))
suite.addTest(LoanComparisonTestcase('test_loan_comparison_verification_code'))
suite.addTest(LoanComparisonTestcase('test_rrn_validation_check'))
suite.addTest(LoanComparisonTestcase('test_loan_comparison_apt_secured_loan'))
suite.addTest(LoanComparisonTestcase('test_check_deposit_today'))
suite.addTest(LoanComparisonTestcase('test_comparison_loan_detail'))
suite.addTest(LoanComparisonTestcase('test_comparison_loan_detail_certification'))
suite.addTest(LoanComparisonTestcase('test_loan_application'))
suite.addTest(LoanComparisonTestcase('test_office_worker_loan_no_certificate'))
suite.addTest(LoanComparisonTestcase('test_unemployed_loan'))
suite.addTest(LoanComparisonTestcase('test_auto_loan_in'))


runner = unittest.TextTestRunner()
runner.run(suite)


result_more = Result_More()
result_join = Result_Join()
result_myhome = Result_MyHome()
result_autoloan = Result_loan()
slackwebhook = SlackWebHook()
#
resultjoin = '\n\n'.join(str(i) for i in result_join.reports)
resultmyhome = '\n\n'.join(str(i) for i in result_myhome.reports)
resultmore = '\n\n'.join(str(i) for i in result_more.reports)
resultautoloan = '\n\n'.join(str(i) for i in result_autoloan.reports)


print(resultjoin)
print(resultmyhome)
print(resultmore)
print(resultautoloan)


print(SlackWebHook.join_SendSlackWebHook(resultjoin))
print(SlackWebHook.myHome_SendSlackWebHook(resultmyhome))
print(SlackWebHook.more_SendSlackWebHook(resultmore))
print(SlackWebHook.autoloan_SendSlackWebHook(resultautoloan))