from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class SRT():
    def __init__(self) -> None:
        super().__init__()

    def srt_login(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
        self.driver.implicitly_wait(15)
        ID = "2281291548"
        PW = "!autoauto1"
        self.driver.find_element(By.ID, 'srchDvNm01').send_keys(ID)
        self.driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(PW)
        self.driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(Keys.RETURN)
        
        self.driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')

    def plan(self, dep, arr, date, hour):

        time.sleep(1)

        self.driver.find_element(By.ID, 'dptRsStnCdNm').clear()
        self.driver.find_element(By.ID, 'dptRsStnCdNm').send_keys(dep)
        self.driver.find_element(By.ID, 'arvRsStnCdNm').clear()
        self.driver.find_element(By.ID, 'arvRsStnCdNm').send_keys(arr)

        elm_dptDt = self.driver.find_element(By.ID, "dptDt")
        self.driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

        Select(self.driver.find_element(By.ID,"dptDt")).select_by_value(date)
        Select(self.driver.find_element(By.ID,"dptTm")).select_by_value(hour)
        self.driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/form/fieldset/div[2]/input").click()

        time.sleep(2)

        self.seats = []
        for count in range(1,11):
            seat_list = []

            try:
                seat_train = self.driver.find_element(By.XPATH, 
                f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{count}]/td[2]").text
                seat_dep = self.driver.find_element(By.XPATH, 
                f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{count}]/td[4]").text
                seat_arr = self.driver.find_element(By.XPATH, 
                f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{count}]/td[5]").text
                seat_ava = self.driver.find_element(By.XPATH, 
                f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{count}]/td[7]").text

            except:
                seat_train = 'None'
                seat_dep = 'None'
                seat_arr = 'None'
                seat_ava = 'None'

            finally:
                seat_list.append(seat_train)
                seat_list.append(seat_dep)
                seat_list.append(seat_arr)
                seat_list.append(seat_ava)
            
            self.seats.append(seat_list)
        
        return self.seats
    
    def try_reservation(self, check):
        while True:
            try:
                for i in check:
                    i += 1
                    if self.driver.find_element(By.XPATH, 
                    f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a").text == "예약하기":
                        element = self.driver.find_element(By.XPATH,
                        f"/html/body/div/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a")
                        self.driver.execute_script("arguments[0].click();", element)
                        self.driver.quit()
                        options = webdriver.ChromeOptions()
                        self.driver = webdriver.Chrome(options=options)
                        self.driver.get('https://etk.srail.kr/hpg/hra/02/selectReservationList.do?pageId=TK0102010000')
                        return "fin"
                    else:
                        pass

                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                element = self.driver.find_element(By.XPATH,
                '/html/body/div[1]/div[4]/div/div[2]/form/fieldset/div[2]/input')
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(1)

            except:
                time.sleep(8)
                continue

# for i in range(1, 3):
#     standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text
    
#     if "예약하기" in standard_seat:
#         print("예약 가능")        
#         driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
        
#         # CSS Selector 사용시 예약하기 대신 좌석선택이 눌러지는 문제가 있어 XPATH로 변경
#         # driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7) > a").click()

# while(1):
#  driver.implicitly_wait(99)
