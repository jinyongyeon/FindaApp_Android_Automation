
class Home:

    # 마이홈 비교대출 배너
    myhome_loans_Result_a = '//*[@text = "대출 한도 조회 📌"]'
    myhome_loans_Result_b = '//*[@text = "대출 알아보기"]'
    loans_a = '//*[@text = "내 대출 한도 한번에 조회하기"]'
    loans_b = '//*[@text = "내게 맞는 더 좋은 대출 찾기"]'
    loans_c = '//*[@text = "다른 방법 알아보기"]'
    loans_d = '//*[@text = "나에게 딱 맞는 대출 찾기"]'
    loans_e = '//*[@text = "대출 이어서 진행하기"]'

    # 마이홈 대출진단 배너
    loandiagnosisbanner_a = "//*[contains(@text, '30일 대환 챌린지')]"
    loandiagnosisbanner_aa = "//*[contains(@text, '시작하기')]"
    loandiagnosisbanner_b = "//*[contains(@text, '늘어난 대출이자에')]"
    loandiagnosisbanner_bb = "//*[contains(@text, '클릭 한번에')]"
    loandiagnosisbanner_c = '//*[@text = "한도조회 누적 달성 1회!"]'
    loandiagnosisbanner_d = '//*[@text = "한도조회 누적 달성 2회!"]'
    loandiagnosisbanner_e = '//*[@text = "한도조회 누적 달성 3회!"]'
    loandiagnosisbanner_f = '//*[@text = "한도조회 누적 달성 4회!"]'

    # 대환대출 진입 결과
    refinanceloanfirstvisit_a = '//*[@text = "내 대출 계좌 연결하기"]'
    refinanceloanfirstvisit_b = '//*[@text = "챌린지 시작하기"]'
    refinance_loan_challenge = '//*[@text = "대환 챌린지"]'
    refinance_loan_challenge_a = '//*[@text = "챌린지를 시작하면 이자를\n연 최대 331만원 아낄 수 있어요!"]'
    refinance_loan_challenge_b = '//*[@text = "당신은 Lv.1 될성부른 꿈나무"]'
    refinance_loan_challenge_c = '//*[@text = "당신은 Lv.2 성실한 우등생"]'
    refinance_loan_challenge_d = '//*[@text = "당신은 Lv.3 만랩 마스터"]'

    # 내 대출 배너
    loan_banner = '//*[@text = "내 대출 2"]'
    loan_a = "//*[contains(@text, '주택도시기금 청년취업(창업)')]"
    loan_aaa = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.view.View[4]'
    loan_aa = '//*[@text = "1.3%"]'
    loan_b = "//*[contains(@text, '주택도시기금 버팀목전세자금')]"
    loan_bbb = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.view.View[5]'
    loan_bb = '//*[@text = "2.1%"]'

    # 내 현금자산 배너
    cash_assets_banner = "//*[contains(@text, '내 현금자산')]"
    cash_assets_banner_result = "//*[contains(@text, '진용연님의 현금자산은')]"
    cash_assets_banner_a = "//*[contains(@text, '입출금')]"
    cash_assets_banner_a_result = '//*[@text = "저축예금"]'
    cash_assets_banner_b = "//*[contains(@text, '예적금')]"
    cash_assets_banner_b_result = '//*[@text = "청년 우대형 주택청약종합저축"]'

    # 상환 예정 배너
    repayment_schedule_banner = '//*[@text = "상환 예정"]'
    notification_enabled_on = '//*[@text = "알림 받기"]'
    notification_enabled_off = '//*[@text = "알림받는중"]'
    repayment_schedule = '//*[@text = "이번달 총 상환액"]'

    # 장기렌트 리스 배너
    lease_contract_banner = '//*[@text = "장기렌트·리스"]'


    # 차 구매 대출 배너
    auto_loan_banner = '//*[@text = "차 구매 대출"]'

