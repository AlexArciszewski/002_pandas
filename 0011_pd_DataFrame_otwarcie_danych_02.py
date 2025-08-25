import pandas as pd

df2 = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\DanePD.xlsx",sheet_name="Arkusz1",names = ["Imie pracownika","Wiek pracownika ","Waga","Plec"])
print(df2.head())