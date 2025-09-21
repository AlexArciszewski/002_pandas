import pandas as pd
import random
df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx")

print(df)

#          Imie   Nazwisko  Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
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

jobs = []
for i in range(17):
    num = random.randint(1, 10)
    jobs.append(num)
print(jobs)

#Dodajemy kolumnęz Series jak bedzie brakowało danych to doda się Nan

liczba_pracodawców_kolumna = pd.Series(jobs)
df["liczba pracodawcow"] = liczba_pracodawców_kolumna
print(df)

#          Imie   Nazwisko  Wiek  ...    Miasto       Zawod  liczba pracodawc�w
# 0    Adrianna       Bono    23  ...  Warszawa    Analityk                 1.0
# 1   Agnieszka   Anielska    31  ...  Warszawa  Sprzedawca                 8.0
# 2     Andrzej        Lis    32  ...    Krak�w   Kierownik                 2.0
# 3     Gracjan      Pa�ka    33  ...    Gda�sk    Ksi�gowy                 4.0
# 4      Janusz     Kocio�    44  ...  Warszawa  Sprzedawca                 9.0
# 5     Jolanta  Bara�czyk    38  ...  Warszawa   Kierownik                 9.0
# 6    Karolina     Zgrzyt    24  ...    Krak�w    Ksi�gowy                 3.0
# 7       �ucja    Zaremba    29  ...      ��d�    Analityk                 4.0
# 8      Micha�  Bara�czyk    30  ...    Krak�w    Analityk                 3.0
# 9     Miko�aj   Kowalski    41  ...      ��d�   Kierownik                 3.0
# 10     Monika   Adamczyk    30  ...    Gda�sk  Sprzedawca                 8.0
# 11      Oskar      Nowak    39  ...      ��d�    Ksi�gowy                 4.0
# 12      Pawe�  Niebieski    33  ...  Warszawa  Sprzedawca                 6.0
# 13      Piotr  Ostrowski    40  ...    Krak�w   Kierownik                10.0
# 14     Szymon   Kowalski    33  ...  Warszawa  Sprzedawca                 9.0
# 15     Tomasz      Kowal    50  ...  Warszawa    Ksi�gowy                10.0
# 16   Weronika     Lipska    31  ...  Warszawa    Analityk                 1.0
# 17    Zuzanna      Pa�ka    35  ...      ��d�    Ksi�gowy                 NaN

df["liczba pracodawcow"].fillna(100, inplace=True)

print(df.tail(1))

#  df["liczba pracodawc�w"].fillna(100, inplace=True)
#        Imie Nazwisko  Wiek  Staz  ...  Plec  Miasto     Zawod liczba pracodawc�w
# 17  Zuzanna    Pa�ka    35     1  ...     K    ��d�  Ksi�gowy              100.0


#Dodawanie kolumny z użyciem listy dodanie mniej elemntów niz jest wierszy daje blad


# ile_l4 =[1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1,]

# df["choroby"] = ile_l4

# print(df)

# File "c:\Dane\2_Python_Data\002_pandas\0027_pd_DataFrame_dodanie_kolumn_series_lista.py", line 72, in <module>
#     df["choroby"] = ile_l4
#     ~~^^^^^^^^^^^
#   File "C:\Users\arcis\AppData\Roaming\Python\Python311\site-packages\pandas\core\frame.py", line 4311, in __setitem__
#     self._set_item(key, value)
#   File "C:\Users\arcis\AppData\Roaming\Python\Python311\site-packages\pandas\core\frame.py", line 4524, in _set_item
#     value, refs = self._sanitize_column(value)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\arcis\AppData\Roaming\Python\Python311\site-packages\pandas\core\frame.py", line 5266, in _sanitize_column
#     com.require_length_match(value, self.index)
#   File "C:\Users\arcis\AppData\Roaming\Python\Python311\site-packages\pandas\core\common.py", line 573, in require_length_match
#     raise ValueError(
# ValueError: Length of values (11) does not match length of index (18)


ile_l4 =[1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1,2,2,2,2,2,2,20]

df["choroby"] = ile_l4

print(df)


