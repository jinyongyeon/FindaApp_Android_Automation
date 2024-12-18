import time
import logging
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.mainlocator.etc import Etc


class More:

    # 초기화
    # def __init__(self):
    def __init__(self):
        self.Etc = Etc()
        self.base = basemethod()

    # 더보기 탭 테스트
    def etc_in(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.etc)).click()
        time.sleep(2)

    def more_top(self):
        a = 7
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.myloan))
                time.sleep(2)
                self.base.scroll_up(0.3)
                break
            except:
                self.base.scroll_up(0.8)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")


    # 내 대출 진입
    def my_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.myloan)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 내 대출 뒤로 가기 탭 복귀
    def my_loan_back(self):
        try:
            banner = WebDriver.driver.find_element(MobileBy.XPATH, Etc.banner_exit)
            myloan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan_back)
            banner.click()
            myloan_back.click()
        except:
            try:
                myloan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan_back)
                myloan_back.click()
            except:
                pass

    # 1:1 채팅 문의 진입
    def chatting(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.chatting)).click()
                time.sleep(3)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 1:1 채팅 문의 닫기
    def chatting_exit(self):
        try:
            chatting_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.chatting_exit)
            chatting_exit.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"chatting_exit : {e}")

    # 자주 묻는 질문 진입
    def qna(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 자주 묻는 질물 항목 선택
    def qna_click_a(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_a)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"qna_click_a : {e}")

    def qna_click_b(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_b)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"qna_click_b : {e}")

    # def qna_click_c(self):
    #     try:
    #         WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_c)).click()
    #         time.sleep(1)
    #     except Exception as e:
    #         logging.error(f"qna_click_c : {e}")

    def qna_click_d(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_d)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"qna_click_d : {e}")

    def qna_click_e(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.qna_e)).click()
            time.sleep(1)
        except Exception as e:
            logging.error(f"qna_click_e : {e}")

    # 자주 묻는 질문 > 뒤로 가기
    def qna_back(self):
        try:
            qna_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_back)
            qna_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"qna_back : {e}")

    # 대출 갈아 타기
    def transfer_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.transfer_loan)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 대출 한 번에 비교 진입
    def comparison_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.comparison_loan)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 대출 한 번에 비교 > 뒤로 가기
    def comparison_loan_back(self):
        try:
            comparison_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.comparison_loan_back)
            comparison_loan_back.click()
            time.sleep(2)
        except:
            try:
                comparison_loan_back_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.comparison_loan_back_b)
                comparison_loan_back_b.click()
                time.sleep(2)
                comparison_loan_back_b_a = WebDriver.driver.find_element(MobileBy.XPATH,Etc.comparison_loan_back_b_a)
                comparison_loan_back_b_a.click()
            except:
                logging.warning("comparison_loan_back > 뒤로가기 버튼 동작 실패")

    # 자동차 구매 대출 진입
    def auto_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.auto_loan)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 자동차 구매 대출 > 뒤로 가기
    def auto_loan_back(self):
        try:
            auto_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.auto_loan_back)
            auto_loan_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_back : {e}")

    # 전원세 추천 진입
    def charter(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.charter)).click()
                time.sleep(20)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 전원세 추천 > 뒤로 가기
    def charter_back(self):
        try:
            charter_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_back)
            charter_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"charter_back : {e}")

    # 30일 안에 대출 갈아 타기 진입
    def change_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.change_loan)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 30일 안에 대출 갈아 타기 > 뒤로 가기
    def change_loan_back(self):
        try:
            change_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.change_loan_back)
            change_loan_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"change_loan_back : {e}")

    def business_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.business_loan)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    def KB_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.KB_loan)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    def analyze_commercial_area(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.analyze_commercial_area)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 나의 금융 정보 > 내 자산 진입
    def my_loan_b(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.myloan_b)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 나의 금융 정보 > 상환 일정 진입
    def amortization_schedule(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.amortization_schedule)).click()
                time.sleep(4)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 나의 금융 정보 > 상환 일정 > 뒤로 가기
    def amortization_schedule_back(self):
        try:
            amortization_schedule_back = WebDriver.driver.find_element(MobileBy.XPATH,Etc.amortization_schedule_back)
            amortization_schedule_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"amortization_schedule_back")

    # 정부 전자문서지갑 진입
    def electronic_wallet(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.electronic_wallet)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")
    def check(self):
        check = WebDriver.driver.find_element(Etc.check)
        check.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 진입
    def credit_score(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.credit_score)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    def exit(self):
        exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.exit)
        exit.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 뒤로 가기
    def credit_score_back(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.credit_score_back)).click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"credit_score_back : {e}")

    # 신용 관리 > 신용 점수 올리기 진입
    def improve_credit_score(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.improve_credit_score)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 신용 관리 > 신용 점수 올리기 뒤로 가기
    def improve_credit_score_back(self):
        try:
            improve_credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.improve_credit_score_back)
            improve_credit_score_back.click()
            time.sleep(2)
            credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
            credit_score_back.click()
        except Exception as e:
            logging.error(f"improve_credit_score_back : {e}")

    # 신용 관리 > 신용 점수 상승 전략 진입
    def credit_analysis(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.credit_analysis)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 신용 관리 > 신용 점수 상승 전략 > 뒤로 가기
    def credit_analysis_back(self):
        try:
            credit_analysis_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_analysis_back)
            credit_analysis_back.click()
            time.sleep(2)
            credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
            credit_score_back.click()
        except Exception as e:
            logging.error(f"credit_analysis_back : {e}")

    # 신용 관리 > 신용 점수 히스토리 진입
    def credit_history(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.credit_history)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 신용 관리 > 신용 점수 히스토리 > 뒤로 가기
    def credit_history_back(self):
        try:
            credit_history_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_history_back)
            credit_history_back.click()
            time.sleep(2)
            credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
            credit_score_back.click()
        except Exception as e:
            logging.error(f"credit_history_back : {e}")

    # 개인사업자 신용관리
    def private_business_credit_management(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.private_business_credit_management)).click()
                time.sleep(10)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 신용퀴즈 어워즈
    def credit_quiz_awards(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.credit_quiz_awards)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 연체 기록 삭제하기 진입
    def delete_delinquent_records(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.delete_delinquent_records)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 여윳돈 계산기 진입
    def extra_money(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.extra_money)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 여윳돈 계산기 뒤로 가기
    def extra_money_back(self):
        try:
            extra_money_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.extra_money_back)
            extra_money_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"extra_money_back : {e}")

    # 계산기 > DSR 계산기 진입
    def dsr(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.dsr)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > DSR 계산기 > 뒤로 가기
    def dsr_back(self):
        try:
            dsr_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.dsr_back)
            dsr_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"dsr_back : {e}")

    # 계산기 > 대출 이자 계산기 진입
    def interest(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.interest)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 대출 이자 계산기 > 뒤로 가기
    def interest_back(self):
        try:
            interest_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.interest_back)
            interest_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"interest_back : {e}")

    # 계산기 > 내 집 마련 대출한도 계산기 진입
    def get_myownhouse(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.get_myownhouse)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 내 집 마련 대출한도 계산기 > 받을 수 있는 돈 계산하기
    def get_myownhouse_next(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.get_myownhouse_next)).click()
        time.sleep(2)

    # 계산기 > 연말 정산 계산기 진입
    def year_end_settlement(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.year_end_settlement)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 연말 정산 계산기 > 뒤로 가기
    def year_end_settlement_back(self):
        try:
            year_end_settlement_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.year_end_settlement_back)
            year_end_settlement_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"year_end_settlement_back : {e}")

    # 계산기 > 전세 vs 월세 계산기 진입
    def charter_vs_monthly_rent(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.charter_vs_monthly_rent)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 전세 vs 월세 계산기 뒤로 가기
    def charter_vs_monthly_rent_back(self):
        try:
            charter_vs_monthly_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_vs_monthly_rent_back)
            charter_vs_monthly_rent_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"charter_vs_monthly_rent_back : {e}")

    # 계산기 > 대출 갈아 타기 계산기 진입
    def refinancing_loan(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.refinancing_loan)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 대출 갈아 타기 계산기 > 뒤로 가기
    def refinancing_loan_back(self):
        try:
            refinancing_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.refinancing_loan_back)
            refinancing_loan_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"refinancing_loan_back : {e}")

    # 계산기 > 청년 도약 계좌 계산기 진입
    def youth_leap_account(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.youth_leap_account)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 계산기 > 자동차 할부 계산기 진입
    def car_installment_calculator(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.car_installment_calculator)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 부가 서비스 > 장기 렌트 리스 진입
    def lease_rent(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.lease_rent)).click()
                time.sleep(5)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 부가 서비스 > 장기 렌트 리스 뒤로 가기
    def lease_rent_back(self):
        try:
            lease_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.lease_rent_back)
            lease_rent_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"lease_rent_back : {e}")

    # 부가 서비스 > 금융 스팸 차단 진입
    def do_not_call(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.do_not_call)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 두낫콜 한 번에 차단 하기 선택
    def do_net_call_cta(self):
        try:
            do_not_call_cta = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_cta)
            do_not_call_cta.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"do_net_call_cta : {e}")

    def terms_of_use_webview_exit(self):
        try:
            webview_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.webview_exit)
            webview_exit.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_webview_exit : {e}")

    # 두낫콜 약관 리스트 진입 동작
    def terms_of_use_a(self):
        try:
            do_not_call_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a)
            do_not_call_a.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_a : {e}")

    def terms_of_use_aa(self):
        try:
            do_not_call_a_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_a)
            do_not_call_a_a.click()
            time.sleep(3)
        except Exception as e:
            logging.error(f"terms_of_use_aa : {e}")

    def terms_of_use_ab(self):
        try:
            do_not_call_a_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_b)
            do_not_call_a_b.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_ab : {e}")

    def terms_of_use_ac(self):
        try:
            do_not_call_a_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_c)
            do_not_call_a_c.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_ac : {e}")

    def terms_of_use_b(self):
        try:
            do_not_call_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b)
            do_not_call_b.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_b : {e}")

    def terms_of_use_ba(self):
        try:
            do_not_call_b_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_a)
            do_not_call_b_a.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_ba : {e}")

    def terms_of_use_bb(self):
        try:
            do_not_call_b_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_b)
            do_not_call_b_b.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_bb : {e}")

    def terms_of_use_bc(self):
        try:
            do_not_call_b_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_c)
            do_not_call_b_c.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_bc : {e}")

    def terms_of_use_bd(self):
        try:
            do_not_call_b_d = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_d)
            do_not_call_b_d.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_bd : {e}")

    def terms_of_use_c(self):
        try:
            do_not_call_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c)
            do_not_call_c.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_c : {e}")

    def terms_of_use_ca(self):
        try:
            do_not_call_c_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_a)
            do_not_call_c_a.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_ca : {e}")

    def terms_of_use_cb(self):
        try:
            do_not_call_c_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_b)
            do_not_call_c_b.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_cb : {e}")

    def terms_of_use_cc(self):
        try:
            do_not_call_c_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_c)
            do_not_call_c_c.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"terms_of_use_cc : {e}")

    # 두낫콜 나가기 동작
    def do_not_call_back(self):
        try:
            do_not_call_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_back)
            do_not_call_back.click()
            time.sleep(1)
            try:
                do_not_call_stop = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_stop)
                do_not_call_stop.click()
            except :
                pass
        except Exception as e:
            logging.error(f"do_not_call_back : {e}")

    # 대출금 갚아주는 보험 진입
    def insurance(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.insurance)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    def insurance_web(self):
        try:
            insuranceweb = WebDriver.driver.find_element(MobileBy.XPATH, Etc.insuranceweb)
            insuranceweb.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"insurance_web : {e}")

    # 예적금 비교 진입
    def deposit_and_savings(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.deposit_and_savings)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 예적금 비교 나가기
    def deposit_and_savings_back(self):
        try:
            deposit_and_savings_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.deposit_and_savings_back)
            deposit_and_savings_back.click()
        except Exception as e:
            logging.error(f"deposit_and_savings_back : {e}")

    # 핀다 포스트 진입
    def finda_post(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.finda_post)).click()
                time.sleep(20)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 핀다 포스트 컨텐츠 진입 확인

    # 핀다 포스트 나가기
    def finda_post_back(self):
        finda_post_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.finda_post_back)
        finda_post_back.click()

    # 더보기 > 내 폰 지키미 진입
    def my_phorn(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.my_phorn)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 더보기 > 내 폰 지키미 > 뒤로 가기
    def my_phorn_back(self):
        try:
            my_phorn_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.my_phorn_back)
            my_phorn_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"my_phorn_back : {e}")

    # 돈되는 혜택 진입
    def event(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.event)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 이벤트 나가기
    def event_back(self):
        try:
            event_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.event_back)
            event_back.click()
        except Exception as e:
            logging.error(f"event_back : {e}")

    # 공지 사항 진입
    def notice(self):
        a = 5
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.notice)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 공지 사항 상세 진입
    def notice_in(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.notice_in)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.5)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 공지 사항 상세 > 뒤로 가기
    def notice_in_back(self):
        try:
            notice_in_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_in_back)
            notice_in_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"notice_in_back : {e}")

    # 공지 사항 나가기
    def notice_back(self):
        try:
            notice_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_back)
            notice_back.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"notice_back : {e}")

    # 대출 후기 진입
    def loan_reviews(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.loan_reviews)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 대출 후기 나가기
    def loan_reviews_back(self):
        try:
            loan_reviews_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.loan_reviews_back)
            loan_reviews_back.click()
        except Exception as e:
            logging.error(f"loan_reviews_back : {e}")

    # 최근 알림 진입
    def alarm(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.alarm)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 최근 알림 > 뒤로 가기
    def alarm_back(self):
        try:
            alarm_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.alarm_back)
            alarm_back.click()
        except Exception as e:
            logging.error(f"alarm_back : {e}")

    # 포인트 진입
    def point(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.point)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 출석체크 진입
    def checkin(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.checkin)).click()
                time.sleep(2)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 물가예측 진입
    def priceforecast(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.priceforecast)).click()
                time.sleep(5)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")

    # 물가예측 참여내역
    def priceforecast_history(self):
        a = 6
        b = 0
        while b < a:
            try:
                WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(Etc.priceforecast_history)).click()
                time.sleep(5)
                break
            except:
                self.base.scroll(0.7)
                b += 1
        if b == a:
            print("로케이터를 찾을 수 없습니다. 요소 확인 필요.")