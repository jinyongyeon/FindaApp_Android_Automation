import logging
import time
from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait

from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc


class Seting:

    # 초기화
    def __init__(self):
        self.Etc = Etc()

    # 설정 진입
    def seting_in(self):
        try:
            seting_buttun = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_buttun)
            seting_buttun.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"seting_in : {e}")

    # 설정 > 내 정보 진입
    def myinfo(self):
        try:
            myinfo = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.myinfo)
            myinfo.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"myinfo : {e}")

    # 설정 > 내정보 > 수정하기 동작
    def myinfo_edit(self):
        try:
            myinfo_edit = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.myinfo_edit)
            myinfo_edit.click()
            time.sleep(2)
            myinfo_authenticate_yourself = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.myinfo_authenticate_yourself)
            myinfo_authenticate_yourself.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"myinfo_edit : {e}")

    # 설정 > 알림설정
    def notification_settings(self):
        notification_settings = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.notification_settings)
        notification_settings.click()

    # 설정 > 비밀번호 변경
    def change_password(self):
        try:
            changepassword = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.changepassword)
            changepassword.click()
        except Exception as e:
            logging.error(f"change_password : {e}")

    # 설정 > 금융 정보 관리(마이데이터) 진입
    def seting_mtdata(self):
        try:
            seting_mtdata = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_mtdata)
            seting_mtdata.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"seting_mtdata : {e}")

    # 설정 > 이용약관 진입
    def seting_terms_of_use(self):
        try:
            seting_terms_of_use = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_terms_of_use)
            seting_terms_of_use.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"seting_terms_of_use : {e}")

    # 설정 > 개인정보 처리방침 진입
    def seting_privacy_policy(self):
        try:
            seting_privacy_policy = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_privacy_policy)
            seting_privacy_policy.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"seting_privacy_policy : {e}")

    # 설정 > 마이데이터 서비스 이용약관 진입
    def seting_mydata_service_terms_of_use(self):
        try:
            seting_mydata_service_terms_of_use = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_mydata_service_terms_of_use)
            seting_mydata_service_terms_of_use.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"seting_mydata_service_terms_of_use : {e}")

    # 설정 > 금융소비자보호 고지사항 진입
    def financial_consumer_protection_notice(self):
        try:
            financial_consumer_protection_notice = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.financial_consumer_protection_notice)
            financial_consumer_protection_notice.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"financial_consumer_protection_notice : {e}")

    # 설정 > 버전 정보 진입
    def seting_version(self):
        try:
            seting_version = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.seting_version)
            seting_version.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"seting_version : {e}")

    # 설정 > 오픈소스 라이선스 진입
    def open_source_license(self):
        try:
            open_source_license = WebDriver.driver.find_element(MobileBy.XPATH, self.Etc.open_source_license)
            open_source_license.click()
            time.sleep(6)
        except Exception as e:
            logging.error(f"open_source_license : {e}")