from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib.request
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(executable_path='/Users/iseulgi/Desktop/Likelion/Crawling/selenium/chromedriver')
driver.get('https://movie.naver.com/')

def changeWindow(number):
  if number == 0: #만약 0일 시 창을 닫는다.
    driver.close()
  driver.switch_to.window(driver.window_handles[number])

xpathPaper = '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a'
driver.find_element_by_xpath(xpathPaper).send_keys(Keys.CONTROL+'\n')

cnt = 0
result = []

for i in range(1, 5): #1위부터
  info = [] # 영화 정보 담는 리스트
  xpathPaper = '//*[@id="old_content"]/table/tbody/tr['+ str(i+1+cnt) +']/td[2]/div/a'
  # 해당 영화에 대한 페이지로 들어간다
  driver.find_element_by_xpath(xpathPaper).send_keys(Keys.CONTROL+'\n')
  changeWindow(1) #페이지를 연다
  title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
  director = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
  info.append(title)
  info.append(director)
  src = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/a/img')
  info.append(src)

  xpathReview = '//*[@id="movieEndTabMenu"]/li[6]/a' #리뷰창
  driver.find_element_by_xpath(xpathReview).send_keys(Keys.CONTROL+'\n')
  changeWindow(0)
  changeWindow(1) # 리뷰창으로 넘어가라

  for comment_num in range(1, 4):
    try: # 리뷰를 1부터 3까지 돌렸는데 있으면! 실행하는 코드
      review = driver.find_element_by_xpath('//*[@id="reviewTab"]/div/div/ul/li['+ str(i) +']/a/strong')
      info.append(review)
    except: # 리뷰가 3까지 없으면 넘어가라
      continue

  result.append(info)
  changeWindow(0) #페이지를 닫는다.
  if i % 10 == 0: #10의 배수이면
    cnt += 1

import pandas as pd
list_df = pd.DataFrame(result, columns=['제목', '감독', '사진', '리뷰1', '리뷰2', '리뷰3'])
list_df.to_csv('크롤링결과.csv',index=False,encoding='euc-kr')

print(result)
