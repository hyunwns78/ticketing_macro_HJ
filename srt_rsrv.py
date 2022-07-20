from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class SRT():
    def __init__(self) -> None:
        super().__init__()

    def srt_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
        self.driver.implicitly_wait(15)
        ID = "2281291548"
        PW = "!autoauto1"
        self.driver.find_element(By.ID, 'srchDvNm01').send_keys(ID)
        self.driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(PW)
        self.driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(Keys.RETURN)
        
        self.driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')


# str_dep_stn = "동탄"
# dep_stn = driver.find_element(By.ID,'dptRsStnCdNm')
# dep_stn.clear() 
# dep_stn.send_keys(str_dep_stn)

# str_arr_stn = "수서"
# arr_stn = driver.find_element(By.ID , 'arvRsStnCdNm')
# arr_stn.clear()
# arr_stn.send_keys(str_arr_stn)

# #elm_dptDt = driver.find_element(By.ID, "dptDt")
# #driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

# Date = "20220801"
# Time = "100000"
# Select(driver.find_element(By.ID,"dptDt")).select_by_value(Date)
# Select(driver.find_element(By.ID,"dptTm")).select_by_value(Time)
# driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/form/fieldset/div[2]/input").click()

# train_list = driver.find_elements(By.CSS_SELECTOR, '#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr')
# print(len(train_list)) # 결과: 10

# for i in range(1, len(train_list)+1):
#     for j in range(3, 8):
#         text = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child({j})").text.replace("\n"," ")
#         print(text, end="")
#     print()


# for i in range(1, 3):
#     standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text
    
#     if "예약하기" in standard_seat:
#         print("예약 가능")        
#         driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
        
#         # CSS Selector 사용시 예약하기 대신 좌석선택이 눌러지는 문제가 있어 XPATH로 변경
#         # driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7) > a").click()

# while(1):
#  driver.implicitly_wait(99)