# [1 rows x 10 columns]
#          Imie   Nazwisko  Wiek  ...       Zawod  liczba pracodawc�w  choroby
# 0    Adrianna       Bono    23  ...    Analityk                10.0        1
# 1   Agnieszka   Anielska    31  ...  Sprzedawca                10.0        2
# 2     Andrzej        Lis    32  ...   Kierownik                 2.0        3
# 3     Gracjan      Pa�ka    33  ...    Ksi�gowy                 4.0        4
# 4      Janusz     Kocio�    44  ...  Sprzedawca                 9.0        1
# 5     Jolanta  Bara�czyk    38  ...   Kierownik                 3.0        1
# 6    Karolina     Zgrzyt    24  ...    Ksi�gowy                 6.0        1
# 7       �ucja    Zaremba    29  ...    Analityk                 9.0        1
# 8      Micha�  Bara�czyk    30  ...    Analityk                 3.0        1
# 9     Miko�aj   Kowalski    41  ...   Kierownik                10.0        1
# 10     Monika   Adamczyk    30  ...  Sprzedawca                 4.0        1
# 11      Oskar      Nowak    39  ...    Ksi�gowy                 5.0        2
# 12      Pawe�  Niebieski    33  ...  Sprzedawca                 1.0        2
# 13      Piotr  Ostrowski    40  ...   Kierownik                 4.0        2
# 14     Szymon   Kowalski    33  ...  Sprzedawca                 8.0        2
# 15     Tomasz      Kowal    50  ...    Ksi�gowy                 5.0        2
# 16   Weronika     Lipska    31  ...    Analityk                 4.0        2
# 17    Zuzanna      Pa�ka    35  ...    Ksi�gowy               100.0       20

# [18 rows x 11 columns]

print(df.columns.tolist())
df["liczba pracodawcow na wiek"] = df['liczba pracodawcow']/ df['Wiek']
df["liczba pracodawcow na wiek"]  =  df["liczba pracodawcow na wiek"].round(2)
print(df)

['Imie', 'Nazwisko', 'Wiek', 'Staz', 'Premia', 'Zarobki', 'Plec', 'Miasto', 'Zawod', 'liczba pracodawcow', 'choroby']
#          Imie   Nazwisko  ...  choroby  liczba pracodawcow na wiek
# 0    Adrianna       Bono  ...        1                        0.39
# 1   Agnieszka   Anielska  ...        2                        0.23
# 2     Andrzej        Lis  ...        3                        0.28
# 3     Gracjan      Pa�ka  ...        4                        0.15
# 4      Janusz     Kocio�  ...        1                        0.14
# 5     Jolanta  Bara�czyk  ...        1                        0.21
# 6    Karolina     Zgrzyt  ...        1                        0.42
# 7       �ucja    Zaremba  ...        1                        0.10
# 8      Micha�  Bara�czyk  ...        1                        0.33
# 9     Miko�aj   Kowalski  ...        1                        0.22
# 10     Monika   Adamczyk  ...        1                        0.30
# 11      Oskar      Nowak  ...        2                        0.08
# 12      Pawe�  Niebieski  ...        2                        0.21
# 13      Piotr  Ostrowski  ...        2                        0.25
# 14     Szymon   Kowalski  ...        2                        0.15
# 15     Tomasz      Kowal  ...        2                        0.04
# 16   Weronika     Lipska  ...        2                        0.06


#Nowa kolumna z integera
df["liczba glow"] = 4

print(df)

df["czy pracownik zyje"] = True
print(df)

#          Imie   Nazwisko  ...  liczba glow  czy pracownik zyje
# 0    Adrianna       Bono  ...            4                True
# 1   Agnieszka   Anielska  ...            4                True
# 2     Andrzej        Lis  ...            4                True
# 3     Gracjan      Pa�ka  ...            4                True
# 4      Janusz     Kocio�  ...            4                True
# 5     Jolanta  Bara�czyk  ...            4                True
# 6    Karolina     Zgrzyt  ...            4                True
# 7       �ucja    Zaremba  ...            4                True
# 8      Micha�  Bara�czyk  ...            4                True
# 9     Miko�aj   Kowalski  ...            4                True
# 10     Monika   Adamczyk  ...            4                True
# 11      Oskar      Nowak  ...            4                True
# 12      Pawe�  Niebieski  ...            4                True
# 13      Piotr  Ostrowski  ...            4                True
# 14     Szymon   Kowalski  ...            4                True
# 15     Tomasz      Kowal  ...            4                True
# 16   Weronika     Lipska  ...            4                True
# 17    Zuzanna      Pa�ka  ...            4                True
