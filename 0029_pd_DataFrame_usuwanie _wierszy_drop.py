import pandas as pd

df = pd.read_csv(r"C:\Dane\2_Python_Data\999_Zbiory danych\homework.csv", names = ["Imie", "Nazwisko", "Wzrost", "Kolor oczu"])
print(df.head())
#         Imie Nazwisko Wzrost  Kolor oczu
# 0     Nazwa1   Nazwa2  Nazwa3      Nazwa4
# 1      Lucja      Lis     180  Niebieskie
# 2       Adam     Ziab     177       Szare
# 3  Agnieszka     Klos     156       Szare
# 4    Paulina    Zgryz     199     Zielone
df.drop(0,inplace=True)
print(df.head())
#         Imie Nazwisko Wzrost  Kolor oczu
# 1      Lucja      Lis    180  Niebieskie
# 2       Adam     Ziab    177       Szare
# 3  Agnieszka     Klos    156       Szare
# 4    Paulina    Zgryz    199     Zielone
