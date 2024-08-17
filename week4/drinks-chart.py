import pandas as pd

drinks = pd.read_csv('./week4/data/drinks.csv')

# 시리즈 반환
beer_servings_mean = drinks.groupby("continent")["beer_servings"].mean()

beer_servings_mean.sort_values(ascending=False, inplace=True)

print(beer_servings_mean)

# 각종 통계량은 describe() 이용
wine_servings = drinks.groupby("continent")["wine_servings"]

print(wine_servings.describe())