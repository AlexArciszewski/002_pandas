import pandas as pd 
import numpy as np


#odczyt danych
df1 = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\USA_cars_datasets.csv")
# print(df1.head(2))
# print(df1.info())
#zapis danych 
df1.to_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars.csv",index=False)



#wszystkie kolumny
# pd.set_option('display.max_columns', None)
# print(df)
#porwórt do 5 od góry
# pd.reset_option('display.max_columns')
df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars.csv")
#przesuneicie indeksu
df.index = df.index + 1
#print(df.head())

df.rename(columns={"condition":"Auction ends"}, inplace= True)
#print(df.head())
#print(df.shape)

#Usuneicie kolumny
df.drop(columns=['Unnamed: 0'], inplace=True)
print(df.head())
print(df.shape) #(2499, 12)
print(df.info())
#<class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2499 entries, 1 to 2499
# Data columns (total 12 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   price         2499 non-null   int64  
#  1   brand         2499 non-null   object 
#  2   model         2499 non-null   object 
#  3   year          2499 non-null   int64  
#  4   title_status  2499 non-null   object 
#  5   mileage       2499 non-null   float64
#  6   color         2499 non-null   object 
#  7   vin           2499 non-null   object 
#  8   lot           2499 non-null   int64  
#  9   state         2499 non-null   object 
#  10  country       2499 non-null   object 
#  11  Auction ends  2499 non-null   object 
# dtypes: float64(1), int64(3), object(8)
# memory usage: 234.4+ KB
# None
print("\n")
print(df.describe())
#               price         year       mileage           lot
# count   2499.000000  2499.000000  2.499000e+03  2.499000e+03
# mean   18767.671469  2016.714286  5.229869e+04  1.676914e+08
# std    12116.094936     3.442656  5.970552e+04  2.038772e+05
# min        0.000000  1973.000000  0.000000e+00  1.593488e+08
# 25%    10200.000000  2016.000000  2.146650e+04  1.676253e+08
# 50%    16900.000000  2018.000000  3.536500e+04  1.677451e+08
# 75%    25555.500000  2019.000000  6.347250e+04  1.677798e+08
# max    84900.000000  2020.000000  1.017936e+06  1.678055e+08

print(df.columns)
# Index(['price', 'brand', 'model', 'year', 'title_status', 'mileage', 'color',
#        'vin', 'lot', 'state', 'country', 'Auction ends'],
#       dtype='object')


df2 = df.sort_values(by='brand', ascending=True)
print(df2)

#zliczanie aut acura
df_acura = df[df['brand'] == 'acura']
print(df_acura)
#      price  brand model  year  ...        lot     state country  Auction ends
# 375   1000  acura  door  2008  ...  167362709  michigan     usa   2 days left
# 391   3900  acura  door  2009  ...  167389316     texas     usa  2 hours left
# 596  16900  acura   mdx  2014  ...  167775829   florida     usa   1 days left


#zliczanie po brand zliczanie marek.
print(df['brand'].value_counts())
# [3 rows x 12 columns]
# brand
# ford               1235
# dodge               432
# nissan              312
# chevrolet           297
# gmc                  42
# jeep                 30
# chrysler             18
# bmw                  17
# hyundai              15
# kia                  13
# buick                13
# infiniti             12
# honda                12
# cadillac             10
# mercedes-benz        10
# heartland             5
# land                  4
# peterbilt             4
# audi                  4
# acura                 3
# lincoln               2
# lexus                 2
# mazda                 2
# maserati              1
# toyota                1
# harley-davidson       1
# jaguar                1
# ram                   1
# Name: count, dtype: int64

#zliczanie po brand zliczanie marek.
print(df['brand'].value_counts(normalize=True))

