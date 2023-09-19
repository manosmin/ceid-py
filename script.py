import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
'''
url = 'https://data.buffalony.gov/resource/2cjd-uvx7.csv'
urllib.request.urlretrieve(url, '2cjd-uvx7.csv')
'''
# scrapped data from previous section
fname = '2cjd-uvx7.csv'

# reading the csv file as a pandas df
df = pd.read_csv(fname)
# displaying the first 5 rows
print(df.head())
# displaying the last 5 rows
print(df.tail())

# displaying unique values in type column
print(df['type'].unique())

# converting values in date column into year
df['date'] = pd.to_datetime(df['date']).dt.to_period('Y')

def f(x):
    b = x['total_in_tons'].sum()
    return pd.Series([b], index=['total_in_tons'])

df2 = df.groupby(['date']).apply(f)

# displaying sum of total_in_tons for all types per year
print(df2)


# storing df column values into an array
data = {'Total In Tons': [df2.iloc[0, 0], df2.iloc[1, 0], df2.iloc[2, 0], df2.iloc[3, 0], df2.iloc[4, 0],
                          df2.iloc[5, 0], df2.iloc[6, 0], df2.iloc[7, 0], df2.iloc[8, 0]],
        'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
        }

# plotting dataframe
df4 = pd.DataFrame(data, columns=['Year', 'Total In Tons'])
df4.plot(x='Year', y='Total In Tons', kind='line',
         title='Συνολικές ποσότητες ανακυκλώσιμων ανά έτος.', figsize=(6, 6))
plt.show(block=False)

df3 = df.groupby(['type']).apply(f)

# displaying sum of total_in_tons for each type
print(df3)
# save Graph1.csv
df2.to_csv('Graph1.csv')

data = ['Asphalt Debris',
        'Bottle Bill',
        'Curb Garbage',
        'Curb Recycling',
        'E-Waste',
        'Haz Waste',
        'Misc. Garbage ',
        'Misc. Recycling',
        'Recycled Tires',
        'Scrap Metal',
        'Sidewalk Debris',
        'Yard Waste']
# storing df column values into an array
index = [df3.iloc[0, 0], df3.iloc[1, 0], df3.iloc[2, 0], df3.iloc[3, 0], df3.iloc[4, 0], df3.iloc[5, 0],
         df3.iloc[6, 0], df3.iloc[7, 0], df3.iloc[8, 0], df3.iloc[9, 0], df3.iloc[10, 0], df3.iloc[11, 0]]

# converting percentages into absolute values
i = [0]
def absolute_value(var):
    a = df3.iloc[i[0] % len(df3), i[0]//len(df3)]
    i[0] += 1
    return a


# plotting dataframe
df5 = pd.DataFrame({'Type': data, 'Total In Tons': index})
df5.groupby(['Type']).sum().plot(kind='pie', y='Total In Tons', autopct=absolute_value,
                                 figsize=(6, 6), title='Ανακυκλώσιμα είδη και οι ποσότητες τους.')
plt.show(block=False)

# save Graph2.csv
df3.to_csv('Graph2.csv')

# reading the csv file as a pandas df
df = pd.read_csv(fname)

df6 = df.drop('date', 1)


# converting values in date column into month-year format
def h(x):
    a = x['month'].unique()
    b = x['total_in_tons'].sum()
    return pd.Series([a, b], index=['month', 'total_in_tons'])

df6 = df.groupby(['month']).apply(h)
print(df6.head())

# save Graph3.csv
df6.to_csv('Graph3.csv', columns = ['total_in_tons'])

# displaying sum of total_in_tons in recycled items for each month
print(df6.sort_values(by=['total_in_tons'], ascending=0))

df7 = df6.sort_values(by=['total_in_tons'], ascending=0)

data = [
    df7.iloc[0, 0].astype(str),
    df7.iloc[1, 0].astype(str),
    df7.iloc[2, 0].astype(str),
    df7.iloc[3, 0].astype(str),
    df7.iloc[4, 0].astype(str)
]
# storing df column values into an array
index = [
        df7.iloc[0, 1], 
        df7.iloc[1, 1],
        df7.iloc[2, 1], 
        df7.iloc[3, 1], 
        df7.iloc[4, 1]
]

# plotting dataframe
df8 = pd.DataFrame({'Date': data, 'Total In Tons': index})
df8.plot.bar(x='Date', y='Total In Tons', rot=0, figsize=(
    6, 6), title='Οι 5 μήνες με την μεγαλύτερη ποσότητα ανακυκλώσιμων.')
plt.show()
