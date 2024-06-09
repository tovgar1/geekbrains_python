import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

one_hot_data = pd.DataFrame()

categories = data['whoAmI'].unique()

for category in categories:
    one_hot_data[category] = data['whoAmI'].apply(lambda x: 1 if x == category else 0)

print(one_hot_data.head())

