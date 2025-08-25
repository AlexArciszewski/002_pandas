import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
print(df.head())

#    Unnamed: 0.1  Unnamed: 0  price  ...       state country      condition
# 0             0           0   6300  ...  new jersey     usa   10 days left
# 1             1           1   2899  ...   tennessee     usa    6 days left
# 2             2           2   5350  ...     georgia     usa    2 days left
# 3             3           3  25000  ...    virginia     usa  22 hours left
# 4             4           4  27700  ...     florida     usa  22 hours left
#usuwanie kolumn z danymi stringami 
# df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
# print(df.head())

df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.head())

#    price      brand    model  ...       state country      condition
# 0   6300     toyota  cruiser  ...  new jersey     usa   10 days left
# 1   2899       ford       se  ...   tennessee     usa    6 days left
# 2   5350      dodge      mpv  ...     georgia     usa    2 days left
# 3  25000       ford     door  ...    virginia     usa  22 hours left
# 4  27700  chevrolet     1500  ...     florida     usa  22 hours left

print(df.tail())
#       price   brand  model  year  ...        lot       state country      condition
# 2494   7800  nissan  versa  2019  ...  167722715  california     usa    1 days left
# 2495   9200  nissan  versa  2018  ...  167762225     florida     usa  21 hours left
# 2496   9200  nissan  versa  2018  ...  167762226     florida     usa  21 hours left
# 2497   9200  nissan  versa  2018  ...  167762227     florida     usa    2 days left
# 2498   9200  nissan  versa  2018  ...  167762228     florida     usa  21 hours left

# [5 rows x 12 columns]

print(df.columns)

# 5 rows x 12 columns]
# Index(['price', 'brand', 'model', 'year', 'title_status', 'mileage', 'color',
#        'vin', 'lot', 'state', 'country', 'condition'],
#       dtype='object')

print(len(df.columns))
#12

print(df.dtypes)
# price             int64
# brand            object
# model            object
# year              int64
# title_status     object
# mileage         float64
# color            object
# vin              object
# lot               int64
# state            object
# country          object
# condition        object
# dtype: object


df.info()

# dtypes: float64(1), int64(3), object(8)
# memory usage: 234.4+ KB

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


print(df.shape)
# (2499, 12)



df = df.sort_values(by='brand')
print(df)
#      price  brand   model  year  ...        lot       state country      condition
# 595  16900  acura     mdx  2014  ...  167775829     florida     usa    1 days left
# 390   3900  acura    door  2009  ...  167389316       texas     usa   2 hours left
# 374   1000  acura    door  2008  ...  167362709    michigan     usa    2 days left
# 409     25   audi    door  2008  ...  167417202       texas     usa  17 hours left
# print(df.head(20))
# df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

df = df.sort_values(by='brand', ascending=False)
print(df.tail())
#      price  brand model  year  ...        lot      state country      condition
# 444  36400   audi     5  2015  ...  167780470  wisconsin     usa    2 days left
# 409     25   audi  door  2008  ...  167417202      texas     usa  17 hours left
# 374   1000  acura  door  2008  ...  167362709   michigan     usa    2 days left
# 390   3900  acura  door  2009  ...  167389316      texas     usa   2 hours left
# 595  16900  acura   mdx  2014  ...  167775829    florida     usa    1 days left


print(df['brand'].value_counts())

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
# audi                  4
# peterbilt             4
# land                  4
# acura                 3
# lexus                 2
# lincoln               2
# mazda                 2
# harley-davidson       1
# ram                   1
# jaguar                1
# maserati              1
# toyota                1
# Name: count, dtype: int64


print(df['brand'].value_counts(normalize=True))
# brand
# ford               0.494198
# dodge              0.172869
# nissan             0.124850
# chevrolet          0.118848
# gmc                0.016807
# jeep               0.012005
# chrysler           0.007203

print(df.isnull())
# 0    False  False  False  False  ...  False  False    False      False
# 505  False  False  False  False  ...  False  False    False      False
# 504  False  False  False  False  ...  False  False    False      False
# 528  False  False  False  False  ...  False  False    False      False
# 516  False  False  False  False  ...  False  False    False      False

print(df.isnull().sum())

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
# condition       0
# dtype: int64


#usuwanie braków
df.dropna()
print(df.isnull().sum())

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
# condition       0
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
# condition       0
# dtype: int64
df.dropna(how='all')

print(df.duplicated())
#       False
# 505    False
# 504    False
# 528    False
# 516    False
#        ...  
# 444    False
# 409    False
# 374    False
# 390    False
# 595    False
# Length: 2499, dtype: bool

print(df.duplicated().sum())
# 0
print(df.drop_duplicates())
print(df.drop_duplicates(inplace=True))


print(df['brand'].value_counts().sort_values(ascending=False))


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
# mercedes-benz        10
# cadillac             10
# heartland             5
# audi                  4
# peterbilt             4
# land                  4
# acura                 3
# lexus                 2
# lincoln               2
# mazda                 2
# harley-davidson       1
# ram                   1
# jaguar                1
# maserati              1
# toyota                1
# Name: count, dtype: int64



