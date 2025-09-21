import pandas as pd

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx")

df.index +=1



print(df.head())
print("\n")
#         Imie  Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
# 1   Adrianna      Bono    23     2    0.00     5000    K  Warszawa    Analityk
# 2  Agnieszka  Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca
# 3    Andrzej       Lis    32    11    0.02    13000    M    Krak�w   Kierownik
# 4    Gracjan     Pa�ka    33     8    0.00     6000    M    Gda�sk    Ksi�gowy
# 5     Janusz    Kocio�    44     7    0.08     6000    M  Warszawa  Sprzedawca

df.drop('Premia', axis=1, inplace=True)
#axis=1 dzialanie na kolumnach inplace=True zmainy przeprowadzone na nazej tabeli axis=0 zmiany na wierszach
print(df.head())


#         Imie  Nazwisko  Wiek  Staz  Zarobki Plec    Miasto       Zawod
# 1   Adrianna      Bono    23     2     5000    K  Warszawa    Analityk
# 2  Agnieszka  Anielska    31     2     7000    K  Warszawa  Sprzedawca
# 3    Andrzej       Lis    32    11    13000    M    Krak�w   Kierownik
# 4    Gracjan     Pa�ka    33     8     6000    M    Gda�sk    Ksi�gowy
# 5     Janusz    Kocio�    44     7     6000    M  Warszawa  Sprzedawca

df.drop(["Imie", "Nazwisko"], axis=1, inplace=True)
print(df)

#     Wiek  Staz  Zarobki Plec    Miasto       Zawod
# 1     23     2     5000    K  Warszawa    Analityk
# 2     31     2     7000    K  Warszawa  Sprzedawca
# 3     32    11    13000    M    Krak�w   Kierownik
# 4     33     8     6000    M    Gda�sk    Ksi�gowy
# 5     44     7     6000    M  Warszawa  Sprzedawca
# 6     38    10    17000    K  Warszawa   Kierownik
# 7     24     2     4000    K    Krak�w    Ksi�gowy
# 8     29     1     5000    K      ��d�    Analityk
# 9     30     3     9000    M    Krak�w    Analityk
# 10    41    10    15000    M      ��d�   Kierownik
# 11    30     3     5500    K    Gda�sk  Sprzedawca
# 12    39     6     4500    M      ��d�    Ksi�gowy
# 13    33     2     6000    M  Warszawa  Sprzedawca
# 14    40     8    12000    M    Krak�w   Kierownik
# 15    33     5     5000    M  Warszawa  Sprzedawca
# 16    50    15     8000    M  Warszawa    Ksi�gowy
# 17    31     5    10000    K  Warszawa    Analityk
# 18    35     1     4000    K      ��d�    Ksi�gowy

# [Done] exited with code=0 in 1.736 seconds