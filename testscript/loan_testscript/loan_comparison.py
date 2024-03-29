import logging
import time
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from config.info import InFo
from drivers.aos_webdrivers import WebDriver
from pages.basemethod.base import basemethod
from pages.mainlocator.loan import Loan


class ComparisonLoan:

    def __init__(self):
        self.loan  = Loan()
        self.info = InFo()
        self.base = basemethod()

    # 다음 버튼
    def next_loan(self):
        next_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.next_loan)
        next_loan.click()

    # 확인 버튼
    def check_loan(self):
        check_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check_loan)
        check_loan.click()


    # 비교 대출 온보딩 페이지 에서 대출 목적 페이지로 진입
    def loan_in(self):
        loan_in = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_in)
        loan_in.click()

    # 생활비 선택 및 대출 희망금액 입력
    def living_expenses(self):
        self.base.scroll_up(0.2)
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


    # 비교 대출 약관
    def loan_terms_and_conditions_a(self):
        try:
            loan_terms_and_conditions_A = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_A)
            loan_terms_and_conditions_A.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_a : {e}")

    def loan_terms_and_conditions_aa(self):
        try:
            loan_terms_and_conditions_Aa = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Aa)
            loan_terms_and_conditions_Aa.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_aa : {e}")

    def loan_terms_and_conditions_ab(self):
        try:
            loan_terms_and_conditions_Ab = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ab)
            loan_terms_and_conditions_Ab.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ab : {e}")

    def loan_terms_and_conditions_ac(self):
        try:
            loan_terms_and_conditions_Ac = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ac)
            loan_terms_and_conditions_Ac.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ac : {e}")

    def loan_terms_and_conditions_ad(self):
        try:
            loan_terms_and_conditions_Ad = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ad)
            loan_terms_and_conditions_Ad.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ad : {e}")

    def loan_terms_and_conditions_ae(self):
        try:
            loan_terms_and_conditions_Ae = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ae)
            loan_terms_and_conditions_Ae.click()
            time.sleep(7)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ae : {e}")

    def loan_terms_and_conditions_b(self):
        try:
            loan_terms_and_conditions_B = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_B)
            loan_terms_and_conditions_B.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_b : {e}")

    def loan_terms_and_conditions_ba(self):
        try:
            loan_terms_and_conditions_Ba = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ba)
            loan_terms_and_conditions_Ba.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ba : {e}")

    def loan_terms_and_conditions_bb(self):
        try:
            loan_terms_and_conditions_Bb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bb)
            loan_terms_and_conditions_Bb.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_bb : {e}")

    def loan_terms_and_conditions_bc(self):
        try:
            loan_terms_and_conditions_Bc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bc)
            loan_terms_and_conditions_Bc.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_bc : {e}")

    def loan_terms_and_conditions_bd(self):
        try:
            loan_terms_and_conditions_Bd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bd)
            loan_terms_and_conditions_Bd.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_bd : {e}")

    def loan_terms_and_conditions_be(self):
        try:
            loan_terms_and_conditions_Be = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Be)
            loan_terms_and_conditions_Be.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_be : {e}")

    def loan_terms_and_conditions_bf(self):
        try:
            loan_terms_and_conditions_Bf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Bf)
            loan_terms_and_conditions_Bf.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_bf : {e}")

    def loan_terms_and_conditions_c(self):
        try:
            loan_terms_and_conditions_C = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_C)
            loan_terms_and_conditions_C.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_c : {e}")

    def loan_terms_and_conditions_ca(self):
        try:
            loan_terms_and_conditions_Ca = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ca)
            loan_terms_and_conditions_Ca.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ca : {e}")

    def loan_terms_and_conditions_cb(self):
        try:
            loan_terms_and_conditions_Cb = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cb)
            loan_terms_and_conditions_Cb.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cb : {e}")

    def loan_terms_and_conditions_cc(self):
        try:
            loan_terms_and_conditions_Cc = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cc)
            loan_terms_and_conditions_Cc.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cc : {e}")

    def loan_terms_and_conditions_cd(self):
        try:
            loan_terms_and_conditions_Cd = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cd)
            loan_terms_and_conditions_Cd.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cd : {e}")

    def loan_terms_and_conditions_ce(self):
        try:
            loan_terms_and_conditions_Ce = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ce)
            loan_terms_and_conditions_Ce.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ce : {e}")

    def loan_terms_and_conditions_cf(self):
        try:
            loan_terms_and_conditions_Cf = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cf)
            loan_terms_and_conditions_Cf.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cf : {e}")

    def loan_terms_and_conditions_cg(self):
        try:
            loan_terms_and_conditions_Cg = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cg)
            loan_terms_and_conditions_Cg.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cg : {e}")

    def loan_terms_and_conditions_ch(self):
        try:
            loan_terms_and_conditions_Ch = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ch)
            loan_terms_and_conditions_Ch.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ch : {e}")

    def loan_terms_and_conditions_ci(self):
        try:
            loan_terms_and_conditions_Ci = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ci)
            loan_terms_and_conditions_Ci.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ci : {e}")

    def loan_terms_and_conditions_cj(self):
        try:
            loan_terms_and_conditions_Cj = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cj)
            loan_terms_and_conditions_Cj.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cj : {e}")

    def loan_terms_and_conditions_ck(self):
        try:
            loan_terms_and_conditions_Ck = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ck)
            loan_terms_and_conditions_Ck.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ck : {e}")

    def loan_terms_and_conditions_cl(self):
        try:
            loan_terms_and_conditions_Cl = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cl)
            loan_terms_and_conditions_Cl.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cl : {e}")

    def loan_terms_and_conditions_cm(self):
        try:
            loan_terms_and_conditions_Cm = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cm)
            loan_terms_and_conditions_Cm.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cm : {e}")

    def loan_terms_and_conditions_cn(self):
        try:
            loan_terms_and_conditions_Cn = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cn)
            loan_terms_and_conditions_Cn.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cn : {e}")

    def loan_terms_and_conditions_co(self):
        try:
            loan_terms_and_conditions_Co = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Co)
            loan_terms_and_conditions_Co.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_co : {e}")

    def loan_terms_and_conditions_cp(self):
        try:
            loan_terms_and_conditions_Cp = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cp)
            loan_terms_and_conditions_Cp.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cp : {e}")

    def loan_terms_and_conditions_cq(self):
        try:
            loan_terms_and_conditions_Cq = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cq)
            loan_terms_and_conditions_Cq.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cq : {e}")

    def loan_terms_and_conditions_cr(self):
        try:
            loan_terms_and_conditions_Cr = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cr)
            loan_terms_and_conditions_Cr.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cr : {e}")

    def loan_terms_and_conditions_cs(self):
        try:
            loan_terms_and_conditions_Cs = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cs)
            loan_terms_and_conditions_Cs.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cs : {e}")

    def loan_terms_and_conditions_ct(self):
        try:
            loan_terms_and_conditions_Ct = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Ct)
            loan_terms_and_conditions_Ct.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_ct : {e}")

    def loan_terms_and_conditions_cu(self):
        try:
            loan_terms_and_conditions_Cu = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cu)
            loan_terms_and_conditions_Cu.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cu : {e}")

    def loan_terms_and_conditions_cv(self):
        try:
            loan_terms_and_conditions_Cv = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Cv)
            loan_terms_and_conditions_Cv.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_cv : {e}")

    def loan_terms_and_conditions_d(self):
        try:
            loan_terms_and_conditions_D = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_D)
            loan_terms_and_conditions_D.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_d : {e}")

    def loan_terms_and_conditions_da(self):
        try:
            loan_terms_and_conditions_Da = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_Da)
            loan_terms_and_conditions_Da.click()
            time.sleep(5)
        except Exception as e:
            logging.error(f"loan_terms_and_conditions_da : {e}")

    def loan_terms_and_conditions_all(self):
        loan_terms_and_conditions_all = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_terms_and_conditions_all)
        loan_terms_and_conditions_all.click()
        time.sleep(2)


    def comparison_loan_verification_resend(self):
        comparison_loan_verification_resend = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.comparison_loan_verification_resend)
        comparison_loan_verification_resend.click()
        time.sleep(2)

    # 잘못된 주민등록번호 뒷자리 입력
    def rrn_fail_input(self):
        try:
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
            WebDriver.driver.press_keycode(14)
            time.sleep(1)
            WebDriver.driver.press_keycode(14)
            time.sleep(1)
        except Exception as e:
            logging.error(f"rrn_fail_input : {e}")

    # 정상적인 주민번호 뒷자리 입력
    def rrn_pass_input(self):
        loan_rrn = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.loan_rrn)
        loan_rrn.send_keys(self.info.loan_rrn)
        time.sleep(2)

    # 소득 정보 직장인선택
    def office_workers(self):
        office_workers = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.office_workers)
        office_workers.click()
        time.sleep(2)

    # 직장명 핀다 입력
    def company_name_input(self):
        company_name_input = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.company_name_input)
        company_name_input.send_keys("핀다")

    # 검색 버튼 선택
    def search(self):
        search = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.search)
        search.click()
        time.sleep(3)

    # 핀다선택
    def company_number(self):
        try:
            company_number = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.company_number)
            company_number.click()
            time.sleep(3)
        except Exception as e:
            logging.error(f"company_number : {e}")

    # 정규직 선택
    def full_time(self):
        try:
            full_time = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.full_time)
            full_time.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"full_time : {e}")

    # 보험 정보 입력
    # 직장의료보험
    def workplace_insurance(self):
        try:
            workplace_insurance = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.workplace_insurance)
            workplace_insurance.click()
            time.sleep(3)
        except Exception as e:
            logging.error(f"workplace_insurance : {e}")

    # 지역의료보험
    def region_insurance(self):
        try:
            region_insurance = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.region_insurance)
            region_insurance.click()
            time.sleep(3)
        except Exception as e:
            logging.error(f"region_insurance : {e}")

    # 연봉정보 입력
    def annualincome_input(self):
        try:
            WebDriver.driver.press_keycode(14)
            time.sleep(1)
            WebDriver.driver.press_keycode(7)
            time.sleep(1)
            WebDriver.driver.press_keycode(7)
            time.sleep(1)
            WebDriver.driver.press_keycode(7)
            time.sleep(1)
        except Exception as e:
            logging.error(f"annualincome_input : {e}")

    # 전/월세 선택
    def monthly_rent(self):
        monthly_rent = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.monthly_rent)
        monthly_rent.click()
        time.sleep(2)

    # 제 명의의 차량을 갖고있어요. 선택
    def mycar_namber(self):
        try:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber_check))
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber)).click()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber)).click()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber_input)).send_keys("" + self.info.autoNo + "")
            time.sleep(3)
        except:
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber)).click()
            WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.mycar_namber_input)).send_keys("" + self.info.autoNo + "")
            time.sleep(3)

    # 후담대 선택
    def my_house_apt(self):
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.my_house)).click()
        WebDriverWait(WebDriver.driver, 10).until(EC.visibility_of_element_located(self.loan.APT)).click()
        time.sleep(2)

    # 아파트 검색
    def address_search(self):
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
        time.sleep(3)
        check = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.check)
        check.click()
        time.sleep(3)

    # 인증서 없이 결과 조회하기
    def no_certificate(self):
        no_certificate = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.no_certificate)
        no_certificate.click()
        time.sleep(100)


    # 대출 종류필터 선택
    def type_of_loan(self):
        type_of_loan = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.type_of_loan)
        type_of_loan.click()
        time.sleep(2)


    # 주택 담보대출 필터 선택
    def secured_loan(self):
        try:
            WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_a)
            time.sleep(2)
            WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_look).click()
            time.sleep(3)
            logging.warning("주택 담보대출 1개")
            print("주택 담보대출 1개")
        except:
            try:
                WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_b)
                time.sleep(2)
                WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_look).click()
                time.sleep(3)
                logging.warning("주택 담보대출 2개")
                print("주택 담보대출 2개")
            except:
                try:
                    WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_c)
                    time.sleep(2)
                    WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_look).click()
                    time.sleep(3)
                    logging.warning("주택 담보대출 3개")
                    print("주택 담보대출 3개")
                except:
                    try:
                        WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_d)
                        time.sleep(2)
                        WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_look).click()
                        time.sleep(3)
                        logging.warning("주택 담보대출 4개")
                        print("주택 담보대출 4개")
                    except:
                        WebDriver.driver.find_element(MobileBy.XPATH, self.loan.secured_loan_look).click()
                        logging.warning("주택 담보대출 없음")
                        print("주택 담보대출 없음")

    # 조회 결과 페이지 > 다시 조회하기 선택
    def lookup_again(self):
        lookup_again = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.lookup_again)
        lookup_again.click()
        time.sleep(2)
        lookup_again_a = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.lookup_again_a)
        lookup_again_a.click()
        time.sleep(2)


    # 기타(무직, 주부등..)선택
    def unemployed(self):
        try:
            unemployed = WebDriver.driver.find_element(MobileBy.XPATH,self.loan.unemployed)
            unemployed.click()
            time.sleep(2)
            unemployed_a = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.unemployed_a)
            unemployed_a.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"unemployed : {e}")

    #비교대출 신청하기
    def loan_application(self):
        try:
            comparison_loan_detail = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.comparison_loan_detail)
            comparison_loan_detail.click()
            time.sleep(10)
        except Exception as e:
            logging.error(f"loan_application : {e}")

    # 자동차 구입 선택
    def auto_loan_in(self):
        try:
            auto_loan = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan)
            auto_loan.click()
            time.sleep(2)
            auto_loan_In = WebDriver.driver.find_element(MobileBy.XPATH, self.loan.auto_loan_In)
            auto_loan_In.click()
            time.sleep(2)
        except Exception as e:
            logging.error(f"auto_loan_in : {e}")
