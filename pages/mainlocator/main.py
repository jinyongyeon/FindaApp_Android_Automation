from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from appium.webdriver.common.mobileby import MobileBy


class Main:

    info = InFo()

    #다음버튼
    next_button = MobileBy.XPATH, '//*[@text ="다음"]'

    # 핀다 앱
    findaapp = MobileBy.XPATH, '//*[@text ="핀다"]'

    # 로그인 완료 확인
    # login_result = '//*[@text ="'+info.name+'님 안녕하세요"]'
    login_result = MobileBy.XPATH, '//*[@text ="금융생활"]'

    #온보딩 시작하기
    start_onboarding = MobileBy.XPATH, '//*[@text ="시작하기"]'

    #악성앱 찾기 버튼
    malicious_app_search_button = MobileBy.XPATH, '//*[@text ="악성앱 찾기"]'

    #문자인증하기 버튼
    message_certification = MobileBy.XPATH, '//*[@text ="계속하기"]'

    #문자보내기 버튼
    send_message = MobileBy.XPATH, '//*[@resource-id ="com.samsung.android.messaging:id/send_button_icon"]'

    #MO인증 결과
    mo_Result = MobileBy.XPATH, '//*[@text ="이름 입력"]'

    #이름 입력 영역
    name = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText'

    #주민등록번호 앞자리 입력 영역
    rrn_a = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]'

    #주민등록번호 뒷자리 입력 영역
    rrn_b = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]'

    #통신사 선택
    kt = MobileBy.XPATH, '//*[@text ="'+info.news_agency+'"]'

    #휴대폰 번호 자동입력 결과
    phone_number_Result = MobileBy.XPATH, '//*[@text ="'+info.phone_number+'"]'
    # phone_number_Result = '//*[@text = "'+info.phone_number+'" ]'

    #서비스 약관 결과
    membership_terms_and_conditions_a_Result = MobileBy.XPATH, '//*[@text = "핀다 필수 항목 모두 동의"]'
    membership_terms_and_conditions_b_Result = MobileBy.XPATH, '//*[@text = "제휴사 필수 항목 모두 동의"]'
    membership_terms_and_conditions_c_Result = MobileBy.XPATH, '//*[@text = "본인인증 필수 항목 모두 동의"]'
    membership_terms_and_conditions_d_Result = MobileBy.XPATH, '//*[@text = "마케팅 정보 수신 동의 (선택)"]'

    #서비스 약관
    membership_terms_and_conditions_a = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View'
    membership_terms_and_conditions_b = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[2]/android.view.View'
    membership_terms_and_conditions_c = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[3]/android.view.View'
    membership_terms_and_conditions_c_a = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[2]/android.view.View'
    membership_terms_and_conditions_d = MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[4]/android.view.View'

    membership_terms_and_conditions_aa = MobileBy.XPATH, '//*[@text ="서비스 이용약관 동의"]'
    membership_terms_and_conditions_aa_Result = MobileBy.XPATH, '//*[@text ="서비스 이용약관"]'
    membership_terms_and_conditions_ab = MobileBy.XPATH, '//*[@text ="개인정보 제3자 제공 동의"]'
    membership_terms_and_conditions_ab_Result = MobileBy.XPATH, '//*[@text ="개인정보_제3자_제공_동의"]'
    membership_terms_and_conditions_ac = MobileBy.XPATH, '//*[@text ="개인정보 수집 및 이용 동의"]'
    membership_terms_and_conditions_ac_Result = MobileBy.XPATH, '//*[@text ="개인정보 수집 및 이용 동의"]'

    membership_terms_and_conditions_ba = MobileBy.XPATH, '//*[@text ="KCB 신용조회 서비스 이용 약관 동의"]'
    membership_terms_and_conditions_ba_Result = MobileBy.XPATH, '//*[@text ="KCB 올크레딧 이용약관"]'
    membership_terms_and_conditions_bb = MobileBy.XPATH, '//*[@text ="개인(신용)정보 수집∙이용 동의(KCB)"]'
    membership_terms_and_conditions_bb_Result = MobileBy.XPATH, '//*[@text ="개인(신용)정보_수집∙이용_동의(KCB)"]'
    membership_terms_and_conditions_bc = MobileBy.XPATH, '//*[@text ="개인(신용)정보 제3자 제공 동의(KCB)"]'
    membership_terms_and_conditions_bc_Result = MobileBy.XPATH, '//*[@text ="개인(신용)정보_제3자_제공_동의(KCB)"]'

    membership_terms_and_conditions_ca = MobileBy.XPATH, '//*[@text ="통신사 이용 약관"]'
    membership_terms_and_conditions_ca_Result = MobileBy.XPATH, '//*[@text ="통신사 이용약관"]'
    membership_terms_and_conditions_cb = MobileBy.XPATH, '//*[@text ="고유식별정보처리 동의"]'
    membership_terms_and_conditions_cb_Result = MobileBy.XPATH, '//*[@text ="고유식별정보처리 동의"]'
    membership_terms_and_conditions_cc = MobileBy.XPATH, '//*[@text ="개인정보 제3자 동의 (KT, LGU+ 알뜰폰)"]'
    membership_terms_and_conditions_cc_Result = MobileBy.XPATH, '//*[@text ="개인정보 제3자 제공 동의"]'
    membership_terms_and_conditions_cd = MobileBy.XPATH, '//*[@text ="개인정보취급동의"]'
    membership_terms_and_conditions_cd_Result = MobileBy.XPATH, '//*[@text ="개인정보 수집/이용/취급 위탁동의"]'
    membership_terms_and_conditions_ce = MobileBy.XPATH, '//*[@text ="본인확인서비스 이용약관"]'
    membership_terms_and_conditions_ce_Result = MobileBy.XPATH, '//*[@text ="본인확인서비스 이용약관"]'

    membership_terms_and_conditions_da = MobileBy.XPATH, '//*[@text ="마케팅 정보 수신 동의"]'
    membership_terms_and_conditions_da_Result = MobileBy.XPATH, '//*[@text ="마케팅 정보 수신동의"]'


    #약관 전체 동의
    membership_terms_and_conditions_all = MobileBy.XPATH, '//*[@text ="약관 전체 동의"]'
    check = MobileBy.XPATH, '//*[@text ="확인"]'

    # 회원가입 인증번호 => 사용안함
    verification_codes = []
    verification_codes_Result = MobileBy.XPATH, '//*[@text = "'+'", "'.join(verification_codes)+'"]'

    # 핀코드 입력 진입
    pincode_in_Result = MobileBy.XPATH, '//*[@text ="사용할 비밀번호를 입력해주세요"]'

    # 인증번호 재요청
    Re_request_verification_code = MobileBy.XPATH, '//*[@text ="인증번호 재요청"]'

    # 지문인증 사용여부
    use_fingerprint = MobileBy.XPATH, '//*[@text ="다음부터 지문 인증을 사용할게요."]'

    # 로그아웃
    logout = MobileBy.XPATH, '//*[@text ="로그아웃"]'
    logout_Result = MobileBy.XPATH, '//*[@text ="안심하세요. 개인정보 보호 중"]'

    # 회원탈퇴
    withdrawal = MobileBy.XPATH, '//*[@text ="회원탈퇴"]'

    # 회원탈퇴_동의
    withdrawal_agreement = MobileBy.XPATH, '//*[@text ="위 내용을 모두 확인했습니다."]'

    # 탈퇴하기
    withdraw = MobileBy.XPATH, '//*[@text ="탈퇴하기"]'

    # 다시 로그인 하기
    re_login = MobileBy.XPATH, '//*[@text ="다시 로그인하기"]'

    withdraw_Result = MobileBy.XPATH, '//*[@text ="원내비"]'