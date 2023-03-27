from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains



# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'D:/next 학회/next 개발세션 자료/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbtn.click()

# 1위곡명 가져오기

# 1위부터 20위까지 가져오기

# 스크롤 내리기

# 실시간 급상승 가수 가져오기

# 곡의 장르 가져오기

# 좋아하는 가수의 곡명 10개

# 순위, 곡명, 가수명 가져오기
import csv

file = open('melon.csv', mode = "w", newline = '')
writer = csv.writer(file)

for i in range(1, 6):
    print(i, '중간점검')
    time.sleep(2)
    number = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[2]/div/span[1]').text
    time.sleep(2)
    title = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a').text
    time.sleep(2)
    singer = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a').text
    time.sleep(2)
    writer.writerow([number, title, singer])
    print(number, title, singer)

file.close()
    



# csv 파일로 변환