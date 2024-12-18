from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo


class Etc:

    info = InFo()


    # 더보기 탭
    etc = MobileBy.XPATH, '//*[@text = "전체"]'
    # 더보기 진입 결과
    etc_result = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[@text = "더보기"]'
    # 내 대출
    myloan = MobileBy.XPATH, '//*[@index = "1" and @text = "내 대출"]'

    # 내 대출 진입 결과
    myloan_Result_a = MobileBy.XPATH, '//*[@text = "카드"]'
    myloan_Result_b = MobileBy.XPATH, '//*[@text = "대출"]'
    myloan_Result_c = MobileBy.XPATH, '//*[@text = "입출금"]'
    myloan_Result_d = MobileBy.XPATH, '//*[@text = "예적금"]'

    # 브레이즈 배너
    banner_exit = '//*[@text = "테스트"]'
    # 내 대출 뒤로가기
    myloan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]'

    # 1:1 채팅문의
    chatting = MobileBy.XPATH, '//*[@text = "1:1 채팅문의"]'

     # 1:1 채팅문의 진입 결과
    chatting_result = MobileBy.XPATH, "//*[contains(@text, '안녕하세요. 핀다입니다')]"
     # 1:1 채팅 닫기
    chatting_exit = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView"

    # 자주묻는 질문
    qna = MobileBy.XPATH, '//*[@text = "자주 묻는 질문"]'

    # 자주묻는 질문 > 질문 항목
    qna_a = MobileBy.XPATH, '//*[contains(@text, "정말 이 조건 그대로 대출 가능한가요?")]'
    qna_result_a = MobileBy.XPATH, "//*[contains(@text, '고객님께서')]"
    qna_b = MobileBy.XPATH, '//*[contains(@text, "신청하면 대출금은 언제 입금이 되나요?")]'
    qna_result_b = MobileBy.XPATH, "//*[contains(@text, '대출이 확정된 후 대출금이')]"
    # qna_c = MobileBy.XPATH, '//*[contains(@text, "대출 조건은 언제까지 유효한가요?")]'
    # qna_result_c = MobileBy.XPATH, "//*[contains(@text, '조회하신')]"
    qna_d = MobileBy.XPATH, '//*[contains(@text, "대출을 알아보는 것으로, 불이익이 있나요?")]'
    qna_result_d = MobileBy.XPATH, "//*[contains(@text, '대출조회는 신용점수')]"
    qna_e = MobileBy.XPATH, '//*[contains(@text, "신용조회가 여러 건 발생했다고 하는데 무슨 일인가요?")]'
    qna_result_e = MobileBy.XPATH, "//*[contains(@text, '걱정하지 마세요.')]"

    # 자주묻는 질문 뒤로가뒤
    qna_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Image"

    # 대출 갈아타기
    transfer_loan = MobileBy.XPATH,'//*[@text = "대출 갈아타기"]'
    transfer_loan_result_a = MobileBy.XPATH, '//*[@text = "대출 갈아타기"]'
    transfer_loan_result_b = MobileBy.XPATH, '//*[@text = "더 낮은 금리로\n더 편하게 갈아타세요"]'

    # 대출 한 번에 비교
    comparison_loan = MobileBy.XPATH, '//*[@text = "대출 한번에 비교"]'

    # 대출 한 번에 비교 결과
    comparison_loan_Result_a = MobileBy.XPATH, '//*[contains(@text, "대출 한 번에 알아보기")]'
    # comparison_loan_Result_a = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'
    # comparison_loan_Result_b = '//*[@text = "오늘입금"]'
    comparison_loan_Result_b = MobileBy.XPATH, '//*[@text = "오늘입금"]'

    # 대출 한 번에 비교 뒤로가기
    comparison_loan_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View/android.widget.Button"

    comparison_loan_back_b = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[1]"
    comparison_loan_back_b_a = '//*[@text = "나가기"]'


    # 자동차 구매 대출
    auto_loan = MobileBy.XPATH, '//*[@text = "자동차 구매 대출"]'

    # 자동차 구매 대출 진입 결과
    auto_loan_Result_a = MobileBy.XPATH, '//*[@text = "1분만에 내 한도 알아보기"]'
    auto_loan_Result_b = MobileBy.XPATH, '//*[@text = "'+info.name+'님의\n가장 좋은 대출 조건이에요."]'

    # 자동차 구매 대출 뒤로가기
    auto_loan_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]"

    # 전월세 추천
    charter = MobileBy.XPATH, '//*[@text = "전월세대출 가이드"]'

    # 전월세 추천 진입 결과
    charter_Result_a = MobileBy.XPATH, '//*[contains(@text, "피할 수 없다면 손쉽게")]'
    charter_Result_b = MobileBy.XPATH, '//*[contains(@text, "전월세대출 맞춤추천")]'

    # 전원세 뒤로가기
    charter_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 30일 대출 챌린지
    change_loan = MobileBy.XPATH, '//*[@text = "대환 챌린지"]'

    # 30일 안에 대출 갈아타기 뒤로가기
    change_loan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    business_loan = MobileBy.XPATH,"//*[contains(@text, '사업자대출')]"
    business_loan_result = MobileBy.XPATH,"//*[contains(@text, '사업자대출 조건 비교하기')]"

    KB_loan = MobileBy.XPATH,"//*[contains(@text, 'KB사장님+')]"
    KB_loan_result = MobileBy.XPATH,"//*[contains(@text, 'KB사장님+ 대출 조건 알아보기')]"

    analyze_commercial_area = MobileBy.XPATH,"//*[contains(@text, '상권 분석 서비스')]"
    analyze_commercial_area_result = MobileBy.XPATH,"//*[contains(@text, '매출 궁금한 곳 검색')]"

    # 나의 금융정보 > 내 대출 진입
    myloan_b = MobileBy.XPATH, '//*[@text = "내 자산"]'

    # 나의 금융정보 > 상환일정
    amortization_schedule = MobileBy.XPATH, '//*[@text = "상환・결제 일정"]'

    # 상환일정 진입 결과
    amortization_schedule_a = MobileBy.XPATH, "//*[contains(@text, '이번달 나갈 돈 합계')]"
    amortization_schedule_b = MobileBy.XPATH, '//*[@text = "내 대출, 카드 한번에 연결하기"]'
    check = MobileBy.XPATH, '//*[@text = "확인"]'

    # 나의 금융정보 > 상환일정 뒤로가기
    amortization_schedule_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    electronic_wallet = MobileBy.XPATH, '//*[@text = "정부 전자문서지갑"]'

    # 신용관리 > 신용점수 진입
    credit_score = MobileBy.XPATH, '//*[@text = "신용점수"]'

    # 신용관리 바텀시트 닫기
    exit = "//*[contains(@text, '닫기')]"

    # 신용점수 페이지 진입 결과
    credit_score_Result = MobileBy.XPATH, '//*[@text = "'+info.name+'님의 신용점수"]'

    # 신용관리 > 신용점수 뒤로가기
    credit_score_back = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]'

    # 신용관리 > 신용점수 올리기 진입
    improve_credit_score = MobileBy.XPATH, '//*[@text = "신용점수 올리기"]'

    # 신용점수 올리기 진입 결과
    improve_credit_score_Result_a = MobileBy.XPATH, '//*[@text = "신용점수 올리기를 통해\n이만큼 올렸어요"]'
    improve_credit_score_Result_b = MobileBy.XPATH, '//*[@text = "은행 계좌를 많이 연결할수록\n점수 상승 가능성을 높일 수 있어요"]'

    # 신용관리 > 신용점수 올리기 뒤로가기
    improve_credit_score_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]'

    # 신용관리 > 신용점수 상승 전략 진입
    credit_analysis = MobileBy.XPATH, '//*[@text = "신용 분석"]'

    # 신용관리 > 신용점수 상승 전략 진입 결과
    credit_analysis_Result = MobileBy.XPATH, "//*[contains(@text, '신용 분석')]"

    # 신용관리 > 신용점수 상승 전략 뒤로가기
    credit_analysis_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 신용관리 > 신용점수 히스트리 진입
    credit_history = MobileBy.XPATH, '//*[@text = "신용점수 히스토리"]'

    # 신용관리 > 신용점수 히스트리 진입 결과
    credit_history_Result = MobileBy.XPATH, '//*[contains(@text, "신용점수 히스토리")]'
    # credit_history_Result = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView'

    # 신용관리 > 신용점수 히스트리 뒤로가기
    credit_history_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 개인사업자 신용관리
    private_business_credit_management = MobileBy.XPATH, '//*[@text = "사업자 신용관리"]'
    private_business_credit_management_result = MobileBy.XPATH, '//*[@text = "개인사업자 신용관리 시작하기"]'

    # 신용퀴즈 어워즈
    credit_quiz_awards = MobileBy.XPATH, '//*[@text = "핀다 퀴즈"]'
    credit_quiz_awards_result = MobileBy.XPATH, "//*[contains(@text, '다음 시즌')]"

    # 연체 기록 삭제하기
    delete_delinquent_records = MobileBy.XPATH, '//*[@text = "연체 기록 삭제하기"]'
    delete_delinquent_records_result = MobileBy.XPATH, "//*[contains(@text, '신용회복 대상자인지 확인하기')]"

    # 계산기 > 여윳돈 계산기 진입
    extra_money = MobileBy.XPATH, '//*[@text = "여윳돈 계산기"]'

    # 계산기 > 여윳돈 계산기 진입 결과
    extra_money_Result = MobileBy.XPATH, '//*[@text = "상환할 여윳돈이 생기셨나요?"]'

    # 계산기 > 여윳돈 계산기 뒤로가기
    extra_money_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 계산기 > DSR계산기 진입
    dsr = MobileBy.XPATH, '//*[@text = "DSR 계산기"]'

    # 계산기 > DSR계산기 진입 결과
    dsr_Result = MobileBy.XPATH, '//*[contains(@text, "얼마나 받을 수 있을지")]'

    # 계산기 > DSR계산기 뒤로가기
    dsr_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 계산기 > 대출이자 계산기 진입
    interest = MobileBy.XPATH, '//*[@text = "대출 이자 계산기"]'

    # 대출이자 계산기 결과
    interest_Result = MobileBy.XPATH, '//*[@text = "대출이자 계산기"]'

    # 계산기 > 대출이자 계산기 뒤로가기
    interest_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 내 집 마련 대출한도 계산기 진입
    get_myownhouse = MobileBy.XPATH, '//*[@text = "내 집 마련 대출한도 계산기"]'
    # 계산기 > 내 집 마련 대출한도 계산기 > 받을 수 있는 돈 계산하기
    get_myownhouse_next = MobileBy.XPATH, '//*[@text = "받을 수 있는 돈 계산하기"]'
    # 계산기 > 내 집 마련 대출한도 계산기 결과
    get_myownhouse_result = MobileBy.XPATH, '//*[contains(@text, "내 집 대출한도 계산기")]'

    # 계산기 > 연말정산 계산기 진입
    year_end_settlement = MobileBy.XPATH, '//*[@text = "연말정산 계산기"]'

    # 연말정산 계산기 결과
    year_end_settlement_Result = MobileBy.XPATH, '//*[contains(@text, "카드 및 현금 소비액 소득공제")]'

    # 계산기 > 연말정산 계산기 뒤로가기
    year_end_settlement_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 전세 vs 월세 계산기 진입
    charter_vs_monthly_rent = MobileBy.XPATH, '//*[@text = "전세 vs 월세 계산기"]'

    # 전세 vs 월세 계산기 결과
    charter_vs_monthly_rent_Result = MobileBy.XPATH, '//*[@text = "전세 vs 월세 계산기"]'

    # 계산기 > 전세 vs 월세 계산기 뒤로가기
    charter_vs_monthly_rent_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 대출 갈아타기 계산기 진입
    refinancing_loan = MobileBy.XPATH, '//*[@text = "대출 갈아타기 계산기"]'

    # 대출 갈아타기 계산기 결과
    refinancing_loan_Result = MobileBy.XPATH, "//*[contains(@text, '갈아타기')]"

    # 계산기 > 대출 갈아타기 계산기 뒤로가기
    refinancing_loan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View/android.widget.Button'

    # 계산기 > 청년도약계좌 계산기
    youth_leap_account = MobileBy.XPATH, '//*[@text = "청년도약계좌 계산기"]'
    youth_leap_account_result = MobileBy.XPATH, '//*[@text = "청년도약계좌 계산기"]'

    # 계산기 > 자동차 할부 계산기
    car_installment_calculator = MobileBy.XPATH, "//*[contains(@text, '자동차 할부 계산기')]"
    car_installment_calculator_result = MobileBy.XPATH, "//*[contains(@text, '할부 계산기')]"

    # 부가서비스 > 장기렌트 리스 진입
    lease_rent = MobileBy.XPATH, "//*[contains(@text, '장기렌트·리스')]"

    # 부가서비스 > 장기렌트 리스 진입 결과
    lease_rent_result = MobileBy.XPATH,'//*[@text = "장기렌트\n보험 세금 부담없이"]'

    # 부가서비스 > 장기렌트 리스 뒤로가기
    lease_rent_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 부가서비스 > 금융 스팸 차단 진입
    do_not_call = MobileBy.XPATH, '//*[@text = "금융 스팸 차단"]'

    # 부가서비스 > 금융 스팸 차단택 한 번에 차단하기 CTA 선택
    do_not_call_cta = '//*[@text = "차단하기"]'

    # 두낫콜 약관 펼치기 1
    do_not_call_a = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View'

    # 두낫콜 약관 펼치기 2
    do_not_call_b = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View'

    # 두낫콜 약관 펼치기 3
    do_not_call_c = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View'

    # 연락중지청구(Do-not-call) 서비스 이용약관
    do_not_call_a_a = '//*[@text = "연락중지청구(Do-not-call) 서비스 이용약관"]'

    # 개인정보 수집·이용에 대한 동의
    do_not_call_a_b = '//*[@text = "개인정보 수집·이용에 대한 동의"]'

    # 개인정보처리방침
    do_not_call_a_c = '//*[@text = "개인정보처리방침"]'

    # 두낫콜 서비스 이용약관 진입 결과 A
    do_not_call_a_Result = MobileBy.XPATH, '//*[@text = "두낫콜 본인확인"]'

    # 개인정보이용동의
    do_not_call_b_a = '//*[@text = "개인정보이용동의"]'

    # 고유식별정보처리동의
    do_not_call_b_b = '//*[@text = "고유식별정보처리동의"]'

    # 서비스이용약관동의
    do_not_call_b_c = '//*[@text = "서비스이용약관동의"]'

    # 통신사이용약관동의
    do_not_call_b_d = '//*[@text = "통신사이용약관동의"]'

    # 두낫콜 서비스 이용약관 진입 결과 B 실패
    do_not_call_b_Result = MobileBy.XPATH, '//*[@text = "금융스팸차단하기 필수 항목 동의"]'

    # [금융스팸차단하기] 서비스 이용 약관
    do_not_call_c_a = '//*[@text = "[금융스팸차단하기] 서비스 이용 약관"]'

    # [금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)
    do_not_call_c_b = '//*[@text = "[금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)"]'

    # [금융스팸차단하기] 개인(신용)정보 제3자 제공 동의(필수)
    do_not_call_c_c = '//*[@text = "[금융스팸차단하기] 개인(신용)정보 제3자 제공 동의(필수)"]'

    # 두낫콜 서비스 이용약관 진입 결과 C 실패
    do_not_call_c_a_Result = MobileBy.XPATH, '//*[@text = "[금융스팸차단] 서비스 이용 약관"]'

    do_not_call_c_b_Result = MobileBy.XPATH, '//*[@text = "[금융스팸차단] 개인(신용)정보 수집·이용 동의"]'

    do_not_call_c_c_Result = MobileBy.XPATH, '//*[@text = "[금융스팸차단] 개인(신용)정보 제3자 제공 동의(필수)"]'

    # 웹뷰 나가기 버튼
    webview_exit = '//*[@content-desc = "탭 닫기"]'

    # 두낫콜 나가기 버튼
    do_not_call_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]'

    # 두낫콜 나가기 > 중단하기 버튼
    do_not_call_stop = '//*[@text = "중단하기"]'

    # 대출금 갚아주는 보험
    insurance = MobileBy.XPATH, '//*[@text = "대출금 갚아주는 보험"]'

    insuranceweb = "//*[contains(@text, '예상 보험료 확인하러 가기')]"

    # 대출금 갚아주는 보험 결과
    insurance_Result = MobileBy.XPATH, "//*[contains(@text, '카디프')]"

    # 예적금 비교 진입
    deposit_and_savings = MobileBy.XPATH, '//*[@text = "예적금 비교"]'

    # 예적금 비교 결과
    deposit_and_savings_Result = MobileBy.XPATH, "//*[contains(@text, '예적금 비교')]"

    # 예적금 비교 > 뒤로가기
    deposit_and_savings_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 핀다 포스트 진입
    finda_post = MobileBy.XPATH, "//*[contains(@text, '사용팁')]"

    # 핀다 포스트 진입 결과
    finda_post_Result = MobileBy.XPATH, "//*[contains(@text, '사용팁')]"

    # 핀다 포스트 컨텐츠
    finda_post_a = '//*[@text = ""]'
    finda_post_b = '//*[@text = ""]'
    finda_post_c = '//*[@text = ""]'
    finda_post_d = '//*[@text = ""]'
    finda_post_e = '//*[@text = ""]'
    finda_post_f = '//*[@text = ""]'
    finda_post_g = '//*[@text = ""]'
    finda_post_h = '//*[@text = ""]'
    finda_post_i = '//*[@text = ""]'
    finda_post_j = '//*[@text = ""]'
    finda_post_k = '//*[@text = ""]'
    finda_post_n = '//*[@text = ""]'
    finda_post_m = '//*[@text = ""]'


    # 핀다 포스트 나가기
    finda_post_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'


    # 내폰 지키미 진입
    my_phorn = MobileBy.XPATH, '//*[@text = "내 폰 지키미"]'
    my_phorn_Result = MobileBy.XPATH, "//*[contains(@text, '내 폰 보호하기')]"

    # 내폰 지키미 > 뒤로가기
    my_phorn_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'

    # 돈되는 혜택
    event = MobileBy.XPATH, '//*[@text = "돈되는 혜택"]'

    # 돈되는 혜택 결과
    event_Result = MobileBy.XPATH, '//*[@text = "돈되는 혜택"]'

    # 이벤트 나가기
    event_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 공지사항
    notice = MobileBy.XPATH, '//*[@text = "공지사항"]'

    # 공지사항 진입 결과
    notice_Result = MobileBy.XPATH, '//*[@text = "공지사항"]'


    # 공지사항 컨텐츠 진입
    notice_in = MobileBy.XPATH, "//*[contains(@text, '정기적 수신 동의')]"

    # 공지사항 컨텐츠 진입 결과
    notice_in_Result = MobileBy.XPATH, '//*[contains(@text, "안녕하세요")]'

    # 공지사항 컨텐츠 > 뒤로가기
    notice_in_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]'

    # 공지사항 나가기
    notice_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 대출후기
    loan_reviews = MobileBy.XPATH, '//*[@text = "대출후기"]'

    # 대출후기 진입 결과
    loan_reviews_Result = MobileBy.XPATH, "//*[contains(@text, '핀다 고객님이 남겨주신')]"

    # 대출후기 > 뒤로가기
    loan_reviews_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'

    # 최근 알림 진입
    alarm = MobileBy.XPATH, "//*[contains(@text, '최근 알림')]"

    # 최근알림 진입 결과
    alarm_Result = MobileBy.XPATH, "//*[contains(@text, '알림 설정')]"

    # 최근 알림 뒤로가기
    alarm_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'

    # 포인트 진입
    point = MobileBy.XPATH, "//*[contains(@text, '포인트')]"

    # 출석체크 진입
    checkin = MobileBy.XPATH, "//*[contains(@text, '출석체크')]"

    priceforecast = MobileBy.XPATH, "//*[contains(@text, '물가예측 시즌1')]"

    priceforecast_result = MobileBy.XPATH, "//*[contains(@text, '포인트 받기')]"

    priceforecast_history = MobileBy.XPATH, "//*[contains(@text, '물가예측 참여내역')]"

    priceforecast_history_result = MobileBy.XPATH, "//*[contains(@text, '받은 예측 포인트')]"


    # 설정 영역 --------------------------------------

    # 설정 페이지
    seting_buttun = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 설정 > 내 정보
    myinfo = MobileBy.XPATH, '//*[@text = "내 정보"]'

    # 설정 > 내 정보 진입 결과
    myinfo_result_a = MobileBy.XPATH, '//*[@text = "내 정보 확인"]'
    myinfo_result_b = MobileBy.XPATH, '//*[@text = "'+info.phone_number+'"]'
    myinfo_result_c = MobileBy.XPATH, '//*[@text = "'+info.news_agency+'"]'
    myinfo_result_d = MobileBy.XPATH, '//*[@text = "'+info.name+'"]'

    # 설정 > 내 정보 > 수정하기
    myinfo_edit = MobileBy.XPATH, '//*[@text = "수정하기"]'

    # 설정 > 내 정보 > 수정하기 > 본인 인증하기
    myinfo_authenticate_yourself = MobileBy.XPATH, '//*[@text = "본인 인증하기"]'

    # 설정 > 내 정보 > 수정하기 > 본인 인증하기 동작 결과
    myinfo_result = MobileBy.XPATH, '//*[@text = "시작하기"]'

    # 설정 > 알림설정 진입
    notification_settings = MobileBy.XPATH, "//*[contains(@text, '알림 설정')]"

    # 설정 > 알림설정 결과
    notification_settings_result = MobileBy.XPATH, "//*[contains(@text, '유용한 이벤트 및 혜택')]"

    # 설정 > 비밀번호 변경
    changepassword = MobileBy.XPATH, '//*[@text = "비밀번호 변경"]'

    # 설정 > 비밀번호 변경 > 현재 비밀번호 입력
    changepassword_a = MobileBy.XPATH, "//*[contains(@text, '현재 비밀번호')]"

    # 설정 > 비밀번호 변경 > 새로운 비밀번호 입력
    changepassword_b = MobileBy.XPATH, "//*[contains(@text, '사용할 비밀번호')]"

    # 설정 > 비밀번호 변경 > 새로운 비밀번호 재 입력
    changepassword_c = MobileBy.XPATH, "//*[contains(@text, '확인을 위해 재입력')]"

    # 설정 > 금융 정보 관리(마이데이터)
    seting_mtdata = MobileBy.XPATH, '//*[@text = "마이데이터 연결 내역 관리"]'
    seting_mtdata_result_a = MobileBy.XPATH, '//*[@text = "연결내역 관리하기"]'
    seting_mtdata_result_b = MobileBy.XPATH, "//*[contains(@text, '마이데이터 연결로 이동합니다.')]"

    # 설정 > 개인신용정보 이용/제공 내역 조회 진입
    credit_information_history = MobileBy.XPATH, '//*[@text = "개인신용정보 이용/제공 내역 조회"]'
    credit_information_history_result = MobileBy.XPATH, '//*[@text = "개인정보 이용·제공 내역 조회"]'

    # 설정 > 이용약관
    seting_terms_of_use = MobileBy.XPATH, '//*[@text = "이용약관"]'
    seting_terms_of_use_result = MobileBy.XPATH, "//*[contains(@text, '서비스 이용약관')]"

    # 설정 > 개인정보 처리방침
    seting_privacy_policy = MobileBy.XPATH, '//*[@text = "개인정보 처리방침"]'
    seting_privacy_policy_result = MobileBy.XPATH, "//*[contains(@text, '개인정보처리방침')]"

    # 설정 > 마이데이터 서비스 이용약관
    seting_mydata_service_terms_of_use = MobileBy.XPATH, '//*[@text = "마이데이터 서비스 이용약관"]'
    seting_mydata_service_terms_of_use_result = MobileBy.XPATH, "//*[contains(@text, '[마이데이터]')]"

    # 설정 > 금융소비자보호 고지사항
    financial_consumer_protection_notice = MobileBy.XPATH, '//*[@text = "금융소비자보호 고지사항"]'
    financial_consumer_protection_notice_result = MobileBy.XPATH, "//*[contains(@text, '금융소비자보호')]"

    # 설정 > 버전 정보
    seting_version = MobileBy.XPATH, '//*[@text = "버전 정보"]'
    seting_version_result = MobileBy.XPATH, "//*[contains(@text, '현재버전')]"

    # 설정 > 오픈소스 라이선스
    open_source_license = MobileBy.XPATH, '//*[@text = "오픈소스 라이선스"]'
    open_source_license_result = MobileBy.XPATH, "//*[contains(@text, 'Accom')]"