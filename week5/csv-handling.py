import pandas as pd

# Pandas DataFrame에 csv 데이터를 불러온 뒤, 변수 df에 저장
df = pd.read_csv('./week5/data/노원구종합도서관데이터.csv')

# 변수 df에 담긴 csv 데이터 중, 0행부터 54행까지의 데이터, 0열부터 6열까지의 데이터를 선택하여 df_subset 변수에 저장
df_subset = df.iloc[0:55, 0:7]

# df_subset 변수에 담긴 csv 데이터 중, Nan으로 표시되는 데이터는 '보완필요' 문구로 표시
df_subset.to_csv('./week5/data/노원구종합도서관데이터.csv', na_rep='보완필요')

# df_subset 변수에 담긴 csv 데이터 출력
print(df_subset)