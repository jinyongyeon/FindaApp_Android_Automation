import time
import logging

from appium.webdriver.common.mobileby import MobileBy


from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc


class More:

    # 초기화
    # def __init__(self):
    def __init__(self):
        self.Etc = Etc()

    # 더보기 탭 테스트
    def etc_in(self):
        try:
            etc_in = WebDriver.driver.find_element(MobileBy.XPATH, Etc.etc)
            etc_in.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"etc_in : {e}")

    # 내 대출 진입
    def my_loan(self):
        myloan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan)
        myloan.click()
        time.sleep(2)

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
        chatting = WebDriver.driver.find_element(MobileBy.XPATH, Etc.chatting)
        chatting.click()
        time.sleep(3)

    # 1:1 채팅 문의 닫기
    def chatting_exit(self):
        chatting_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.chatting_exit)
        chatting_exit.click()
        time.sleep(2)

    # 자주 묻는 질문 진입
    def qna(self):
        qna = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna)
        qna.click()
        time.sleep(2)

    # 자주 묻는 질물 항목 선택
    def qna_click_a(self):
        qna_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_a)
        qna_a.click()
        time.sleep(1)

    def qna_click_b(self):
        qna_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_b)
        qna_b.click()
        time.sleep(1)

    def qna_click_c(self):
        qna_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_c)
        qna_c.click()
        time.sleep(1)

    def qna_click_d(self):
        qna_d = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_d)
        qna_d.click()
        time.sleep(1)

    def qna_click_e(self):
        qna_e = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_e)
        qna_e.click()
        time.sleep(1)

    # 자주 묻는 질문 > 뒤로 가기
    def qna_back(self):
        qna_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_back)
        qna_back.click()
        time.sleep(2)

    # 대출 갈아 타기
    def transfer_loan(self):
        transfer_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.transfer_loan)
        transfer_loan.click()
        time.sleep(4)

    # 대출 한 번에 비교 진입
    def comparison_loan(self):
        comparison_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.comparison_loan)
        comparison_loan.click()
        time.sleep(4)

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
                print("뒤로가기 버튼 동작 실패")

    # 자동차 구매 대출 진입
    def auto_loan(self):
        auto_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.auto_loan)
        auto_loan.click()
        time.sleep(2)

    # 자동차 구매 대출 > 뒤로 가기
    def auto_loan_back(self):
        auto_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.auto_loan_back)
        auto_loan_back.click()
        time.sleep(2)

    # 전원세 추천 진입
    def charter(self):
        charter = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter)
        charter.click()
        time.sleep(2)

    # 전원세 추천 > 뒤로 가기
    def charter_back(self):
        charter_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_back)
        charter_back.click()
        time.sleep(2)

    # 30일 안에 대출 갈아 타기 진입
    def change_loan(self):
        change_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.change_loan)
        change_loan.click()
        time.sleep(2)

    # 30일 안에 대출 갈아 타기 > 뒤로 가기
    def change_loan_back(self):
        change_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.change_loan_back)
        change_loan_back.click()
        time.sleep(2)

    # 나의 금융 정보 > 내 대출 진입
    def my_loan_b(self):
        myloan_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan_b)
        myloan_b.click()
        time.sleep(2)

    # 나의 금융 정보 > 상환 일정 진입
    def amortization_schedule(self):
        amortization_schedule = WebDriver.driver.find_element(MobileBy.XPATH, Etc.amortization_schedule)
        amortization_schedule.click()
        time.sleep(2)

    # 나의 금융 정보 > 상환 일정 > 뒤로 가기
    def amortization_schedule_back(self):
        amortization_schedule_back = WebDriver.driver.find_element(MobileBy.XPATH,Etc.amortization_schedule_back)
        amortization_schedule_back.click()
        time.sleep(2)

    def check(self):
        check =WebDriver.driver.find_element(MobileBy.XPATH,Etc.check)
        check.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 진입
    def credit_score(self):
        credit_score = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score)
        credit_score.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 뒤로 가기
    def credit_score_back(self):
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 올리기 진입
    def improve_credit_score(self):
        improve_credit_score = WebDriver.driver.find_element(MobileBy.XPATH, Etc.improve_credit_score)
        improve_credit_score.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 올리기 뒤로 가기
    def improve_credit_score_back(self):
        improve_credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.improve_credit_score_back)
        improve_credit_score_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 신용 관리 > 신용 점수 상승 전략 진입
    def credit_analysis(self):
        credit_analysis = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_analysis)
        credit_analysis.click()
        time.sleep(2)

    # 신용 관리 > 신용 점수 상승 전략 > 뒤로 가기
    def credit_analysis_back(self):
        credit_analysis_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_analysis_back)
        credit_analysis_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 신용 관리 > 신용 점수 히스토리 진입
    def credit_history(self):
        credit_history = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_history)
        credit_history.click()
        time.sleep(4)

    # 신용 관리 > 신용 점수 히스토리 > 뒤로 가기
    def credit_history_back(self):
        credit_history_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_history_back)
        credit_history_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 개인사업자 신용관리
    def private_business_credit_management(self):
        private_business_credit_management = WebDriver.driver.find_element(MobileBy.XPATH, Etc.private_business_credit_management)
        private_business_credit_management.click()
        time.sleep(2)

    # 신용퀴즈 어워즈
    def credit_quiz_awards(self):
        credit_quiz_awards = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_quiz_awards)
        credit_quiz_awards.click()
        time.sleep(2)

    # 계산기 > 여윳돈 계산기 진입
    def extra_money(self):
        extra_money = WebDriver.driver.find_element(MobileBy.XPATH, Etc.extra_money)
        extra_money.click()
        time.sleep(2)

    # 계산기 > 여윳돈 계산기 뒤로 가기
    def extra_money_back(self):
        extra_money_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.extra_money_back)
        extra_money_back.click()
        time.sleep(2)

    # 계산기 > DSR 계산기 진입
    def dsr(self):
        dsr = WebDriver.driver.find_element(MobileBy.XPATH, Etc.dsr)
        dsr.click()
        time.sleep(2)

    # 계산기 > DSR 계산기 > 뒤로 가기
    def dsr_back(self):
        dsr_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.dsr_back)
        dsr_back.click()
        time.sleep(2)

    # 계산기 > 대출 이자 계산기 진입
    def interest(self):
        interest = WebDriver.driver.find_element(MobileBy.XPATH, Etc.interest)
        interest.click()
        time.sleep(2)

    # 계산기 > 대출 이자 계산기 > 뒤로 가기
    def interest_back(self):
        interest_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.interest_back)
        interest_back.click()
        time.sleep(2)

    # 계산기 > 연말 정산 계산기 진입
    def year_end_settlement(self):
        year_end_settlement = WebDriver.driver.find_element(MobileBy.XPATH, Etc.year_end_settlement)
        year_end_settlement.click()
        time.sleep(2)

    # 계산기 > 연말 정산 계산기 > 뒤로 가기
    def year_end_settlement_back(self):
        year_end_settlement_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.year_end_settlement_back)
        year_end_settlement_back.click()
        time.sleep(2)

    # 계산기 > 전세 vs 월세 계산기 진입
    def charter_vs_monthly_rent(self):
        charter_vs_monthly_rent = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_vs_monthly_rent)
        charter_vs_monthly_rent.click()
        time.sleep(2)

    # 계산기 > 전세 vs 월세 계산기 뒤로 가기
    def charter_vs_monthly_rent_back(self):
        charter_vs_monthly_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_vs_monthly_rent_back)
        charter_vs_monthly_rent_back.click()
        time.sleep(2)

    # 계산기 > 대출 갈아 타기 계산기 진입
    def refinancing_loan(self):
        refinancing_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.refinancing_loan)
        refinancing_loan.click()
        time.sleep(2)

    # 계산기 > 대출 갈아 타기 계산기 > 뒤로 가기
    def refinancing_loan_back(self):
        refinancing_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.refinancing_loan_back)
        refinancing_loan_back.click()
        time.sleep(2)

    # 계산기 > 청년 도약 계좌 계산기 진입
    def youth_leap_account(self):
        youth_leap_account = WebDriver.driver.find_element(MobileBy.XPATH, Etc.youth_leap_account)
        youth_leap_account.click()
        time.sleep(2)

    # 부가 서비스 > 장기 렌트 리스 진입
    def lease_rent(self):
        lease_rent = WebDriver.driver.find_element(MobileBy.XPATH, Etc.lease_rent)
        lease_rent.click()
        time.sleep(2)

    # 부가 서비스 > 장기 렌트 리스 뒤로 가기
    def lease_rent_back(self):
        lease_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.lease_rent_back)
        lease_rent_back.click()
        time.sleep(2)

    # 부가 서비스 > 금융 스팸 차단 진입
    def do_not_call(self):
        do_not_call = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call)
        do_not_call.click()
        time.sleep(2)

    # 두낫콜 한 번에 차단 하기 선택
    def do_net_call_cta(self):
        do_not_call_cta = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_cta)
        do_not_call_cta.click()
        time.sleep(2)

    def terms_of_use_webview_exit(self):
        webview_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.webview_exit)
        webview_exit.click()
        time.sleep(2)

    # 두낫콜 약관 리스트 진입 동작
    def terms_of_use_a(self):
        do_not_call_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a)
        do_not_call_a.click()
        time.sleep(2)

    def terms_of_use_aa(self):
        do_not_call_a_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_a)
        do_not_call_a_a.click()
        time.sleep(3)

    def terms_of_use_ab(self):
        do_not_call_a_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_b)
        do_not_call_a_b.click()
        time.sleep(2)

    def terms_of_use_ac(self):
        do_not_call_a_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_c)
        do_not_call_a_c.click()
        time.sleep(2)

    def terms_of_use_b(self):
        do_not_call_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b)
        do_not_call_b.click()
        time.sleep(2)

    def terms_of_use_ba(self):
        do_not_call_b_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_a)
        do_not_call_b_a.click()
        time.sleep(2)

    def terms_of_use_bb(self):
        do_not_call_b_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_b)
        do_not_call_b_b.click()
        time.sleep(2)

    def terms_of_use_bc(self):
        do_not_call_b_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_c)
        do_not_call_b_c.click()
        time.sleep(2)

    def terms_of_use_bd(self):
        do_not_call_b_d = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_d)
        do_not_call_b_d.click()
        time.sleep(2)

    def terms_of_use_c(self):
        do_not_call_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c)
        do_not_call_c.click()
        time.sleep(2)

    def terms_of_use_ca(self):
        do_not_call_c_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_a)
        do_not_call_c_a.click()
        time.sleep(2)

    def terms_of_use_cb(self):
        do_not_call_c_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_b)
        do_not_call_c_b.click()
        time.sleep(2)

    def terms_of_use_cc(self):
        do_not_call_c_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_c)
        do_not_call_c_c.click()
        time.sleep(2)

    # 두낫콜 나가기 동작
    def do_not_call_back(self):
        do_not_call_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_back)
        do_not_call_back.click()
        time.sleep(1)
        try:
            do_not_call_stop = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_stop)
            do_not_call_stop.click()
        except :
            pass

    # 대출금 갚아주는 보험 진입
    def insurance(self):
        insurance = WebDriver.driver.find_element(MobileBy.XPATH, Etc.insurance)
        insurance.click()
        time.sleep(2)

    def insurance_web(self):
        insuranceweb = WebDriver.driver.find_element(MobileBy.XPATH, Etc.insuranceweb)
        insuranceweb.click()
        time.sleep(2)

    # 예적금 비교 진입
    def deposit_and_savings(self):
        deposit_and_savings = WebDriver.driver.find_element(MobileBy.XPATH, Etc.deposit_and_savings)
        deposit_and_savings.click()
        time.sleep(2)

    # 예적금 비교 나가기
    def deposit_and_savings_back(self):
        deposit_and_savings_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.deposit_and_savings_back)
        deposit_and_savings_back.click()

    # 핀다 포스트 진입
    def finda_post(self):
        finda_post = WebDriver.driver.find_element(MobileBy.XPATH, Etc.finda_post)
        finda_post.click()
        time.sleep(2)

    # 핀다 포스트 컨텐츠 진입 확인

    # 핀다 포스트 나가기
    def finda_post_back(self):
        finda_post_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.finda_post_back)
        finda_post_back.click()

    # 더보기 > 내 폰 지키미 진입
    def my_phorn(self):
        my_phorn = WebDriver.driver.find_element(MobileBy.XPATH, Etc.my_phorn)
        my_phorn.click()
        time.sleep(10)

    # 더보기 > 내 폰 지키미 > 뒤로 가기
    def my_phorn_back(self):
        my_phorn_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.my_phorn_back)
        my_phorn_back.click()
        time.sleep(2)

    # 돈되는 혜택 진입
    def event(self):
        event = WebDriver.driver.find_element(MobileBy.XPATH, Etc.event)
        event.click()
        time.sleep(2)

    # 이벤트 나가기
    def event_back(self):
        event_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.event_back)
        event_back.click()

    # 공지 사항 진입
    def notice(self):
        notice = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice)
        notice.click()
        time.sleep(2)

    # 공지 사항 상세 진입
    def notice_in(self):
        notice_in = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_in)
        notice_in.click()
        time.sleep(2)

    # 공지 사항 상세 > 뒤로 가기
    def notice_in_back(self):
        notice_in_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_in_back)
        notice_in_back.click()
        time.sleep(2)

    # 공지 사항 나가기
    def notice_back(self):
        notice_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_back)
        notice_back.click()
        time.sleep(2)

    # 대출 후기 진입
    def loan_reviews(self):
        loan_reviews = WebDriver.driver.find_element(MobileBy.XPATH, Etc.loan_reviews)
        loan_reviews.click()
        time.sleep(2)

    # 대출 후기 나가기
    def loan_reviews_back(self):
        loan_reviews_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.loan_reviews_back)
        loan_reviews_back.click()

    # 최근 알림 진입
    def alarm(self):
        alarm = WebDriver.driver.find_element(MobileBy.XPATH, Etc.alarm)
        alarm.click()
        time.sleep(2)

    # 최근 알림 > 뒤로 가기
    def alarm_back(self):
        alarm_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.alarm_back)
        alarm_back.click()