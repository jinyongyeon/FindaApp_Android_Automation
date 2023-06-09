from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan
from pages.basemethod.slackreports import SlackWebHook

import unittest

from testcase.loan_testcase import Auto_Loan_Testcase
from testcase.login_testcase import LoginTestCase, JoInTestCase
from testcase.more_testcase import MoreTestcase_A
from testcase.more_testcase import MoreTestcase_B
from testcase.more_testcase import MoreTestcase_C
from testcase.myhome_testcase import MyHome_Testcase

suite = unittest.TestSuite()

suite.addTest(LoginTestCase('test_Check_In'))
suite.addTest(MyHome_Testcase('test_ComPariSonLoan'))
suite.addTest(MyHome_Testcase('test_LoanDiagnosisBanner'))
suite.addTest(MyHome_Testcase('test_Loan_Banner'))
suite.addTest(MyHome_Testcase('test_Cash_Assets_Banner'))
suite.addTest(MyHome_Testcase('test_Repayment_Schedule_Banner'))
suite.addTest(MyHome_Testcase('test_Lease_Contract_Banner'))
suite.addTest(MyHome_Testcase('test_Auto_Loan_Banner'))
suite.addTest(MoreTestcase_A('test_Check_More_Tab'))
suite.addTest(MoreTestcase_A('test_Myloan_In'))
suite.addTest(MoreTestcase_A('test_ChatTing'))
suite.addTest(MoreTestcase_A('test_Qna'))
suite.addTest(MoreTestcase_A('test_Refinancing_Loan_Advance_Application'))
suite.addTest(MoreTestcase_A('test_ComPariSonLoan'))
suite.addTest(MoreTestcase_A('test_AutoLoan'))
suite.addTest(MoreTestcase_A('test_CharTer'))
suite.addTest(MoreTestcase_A('test_Change_Loan'))
suite.addTest(MoreTestcase_A('test_Myloan_B'))
suite.addTest(MoreTestcase_A('test_Amortization_Schedule'))
suite.addTest(MoreTestcase_B('test_Credit_Score'))
suite.addTest(MoreTestcase_B('test_Improve_Credit_Score'))
suite.addTest(MoreTestcase_B('test_Credit_Analysis'))
suite.addTest(MoreTestcase_B('test_Credit_History'))
suite.addTest(MoreTestcase_B('test_Extra_Money'))
suite.addTest(MoreTestcase_B('test_Dsr'))
suite.addTest(MoreTestcase_B('test_Interest'))
suite.addTest(MoreTestcase_B('test_Year_End_Settlement'))
suite.addTest(MoreTestcase_B('test_Charter_Vs_Monthly_Rent'))
suite.addTest(MoreTestcase_B('test_Refinancing_Loan'))
suite.addTest(MoreTestcase_C('test_Lease_Rent'))
suite.addTest(MoreTestcase_C('test_Do_Not_Call_Terms_Of_Use'))
suite.addTest(MoreTestcase_C('test_Insurance'))
suite.addTest(MoreTestcase_C('test_Deposit_And_Savings'))
suite.addTest(MoreTestcase_C('test_Finda_Post'))
suite.addTest(MoreTestcase_C('test_My_Phorn'))
suite.addTest(MoreTestcase_C('test_Event'))
suite.addTest(MoreTestcase_C('test_Notice'))
suite.addTest(MoreTestcase_C('test_loan_Reviews'))
suite.addTest(MoreTestcase_C('test_Alarm'))
suite.addTest(LoginTestCase('test_LogOut'))
suite.addTest(JoInTestCase('test_Message_Certification'))
suite.addTest(JoInTestCase('test_Enter_Personal_Information'))
suite.addTest(JoInTestCase('test_Membership_Terms_And_Conditions'))
suite.addTest(JoInTestCase('test_Certification_Number'))
suite.addTest(JoInTestCase('test_Join'))
suite.addTest(LoginTestCase('test_Withdraw'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_New_NewCar_Terms'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_New_NewCar_Certification_Number'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_New'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_Detail'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_Application'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_New_UsedCar'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_existing_NewCar'))
suite.addTest(Auto_Loan_Testcase('test_Auto_Loan_existing_UsedCar'))

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
#
print(SlackWebHook.join_SendSlackWebHook(resultjoin))
print(SlackWebHook.myHome_SendSlackWebHook(resultmyhome))
print(SlackWebHook.more_SendSlackWebHook(resultmore))
print(SlackWebHook.autoloan_SendSlackWebHook(resultautoloan))