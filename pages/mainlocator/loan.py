from config.info import InFo


class Loan:

    auto_loan_inquiry = '//*[@text = "1분만에 내 한도 알아보기"]'

    auto_loan_terms_a = '//*[@text = "본인인증 필수 항목 모두 동의"]'
    auto_loan_terms_a_unfold = '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View'
    auto_loan_terms_aa = '//*[@text = "통신사 이용 약관"]'
    auto_loan_terms_aa_r = '//*[@text = "통신사 이용약관"]'
    auto_loan_terms_ab = '//*[@text = "개인정보취급동의"]'
    auto_loan_terms_ab_r = '//*[@text = "개인정보 수집/이용/취급 위탁동의"]'
    auto_loan_terms_ac = '//*[@text = "고유식별정보처리 동의"]'
    auto_loan_terms_ac_r = '//*[@text = "고유식별정보처리 동의"]'
    auto_loan_terms_ad = '//*[@text = "본인확인서비스 이용약관"]'
    auto_loan_terms_ad_r = '//*[@text = "본인확인서비스 이용약관"]'
    auto_loan_terms_ae = '//*[@text = "개인정보 제3자 동의 (KT, LGU+ 알뜰폰)"]'
    auto_loan_terms_ae_r = '//*[@text = "개인정보 제3자 제공 동의"]'

    auto_loan_terms_b = '//*[@text = "핀다 필수 항목 동의"]'
    auto_loan_terms_b_unfold = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[2]/android.view.View'
    auto_loan_terms_ba = '//*[@text = "오토론 서비스 이용약관"]'
    auto_loan_terms_ba_r = '//*[@text = "서비스 이용 약관 [오토론]"]'
    auto_loan_terms_bb = '//*[@text = "핀다 개인(신용)정보 수집이용제공 동의서"]'
    auto_loan_terms_bb_r = '//*[@text = "핀다 개인(신용)정보 수집이용제공 동의[오토론]"]'


    auto_loan_terms_c = '//*[@text = "금융기관 필수 항목 동의"]'
    auto_loan_terms_c_unfold = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[3]/android.view.View'
    auto_loan_terms_ca = '//*[@text = "금융기관 개인(신용)정보 수집이용제공 동의[오토론]"]'
    auto_loan_terms_ca_r = '//*[@text = "금융기관 개인(신용)정보 수집이용제공 동의[오토론]"]'
    auto_loan_terms_cb = '//*[@text = "개인(신용)정보 조회 동의서[오토론]"]'
    auto_loan_terms_cb_r = '//*[@text = "개인(신용)정보 조회 동의서[오토론]"]'
    auto_loan_terms_cc = '//*[@text = "개인(신용)정보 수집 이용 제공 동의서[오토론]"]'
    auto_loan_terms_cc_r = '//*[@text = "개인(신용)정보 수집 이용 제공 동의서[오토론]"]'
    auto_loan_terms_cd = '//*[@text = "개인(신용)정보 수집이용제공동의서[가계여신 금융 거래][오토론]"]'
    auto_loan_terms_cd_r = '//*[@text = "개인(신용)정보 수집이용제공동의서[가계여신 금융 거래][오토론]"]'
    auto_loan_terms_ce = '//*[@text = "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용) [오토론]"]'
    auto_loan_terms_ce_r = '//*[@text = "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[오토론]"]'
    auto_loan_terms_cf = '//*[@text = "개인정보 제 3자 제공 동의서[OPENAPI][오토론]"]'
    auto_loan_terms_cf_r = '//*[@text = "개인정보 제 3자 제공 동의서[OPENAPI][오토론]"]'

    auto_loan_terms_all = '//*[@text = "약관 전체 동의"]'

    auto_loan_terms_check = '//*[@text = "확인"]'
    auto_loan_terms_next = '//*[@text = "다음"]'

    auto_loan_certification_number = '//*[@text = "주민등록번호 뒷자리 입력"]'

    auto_loan_rrn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View'

    auto_loan_annual_income = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View'

    auto_loan_new = '//*[@text = "새로운 대출 받기"]'

    auto_loan_newcar = '//*[@text = "신차"]'

    auto_loan_result = '//*[@text = "'+InFo.name+'님의\n가장 좋은 대출 조건이에요."]'

    auto_loan_result_a = '//*[@text = "아쉽게도\n신청이 어려워요"]'

    auto_loan_detail = '//*[@text = "하나은행"]'

    auto_loan_detail_result = '//*[@text = "조회결과"]'

    auto_loan_application = '//*[@text = "대출 신청하기"]'

    auto_loan_application_r_a = '//*[@text = "하나은행 홈페이지로\n이동할게요"]'
    auto_loan_application_r_b = '//*[@text = "대출 신청"]'
    auto_loan_application_r_c = '//*[@text = "서류 제출"]'
    auto_loan_application_r_d = '//*[@text = "약정 및 입금"]'
    auto_loan_application_r_e = '//*[@text = "출고 확인"]'
    auto_loan_application_r_f = '//*[@text = "진행을 위해 이런 서류들이 필요해요!"]'

    auto_loan_url_r = '//*[@text = "하나은행 X 핀다"]'

    auto_loan_application_exit = '//*[@text = "나가기"]'

    # 비교대출 로케이터

    # 다음 버튼
    next_loan = '//*[@text = "다음"]'

    # 확인 버튼
    check_loan = '//*[@text = "확인"]'

    # 비교대출 온보딩페이지 CTA버튼
    loan_in = '//*[@text = "오늘의 내 최저금리 알아보기"]'

    # 대출 목적
    #생활비
    living_expenses = '//*[@text = "생활비"]'
    # 자동차 구입
    auto_loan = '//*[@text = "자동차구입"]'
    auto_loan_In = '//*[@text = "이동"]'

    # 대출 희망 금액
    loan_amount = '//*[@text = "희망 금액 입력"]'

    # 비교대출 서비스 약관
    loan_terms_and_conditions_A_result = '//*[@text = "본인인증 필수 항목 모두 동의"]'
    loan_terms_and_conditions_B_result = '//*[@text = "핀다 필수 항목 모두 동의"]'
    loan_terms_and_conditions_C_result = '//*[@text = "금융기관 필수 항목 모두 동의"]'
    loan_terms_and_conditions_D_result = '//*[@text = "서비스 이용 안내 수신 동의 (선택)"]'

    loan_terms_and_conditions_A = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.view.View'
    loan_terms_and_conditions_Aa = '//*[@text = "통신사 이용 약관"]'
    loan_terms_and_conditions_Aa_result = '//*[@text = "통신사 이용약관"]'
    loan_terms_and_conditions_Ab = '//*[@text = "개인정보취급동의"]'
    loan_terms_and_conditions_Ab_result = '//*[@text = "개인정보 수집/이용/취급 위탁동의"]'
    loan_terms_and_conditions_Ac = '//*[@text = "고유식별정보처리 동의"]'
    loan_terms_and_conditions_Ac_result = '//*[@text = "고유식별정보처리 동의"]'
    loan_terms_and_conditions_Ad = '//*[@text = "본인확인서비스 이용약관"]'
    loan_terms_and_conditions_Ad_result = '//*[@text = "KCB휴대폰 본인확인 이용약관"]'
    loan_terms_and_conditions_Ae = '//*[@text = "개인정보 제3자 동의 (KT, LGU+ 알뜰폰)"]'
    loan_terms_and_conditions_Ae_result = '//*[@text = "개인정보 제3자 제공 동의"]'

    loan_terms_and_conditions_B = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View'
    loan_terms_and_conditions_Ba = '//*[@text = "개인(신용)정보 수집·이용·제공 동의서(FINDA)"]'
    loan_terms_and_conditions_Ba_result = '//*[@text = "개인(신용)정보 수집·이용·제공 동의서(FINDA)"]'
    loan_terms_and_conditions_Bb = '//*[@text = "서비스 이용 약관 [비교대출]"]'
    loan_terms_and_conditions_Bb_result = '//*[@text = "서비스 이용 약관 [대출비교]"]'
    loan_terms_and_conditions_Bc = '//*[@text = "간편 인증 서비스 이용 약관 동의"]'
    loan_terms_and_conditions_Bc_result = '//*[@text = "[간편인증] 서비스 이용 약관 동의"]'
    loan_terms_and_conditions_Bd = '//*[@text = "간편 인증 개인 정보 이용 동의"]'
    loan_terms_and_conditions_Bd_result = '//*[@text = "[간편인증] 개인정보 이용 동의"]'
    loan_terms_and_conditions_Be = '//*[@text = "간편 인증 제 3자 제공 동의"]'
    loan_terms_and_conditions_Be_result = '//*[@text = "[간편인증] 제3자 정보제공 동의"]'
    loan_terms_and_conditions_Bf = '//*[@text = "간편 인증 고유식별번호처리 동의"]'
    loan_terms_and_conditions_Bf_result = '//*[@text = "[간편인증] 고유식별번호처리 동의"]'

    loan_terms_and_conditions_C = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]/android.view.View'
    loan_terms_and_conditions_Ca = '//*[@text = "개인정보 수집·이용·제공 동의서 (금융기관 용)"]'
    loan_terms_and_conditions_Ca_result = '//*[@text = "개인(신용)정보 수집·이용·제공 동의서(금융기관 용)"]'
    loan_terms_and_conditions_Cb = '//*[@text = "개인(신용)정보 조회 동의서(금융기관 용)"]'
    loan_terms_and_conditions_Cb_result = '//*[@text = "개인(신용)정보 수집·이용·제공·조회 동의서(금융기관 용)"]'
    loan_terms_and_conditions_Cc = '//*[@text = "고유식별정보 수집∙이용∙제공∙조회"]'
    loan_terms_and_conditions_Cc_result = '//*[@text = "고유식별정보 수집·이용·제공·조회 동의서"]'
    loan_terms_and_conditions_Cd = '//*[@text = "개인(신용)정보 조회 동의서(서민금융진흥원)"]'
    loan_terms_and_conditions_Cd_result = '//*[@text = "개인(신용)정보 조회 동의서(서민금융진흥원)"]'
    loan_terms_and_conditions_Ce = '//*[@text = "개인정보 수집·이용·제공 동의서 (서민금융진흥원)"]'
    loan_terms_and_conditions_Ce_result = '//*[@text = "개인정보 수집·이용·제공 동의서(서민금융진흥원)"]'
    loan_terms_and_conditions_Cf = '//*[@text = "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[비교대출]"]'
    loan_terms_and_conditions_Cf_result = '//*[@text = "계약 체결이행 등을 위한 상세 동의서(개인금융성 신용보험용)[비교대출]"]'
    loan_terms_and_conditions_Cg = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [토스뱅크][비교대출]"]'
    loan_terms_and_conditions_Cg_result = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [토스뱅크][비교대출]"]'
    loan_terms_and_conditions_Ch = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [중소기업중앙회][비교대출]"]'
    loan_terms_and_conditions_Ch_result = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [중소기업중앙회][비교대출]"]'
    loan_terms_and_conditions_Ci = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [OPENAPI][비교대출]"]'
    loan_terms_and_conditions_Ci_result = '//*[@text = "개인(신용)정보 제3자 제공 동의서 [OPENAPI][비교대출]"]'
    loan_terms_and_conditions_Cj = '//*[@text = "개인(신용)정보 수집 이용 동의서 [서민금융진흥원][비교대출]"]'
    loan_terms_and_conditions_Cj_result = '//*[@text = "개인(신용)정보 수집 이용 제공 조회 동의서 [서민금융진흥원][비교대출]"]'
    loan_terms_and_conditions_Ck = '//*[@text = "개인(신용)정보 제 3자 제공 조회 동의서 [대안정보이용][비교대출]"]'
    loan_terms_and_conditions_Ck_result = '//*[@text = "개인(신용)정보 제 3자 제공 조회 동의서 [대안정보이용][비교대출]"]'
    loan_terms_and_conditions_Cl = '//*[@text = "고유식별정보 수집∙이용 동의서[KCB대안신용평가모델]"]'
    loan_terms_and_conditions_Cl_result = '//*[@text = "고유식별정보 수집∙이용 동의서[KCB대안신용평가모델]"]'
    loan_terms_and_conditions_Cm = '//*[@text = "개인(신용)정보 이용 및 제3자 제공 동의서[KCB대안신용평가모델]"]'
    loan_terms_and_conditions_Cm_result = '//*[@text = "개인(신용)정보 이용 및 제3자 제공 동의서[KCB대안신용평가모델]"]'

    loan_terms_and_conditions_D = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View'
    loan_terms_and_conditions_Da = '//*[@text = "개인정보 제3자 제공 동의(대출안심플랜)"]'
    loan_terms_and_conditions_Da_result = '//*[@text = "개인정보 제3자 제공 동의(대출안심플랜)"]'

    # 약관 전체 동의
    loan_terms_and_conditions_all = '//*[@text = "약관 전체 동의"]'

    # 비교대출 인증번호 재요청
    comparison_loan_verification_resend = '//*[@text = "인증번호 재요청"]'

    # 비교대출 인증번호 결과
    comparison_loan_verification_result = '//*[@text = "주민등록번호 뒷자리 입력"]'

    # 주민등록번호 적합성 검사 결과
    rrn_validation_fail_result = '//*[@text = "주민등록번호를 다시 한 번 확인해주세요."]'
    rrn_validation_pass_result = '//*[@text = "소득 정보 입력"]'

    # 소득정보 : 직장인
    office_workers = '//*[@text = "직장인"]'
    company_name_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText'
    search = '//*[@text = "검색"]'
    company_number = '//*[@text = "1618700209"]'
    full_time = '//*[@text = "정규직"]'
    workplace_insurance = '//*[@text = "직장의료보험"]'
    region_insurance = '//*[@text = "지역의료보험"]'

    annual_income = '//*[@text = "연소득(세전) 입력"]'

    #후담대 정보
    my_house = '//*[@text = "자가"]'
    monthly_rent = '//*[@text = "전/월세"]'
    APT = '//*[@text = "아파트에요"]'
    address_search = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]'
    address_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText'
    home_address = '//*[@text = "김포시 걸포동 한강메트로자이2단지"]'
    area = '//*[@text = "45 평 (149.00 ㎡)"]'

    no_certificate = '//*[@text = "인증서 없이 대출 조회하기"]'

    #대출 종류
    type_of_loan = '//*[@text = "대출종류"]'

    #주택담보대출
    secured_loan_a = '//*[@text = "주택 담보대출 1"]'
    secured_loan_a_look = '//*[@text = "1개 결과 보기"]'
    secured_loan_b = '//*[@text = "주택 담보대출 2"]'
    secured_loan_b_look = '//*[@text = "2개 결과 보기"]'
    secured_loan_c = '//*[@text = "주택 담보대출 3"]'
    secured_loan_c_look = '//*[@text = "3개 결과 보기"]'
    secured_loan_d = '//*[@text = "주택 담보대출 4"]'
    secured_loan_d_look = '//*[@text = "4개 결과 보기"]'

    #후담대 조회 결과
    secured_loan_result_a = '//*[@text = "아파트담보대출"]'
    secured_loan_result_b = '//*[@text = "주택담보대출"]'

    # 대출조회 결과
    safe_number_result_a = '//*[@text = "최저금리"]'
    safe_number_result_b = '//*[@text = "최대한도"]'
    safe_number_result_c = '//*[@text = "오늘입금"]'
    safe_number_result_d = '//*[@text = "계좌개설 없음"]'
    safe_number_result_e = '//*[@text = "금리 낮은순"]'

    # 다시 조회하기
    lookup_again = '//*[@text = "다시 조회하기"]'
    lookup_again_a= '//*[@text = "다시 대출 알아보기"]'

    # 기타(무직,주부등..)
    unemployed = '//*[@text = "기타"]'
    unemployed_a = '//*[@text = "연소득이 없어요."]'


    a = "//*[contains(text(), '심의필')]"
    # a = "//*[@text = '신청 즉시 입금']"


