import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
print(df.head())

print(df.columns)
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.columns)
df.index += 1
print(df.head())
df.sort_values(by='brand', inplace=True)
print(df.head())
# [5 rows x 12 columns]
#      price  brand model  year  ...        lot      state country      condition
# 596  16900  acura   mdx  2014  ...  167775829    florida     usa    1 days left
# 391   3900  acura  door  2009  ...  167389316      texas     usa   2 hours left
# 375   1000  acura  door  2008  ...  167362709   michigan     usa    2 days left
# 410     25   audi  door  2008  ...  167417202      texas     usa  17 hours left
# 445  36400   audi     5  2015  ...  167780470  wisconsin     usa    2 days left

df = df.rename(columns={'condition':'ends in'})

print(df.head())

