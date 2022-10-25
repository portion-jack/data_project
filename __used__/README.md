## project: health_info realationship with medicine perscription
(2022_10_20~)

## data
- 건강검진정보 (~2020)
- 약처방정보  (~2020)
- 의약품주성분코드~의약품일반명 매핑용 자료(csv)

### repo_outline

```
.
├── data
│   ├── preprocessed_data
│   │   ├── health_2020.csv
│   │   ├── medicin_mapper.pkl
│   │   └── medicine
│   └── raw_data
│       ├── data_manual.pdf
│       ├── medicine_2020
│       ├── 국민건강보험공단_건강검진정보2020.CSV
│       └── 의약품_매핑.csv
└── preprocessing_baseline_1.ipynb

5 directories, 6 files
```

### did
1. 한글 font matplotlib setting
-   plt.rc('font',family='AppleGothic')
2. 한글 encoding 불러오기 cp949 
- 한글 df 저장 encoding = 'cp949'
3. DataFrame to dictionary
- my_dict = df_mapper.to_dict("records")
-   - to_dict methods
-   -   - df.to_dict("split")
-   -   - df.to_dict("records")
-   -   - df.to_dict("index")
-   -   - df.to_dict("tight")
- my_dict = {items['column1']:items['column2'] for items in my_dict}

4. DataFrame mapping by dictionary
- df.loc[:,"my_columns"].map(my_dict)

5. string parsing from doctring
- my_string = 
    """   

    """
- csv가 아닌 string도 dockstring을 사용하여 파싱하면 편하게 작업할 수 있다.

#### google drive에 옮기기 너무 큼
column 자를꺼 자르기
