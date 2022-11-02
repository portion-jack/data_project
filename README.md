```
.
├── 1_crwaling.ipynb
├── 2_pickle2df.ipynb
├── 3_wordcloud.ipynb
├── README.md
├── outline.md
├── preprocessed_data
│   └── news_data.csv
└── raw_data
    └── naver_news_ranking_raw_data

3 directories, 6 files

```




1. 네이버 뉴스에서 탑랭킹에 속한 9개 뉴스브랜드의 5개의 뉴스들
    - 총 45개의 뉴스타이틀을 크롤링합니다.
2. 뉴스브랜드_날짜.pickle 로 이를 리스트 형식으로 저장합니다
3. 저장된 pickle들을 뉴스브랜드 별로 읽어옵니다
    - 이때 파일의 형식을
        ```
        news_brand = {
            'date_1':[news_detail_1,news_detail_2],
            'date_2':[news_detail_1,news_detail_2]
        }
        ```
4. 이 dictionary를 dataframe 형태로 변환합니다.
5. 그럼 데이터프레임을 

```
my_dataframe :
    news_brand_1 news_brand_2 news_brand_3
date
20210101
20210102
.
.
.
형식으로 만듭니다
```
6. 
    



# news_crawling

- naver news ranking을 크롤링 하여 wordcloud 만들기
- django를 통해 naver news ranking을 wordcloud 만들어 link 제공하기
- https://www.bigkinds.or.kr/
- 한국언론진흥재단에 쏨함

## preprocessed_1_
- news_brand.pickle
    ```
    with open('preprocessed_1_/news_brand.pickle') as f:
        news_brand = pickle.load(f)
    ```


#### Selenium

#### WordCloud

#### pickle

#### konlpy