# Name: count, dtype: int64
# brand
# ford               0.494198
# dodge              0.172869
# nissan             0.124850
# chevrolet          0.118848
# gmc                0.016807
# jeep               0.012005
# chrysler           0.007203
# bmw                0.006803
# hyundai            0.006002
# kia                0.005202
# buick              0.005202
# infiniti           0.004802
# honda              0.004802
# cadillac           0.004002
# mercedes-benz      0.004002
# heartland          0.002001
# land               0.001601
# peterbilt          0.001601
# audi               0.001601
# acura              0.001200
# lincoln            0.000800
# lexus              0.000800
# mazda              0.000800
# maserati           0.000400
# toyota             0.000400
# harley-davidson    0.000400
# jaguar             0.000400
# ram                0.000400
# Name: proportion, dtype: float64

print(df2.isnull()) #czy są nulle w df2

#czy są nulle w kolumne
print(df2.isnull().sum())

# [2499 rows x 12 columns]
# price           0
# brand           0
# model           0
# year            0
# title_status    0
# mileage         0
# color           0
# vin             0
# lot             0
# state           0
# country         0
# Auction ends    0
# dtype: int64

#usuwamy nulle dropna()
df3 = df2
print(df3.head())
df4 = df3.dropna()
print(df4.isnull().sum())
#brak nulli
# [5 rows x 12 columns]
# price           0
# brand           0
# model           0
# year            0
# title_status    0
# mileage         0
# color           0
# vin             0
# lot             0
# state           0
# country         0
# Auction ends    0
# dtype: int64
print("\n")
#usuniecie wierszy które mają przynajmniej jeden brak
df3 = df2.dropna(how='all')
# dtype: int64
# price           0
# brand           0
# model           0
# year            0
# title_status    0
# mileage         0
# color           0
# vin             0
# lot             0
# state           0
# country         0
# Auction ends    0
# dtype: int64

print(df3.isnull().sum())
print("duplicated\n")
#Sprawdzanie duplikatów
print(df3.duplicated())

# duplicated

# 596    False
# 391    False
# 375    False
# 410    False
# 445    False
#        ...  
# 517    False
# 529    False
# 505    False
# 506    False
# 1      False


#usuwanie duplikatów
df3.drop_duplicates(inplace=True)


print(df2)


#ustawiam nowy index danych

df2 = df2.reset_index(drop=True)
df2.index += 1
print(df2)

df3 = df2
df3 = df3.set_index('brand')
print(df3)

print(df3.loc['ford'])

# [2499 rows x 11 columns]
#        price     model  year  ...           state  country     Auction ends
# brand                         ...                                          
# ford   11800  ecosport  2018  ...          nevada      usa      2 days left
# ford   23600   transit  2019  ...          nevada      usa      2 days left
# ford   24500     f-150  2019  ...          nevada      usa      2 days left
# ford   13000      edge  2015  ...         florida      usa      4 days left
# ford    3900    fiesta  2018  ...          nevada      usa  Listing Expired
# ...      ...       ...   ...  ...             ...      ...              ...
# ford   24400   transit  2018  ...      california      usa      1 days left
# ford   16200    fusion  2019  ...  south carolina      usa    21 hours left
# ford   35000   mustang  2018  ...        illinois      usa    21 hours left
# ford   30000    ranger  2019  ...       wisconsin      usa    21 hours left
# ford   24700  explorer  2018  ...        illinois      usa    21 hours left



print(df2.iloc[1])

# [1235 rows x 11 columns]
# price                          3900
# brand                         acura
# model                          door
# year                           2009
# title_status          clean vehicle
# mileage                    179389.0
# color                         black
# vin               19uua96529a004646
# lot                       167389316
# state                         texas
# country                         usa
# Auction ends           2 hours left
# Name: 2, dtype: object




# acura
print(df2.head(5))
print(df2.loc[2,'model'])

# df2.loc[1,'Wiek'] = 20000

df2.loc[2,'model'] = 'nsx'
print(df2.loc[2,'model'])

# nsx



print(df2['brand'] == 'ford')


# 1       False
# 2       False
# 3       False
# 4       False
# 5       False
#         ...  
# 2495    False
# 2496    False
# 2497    False
# 2498    False
# 2499    False
# Name: brand, Length: 2499, dtype: bool

ford_sum = (df2['brand'] == 'ford').sum()
print(ford_sum) 
#1235

