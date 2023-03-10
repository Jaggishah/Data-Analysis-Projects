import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("transformed_data.csv")
data2 = pd.read_csv("raw_data.csv")
# print(data)

# print(data.head())
# print(data['COUNTRY'].value_counts())
print(data['COUNTRY'].value_counts().mode())

code = data['CODE'].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)  # data.loc[data['rows']>7,coums]
    tc.append((data2.loc[data2["location"] == i, "total_cases"]).sum()) # data.iloc[[2,2,2]]
    td.append((data2.loc[data2["location"] == i, "total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data2.loc[data2["location"] == i, "population"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                               columns = ["Country Code", "Country", "HDI", 
                                          "Total Cases", "Total Deaths", 
                                          "Stringency Index", "Population"])
# print(aggregated_data.head())

data  =aggregated_data.sort_values(by=['Total Cases'],ascending=False)
# print(data.head())

data = data.head(10)
print(data)


data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
                            11497.65, 7027.61, 9946.03, 
                            29564.74, 6001.40, 6424.98, 42354.41]
data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
                            10126.72, 6126.87, 8346.70, 
                            27057.16, 5090.72, 5332.77, 40284.64]
print(data)

plt.bar(data['Country'],data['Total Cases'])
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.title('Country Vs Total Cases')
plt.legend()
plt.show()