import time

import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo
from drivers.aos_webdrivers import WebDriver


class Etc:

    info = InFo()


    # 더보기 탭
    etc = '//*[@text = "더보기"]'
    # 더보기 진입 결과
    etc_Result = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[@text = "더보기"]'
    # 내 대출
    myloan = '//*[@index = "1" and @text = "내 대출"]'

    # 내 대출 진입 결과
    myloan_Result_a = '//*[@text = "내 현금흐름"]'
    myloan_Result_b = '//*[@text = "대출"]'
    myloan_Result_c = '//*[@text = "입출금"]'
    myloan_Result_d = '//*[@text = "예적금"]'

    # 브레이즈 배너
    banner_exit = '//*[@text = "테스트"]'
    # 내 대출 뒤로가기
    myloan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]'

    # 1:1 채팅문의
    chatting = '//*[@text = "1:1 채팅문의"]'

     # 1:1 채팅문의 진입 결과
    chatting_Result = '//*[@text = "채널톡 이용중"]'
     # 1:1 채팅 닫기
    chatting_exit = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView"

    # 자주묻는 질문
    qna = '//*[@text = "자주 묻는 질문"]'

    # 자주묻는 질문 > 질문 항목
    qna_a = '//*[@text = "정말 이 조건 그대로 대출 가능한가요?"]'
    qna_Result_a = '네, 가능합니다. 고객님께서 입력해주신 정보의 정확도 등에 따라 금융사 최종심사에 일부 차이가 발생할 수 있지만, 정확한 정보 입력 후 공동인증서를 연동하여 조회하셨다면 실제 심사결과에 부합하는 조건을 받아보실 수 있습니다.'
    qna_b = '//*[@text = "신청하면 대출금은 언제 입금이 되나요?"]'
    qna_Result_b = '대출이 확정된 후 대출금이 입금되기까지는 금융사마다 차이가 존재합니다. 빠르게 처리가 이루어지는 경우 입금까지 5분이내에 입금이 이루어지며, 고객과의 전화통화 이후 대출이 진행되는 경우에는 몇 시간에서 1~2영업일 가량 소요되기도 합니다. 일반적으로는 금융사의 영업일/영업시간 내에만 입금이 진행되지만, 주말/공휴일을 포함하여 24시간 대출금 입금이 가능한 금융사 또한 존재합니다.'
    qna_c = '//*[@text = "대출 조건은 언제까지 유효한가요?"]'
    qna_Result_c = '조회하신 대출 조건은 조회 당일 자정까지만 유효하며, 다음날 조회 시 조건이 달라질 수 있습니다. 매일 조금씩 조건이 달라지는만큼, 대출이 필요한 시기에 맞춰 한도조회를 다시 진행해 주시면 가장 정확한 조건을 확인하실 수 있습니다.'
    qna_d = '//*[@text = "대출을 알아보는 것으로, 불이익이 있나요?"]'
    qna_Result_d = '대출조회는 신용점수에 전혀 영향을 미치지 않습니다. 2011년 10월, 금융위원회는 대출조회가 신용점수에 불이익을 주지 않도록 정책을 변경하였습니다. 또한, 핀다는 단 1건의 신용조회로 60개 이상 금융사의 금융상품 중 고객님께 맞는 상품을 안내해 드리고 있으니 걱정없이 대출상품을 알아 볼 수 있습니다. * 단, 단기간 너무 많은 조회를 할 경우 ‘대출사기’로 의심되어 대출이 거절될 수 있습니다. * 핀다를 통한 한도조회는 주 2~3회가 적합합니다.'
    qna_e = '//*[@text = "신용조회가 여러 건 발생했다고 하는데 무슨 일인가요?"]'
    qna_Result_e = '걱정하지 마세요. 핀다에서는 여러 금융사의 상품을 조회해도, 단 1건의 신용조회로 처리됩니다. 신용평가회사에 따라 내역 조회 시, 여러 건으로 표기가 되기도 하지만 실제 신용조회기록에 반영되는 것은 ‘핀다’ 플랫폼 코드 1건만이 반영됩니다. 또한, 신용조회는 신용점수에 영향을 주지 않으니 안심하고 핀다를 이용하세요!'

    # 자주묻는 질문 뒤로가뒤
    qna_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Image"

    # 대출 갈아타기
    refinancing_loan = '//*[@text = "대출 갈아타기"]'
    refinancing_loan_Result_a = '//*[@text = "대출 갈아타러 가기"]'
    refinancing_loan_Result_b = '//*[@text = "매월 부담되는 이자를\n지금 바로 줄이고 싶다면?"]'

    # 대출 한 번에 비교
    comparison_loan = '//*[@text = "대출 한 번에 비교"]'

    # 대출 한 번에 비교 결과
    comparison_loan_Result_a = '//*[@text = "오늘의 내 최저금리 알아보기"]'
    # comparison_loan_Result_a = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'
    # comparison_loan_Result_b = '//*[@text = "오늘입금"]'
    comparison_loan_Result_b = '//*[@text = "오늘입금"]'

    # 대출 한 번에 비교 뒤로가기
    comparison_loan_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View/android.widget.Button"

    comparison_loan_back_b = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[1]"
    comparison_loan_back_b_a = '//*[@text = "나가기"]'


    # 자동차 구매 대출
    auto_loan = '//*[@text = "자동차 구매 대출"]'

    # 자동차 구매 대출 진입 결과
    auto_loan_Result_a = '//*[@text = "1분만에 내 한도 알아보기"]'
    auto_loan_Result_b = '//*[@text = "'+info.name+'님의\n가장 좋은 대출 조건이에요."]'

    # 자동차 구매 대출 뒤로가기
    auto_loan_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]"

    # 전월세 추천
    charter = '//*[@text = "전월세 추천"]'

    # 전월세 추천 진입 결과
    charter_Result_a = '//*[@text = "전월세대출 맞춤추천"]'
    charter_Result_b = '//*[@text = "1:1 맞춤형 전월세대출 가이드"]'

    # 전원세 뒤로가기
    charter_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 30일 안에 대출 갈아타기
    change_loan = '//*[@text = "30일 대출 챌린지"]'

    # 30일 안에 대출 갈아타기 결과
    change_loan_Result_a = '//*[@text = "매주 한도조회하면 내 레벨도 함께 높아져요"]'
    change_loan_Result_b = '//*[@text = "30일 대환 챌린지 Beta"]'

    # 30일 안에 대출 갈아타기 뒤로가기
    change_loan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'


    # 나의 금융정보 > 내 대출 진입
    myloan_B = '//*[@index = "0" and @text = "내 대출"]'

    # 나의 금융정보 > 상환일정
    amortization_schedule = '//*[@text = "상환일정"]'

    # 상환일정 진입 결과
    amortization_schedule_a = '//*[@text = "이번달 총 상환액"]'
    amortization_schedule_b = '//*[@text = "상환 일정이 없습니다."]'

    # 나의 금융정보 > 상환일정 뒤로가기
    amortization_schedule_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 신용관리 > 신용점수 진입
    credit_score = '//*[@text = "신용점수"]'

    # 신용점수 페이지 진입 결과
    credit_score_Result = '//*[@text = "내 신용점수"]'

    # 신용관리 > 신용점수 뒤로가기
    credit_score_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]'

    # 신용관리 > 신용점수 올리기 진입
    improve_credit_score = '//*[@text = "신용점수 올리기"]'

    # 신용점수 올리기 진입 결과
    improve_credit_score_Result_a = '//*[@text = "신용점수 올리고\n대출이자 낮춰봐요"]'
    improve_credit_score_Result_b = '//*[@text = "최근 6개월내 신용점수 올리기를\n이용했어요"]'

    # 신용관리 > 신용점수 올리기 뒤로가기
    improve_credit_score_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]'

    # 신용관리 > 신용점수 상승 전략 진입
    credit_analysis = '//*[@text = "신용점수 상승 전략"]'

    # 신용관리 > 신용점수 상승 전략 진입 결과
    credit_analysis_Result = '//*[@text = "신용점수 상승 전략"]'

    # 신용관리 > 신용점수 상승 전략 뒤로가기
    credit_analysis_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 신용관리 > 신용점수 히스트리 진입
    credit_history = '//*[@text = "신용점수 히스토리"]'

    # 신용관리 > 신용점수 히스트리 진입 결과
    credit_history_Result = '//*[@text = "신용점수 히스토리"]'

    # 신용관리 > 신용점수 히스트리 뒤로가기
    credit_history_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 여윳돈 계산기 진입
    extra_money = '//*[@text = "여윳돈 계산기"]'

    # 계산기 > 여윳돈 계산기 진입 결과
    extra_money_Result = '//*[@text = "상환할 여윳돈이 생기셨나요?"]'

    # 계산기 > 여윳돈 계산기 뒤로가기
    extra_money_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 계산기 > DSR계산기 진입
    dsr = '//*[@text = "DSR 계산기"]'

    # 계산기 > DSR계산기 진입 결과
    dsr_Result = '//*[@text = "DSR 계산기"]'

    # 계산기 > DSR계산기 뒤로가기
    dsr_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 계산기 > 대출이자 계산기 진입
    interest = '//*[@text = "대출이자 계산기"]'

    # 대출이자 계산기 결과
    interest_Result = '//*[@text = "대출이자 계산기"]'

    # 계산기 > 대출이자 계산기 뒤로가기
    interest_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 연말정산 계산기 진입
    year_end_settlement = '//*[@text = "연말정산 계산기"]'

    # 연말정산 계산기 결과
    year_end_settlement_Result = '//*[@text = "카드 및 현금 소비액 소득공제"]'

    # 계산기 > 연말정산 계산기 뒤로가기
    year_end_settlement_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 전세 vs 월세 계산기 진입
    charter_vs_monthly_rent = '//*[@text = "전세 vs 월세 계산기"]'

    # 전세 vs 월세 계산기 결과
    charter_vs_monthly_rent_Result = '//*[@text = "전세 vs 월세 계산기"]'

    # 계산기 > 전세 vs 월세 계산기 뒤로가기
    charter_vs_monthly_rent_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 계산기 > 대출 갈아타기 계산기 진입
    refinancing_loan = '//*[@text = "대출 갈아타기 계산기"]'

    # 대출 갈아타기 계산기 결과
    refinancing_loan_Result = '//*[@text = "대출 갈아타기 계산기"]'

    # 계산기 > 대출 갈아타기 계산기 뒤로가기
    refinancing_loan_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View/android.widget.Button'

    # 부가서비스 > 장기렌트 리스 진입
    lease_rent = '//*[@text = "장기렌트 리스"]'

    # 부가서비스 > 장기렌트 리스 진입 결과
    lease_rent_Result = '//*[@text = "리스렌트"]'

    # 부가서비스 > 장기렌트 리스 뒤로가기
    lease_rent_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    # 부가서비스 > 금융 스팸 차단 진입
    do_not_call = '//*[@text = "금융 스팸 차단"]'

    # 부가서비스 > 금융 스팸 차단택 한 번에 차단하기 CTA 선택
    do_not_call_cta = '//*[@text = "한 번에 차단하기"]'

    # 두낫콜 약관 펼치기 1
    do_not_call_a = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View'

    # 두낫콜 약관 펼치기 2
    do_not_call_b = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View'

    # 두낫콜 약관 펼치기 3
    do_not_call_c = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[6]/android.view.View'

    # 연락중지청구(Do-not-call) 서비스 이용약관
    do_not_call_a_a = '//*[@text = "연락중지청구(Do-not-call) 서비스 이용약관"]'

    # 개인정보 수집·이용에 대한 동의
    do_not_call_a_b = '//*[@text = "개인정보 수집·이용에 대한 동의"]'

    # 개인정보처리방침
    do_not_call_a_c = '//*[@text = "개인정보처리방침"]'

    # 두낫콜 서비스 이용약관 진입 결과 A
    do_not_call_a_Result = '//*[@text = "두낫콜 본인확인"]'

    # 개인정보이용동의
    do_not_call_b_a = '//*[@text = "개인정보이용동의"]'

    # 고유식별정보처리동의
    do_not_call_b_b = '//*[@text = "고유식별정보처리동의"]'

    # 서비스이용약관동의
    do_not_call_b_c = '//*[@text = "서비스이용약관동의"]'

    # 통신사이용약관동의
    do_not_call_b_d = '//*[@text = "통신사이용약관동의"]'

    # 두낫콜 서비스 이용약관 진입 결과 B 실패
    do_not_call_b_Result = '//*[@text = "사이트에 연결할 수 없음"]'

    # [금융스팸차단하기] 서비스 이용 약관
    do_not_call_c_a = '//*[@text = "[금융스팸차단하기] 서비스 이용 약관"]'

    # [금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)
    do_not_call_c_b = '//*[@text = "[금융스팸차단하기] 개인(신용)정보 수집.이용 동의(필수)"]'

    # [금융스팸차단하기] 개인(신용)정보 제3자 제공 동의(필수)
    do_not_call_c_c = '//*[@text = "[금융스팸차단하기] 개인(신용)정보 제3자 제공 동의(필수)"]'

    # 두낫콜 서비스 이용약관 진입 결과 C 실패
    do_not_call_c_Result = '//*[@text = "페이지를 찾을 수 없습니다"]'

    # 웹뷰 나가기 버튼
    webview_exit = '//*[@content-desc = "탭 닫기"]'

    # 두낫콜 나가기 버튼
    do_not_call_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]'

    # 두낫콜 나가기 > 중단하기 버튼
    do_not_call_stop = '//*[@text = "중단하기"]'

    # 대출금 갚아주는 보험
    insurance = '//*[@text = "대출금 갚아주는 보험"]'

    # 대출금 갚아주는 보험 결과
    insurance_Result = '//*[@text = "BNP파리바 카디프생명"]'

    # 예적금 비교 진입
    deposit_and_savings = '//*[@text = "예적금 비교"]'

    # 예적금 비교 결과
    deposit_and_savings_Result = '//*[@text = "예적금 비교"]'

    # 예적금 비교 > 뒤로가기
    deposit_and_savings_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'

    # 핀다 포스트 진입
    finda_post = '//*[@text = "핀다포스트"]'

    # 핀다 포스트 진입 결과
    finda_post_Result = '//*[@text = "핀다포스트"]'

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
    finda_post_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'


    # 내폰 지키미 진입
    my_phorn = '//*[@text = "내 폰 지키미"]'

    # 내폰 지키미 진입
    my_phorn_Result = '//*[@text = "내 폰 보호하기"]'

    # 내폰 지키미 > 뒤로가기
    my_phorn_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'

    # 이벤트
    event = '//*[@text = "이벤트"]'

    # 이벤트 결과
    event_Result = '//*[@text = "진행 중인 이벤트"]'

    # 이벤트 나가기
    event_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 공지사항
    notice = '//*[@text = "공지사항"]'

    # 공지사항 진입 결과
    notice_Result = '//*[@text = "공지사항"]'


    # 공지사항 컨텐츠 진입
    notice_in = '//*[@text = "2차 대출 환승 이벤트 당첨자 안내"]'

    # 공지사항 컨텐츠 진입 결과
    notice_in_Result = '//*[@text = "안녕하세요 핀다입니다."]'

    # 공지사항 컨텐츠 > 뒤로가기
    notice_in_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]'

    # 공지사항 나가기
    notice_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

    # 대출후기
    loan_reviews = '//*[@text = "대출후기"]'

    # 대출후기 진입 결과
    loan_reviews_Result = '//*[@text = "핀다 신용대출 신청 서비스로\n대출받으신 고객님들의 후기입니다."]'

    # 대출후기 > 뒤로가기
    loan_reviews_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'

    # 최근 알림 진입
    alarm = '//*[@text = "최근 알림"]'

    # 최근알림 진입 결과
    alarm_Result = '//*[@text = "최근 알림"]'

    # 최근 알림 뒤로가기
    alarm_back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Image'



    # 설정 페이지
    seting_buttun = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]'

