import pandas as pd

df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\USA_cars_datasets.csv")
print(df.head())
df_cars = df
df_cars.rename(columns={'condition':'time left'}, inplace=True)
df_cars.drop(columns=['Unnamed: 0'], inplace=True)
df_cars = df_cars.sort_values(by='brand', ascending=True)
df_cars = df_cars.reset_index(drop=True)
df_cars.index += 1
print(df_cars.head())

#   price  brand model  year  ...        lot      state country      time left
# 1  16900  acura   mdx  2014  ...  167775829    florida     usa    1 days left
# 2   3900  acura  door  2009  ...  167389316      texas     usa   2 hours left
# 3   1000  acura  door  2008  ...  167362709   michigan     usa    2 days left
# 4     25   audi  door  2008  ...  167417202      texas     usa  17 hours left
# 5  36400   audi     5  2015  ...  167780470  wisconsin     usa    2 days left


print(df_cars['brand'] == 'acura')

# [5 rows x 12 columns]
# 1        True
# 2        True
# 3        True
# 4       False
# 5       False
#         ...  
# 2495    False
# 2496    False
# 2497    False
# 2498    False
# 2499    False
# Name: brand, Length: 2499, dtype: bool


print(df_cars[df_cars['brand'] == 'acura'])

#reszta aut print(df_cars[df_cars['brand'] != 'acura'])

#    price  brand model  year  ...        lot     state country     time left
# 1  16900  acura   mdx  2014  ...  167775829   florida     usa   1 days left
# 2   3900  acura  door  2009  ...  167389316     texas     usa  2 hours left
# 3   1000  acura  door  2008  ...  167362709  michigan     usa   2 days left

# [3 rows x 12 columns]



print(df_cars[(df_cars['brand'] == 'ford') & (df_cars['model'] == 'mustang')& (df_cars['state'] == 'texas')])

#       price brand    model  year  ...        lot  state country     time left
# 1406  29000  ford  mustang  2019  ...  167638863  texas     usa  10 days left
# 1858  22000  ford  mustang  2018  ...  167786970  texas     usa   5 days left


print(df_cars[(df_cars['model'] == 'camaro') | (df_cars['model'] == 'mustang')])

#       price      brand    model  ...         state country        time left
# 49    26300  chevrolet   camaro  ...        kansas     usa      2 days left
# 51    27500  chevrolet   camaro  ...        nevada     usa  Listing Expired
# 259   31100  chevrolet   camaro  ...      oklahoma     usa    21 hours left
# 301   18300  chevrolet   camaro  ...       florida     usa    22 hours left
# 314   22500  chevrolet   camaro  ...       georgia     usa      3 days left
# 342   29800  chevrolet   camaro  ...  pennsylvania     usa    22 hours left
# 805   31600       ford  mustang  ...       georgia     usa    21 hours left
# 815   27300       ford  mustang  ...        nevada     usa      2 days left
# 821   19600       ford  mustang  ...        nevada     usa      2 days left
# 925   17100       ford  mustang  ...        nevada     usa      2 days left
# 948   27900       ford  mustang  ...    new mexico     usa    21 hours left
# 1125  27000       ford  mustang  ...      virginia     usa      2 days left
# 1147  29800       ford  mustang  ...      illinois     usa    21 hours left
# 1194  17200       ford  mustang  ...    california     usa      8 days left
# 1204  17200       ford  mustang  ...    california     usa      8 days left
# 1207  29400       ford  mustang  ...       florida     usa      2 days left
# 1227  20600       ford  mustang  ...       florida     usa      2 days left
# 1346  15500       ford  mustang  ...      illinois     usa    19 hours left
# 1406  29000       ford  mustang  ...         texas     usa     10 days left
# 1439  20500       ford  mustang  ...       florida     usa      2 days left
# 1590  21900       ford  mustang  ...    new jersey     usa      2 days left
# 1630  25511       ford  mustang  ...      michigan     usa    19 hours left
# 1777  19100       ford  mustang  ...    california     usa      2 days left
# 1782  18800       ford  mustang  ...    california     usa      2 days left
# 1783  21800       ford  mustang  ...    california     usa    21 hours left
# 1829  34100       ford  mustang  ...   mississippi     usa    21 hours left
# 1845  34100       ford  mustang  ...   mississippi     usa    21 hours left
# 1858  22000       ford  mustang  ...         texas     usa      5 days left
# 1933  35100       ford  mustang  ...   mississippi     usa    21 hours left
# 1963  21600       ford  mustang  ...      virginia     usa      2 days left
# 1981  49000       ford  mustang  ...      illinois     usa      2 days left
# 1987  21500       ford  mustang  ...      virginia     usa      2 days left
# 2019  22000       ford  mustang  ...      illinois     usa      2 days left
# 2023  38200       ford  mustang  ...       florida     usa      1 days left
# 2027  35000       ford  mustang  ...      illinois     usa    21 hours left

# [35 rows x 12 columns]