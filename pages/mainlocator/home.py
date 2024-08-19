from appium.webdriver.common.mobileby import MobileBy

from config.info import InFo


class Home:

    info = InFo()
    # 마이홈 비교대출 배너
    myhome_loans_Result_a = '//*[@text = "대출 한도 조회 📌"]'
    myhome_loans_Result_b = "//*[contains(@text, '대출 알아보기')]"
    loans_a = '//*[@text = "내 대출 한도 한번에 조회하기"]'
    loans_b = '//*[@text = "내게 맞는 더 좋은 대출 찾기"]'
    loans_c = '//*[@text = "다른 방법 알아보기"]'
    loans_d = '//*[@text = "나에게 딱 맞는 대출 찾기"]'
    loans_e = "//*[contains(@text, '대출 이어서 진행하기')]"
    loans_f = '//*[@text = "대출받기"]'

    # 퀵메뉴
    quick_menu_a = MobileBy.XPATH, "//*[contains(@text, '대출받기')]"
    quick_menu_b = MobileBy.XPATH, "//*[contains(@text, '대출갈아타기')]"
    quick_menu_c = MobileBy.XPATH, "//*[contains(@text, '사업자대출')]"
    quick_menu_d = MobileBy.XPATH, "//*[contains(@text, '주택담보대출')]"
    quick_menu_e = MobileBy.XPATH, "//*[contains(@text, '전세대출')]"
    quick_menu_f = MobileBy.XPATH, "//*[contains(@text, '차 구매대출')]"
    quick_menu_g = MobileBy.XPATH, "//*[contains(@text, '차 리스렌트')]"

    # 큇메뉴 진입 결과
    result_quick_menu_a = MobileBy.XPATH, "//*[contains(@text, '신용대출 조건 비교하기')]"
    result_quick_menu_b = MobileBy.XPATH, "//*[contains(@text, '대출 갈아타기')]"
    result_quick_menu_c = MobileBy.XPATH, "//*[contains(@text, '사업자대출 조건 비교하기')]"
    result_quick_menu_d = MobileBy.XPATH, "//*[contains(@text, '주택담보대출 조건 비교하기')]"
    result_quick_menu_e = MobileBy.XPATH, "//*[contains(@text, '전세자금대출 조건 비교하기')]"
    result_quick_menu_f = MobileBy.XPATH, "//*[contains(@text, '1분만에 내 한도 알아보기')]"

    # 마이홈 대출진단 배너
    loandiagnosisbanner_a = "//*[contains(@text, '30일 대환 챌린지')]"
    loandiagnosisbanner_aa = "//*[contains(@text, '시작하기')]"
    loandiagnosisbanner_b = "//*[contains(@text, '늘어난 대출이자에')]"
    loandiagnosisbanner_bb = "//*[contains(@text, '클릭 한번에')]"
    loandiagnosisbanner_g = "//*[contains(@text, '레벨업!')]"
    loandiagnosisbanner_gg = "//*[contains(@text, '챌린지 바로가기')]"
    loandiagnosisbanner_c = "//*[contains(@text, '실버 달성')]"
    loandiagnosisbanner_d = "//*[contains(@text, '토파즈 달성')]"
    loandiagnosisbanner_e = "//*[contains(@text, '사파이어 달성')]"
    loandiagnosisbanner_f = "//*[contains(@text, '다이아몬드 달성')]"
    loandiagnosisbanner_h = "//*[contains(@text, '마스터 달성')]"

    # 대환대출 진입 결과
    refinanceloanfirstvisit_a = MobileBy.XPATH, '//*[@text = "다시 오픈할 때 알림받기"]'
    refinanceloanfirstvisit_b = MobileBy.XPATH, "//*[contains(@text, '챌린지 시작')]"
    refinance_loan_challenge = MobileBy.XPATH, '//*[@text = "대환 챌린지"]'
    refinance_loan_challenge_a = MobileBy.XPATH, '//*[@text = "챌린지를 시작하면 이자를\n연 최대 331만원 아낄 수 있어요!"]'
    refinance_loan_challenge_b = MobileBy.XPATH, '//*[@text = "당신은 Lv.1 될성부른 꿈나무"]'
    refinance_loan_challenge_c = MobileBy.XPATH, '//*[@text = "당신은 Lv.2 성실한 우등생"]'
    refinance_loan_challenge_d = MobileBy.XPATH, '//*[@text = "당신은 Lv.3 만랩 마스터"]'

    # 내 대출 배너
    loan_banner = MobileBy.XPATH, "//*[@text = '금융생활']"
    loan_a = MobileBy.XPATH,"//*[contains(@text, '남은 대출금')]"

    # 내 현금자산 배너
    cash_assets_banner = "//*[contains(@text, '내 현금자산')]"
    cash_assets_banner_result = "//*[contains(@text, '내 자산')]"
    cash_assets_banner_a = "//*[contains(@text, '입출금')]"
    # cash_assets_banner_a_result = '//*[@text = "저축예금"]'
    cash_assets_banner_b = "//*[contains(@text, '예적금')]"
    # cash_assets_banner_b_result = '//*[@text = "청년 우대형 주택청약종합저축"]'

    # 상환 예정 배너
    repayment_schedule_banner = '//*[@text = "상환 ∙ 결제 예정"]'
    notification_enabled_on = '//*[@text = "알림 받기"]'
    notification_enabled_off = '//*[@text = "알림받는중"]'
    repayment_schedule = '//*[@text = "이달의 총 나가는 돈"]'

    # 장기렌트 리스 배너
    lease_contract_banner = MobileBy.XPATH, '//*[@text = "차 리스렌트"]'


    # 차 구매 대출 배너
    auto_loan_banner = MobileBy.XPATH, '//*[@text = "차 구매대출"]'


    # 신용점수
    credit_score = MobileBy.XPATH, "//*[contains(@text, '눌러서 보기')]"
