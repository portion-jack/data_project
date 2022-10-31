import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import bs4
import pickle

d_path = r"/Users/jack/utils/chromedriver"
s = Service(d_path)
driver = webdriver.Chrome(service=s)

url = 'https://news.naver.com/main/ranking/popularDay.naver'
driver.get(url)

# start_url
"""
date = 20220518
url = f"https://news.naver.com/main/ranking/popularDay.naver?date={date}"
driver.get(url)
"""

while True:
    try:
        next_page_xpath = '//*[@id="wrap"]/div[4]/ul/li[4]/a'
        driver.find_element(by=By.XPATH,value=next_page_xpath).click()
        time.sleep(1.3)
        print(f"---{driver.current_url[-8:]}----")
    except:
        break
    try:
        _date=driver.current_url[-8:]

        soup = bs4.BeautifulSoup(driver.page_source,features='html.parser')
        ranking_news = soup.find('div', class_="_officeCard _officeCard0").find_all('div', class_='rankingnews_box')
        for news in ranking_news:
            news_name = news.find('strong', class_='rankingnews_name').get_text(strip=True)
            _temp = list()
            for titles in news.find_all('a', class_="list_title nclicks('RBP.rnknws')"):
                _temp.append(titles.get_text(strip=True))
            with open(f"news_crawling/{news_name}_{_date}.pickle",'wb') as f:
                pickle.dump(_temp,f)
    except AttributeError:
        driver.back()
        time.sleep(3)
