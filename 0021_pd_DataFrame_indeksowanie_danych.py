import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx")

# print(df)
# df.index = df.index +1
print(df)

#          Imi�   Nazwisko  Wiek  Sta�  ...  Zarobki  P�e�    Miasto       Zaw�d
# 0    Adrianna       Bono    23     2  ...     5000     K  Warszawa    Analityk
# 1   Agnieszka   Anielska    31     2  ...     7000     K  Warszawa  Sprzedawca
# 2     Andrzej        Lis    32    11  ...    13000     M    Krak�w   Kierownik
# 3     Gracjan      Pa�ka    33     8  ...     6000     M    Gda�sk    Ksi�gowy
# 4      Janusz     Kocio�    44     7  ...     6000     M  Warszawa  Sprzedawca
# 5     Jolanta  Bara�czyk    38    10  ...    17000     K  Warszawa   Kierownik
# 6    Karolina     Zgrzyt    24     2  ...     4000     K    Krak�w    Ksi�gowy
# 7       �ucja    Zaremba    29     1  ...     5000     K      ��d�    Analityk
# 8      Micha�  Bara�czyk    30     3  ...     9000     M    Krak�w    Analityk
# 9     Miko�aj   Kowalski    41    10  ...    15000     M      ��d�   Kierownik
# 10     Monika   Adamczyk    30     3  ...     5500     K    Gda�sk  Sprzedawca
# 11      Oskar      Nowak    39     6  ...     4500     M      ��d�    Ksi�gowy
# 12      Pawe�  Niebieski    33     2  ...     6000     M  Warszawa  Sprzedawca
# 13      Piotr  Ostrowski    40     8  ...    12000     M    Krak�w   Kierownik
# 14     Szymon   Kowalski    33     5  ...     5000     M  Warszawa  Sprzedawca
# 15     Tomasz      Kowal    50    15  ...     8000     M  Warszawa    Ksi�gowy
# 16   Weronika     Lipska    31     5  ...    10000     K  Warszawa    Analityk
# 17    Zuzanna      Pa�ka    35     1  ...     4000     K      ��d�    Ksi�gowy

print("\n")
print(df[:2])
#        Imi�  Nazwisko  Wiek  Sta�  Premia  Zarobki P�e�    Miasto       Zaw�d
# 0   Adrianna      Bono    23     2    0.00     5000    K  Warszawa    Analityk
# 1  Agnieszka  Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca

print("\n")
print(df[1:4])

#         Imi�  Nazwisko  Wiek  Sta�  Premia  Zarobki P�e�    Miasto       Zaw�d
# 1  Agnieszka  Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca
# 2    Andrzej       Lis    32    11    0.02    13000    M    Krak�w   Kierownik
# 3    Gracjan     Pa�ka    33     8    0.00     6000    M    Gda�sk    Ksi�gowy

print("\n")
print(df['Nazwisko'])

# 0          Bono
# 1      Anielska
# 2           Lis
# 3         Pa�ka
# 4        Kocio�
# 5     Bara�czyk
# 6        Zgrzyt
# 7       Zaremba
# 8     Bara�czyk
# 9      Kowalski
# 10     Adamczyk
# 11        Nowak
# 12    Niebieski
# 13    Ostrowski
# 14     Kowalski
# 15        Kowal
# 16       Lipska
# 17        Pa�ka
# Name: Nazwisko, dtype: object

print("\n")
print(df[['Nazwisko','Wiek']])
# Nazwisko  Wiek
# 0        Bono    23
# 1    Anielska    31
# 2         Lis    32
# 3       Pa�ka    33
# 4      Kocio�    44
# 5   Bara�czyk    38
# 6      Zgrzyt    24
# 7     Zaremba    29
# 8   Bara�czyk    30
# 9    Kowalski    41
# 10   Adamczyk    30
# 11      Nowak    39
# 12  Niebieski    33
# 13  Ostrowski    40
# 14   Kowalski    33
# 15      Kowal    50
# 16     Lipska    31
# 17      Pa�ka    35

print("\n")
print(df[1:3][['Nazwisko','Wiek']])

#    Nazwisko  Wiek
# 1  Anielska    31
# 2       Lis    32

