import pandas as pd

df = pd.read_csv(r"C:\Dane\2_Python_Data\999_Zbiory danych\homework.csv",names=['Imie', 'Nazwisko', 'Wzrost', 'Oczy'])


print("\n")
df.rename(columns={'Oczy':"Kolor oczu"}, inplace=True)
df = df.drop(index=0)
# Zadanie 1. Wyświetl za pomocą odpowiedniej metody 2 pierwsze elementy tablicy.
print(df.head(2))

#     Imie Nazwisko Wzrost  Kolor oczu
# 1  Lucja      Lis    180  Niebieskie
# 2   Adam     Ziab    177       Szare

# Zadanie 2. Wyświetl za pomocą odpowiedniej metody trzy ostatnie elementy tablicy.
print(df.tail(3))
#         Imie Nazwisko Wzrost Kolor oczu
# 2       Adam     Ziab    177      Szare
# 3  Agnieszka     Klos    156      Szare
# 4    Paulina    Zgryz    199    Zielone


# Zadanie 3. Wyświetl podstawowe informacje o typach danych naszej tabeli danych.
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 1 to 4
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   Imie        4 non-null      object
#  1   Nazwisko    4 non-null      object
#  2   Wzrost      4 non-null      object
#  3   Kolor oczu  4 non-null      object
# dtypes: object(4)
# memory usage: 260.0+ bytes
# None
print("\n")
# Zadanie 4. Wyświetl kształt tabeli danych (liczba wierszy i kolumn).
print(df.shape)
# dtypes: object(4)
# memory usage: 260.0+ bytes
# (4, 4)

# Zadanie 5. Wyświetl podstawowe statystyki opisujące nasz zbiór danych.

print(df.describe())
#          Imie Nazwisko Wzrost Kolor oczu
# count       4        4      4          4
# unique      4        4      4          3
# top     Lucja      Lis    180      Szare
# freq        1        1      1          2

#Zadanie 6. Sprawdź, czy w zbiorze znajdują się puste dane i duplikaty.
print(df.isnull())

#     Imie  Nazwisko  Wzrost  Kolor oczu
# 1  False     False   False       False
# 2  False     False   False       False
# 3  False     False   False       False
# 4  False     False   False       False

print(df.duplicated())

# 1    False
# 2    False
# 3    False
# 4    False
# dtype: bool

print(df.isnull().sum())
# Imie          0
# Nazwisko      0
# Wzrost        0
# Kolor oczu    0
# dtype: int64

print(df.duplicated().sum())
#0
# Zadanie 7. Sprawdź ile w zbiorze danych znajduje się osób o każdym kolorze oczu. Posortuj wyniki malejąco
print(df['Kolor oczu'].value_counts())

# Szare         2
# Niebieskie    1
# Zielone       1
# Name: count, dtype: int64

print(df['Kolor oczu'].value_counts(ascending=False))

# Kolor oczu
# Szare         2
# Niebieskie    1
# Zielone       1
# Name: count, dtype: int64