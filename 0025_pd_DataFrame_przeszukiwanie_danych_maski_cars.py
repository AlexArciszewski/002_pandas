import pandas as pd


df =pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
#print(df.head())
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
#print(df.head())

df.index +=1
#print(df.head())


df.set_index('brand', inplace=True)
print(df.head())

print(df['model'] == 'cruiser')

# brand
# toyota        True
# ford         False
# ....

print(df[ df['model'] == 'cruiser'])

#        price    model  year  ...       state  country     condition
# brand                         ...                                   
# toyota   6300  cruiser  2008  ...  new jersey      usa  10 days left


print(df[ df['model'] == 'mustang' ])

# [1 rows x 11 columns]
#        price    model  year  ...        state  country      condition
# brand                        ...                                     
# ford   25511  mustang  2019  ...     michigan      usa  19 hours left
# ford   21900  mustang  2018  ...   new jersey      usa    2 days left
# ford   22000  mustang  2018  ...     illinois      usa    2 days left
# ford   38200  mustang  2019  ...      florida      usa    1 days left
# ford   35000  mustang  2018  ...     illinois      usa  21 hours left
# ford   49000  mustang  2017  ...     illinois      usa    2 days left
# ford   21600  mustang  2019  ...     virginia      usa    2 days left
# ford   21500  mustang  2019  ...     virginia      usa    2 days left
# ford   35100  mustang  2019  ...  mississippi      usa  21 hours left
# ford   34100  mustang  2019  ...  mississippi      usa  21 hours left

# print("adding df2")



print(df[ (df['model'] == 'mustang') & (df['color'] == 'red') ])

#       price    model  year  ...        state  country      condition
# brand                        ...                                     
# ford   21900  mustang  2018  ...   new jersey      usa    2 days left
# ford   22000  mustang  2018  ...     illinois      usa    2 days left
# ford   21500  mustang  2019  ...     virginia      usa    2 days left
# ford   35100  mustang  2019  ...  mississippi      usa  21 hours left
# ford   34100  mustang  2019  ...  mississippi      usa  21 hours left
# ford   27000  mustang  2020  ...     virginia      usa    2 days left
# ford   15500  mustang  2019  ...     illinois      usa  19 hours left

# [7 rows x 11 columns]

print(df[ (df['model'] == 'mustang') & ((df['color'] == 'red')| (df['color'] == 'black') )])

#        price    model  year  ...        state  country      condition
# brand                        ...                                     
# ford   21900  mustang  2018  ...   new jersey      usa    2 days left
# ford   22000  mustang  2018  ...     illinois      usa    2 days left
# ford   49000  mustang  2017  ...     illinois      usa    2 days left
# ford   21500  mustang  2019  ...     virginia      usa    2 days left
# ford   35100  mustang  2019  ...  mississippi      usa  21 hours left
# ford   34100  mustang  2019  ...  mississippi      usa  21 hours left
# ford   27000  mustang  2020  ...     virginia      usa    2 days left
# ford   31600  mustang  2019  ...      georgia      usa  21 hours left
# ford   20500  mustang  2019  ...      florida      usa    2 days left
# ford   15500  mustang  2019  ...     illinois      usa  19 hours left
# ford   29000  mustang  2019  ...        texas      usa   10 days left

# [11 rows x 11 columns]

print(df['model'].isin(['mustang','camaro']))

# brand
# toyota       False
# ford         False
# dodge        False
# ford         False
# chevrolet    False
#              ...  
# nissan       False
# nissan       False
# nissan       False
# nissan       False
# nissan       False
# Name: model, Length: 2499, dtype: bool



print(df[ df['model'].isin(['mustang','camaro']) ])

# brand                            ...                                        
# chevrolet  29800   camaro  1973  ...  pennsylvania      usa    22 hours left
# chevrolet  18300   camaro  2017  ...       florida      usa    22 hours left
# chevrolet  22500   camaro  2020  ...       georgia      usa      3 days left
# ford       25511  mustang  2019  ...      michigan      usa    19 hours left
# chevrolet  31100   camaro  2019  ...      oklahoma      usa    21 hours left
# chevrolet  27500   camaro  2016  ...        nevada      usa  Listing Expired
# chevrolet  26300   camaro  2018  ...        kansas      usa      2 days left
# ford       21900  mustang  2018  ...    new jersey      usa      2 days left
# ford       22000  mustang  2018  ...      illinois      usa      2 days left
# ford       38200  mustang  2019  ...       florida      usa      1 days left
# ford       35000  mustang  2018  ...      illinois      usa    21 hours left
# ford       49000  mustang  2017  ...      illinois      usa      2 days left
# ford       21600  mustang  2019  ...      virginia      usa      2 days left
# ford       21500  mustang  2019  ...      virginia      usa      2 days left
# ford       35100  mustang  2019  ...   mississippi      usa    21 hours left
# ford       34100  mustang  2019  ...   mississippi      usa    21 hours left
# ford       34100  mustang  2019  ...   mississippi      usa    21 hours left
# ford       21800  mustang  2018  ...    california      usa    21 hours left
# ford       18800  mustang  2018  ...    california      usa      2 days left
# ford       19100  mustang  2018  ...    california      usa      2 days left
# ford       22000  mustang  2018  ...         texas      usa      5 days left
# ford       27000  mustang  2020  ...      virginia      usa      2 days left
# ford       27900  mustang  2019  ...    new mexico      usa    21 hours left
# ford       19600  mustang  2019  ...        nevada      usa      2 days left
# ford       27300  mustang  2019  ...        nevada      usa      2 days left
# ford       31600  mustang  2019  ...       georgia      usa    21 hours left
# ford       17100  mustang  2018  ...        nevada      usa      2 days left
# ford       29800  mustang  2016  ...      illinois      usa    21 hours left
# ford       20600  mustang  2019  ...       florida      usa      2 days left
# ford       17200  mustang  2018  ...    california      usa      8 days left
# ford       17200  mustang  2018  ...    california      usa      8 days left
# ford       29400  mustang  2019  ...       florida      usa      2 days left
# ford       20500  mustang  2019  ...       florida      usa      2 days left
# ford       15500  mustang  2019  ...      illinois      usa    19 hours left
# ford       29000  mustang  2019  ...         texas      usa     10 days left

# [35 rows x 11 columns]

print(df.columns)
# Index(['price', 'model', 'year', 'title_status', 'mileage', 'color', 'vin',
#        'lot', 'state', 'country', 'condition'],
#       dtype='object')


print(df[(df['model'] == 'camaro') & (df['year'] < 2000)])

#            price   model  year  ...         state  country      condition
# brand                           ...                                      
# chevrolet  29800  camaro  1973  ...  pennsylvania      usa  22 hours left

# [1 rows x 11 columns]












