import pandas as pd

# 변수 data에 데이터 저장
data = {
    'A' : ['apple', 'banana', 'grape'],
    'B' : [11, 34, 22]
}

# Pandas DataFrame에 변수 data 전달
df = pd.DataFrame(data)

# DataFrame 중 마지막 열에 열 추가
df['C'] = ['good', 'soso', 'not bad']

# DataFrame 중 원하는 위치(=0열)에 열 추가
df.insert(0, 'C', ['good', 'soso', 'not bad'])

# DataFrame은 보존하되, 새로운 열을 마지막 열에 일시적으로 덧붙여 반환
assigned = df.assign(C = ['good', 'soso', 'not bad'])
print(df)
print(assigned)

# DataFrame 중 필요한 열(=A열)만 반환
df = df[['A']]
print(df)