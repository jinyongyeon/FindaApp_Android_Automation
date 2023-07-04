import time


from appium.webdriver.common.mobileby import MobileBy


from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.mainlocator.loan import Loan


class ComparisonLoan:

    def __init__(self):
        self.loan = Loan()
        self.info = InFo()

    # 다음 버튼
    def next_Loan(self):
        next_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.next_loan)
        next_loan.click()

    # 확인 버튼
    def check_Loan(self):
        check_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check_loan)
        check_loan.click()


            # 비교대출 온보딩 페이지에서 대출 목정페이지로 진입
    def loan_In(self):
        loan_in = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_in)
        loan_in.click()

    # 생활비 선택 및 대출 희망금액 입력
    def living_Expenses(self):
        living_expenses = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.living_expenses)
        living_expenses.click()
        loan_amount = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_amount)
        loan_amount.click()
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)

    #비교대출 약관
    def loan_Terms_And_Conditions_A(self):
        loan_terms_and_conditions_A = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_A)
        loan_terms_and_conditions_A.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Aa(self):
        loan_terms_and_conditions_Aa = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Aa)
        loan_terms_and_conditions_Aa.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ab(self):
        loan_terms_and_conditions_Ab = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ab)
        loan_terms_and_conditions_Ab.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ac(self):
        loan_terms_and_conditions_Ac = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ac)
        loan_terms_and_conditions_Ac.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ad(self):
        loan_terms_and_conditions_Ad = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ad)
        loan_terms_and_conditions_Ad.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ae(self):
        loan_terms_and_conditions_Ae = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ae)
        loan_terms_and_conditions_Ae.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_B(self):
        loan_terms_and_conditions_B = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_B)
        loan_terms_and_conditions_B.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Ba(self):
        loan_terms_and_conditions_Ba = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ba)
        loan_terms_and_conditions_Ba.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bb(self):
        loan_terms_and_conditions_Bb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bb)
        loan_terms_and_conditions_Bb.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bc(self):
        loan_terms_and_conditions_Bc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bc)
        loan_terms_and_conditions_Bc.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bd(self):
        loan_terms_and_conditions_Bd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bd)
        loan_terms_and_conditions_Bd.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Be(self):
        loan_terms_and_conditions_Be = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Be)
        loan_terms_and_conditions_Be.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Bf(self):
        loan_terms_and_conditions_Bf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bf)
        loan_terms_and_conditions_Bf.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_C(self):
        loan_terms_and_conditions_C = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_C)
        loan_terms_and_conditions_C.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Ca(self):
        loan_terms_and_conditions_Ca = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ca)
        loan_terms_and_conditions_Ca.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cb(self):
        loan_terms_and_conditions_Cb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cb)
        loan_terms_and_conditions_Cb.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cc(self):
        loan_terms_and_conditions_Cc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cc)
        loan_terms_and_conditions_Cc.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cd(self):
        loan_terms_and_conditions_Cd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cd)
        loan_terms_and_conditions_Cd.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ce(self):
        loan_terms_and_conditions_Ce = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ce)
        loan_terms_and_conditions_Ce.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cf(self):
        loan_terms_and_conditions_Cf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cf)
        loan_terms_and_conditions_Cf.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cg(self):
        loan_terms_and_conditions_Cg = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cg)
        loan_terms_and_conditions_Cg.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ch(self):
        loan_terms_and_conditions_Ch = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ch)
        loan_terms_and_conditions_Ch.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ci(self):
        loan_terms_and_conditions_Ci = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ci)
        loan_terms_and_conditions_Ci.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cj(self):
        loan_terms_and_conditions_Cj = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cj)
        loan_terms_and_conditions_Cj.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Ck(self):
        loan_terms_and_conditions_Ck = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ck)
        loan_terms_and_conditions_Ck.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cl(self):
        loan_terms_and_conditions_Cl = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cl)
        loan_terms_and_conditions_Cl.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_Cm(self):
        loan_terms_and_conditions_Cm = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cm)
        loan_terms_and_conditions_Cm.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_D(self):
        loan_terms_and_conditions_D = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_D)
        loan_terms_and_conditions_D.click()
        time.sleep(2)

    def loan_Terms_And_Conditions_Da(self):
        loan_terms_and_conditions_Da = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Da)
        loan_terms_and_conditions_Da.click()
        time.sleep(5)

    def loan_Terms_And_Conditions_All(self):
        loan_terms_and_conditions_all = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_all)
        loan_terms_and_conditions_all.click()
        time.sleep(2)

    def comparison_Loan_Verification_Resend(self):
        comparison_loan_verification_resend = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.comparison_loan_verification_resend)
        comparison_loan_verification_resend.click()
        time.sleep(2)

    # 잘못된 주민번호 뒷자리 입력
    def rrn_Fail_Input(self):
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)

    # 정상적인 주민번호 뒷자리 입력
    def rrn_Pass_Input(self):
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(8)
        time.sleep(1)
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(1)
        WebDriver.driver.press_keycode(9)
        time.sleep(2)

    # 소득 정보 직장인선택
    def office_Workers(self):
        office_workers = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.office_workers)
        office_workers.click()
        time.sleep(2)

    # 직장명 핀다 입력
    def company_Name_Input(self):
        company_name_input = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.company_name_input)
        company_name_input.send_keys("핀다")

    #검색 버튼 선택
    def search(self):
        search = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.search)
        search.click()
        time.sleep(3)

    # 핀다선택
    def company_Number(self):
        company_number = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.company_number)
        company_number.click()
        time.sleep(3)

    # 정규직 선택
    def full_Time(self):
        full_time = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.full_time)
        full_time.click()
        time.sleep(2)

    # 보험 정보 입력
        # 직장의료보험
    def workplace_Insurance(self):
        workplace_insurance = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.workplace_insurance)
        workplace_insurance.click()
        time.sleep(3)
        # 지역의료보험
    def region_Insurance(self):
        region_insurance = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.region_insurance)
        region_insurance.click()
        time.sleep(3)

    # 연봉정보 입력
    def annual_Income_Input(self):
        # annual_income = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.annual_income)
        # annual_income.click()
        WebDriver.driver.press_keycode(14)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)
        WebDriver.driver.press_keycode(7)
        time.sleep(1)

    # 전/월세 선택
    def monthly_Rent(self):
        monthly_rent = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.monthly_rent)
        monthly_rent.click()
        time.sleep(2)

    # 후담대 선택
    def my_House_APT(self):
        my_house = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.my_house)
        my_house.click()
        time.sleep(2)
        APT = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.APT)
        APT.click()
        time.sleep(2)

    # 아파트 검색
    def address_Search(self):
        address_search = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.address_search)
        address_search.click()
        time.sleep(2)
        address_input = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.address_input)
        address_input.send_keys("한강메트로자이")
        search = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.search)
        search.click()
        home_address = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.home_address)
        home_address.click()
        area = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.area)
        area.click()

    # 인증서 없이 결과 조회하기
    def no_Certificate(self):
        no_certificate = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.no_certificate)
        no_certificate.click()
        time.sleep(100)

    # 대출 종류필터 선택
    def type_Of_Loan(self):
        type_of_loan = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.type_of_loan)
        type_of_loan.click()
        time.sleep(2)

    # 주택 담보대출 필터 선택
    def secured_Loan(self):
        try:
            secured_loan_a = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_a)
            secured_loan_a.click()
            time.sleep(2)
            secured_loan_a_look = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_a_look)
            secured_loan_a_look.click()
            time.sleep(3)
        except:
            try:
                secured_loan_b = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_b)
                secured_loan_b.click()
                time.sleep(2)
                secured_loan_b_look = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_b_look)
                secured_loan_b_look.click()
                time.sleep(3)
            except:
                try:
                    secured_loan_c = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_c)
                    secured_loan_c.click()
                    time.sleep(2)
                    secured_loan_c_look = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_c_look)
                    secured_loan_c_look.click()
                    time.sleep(3)
                except:
                    try:
                        secured_loan_d = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_d)
                        secured_loan_d.click()
                        time.sleep(2)
                        secured_loan_d_look = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.secured_loan_d_look)
                        secured_loan_d_look.click()
                        time.sleep(3)
                    except:
                        print("주택 담보대출 없음")

    # 조회 결과 페이지 > 다시 조회하기 선택
    def lookup_Again(self):
        lookup_again = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.lookup_again)
        lookup_again.click()
        time.sleep(2)
        lookup_again_a = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.lookup_again_a)
        lookup_again_a.click()
        time.sleep(2)

    # 기타(무직, 주부등..)선택
    def unemployed(self):
        unemployed = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.unemployed)
        unemployed.click()
        time.sleep(2)
        unemployed_a = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.unemployed_a)
        unemployed_a.click()
        time.sleep(2)

    # 자동차 구입 선택
    def auto_Loan_In(self):
        auto_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan)
        auto_loan.click()
        time.sleep(2)
        auto_loan_In = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_In)
        auto_loan_In.click()
        time.sleep(2)

