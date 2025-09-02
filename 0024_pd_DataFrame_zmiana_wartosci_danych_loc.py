import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx", engine='openpyxl')

# print(df)
# df.index = df.index +1
#df2 = df.set_index('Imie')
print(df)

#         Imie   Nazwisko  Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
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

# [18 rows x 9 columns]


df.loc[1,'Wiek'] = 20000

print(df)
#          Imie   Nazwisko   Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
# 0    Adrianna       Bono     23     2  ...     5000     K  Warszawa    Analityk
# 1   Agnieszka   Anielska  20000     2  ...     7000     K  Warszawa  Sprzedawca
# 2     Andrzej        Lis     32    11  ...    13000     M    Krak�w   Kierownik
# 3     Gracjan      Pa�ka     33     8  ...     6000     M    Gda�sk    Ksi�gowy