# import os
from multiprocessing import Process
# from appium.webdriver.appium_service import AppiumService

from pages.basemethod.base import basemethod

base = basemethod()
process = Process(target=base.appium_run)

# 프로세스를 시작합니다.
process.start()

# 병렬로 실행되는 동안 다른 작업을 수행할 수 있습니다.

# 프로세스가 종료될 때까지 대기합니다.
# process.join()
# import subprocess

# from appium.webdriver.appium_service import AppiumService





# print(appium_Run())
# print("test")