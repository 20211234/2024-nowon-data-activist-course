import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

returns = pd.DataFrame(np.random.normal(1.0, 0.03, (100, 10)))
'''
- 변수 returns 안에 DataFrame 담기
- DataFrame 안에 


이 코드는 100개의 행과 10개의 열을 가진 Pandas DataFrame을 생성합니다.
각 셀에는 평균이 1.0, 표준편차가 0.03인 정규 분포에서 무작위로 생성된 값이 들어 있습니다.
이 DataFrame은 "수익률"을 나타내는 데이터라고 생각할 수 있습니다.

'''
prices = returns.cumprod()
prices.plot(figsize=(16,9))

plt.title('Randomly-generated Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

plt.show()