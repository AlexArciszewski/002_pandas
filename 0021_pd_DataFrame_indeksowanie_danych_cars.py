import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
print(df.head())

print(df[1:4])
print(df[:4])

print(df[['brand','model']])
#          brand    model
# 0        toyota  cruiser
# 1          ford       se
print(df[1:3][['brand','model']])
#    brand model
# 1   ford    se
# 2  dodge   mpv

print(df[1:3]['brand'])
# 1     ford
# 2    dodge
# Name: brand, dtype: object


print(df.loc['brand'])