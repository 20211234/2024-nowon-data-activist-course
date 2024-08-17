import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 글꼴 설정
font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

scores = pd.read_csv('./week4/data/scores.csv', encoding="euc-kr")

print(scores.info())

subjects = scores.columns[1:]

scores['총점']  = scores[subjects].sum(axis=1)
scores['평균'] = scores['총점'] / len(subjects)

print(scores.head())

sorted_scores = scores.sort_values(by=['평균'], ascending=False)

print(sorted_scores)

sorted_scores.index = sorted_scores['이름']
sorted_scores['평균'].plot(kind='bar', figsize=(8, 4))

plt.show()