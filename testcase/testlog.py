from pages.basemethod.result import Result_More, Result_Join, Result_MyHome, Result_loan, Result_refinancing_loan, \
    Result_seting
from pages.basemethod.slackreports import SlackWebHook
import logging
import datetime
import unittest

from testcase.testcase_loan import AutoLoanTestcase, LoanComparisonTestcase
from testcase.testcase_login import LoginTestCase, JoinTestCase
from testcase.testcase_more import MoreTestcase_A
from testcase.testcase_more import MoreTestcase_B
from testcase.testcase_more import MoreTestcase_C
from testcase.testcase_myhome import MyHome_Testcase
from testcase.testcase_seting import Seting_Testcase


result_myhome = Result_MyHome()
result_more = Result_More()
result_seting = Result_seting()
result_join = Result_Join()
result_auto_loan = Result_loan()

suite = unittest.TestSuite()
suite.addTest(MyHome_Testcase('test_loan_banner'))


current_date = datetime.datetime.now().strftime("%Y-%m-%d")
logging.basicConfig(filename=f"apptestlog_{current_date}.log", level=logging.INFO)
unittest.TextTestRunner().run(suite)

# result_auto_loan = '\n\n'.join(str(i) for i in result_auto_loan.reports)
# print(SlackWebHook.auto_loan_send_slack_webhook(result_auto_loan))