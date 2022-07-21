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



        train_list = self.driver.find_elements(By.CSS_SELECTOR, '#tableResult > tbody > tr')
        print("검색한 노선 : ", end = "")
        print(len(train_list)) # 결과: 10


        #모든 노선 출력
        for i in range(1, len(train_list)*2+1,2):
          for j in range(2, 8):
              text = self.driver.find_element(By.CSS_SELECTOR, f"#tableResult > tbody > tr:nth-child({i}) > td:nth-child({j})").text.replace("\n"," ")
              print(text, end="")
          print()

        time.sleep(2)
        

test = KTX()
test.ktx_login()
test.plan("서울","부산","20220802","09")