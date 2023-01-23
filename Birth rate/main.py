import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('births.csv')
# print(data.head())
# print(data['day'].isnull().count())
data['day'].fillna(0 , inplace=True)
data['day']  = data['day'].astype(int)
data['decade'] = 10 * (data['year'] // 10)
sns.set()
data2 = data.pivot_table(data,index='decade',columns='gender',aggfunc='sum')
# print(data.head())
# print(data2)
# y = [ data2['F'] ,  data2['M'] ]
# x = data2['decade']
data2.plot()
plt.ylabel("Total Birth Per Year")
# plt.plot(x,y)

plt.show()