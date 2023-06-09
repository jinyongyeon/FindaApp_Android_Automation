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