import pandas as pd

# Pandas Dataframe에 데이터 입력 후 변수 df에 입력
df = pd.DataFrame({
    'A': ['a1', 'a2', 'a3', 'a4'],
    'B': ['b1', 'b2', 'b3', 'b4'],
    'C': ['c1', 'c2', 'c3', 'c4']
})

# loc 행
df.loc[0, 4] = ['a5', 'b5', 'c5']
print(df)