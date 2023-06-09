import time

from appium.webdriver.common.mobileby import MobileBy


from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.etc import Etc


class More:

    # 초기화
    # def __init__(self):
    def __init__(self):
        self.Etc = Etc()
        # self.click = basemethod.click()

    # def click(selector, by=MobileBy.XPATH):
    #     element = WebDriverWait(WebDriver.driver, 10).until(
    #         EC.element_to_be_clickable((by, selector))
    #     )
    #     element.click()


        # 더보기 탭 테스트
    def etcIn(self):
        # print("더보기 탭 진입")
        etc_in = WebDriver.driver.find_element(MobileBy.XPATH, Etc.etc)
        etc_in.click()
        time.sleep(2)

        # 내 대출 진입
    def myLoan(self):
        # print("내 대출 진입")
        myloan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan)
        myloan.click()
        time.sleep(2)

    # 내 대출 뒤로가기로 탭 복귀
    def myLoanBack(self):

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

    # 내 대출 뒤로가기로 탭 복귀
    # def myLoanBack(self):
    #     myloan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan_back)
    #     myloan_back.click()
    #     time.sleep(2)

    # 1:1 채팅문의 진입
    def chatTing(self):
        # print("1:1 채팅문의 진입")
        chatting = WebDriver.driver.find_element(MobileBy.XPATH, Etc.chatting)
        chatting.click()
        time.sleep(3)

    # 1:1 채팅문의 닫기
    def chatTingExit(self):
        chatting_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.chatting_exit)
        chatting_exit.click()
        time.sleep(2)

    # 자주묻는 질문 진입
    def qnA(self):
        # print("자주 묻는 질문 진입")
        qna = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna)
        qna.click()
        time.sleep(2)

    # 자주묻는 질물 항목 선택
    def qna_Click_A(self):
        qna_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_a)
        qna_a.click()
        time.sleep(1)

    def qna_Click_B(self):
        qna_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_b)
        qna_b.click()
        time.sleep(1)

    def qna_Click_C(self):
        qna_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_c)
        qna_c.click()
        time.sleep(1)

    def qna_Click_D(self):
        qna_d = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_d)
        qna_d.click()
        time.sleep(1)

    def qna_Click_E(self):
        qna_e = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_e)
        qna_e.click()
        time.sleep(1)

    # 자주묻는 질문 뒤로가기
    def qnaBack(self):
        qna_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.qna_back)
        qna_back.click()
        time.sleep(2)

    # 대출 갈아타기
    def transfer_Loan(self):
        transfer_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.transfer_loan)
        transfer_loan.click()
        time.sleep(4)

    # 대출 한 번에 비교 진입
    def comPariSonLoan(self):
        # print("대출 한 번에 비교 진입")
        comparison_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.comparison_loan)
        comparison_loan.click()
        time.sleep(4)

    # 대출 한 번에 비교 뒤로가기
    def comPariSonLoanBback(self):

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
                pass

    # 자동차 구매 대출 진입
    def autoLoan(self):
        # print("자동차 구매 대출 진입")
        auto_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.auto_loan)
        auto_loan.click()
        time.sleep(2)


    # 자동차 구매 대출 뒤로가기
    def autoLoanBack(self):
        auto_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.auto_loan_back)
        auto_loan_back.click()
        time.sleep(2)

    # 전원세 추천 진입
    def charTer(self):
        # print("전원세 추천 진입")
        charter = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter)
        charter.click()
        time.sleep(2)

    # 전원세 추천 뒤로가기
    def charTerBack(self):
        charter_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_back)
        charter_back.click()
        time.sleep(2)

    # 30일 안에 대출 갈아타기 진입
    def change_Loan(self):
        change_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.change_loan)
        change_loan.click()
        time.sleep(2)

    # 30일 안에 대출 갈아타기 > 뒤로가기
    def change_Loan_Back(self):
        change_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.change_loan_back)
        change_loan_back.click()
        time.sleep(2)



    # 나의 금융정보 > 내 대출 진입
    def myLoan_B(self):
        myloan_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.myloan_B)
        myloan_b.click()
        time.sleep(2)

    # 나의 금융정보 > 상환일정 진입
    def amortization_Schedule(self):
        amortization_schedule = WebDriver.driver.find_element(MobileBy.XPATH, Etc.amortization_schedule)
        amortization_schedule.click()
        time.sleep(2)

    # 나의 금융정보 > 상환일정 > 뒤로가기
    def amortization_Schedule_back(self):
        amortization_schedule_back = WebDriver.driver.find_element(MobileBy.XPATH,Etc.amortization_schedule_back)
        amortization_schedule_back.click()
        time.sleep(2)

    # 신용관리 > 신용점수 진입
    def credit_Score(self):
        credit_score = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score)
        credit_score.click()
        time.sleep(2)

    # 신용관리 > 신용점수 뒤로가기
    def credit_Score_Back(self):
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()
        time.sleep(2)

    # 신용관리 > 신용점수 올리기 진입
    def improve_Credit_Score(self):
        improve_credit_score = WebDriver.driver.find_element(MobileBy.XPATH, Etc.improve_credit_score)
        improve_credit_score.click()
        time.sleep(2)


    # 신용관리 > 신용점수 올리기 뒤로가기
    def improve_Credit_Score_Back(self):
        improve_credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.improve_credit_score_back)
        improve_credit_score_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 신용관리 > 신용점수 상승 전략 진입
    def credit_Analysis(self):
        credit_analysis = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_analysis)
        credit_analysis.click()
        time.sleep(2)

    # 신용관리 > 신용점수 상승 전략 > 뒤로가기
    def credit_Analysis_Back(self):
        credit_analysis_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_analysis_back)
        credit_analysis_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 신용관리 > 신용점수 히스토리 진입
    def credit_History(self):
        credit_history = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_history)
        credit_history.click()
        time.sleep(4)

    # 신용관리 > 신용점수 히스토리 > 뒤로가기
    def credit_History_Back(self):
        credit_history_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_history_back)
        credit_history_back.click()
        time.sleep(2)
        credit_score_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.credit_score_back)
        credit_score_back.click()

    # 계산기 > 여윳돈 계산기 진입
    def extra_Money(self):
        extra_money = WebDriver.driver.find_element(MobileBy.XPATH, Etc.extra_money)
        extra_money.click()
        time.sleep(2)

    # 계산기 > 여윳돈 계산기 뒤로가기
    def extra_Money_Back(self):
        extra_money_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.extra_money_back)
        extra_money_back.click()
        time.sleep(2)

    # 계산기 > DSR계산기 진입
    def dsR(self):
        dsr = WebDriver.driver.find_element(MobileBy.XPATH, Etc.dsr)
        dsr.click()
        time.sleep(2)

    # 계산기 > DSR계산기 뒤로가기
    def dsr_Back(self):
        dsr_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.dsr_back)
        dsr_back.click()
        time.sleep(2)

    # 계산기 > 대출이자 계산기 진입
    def interest(self):
        interest = WebDriver.driver.find_element(MobileBy.XPATH, Etc.interest)
        interest.click()
        time.sleep(2)

    # 계산기 > 대출이자 계산기 뒤로가기
    def interest_Back(self):
        interest_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.interest_back)
        interest_back.click()
        time.sleep(2)

    # 계산기 > 연말정산 계산기 진입
    def year_End_Settlement(self):
        year_end_settlement = WebDriver.driver.find_element(MobileBy.XPATH, Etc.year_end_settlement)
        year_end_settlement.click()
        time.sleep(2)

    # 계산기 > 연말정산 계산기 뒤로가기
    def year_End_Settlement_Back(self):
        year_end_settlement_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.year_end_settlement_back)
        year_end_settlement_back.click()
        time.sleep(2)

    # 계산기 > 전세 vs 월세 계산기 진입
    def charter_Vs_Monthly_Rent(self):
        charter_vs_monthly_rent = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_vs_monthly_rent)
        charter_vs_monthly_rent.click()
        time.sleep(2)


    # 계산기 > 전세 vs 월세 계산기 뒤로가기
    def charter_Vs_Monthly_Rent_Back(self):
        charter_vs_monthly_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.charter_vs_monthly_rent_back)
        charter_vs_monthly_rent_back.click()
        time.sleep(2)

    # 계산기 > 대출 갈아타기 계산기 진입
    def refinancing_Loan(self):
        refinancing_loan = WebDriver.driver.find_element(MobileBy.XPATH, Etc.refinancing_loan)
        refinancing_loan.click()
        time.sleep(2)

    # 계산기 > 대출 갈아타기 계산기 뒤로가기
    def refinancing_Loan_Back(self):
        refinancing_loan_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.refinancing_loan_back)
        refinancing_loan_back.click()
        time.sleep(2)

    # 부가서비스 > 장기렌트 리스 진입
    def lease_Rent(self):
        lease_rent = WebDriver.driver.find_element(MobileBy.XPATH, Etc.lease_rent)
        lease_rent.click()
        time.sleep(2)

    # 부가서비스 > 장기렌트 리스 뒤로가기
    def lease_Rent_Back(self):
        lease_rent_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.lease_rent_back)
        lease_rent_back.click()
        time.sleep(2)

    # 부가서비스 > 금융 스팸 차단 진입
    def do_Not_Call(self):
        do_not_call = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call)
        do_not_call.click()
        time.sleep(2)

    # 두낫콜 한 번에 차단하기 선택
    def do_Net_Call_Cta(self):
        do_not_call_cta = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_cta)
        do_not_call_cta.click()
        time.sleep(2)

    def terms_Of_Use_Webview_Exit(self):
        webview_exit = WebDriver.driver.find_element(MobileBy.XPATH, Etc.webview_exit)
        webview_exit.click()
        time.sleep(2)

    # 두낫콜 약관 리스트 진입 동작
    def terms_Of_Use_A(self):
        do_not_call_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a)
        do_not_call_a.click()
        time.sleep(2)

    def terms_Of_Use_Aa(self):
        do_not_call_a_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_a)
        do_not_call_a_a.click()
        time.sleep(3)

    def terms_Of_Use_Ab(self):
        do_not_call_a_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_b)
        do_not_call_a_b.click()
        time.sleep(2)

    def terms_Of_Use_Ac(self):
        do_not_call_a_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_a_c)
        do_not_call_a_c.click()
        time.sleep(2)

    def terms_Of_Use_B(self):
        do_not_call_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b)
        do_not_call_b.click()
        time.sleep(2)

    def terms_Of_Use_Ba(self):
        do_not_call_b_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_a)
        do_not_call_b_a.click()
        time.sleep(2)

    def terms_Of_Use_Bb(self):
        do_not_call_b_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_b)
        do_not_call_b_b.click()
        time.sleep(2)

    def terms_Of_Use_Bc(self):
        do_not_call_b_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_c)
        do_not_call_b_c.click()
        time.sleep(2)

    def terms_Of_Use_Bd(self):
        do_not_call_b_d = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_b_d)
        do_not_call_b_d.click()
        time.sleep(2)

    def terms_Of_Use_C(self):
        do_not_call_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c)
        do_not_call_c.click()
        time.sleep(2)

    def terms_Of_Use_Ca(self):
        do_not_call_c_a = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_a)
        do_not_call_c_a.click()
        time.sleep(2)

    def terms_Of_Use_Cb(self):
        do_not_call_c_b = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_b)
        do_not_call_c_b.click()
        time.sleep(2)

    def terms_Of_Use_Cc(self):
        do_not_call_c_c = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_c_c)
        do_not_call_c_c.click()
        time.sleep(2)

    # 두낫콜 나가기 동작
    def do_Not_Call_Back(self):
        do_not_call_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_back)
        do_not_call_back.click()
        time.sleep(1)
        try:
            do_not_call_stop = WebDriver.driver.find_element(MobileBy.XPATH, Etc.do_not_call_stop)
            do_not_call_stop.click()
        except :
            pass

    # 대출금 갚아주는 보험
    def insurance(self):
        insurance = WebDriver.driver.find_element(MobileBy.XPATH, Etc.insurance)
        insurance.click()
        time.sleep(2)

    # 예적금 비교 진입
    def deposit_And_Savings(self):
        deposit_and_savings = WebDriver.driver.find_element(MobileBy.XPATH, Etc.deposit_and_savings)
        deposit_and_savings.click()
        time.sleep(2)

    # 예적금 비교 나가기
    def deposit_And_Savings_Back(self):
        deposit_and_savings_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.deposit_and_savings_back)
        deposit_and_savings_back.click()

    # 핀다 포스트 진입
    def finda_Post(self):
        finda_post = WebDriver.driver.find_element(MobileBy.XPATH, Etc.finda_post)
        finda_post.click()
        time.sleep(2)

    # 핀다 포스트 컨텐츠 진입 확인

    # 핀다 포스트 나가기
    def finda_Post_Back(self):
        finda_post_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.finda_post_back)
        finda_post_back.click()

    # 더보기 > 내 폰 지키미 진입
    def my_Phorn(self):
        my_phorn = WebDriver.driver.find_element(MobileBy.XPATH, Etc.my_phorn)
        my_phorn.click()
        time.sleep(2)

    # 더보기 > 내 폰 지키미 > 뒤로가기
    def my_Phorn_Back(self):
        my_phorn_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.my_phorn_back)
        my_phorn_back.click()
        time.sleep(2)

    # 이벤트 진입
    def event(self):
        event = WebDriver.driver.find_element(MobileBy.XPATH, Etc.event)
        event.click()
        time.sleep(2)

    # 이벤트 나가기
    def event_Back(self):
        event_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.event_back)
        event_back.click()

    # 공지사항 진입
    def notice(self):
        notice = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice)
        notice.click()
        time.sleep(2)

    # 공지사항 상세 진입
    def notice_In(self):
        notice_in = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_in)
        notice_in.click()
        time.sleep(2)

    # 공지사항 상세 뒤로가기
    def notice_In_Back(self):
        notice_in_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_in_back)
        notice_in_back.click()
        time.sleep(2)

    # 공지사항 나가기
    def notice_Back(self):
        notice_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.notice_back)
        notice_back.click()
        time.sleep(2)

    # 대출후기 진입
    def loan_Reviews(self):
        loan_reviews = WebDriver.driver.find_element(MobileBy.XPATH, Etc.loan_reviews)
        loan_reviews.click()
        time.sleep(2)

    # 대출후기 나가기
    def loan_Reviews_Back(self):
        loan_reviews_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.loan_reviews_back)
        loan_reviews_back.click()

    # 최근알림 진입
    def alarm(self):
        alarm = WebDriver.driver.find_element(MobileBy.XPATH, Etc.alarm)
        alarm.click()
        time.sleep(2)

    # 최근알림 뒤로가기
    def alarm_Back(self):
        alarm_back = WebDriver.driver.find_element(MobileBy.XPATH, Etc.alarm_back)
        alarm_back.click()