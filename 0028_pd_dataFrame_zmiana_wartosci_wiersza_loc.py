import pandas as pd


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")

df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.columns)


df['crashed'] = 0 
print(df.head())


df.loc[ df['model'] == 'se', 'crashed'] = 'YES'
#df.loc[  #lokalizacja wiersza, lokalizacja komorki do zmiany ]= na co zmieniamy
print(df.head())
#    price      brand    model  year  ...       state  country      condition crashed
# 0   6300     toyota  cruiser  2008  ...  new jersey      usa   10 days left       0
# 1   2899       ford       se  2011  ...   tennessee      usa    6 days left     YES










