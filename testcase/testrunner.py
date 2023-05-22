from pages.basemethod.result import Result_More, Result_Join
from pages.basemethod.slackreports import SlackWebHook

import unittest
from testcase.login_testcase import LoginTestCase
from testcase.more_testcase import MoreTestcase_A
from testcase.more_testcase import MoreTestcase_B
from testcase.more_testcase import MoreTestcase_C


suite = unittest.TestSuite()

# suite.addTest(LoginTestCase('test_Check_In'))
# suite.addTest(MoreTestcase_A('test_Check_More_Tab'))
# suite.addTest(MoreTestcase_A('test_Myloan_In'))
# suite.addTest(MoreTestcase_A('test_ChatTing'))
# suite.addTest(MoreTestcase_A('test_Qna'))
# suite.addTest(MoreTestcase_A('test_Refinancing_Loan_Advance_Application'))
# suite.addTest(MoreTestcase_A('test_ComPariSonLoan'))
# suite.addTest(MoreTestcase_A('test_AutoLoan'))
# suite.addTest(MoreTestcase_A('test_CharTer'))
# suite.addTest(MoreTestcase_A('test_Change_Loan'))
# suite.addTest(MoreTestcase_A('test_Myloan_B'))
# suite.addTest(MoreTestcase_A('test_Amortization_Schedule'))
# suite.addTest(MoreTestcase_B('test_Credit_Score'))
# suite.addTest(MoreTestcase_B('test_Improve_Credit_Score'))
# suite.addTest(MoreTestcase_B('test_Credit_Analysis'))
# suite.addTest(MoreTestcase_B('test_Credit_History'))
# suite.addTest(MoreTestcase_B('test_Extra_Money'))
# suite.addTest(MoreTestcase_B('test_Dsr'))
# suite.addTest(MoreTestcase_B('test_Interest'))
# suite.addTest(MoreTestcase_B('test_Year_End_Settlement'))
# suite.addTest(MoreTestcase_B('test_Charter_Vs_Monthly_Rent'))
# suite.addTest(MoreTestcase_B('test_Refinancing_Loan'))
# suite.addTest(MoreTestcase_C('test_Lease_Rent'))
# suite.addTest(MoreTestcase_C('test_Do_Not_Call_Terms_Of_Use'))
# suite.addTest(MoreTestcase_C('test_Insurance'))
# suite.addTest(MoreTestcase_C('test_Deposit_And_Savings'))
# suite.addTest(MoreTestcase_C('test_Finda_Post'))
# suite.addTest(MoreTestcase_C('test_My_Phorn'))
# suite.addTest(MoreTestcase_C('test_Event'))
# suite.addTest(MoreTestcase_C('test_Notice'))
# suite.addTest(MoreTestcase_C('test_loan_Reviews'))
# suite.addTest(MoreTestcase_C('test_Alarm'))
suite.addTest(LoginTestCase('test_LogOut'))
suite.addTest(LoginTestCase('test_Message_Certification'))
suite.addTest(LoginTestCase('test_Enter_Personal_Information'))
suite.addTest(LoginTestCase('test_Membership_Terms_And_Conditions'))
suite.addTest(LoginTestCase('test_Certification_Number'))
suite.addTest(LoginTestCase('test_Join'))
suite.addTest(LoginTestCase('test_Withdraw'))

runner = unittest.TextTestRunner()
runner.run(suite)
result_more = Result_More()
result_join = Result_Join()
slackwebhook = SlackWebHook()

resultjoin = '\n\n'.join(str(i) for i in result_join.reports)
resultmore = '\n\n'.join(str(i) for i in result_more.reports)

print(resultjoin)
# print(resultmore)

print(SlackWebHook.join_SendSlackWebHook(resultjoin))
# print(SlackWebHook.more_SendSlackWebHook(resultmore))