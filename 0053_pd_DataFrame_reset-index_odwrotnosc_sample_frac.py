import pandas as pd

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

#Z df pobieram 100% danych losowo mieszajac
#frac=1 to 100%
df_shuffled = df.sample(frac=1)
print(df_shuffled)

#         Imie   Nazwisko  Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
# 14     Szymon   Kowalski    33     5  ...     5000     M  Warszawa  Sprzedawca
# 12      Pawe�  Niebieski    33     2  ...     6000     M  Warszawa  Sprzedawca
# 2     Andrzej        Lis    32    11  ...    13000     M    Krak�w   Kierownik
# 10     Monika   Adamczyk    30     3  ...     5500     K    Gda�sk  Sprzedawca
# 17    Zuzanna      Pa�ka    35     1  ...     4000     K      ��d�    Ksi�gowy
# 8      Micha�  Bara�czyk    30     3  ...     9000     M    Krak�w    Analityk
# 9     Miko�aj   Kowalski    41    10  ...    15000     M      ��d�   Kierownik
# 15     Tomasz      Kowal    50    15  ...     8000     M  Warszawa    Ksi�gowy
# 3     Gracjan      Pa�ka    33     8  ...     6000     M    Gda�sk    Ksi�gowy
# 6    Karolina     Zgrzyt    24     2  ...     4000     K    Krak�w    Ksi�gowy
# 7       �ucja    Zaremba    29     1  ...     5000     K      ��d�    Analityk
# 16   Weronika     Lipska    31     5  ...    10000     K  Warszawa    Analityk
# 11      Oskar      Nowak    39     6  ...     4500     M      ��d�    Ksi�gowy
# 1   Agnieszka   Anielska    31     2  ...     7000     K  Warszawa  Sprzedawca
# 4      Janusz     Kocio�    44     7  ...     6000     M  Warszawa  Sprzedawca
# 0    Adrianna       Bono    23     2  ...     5000     K  Warszawa    Analityk
# 13      Piotr  Ostrowski    40     8  ...    12000     M    Krak�w   Kierownik
# 5     Jolanta  Bara�czyk    38    10  ...    17000     K  Warszawa   Kierownik
print(df_shuffled.reset_index())

#Dostaniemy dodatkowy index ktorego nie chcemy
# 0      17    Zuzanna      Pa�ka    35  ...     4000     K      ��d�    Ksi�gowy
# 1      15     Tomasz      Kowal    50  ...     8000     M  Warszawa    Ksi�gowy
# 2      11      Oskar      Nowak    39  ...     4500     M      ��d�    Ksi�gowy
# 3       8     Micha�  Bara�czyk    30  ...     9000     M    Krak�w    Analityk
# 4      13      Piotr  Ostrowski    40  ...    12000     M    Krak�w   Kierownik
# 5      16   Weronika     Lipska    31  ...    10000     K  Warszawa    Analityk
# 6       7      �ucja    Zaremba    29  ...     5000     K      ��d�    Analityk
# 7       1  Agnieszka   Anielska    31  ...     7000     K  Warszawa  Sprzedawca
# 8       4     Janusz     Kocio�    44  ...     6000     M  Warszawa  Sprzedawca
# 9       9    Miko�aj   Kowalski    41  ...    15000     M      ��d�   Kierownik
# 10     12      Pawe�  Niebieski    33  ...     6000     M  Warszawa  Sprzedawca
# 11      5    Jolanta  Bara�czyk    38  ...    17000     K  Warszawa   Kierownik
# 12     14     Szymon   Kowalski    33  ...     5000     M  Warszawa  Sprzedawca
# 13      0   Adrianna       Bono    23  ...     5000     K  Warszawa    Analityk
# 14     10     Monika   Adamczyk    30  ...     5500     K    Gda�sk  Sprzedawca
# 15      2    Andrzej        Lis    32  ...    13000     M    Krak�w   Kierownik
# 16      3    Gracjan      Pa�ka    33  ...     6000     M    Gda�sk    Ksi�gowy
# 17      6   Karolina     Zgrzyt    24  ...     4000     K    Krak�w    Ksi�gowy
df_ordered = df_shuffled.reset_index(inplace=True)

print(df_ordered)