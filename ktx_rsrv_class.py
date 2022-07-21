from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class KTX():
    def __init__(self) -> None:
        super().__init__()

    def ktx_login(self):
        #로그인 사이트 접속
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.letskorail.com/korail/com/login.do')
        self.driver.implicitly_wait(15)

        #ID자동입력
        ID = "1860530560"
        PW = "!autoauto1"
        self.driver.find_element(By.ID, 'txtMember').send_keys(ID)
        self.driver.find_element(By.ID, 'txtPwd').send_keys(PW)

        #click login button
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[1]/form[1]/fieldset/div[1]/ul/li[3]/a/img').click()

        #예매 사이트 접속
        self.driver.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')
        self.driver.implicitly_wait(15)



    def plan(self, dep, arr, date, hour):

        time.sleep(1)

        #ktx클릭
        self.driver.find_element(By.ID,"selGoTrainRa00").click()

        #출발지, 도착지입력
        dep_stn = self.driver.find_element(By.ID,'start')
        dep_stn.clear() 
        dep_stn.send_keys(dep)
        dep_stn.send_keys(Keys.RETURN)

        arr_stn = self.driver.find_element(By.ID , 'get')
        arr_stn.clear()
        arr_stn.send_keys(arr)
        arr_stn.send_keys(Keys.RETURN)

        #시간선택
        year = date[:4]
        month = date[4:6]
        day = date[6:8]
        hour = hour[:2]

        year_select = Select(self.driver.find_element(By.ID,"s_year"))
        year_select.select_by_value(year)

        month_select = Select(self.driver.find_element(By.ID,"s_month"))
        month_select.select_by_value(month)

        day_select = Select(self.driver.find_element(By.ID,"s_day"))
        day_select.select_by_value(day)

        hour_select = Select(self.driver.find_element(By.ID,"s_hour"))
        hour_select.select_by_value(hour)

        #조회하기 클릭
        self.driver.find_element(By.CSS_SELECTOR,"#center > form > div > p > a > img").click()


        self.driver.implicitly_wait(15)

        train_list = self.driver.find_elements(By.CSS_SELECTOR, '#tableResult > tbody > tr')
        print("검색한 노선 : ", end = "")
        print(len(train_list)) # 결과: 10


        

        self.seats = []
        #표의 갯수
        table_row = 10
        #모든 노선 출력
        for i in range(1, table_row*2+1,2):
            seat_list = []                                    
               
            try:
                seat_train = self.driver.find_element(By.CSS_SELECTOR, 
                f"#tableResult > tbody > tr:nth-child({i}) > td:nth-child(2)").text[:3]
                seat_dep = self.driver.find_element(By.CSS_SELECTOR, 
                f"#tableResult > tbody > tr:nth-child({i}) > td:nth-child(3)").text
                seat_arr = self.driver.find_element(By.CSS_SELECTOR, 
                f"#tableResult > tbody > tr:nth-child({i}) > td:nth-child(4)").text
             
                ava_cselector = self.driver.find_elements(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({i}) > td:nth-child(6) > a')
                ava_html_cnt = len(ava_cselector)
                if ava_html_cnt == 0:
                    seat_ava = "좌석매진"#self.driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{(i-1)/2 + 1}]/td[6]/img").get_attribute("alt")
                elif ava_html_cnt == 1:
                    seat_ava = "입석+좌석"#self.driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{(i-1)/2 + 1}]/td[6]/a/img").get_attribute("alt")
                elif ava_html_cnt == 2:
                    seat_ava = "예약가능"#self.driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{(i-1)/2 + 1}]/td[6]/a[1]/img").get_attribute("alt")
            
                

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
            
            print(seat_list)
            self.seats.append(seat_list)

        return self.seats

        
    def ticket_reservation(self, index_seq):
        is_reserve = None
        Flag = 1
        while Flag:
            print("예약시도")
            is_reserve = self.driver.find_elements(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({index_seq*2-1}) > td:nth-child(6) > a')
            print(len(is_reserve))
            if len(is_reserve) == 2:
                try:
                    self.driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{index_seq}]/td[6]/a[1]/img").click()
                    time.sleep(2)
                    print("예약완료")
                    popup_iframe = self.driver.find_element(By.ID,"embeded-modal-traininfo")
                    self.driver.switch_to.frame(popup_iframe)
                    self.driver.find_element(By.XPATH,"/html/body/div/div[2]/p[3]/a").click()
                    time.sleep(2)
                finally:
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    time.sleep(1)
                    return  
            else:
                print("새로고침합니다")
                self.driver.find_element(By.CSS_SELECTOR,"#center > div.ticket_box > p > a > img").click()
                time.sleep(2)


test = KTX()
test.ktx_login()
testlist = test.plan("서울","부산","20220723","00")
print(testlist)
test.ticket_reservation(2)