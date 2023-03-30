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
# chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
# chartbtn.click()
# 1위곡명 가져오기
# first = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
# print(first)
# time.sleep(3)
# 1위부터 20위까지 가져오기
# song_list = []
# for i in range(1, 21):
#     song = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a').text
#     song_list.append(song)
# print(song_list)
# 스크롤 내리기
# scroll.move_to_element()
# 실시간 급상승 가수 가져오기
# bar = driver.find_element(By.XPATH, '//*[@id="gnb"]/div[2]/div')
# ActionChains(driver).move_to_element(bar)
# hot_singer = driver.find_element(By.XPATH, '//*[@id="gnb"]/div[2]/div/ol/li[1]/a').text
# print(hot_singer)

# 곡의 장르 가져오기
# genre_list = []
# for i in range(1, 4):
#     print(i, '확인용')
#     songbtn = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[5]/div/a')
#     songbtn.click()
#     time.sleep(2)
#     print('중간점검')
#     genre = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
#     genre_list.append(genre)
#     driver.back()
# print(genre_list)
# 좋아하는 가수의 곡명 10개
# search = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/fieldset/input[1]')
# search.click()
# time.sleep(2)
# love_singer = '세븐틴'
# search.send_keys(love_singer)
# searchbtn = driver.find_element(By.XPATH, '//*[@id="gnb"]/fieldset/button[2]/span')
# searchbtn.click()
# time.sleep(2)
# song_list = []
# for i in range(1, 11):
#     song = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div[1]/div[4]/div/form[1]/div/table/tbody/tr[{i}]/td[3]/div/div/a[2]').text
#     song_list.append(song)
# print(song_list)
# 순위, 곡명, 가수명 가져오기
# for i in enumerate(, 100):
#     number = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[2]/div/span[1]')
#     title = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a')
#     singer = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a')

# csv 파일로 변경