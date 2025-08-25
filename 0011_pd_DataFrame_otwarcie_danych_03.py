import pandas as pd


df =pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\dane.xlsx", sheet_name ="Zarzad", names = ["Imie",  "Wiek", "Wzrost", "Miasto", "Plec"])
df.index += 1
print(df.head())







