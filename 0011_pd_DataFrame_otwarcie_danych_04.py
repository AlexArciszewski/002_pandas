import pandas as pd


df = pd.read_csv(r"C:\Dane\2_Python_Data\999_Zbiory danych\danecsv.csv")
print(df.head())

#       Imie  Wiek  Wzrost    Miasto
# 0  Zuzanna    33     170  Warszawa
# 1  Andrzej    22     166  Warszawa
# 2   Michal    19     180   Olsztyn
# 3   Szymon    38     190   Ostroda
# 4   Konrad    43     167    Krakow

df.to_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\danexlszcsv.xlsx")