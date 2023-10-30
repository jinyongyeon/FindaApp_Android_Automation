import multiprocessing
import os
import time
from testcase.testrunner_test_1 import test



# class appium:
def start_appium_server():
    appium_command = "appium -a 127.0.0.1 -p 4723 -pa /wd/hub"
    os.system(appium_command)
    # appium_script_path = "/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/pages/basemethod/appiumrunner.py"
    # os.system(f"/Users/yongyeon/PycharmProjects/Finda_Android_App_Automation/venv/bin/python {appium_script_path} &")

def kill_appium_server():
    appium_command = "pkill -9 -f appium"
    os.system(appium_command)



if __name__ == '__main__':

    appium_process = multiprocessing.Process(target = start_appium_server)
    appium_process.start()
    time.sleep(10)
    appium_process.join()

    test = test()
    test.testsuite1()
    test.testsuite2()
    test.testsuite3()
    test.testsuite4()
    test.testsuite5()



