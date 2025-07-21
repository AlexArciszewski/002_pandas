import pandas as pd
import numpy as np

df = pd.read_excel("C:/Dane/2_Python_Data/999_Zbiory danych/002_iris.xlsx", sheet_name='kwiatki')
# print(df)

#nagłówek i 5 wierszy
print(df.head())

#    Unnamed: 0  5.1  3.5  1.4  0.2  Iris-setosa
# 0           0  4.9  3.0  1.4  0.2  Iris-setosa
# 1           1  4.7  3.2  1.3  0.2  Iris-setosa
# 2           2  4.6  3.1  1.5  0.2  Iris-setosa
# 3           3  5.0  3.6  1.4  0.2  Iris-setosa
# 4           4  5.4  3.9  1.7  0.4  Iris-setosa
print("\n")
#Ostatnie 5 wierszy
print(df.tail())

#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 144         144  6.7  3.0  5.2  2.3  Iris-virginica
# 145         145  6.3  2.5  5.0  1.9  Iris-virginica
# 146         146  6.5  3.0  5.2  2.0  Iris-virginica
# 147         147  6.2  3.4  5.4  2.3  Iris-virginica
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica
print("\n")

#Wiersz zerowy
print(df.head(0))
# Empty DataFrame
# Columns: [Unnamed: 0, 5.1, 3.5, 1.4, 0.2, Iris-setosa]
# Index: []
print("\n")

#Sprawdzenie kolumn
print(df.columns)
# Index(['Unnamed: 0', '5.1', '3.5', '1.4', '0.2', 'Iris-setosa'], dtype='object')
print("\n")

#ile jest kolumn
print(len(df.columns))
#6
print("\n")

#Sprawdzenie typów kolumn
print(df.dtypes)
# Unnamed: 0       int64
# 5.1            float64
# 3.5            float64
# 1.4            float64
# 0.2            float64
# Iris-setosa     object
# dtype: object
print("\n")

#Ostatni wiersz
print(df.tail(1))
#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica
print("\n")

#Ile wierszy ile kolumn
print(df.shape)
#(149, 6)
print("\n")

# metoda info podstawowe dane o zbiorze danych wszystkie kolumny , rekordy not null jak not-null 891 rekordów a w bazie jest 891 rekordów to nie ma pustych nullowych rekordów dobrze

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 149 entries, 0 to 148
# Data columns (total 6 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Unnamed: 0   149 non-null    int64  
#  1   5.1          149 non-null    float64
#  2   3.5          149 non-null    float64
#  3   1.4          149 non-null    float64
#  4   0.2          149 non-null    float64
#  5   Iris-setosa  149 non-null    object 
# dtypes: float64(4), int64(1), object(1)
# memory usage: 7.1+ KB

print("\n")
# warto sprawdzić czy te typy danych zgadzają się z naszą logiką…..czy float jest tam gdzie być powinien.... itd
#metoda info podstawowe dane o zbiorze danych wszystkie kolumny , rekordy not null jak not-null 891 rekordów a w bazie jest 891 rekordów to nie ma pustych nullowych rekordów dobrze
print(df.describe())

#        Unnamed: 0         5.1         3.5         1.4         0.2
# count  149.000000  149.000000  149.000000  149.000000  149.000000
# mean    74.000000    5.848322    3.051007    3.774497    1.205369
# std     43.156691    0.828594    0.433499    1.759651    0.761292
# min      0.000000    4.300000    2.000000    1.000000    0.100000
# 25%     37.000000    5.100000    2.800000    1.600000    0.300000
# 50%     74.000000    5.800000    3.000000    4.400000    1.300000
# 75%    111.000000    6.400000    3.300000    5.100000    1.800000
# max    148.000000    7.900000    4.400000    6.900000    2.500000
print("\n")



#Załadowanie danych i zmiana indeksu
df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\dane.xlsx")
print(df)
#         Imie  Wiek  Wzrost    Miasto
# 0    Zuzanna    33     170  Warszawa
# 1    Andrzej    22     166  Warszawa
# 2     Michal    19     180   Olsztyn
# 3     Szymon    38     190   Ostr�da
# 4     Konrad    43     167    Krak�w
# 5  Agnieszka    18     181    Gda�sk

df.index = df.index + 1
print(df)

#         Imie  Wiek  Wzrost    Miasto
# 1    Zuzanna    33     170  Warszawa
# 2    Andrzej    22     166  Warszawa
# 3     Michal    19     180   Olsztyn
# 4     Szymon    38     190   Ostr�da
# 5     Konrad    43     167    Krak�w
# 6  Agnieszka    18     181    Gda�sk

print("\n")

#Sortowanie wedgług zmiennej
print(df)

#         Imie  Wiek  Wzrost    Miasto
# 1    Zuzanna    33     170  Warszawa
# 2    Andrzej    22     166  Warszawa
# 3     Michal    19     180   Olsztyn
# 4     Szymon    38     190   Ostr�da
# 5     Konrad    43     167    Krak�w
# 6  Agnieszka    18     181    Gda�sk
print("\n")

df2 = df.sort_values(by='Imie')
print(df2)
#         Imie  Wiek  Wzrost    Miasto
# 6  Agnieszka    18     181    Gda�sk
# 2    Andrzej    22     166  Warszawa
# 5     Konrad    43     167    Krak�w
# 3     Michal    19     180   Olsztyn
# 4     Szymon    38     190   Ostr�da
# 1    Zuzanna    33     170  Warszawa

print("\n")

df3 = df.sort_values(by='Imie',ascending=False)
print(df3)

#         Imie  Wiek  Wzrost    Miasto
# 1    Zuzanna    33     170  Warszawa
# 4     Szymon    38     190   Ostr�da
# 3     Michal    19     180   Olsztyn
# 5     Konrad    43     167    Krak�w
# 2    Andrzej    22     166  Warszawa
# 6  Agnieszka    18     181    Gda�sk







