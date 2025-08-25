import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
print(df.head())

print(df.columns)
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.columns)
# df.to_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\cars_final.csv")
print(df['brand'].value_counts())
df2 = df
df2.set_index('brand', inplace=True)
print(df2.head())
print(df2.loc['maserati'])
# price                         30300
# model                        ghibli
# year                           2017
# title_status          clean vehicle
# mileage                     37021.0
# color                         black
# vin               zam57xslxh1248775
# lot                       167607797
# state                       florida
# country                         usa
# condition               2 days left
# Name: maserati, dtype: object
print(df2)
print(df2.loc['maserati','price'])
# 30300
df2.loc['maserati','price'] = 4444
print(df2.loc['maserati','price'])
#4444
#nie dziala
print(df2.loc['maserati':'toyota','price':'model'])