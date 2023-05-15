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

file_one = open('movie1.csv', mode = "w", newline = '', encoding = 'utf-8')
writer_one = csv.writer(file_one)

# file_two = open('movie2.csv', mode = "w", newline = '', encoding = 'utf-8')
# writer_two = csv.writer(file_two)
# 실행할 웹페이지 불러오기
driver.get("https://movie.naver.com/")

#영화 랭킹 1-20위 가져오기
rankingbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankingbtn.click()
time.sleep(3)

for i in range(1, 21):
    time.sleep(10)
    click_movie = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i + 1}]/td[2]/div/a')
    time.sleep(10)
    click_movie.click()
    time.sleep(10)
    try:
        genre = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        time.sleep(10)
        master = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
        time.sleep(10)
        score = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/span/em').text
        time.sleep(10)
    except:
        genre = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        time.sleep(10)
        master = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
        time.sleep(10)
        score = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[4]/div[2]/div[2]/div[1]/div/span/em').text
        time.sleep(10)

    writer_one.writerow([genre, master, score])
    time.sleep(10)
    driver.back()

#좋아하는 영화 제목, 감독, 평점, 리뷰 개수
# searchbox = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
# time.sleep(10)
# searchbox.send_keys('테넷')
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# click_my_movie = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dt/a')
# time.sleep(5)
# click_my_movie.click()
# time.sleep(5)
# movie_name = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
# time.sleep(5)
# movie_directer = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
# time.sleep(5)
# movie_score = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em')
# time.sleep(5)
# movie_score_number = ActionChains(driver).move_to_element(movie_score).perform()
# time.sleep(5)
# movie_score = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
# time.sleep(5)
# movie_number = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em')
# time.sleep(5)
# movie_number_number = ActionChains(driver).move_to_element(movie_number).perform()
# time.sleep(5)
# movie_number = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
# time.sleep(5)

# writer_two.writerow(['영화제목', '영화감독', '영화 평점', '영화 리뷰 개수'])
# writer_two.writerow([movie_name, movie_directer, movie_score, movie_number])

