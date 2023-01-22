import pandas as pd

d ={ 'col1':[1,2,3],'col2':[2,3,4]}
f = [[1,2,3],[2,4,5]]
df = pd.DataFrame(data=f,index=['jaggi','shah'],columns=['a','b','c'])
print(df)

# df.drop(columns=['jaggi'])

# data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
#                             11497.65, 7027.61, 9946.03, 
#                             29564.74, 6001.40, 6424.98, 42354.41]
# data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
#                             10126.72, 6126.87, 8346.70, 
#                             27057.16, 5090.72, 5332.77, 40284.64]
# print(data)