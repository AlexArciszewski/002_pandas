# Metoda .loc pozwala wyciągnąć z danych wybrane wiersze bazując na ich indeksach. W odróżnieniu od standardowego indeksowania nie podajemy tutaj numerów wierszy, a wartości indeksów.

import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx", engine='openpyxl')

# print(df)
# df.index = df.index +1
print(df)
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

#imie staje sie indeksem po którym bedziemy wyszukwiać. odwraca to metoda reset_index
df2 = df.set_index('Imie')
print(df2)

#            Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
# Imie                                                                        
# Adrianna        Bono    23     2    0.00     5000    K  Warszawa    Analityk
# Agnieszka   Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca
# Andrzej          Lis    32    11    0.02    13000    M    Krak�w   Kierownik
# Gracjan        Pa�ka    33     8    0.00     6000    M    Gda�sk    Ksi�gowy
# Janusz        Kocio�    44     7    0.08     6000    M  Warszawa  Sprzedawca
# Jolanta    Bara�czyk    38    10    0.02    17000    K  Warszawa   Kierownik
# Karolina      Zgrzyt    24     2    0.00     4000    K    Krak�w    Ksi�gowy
# �ucja        Zaremba    29     1    0.00     5000    K      ��d�    Analityk
# Micha�     Bara�czyk    30     3    0.00     9000    M    Krak�w    Analityk
# Miko�aj     Kowalski    41    10    0.03    15000    M      ��d�   Kierownik
# Monika      Adamczyk    30     3    0.07     5500    K    Gda�sk  Sprzedawca
# Oskar          Nowak    39     6    0.00     4500    M      ��d�    Ksi�gowy
# Pawe�      Niebieski    33     2    0.10     6000    M  Warszawa  Sprzedawca
# Piotr      Ostrowski    40     8    0.02    12000    M    Krak�w   Kierownik
# Szymon      Kowalski    33     5    0.10     5000    M  Warszawa  Sprzedawca
# Tomasz         Kowal    50    15    0.00     8000    M  Warszawa    Ksi�gowy
# Weronika      Lipska    31     5    0.00    10000    K  Warszawa    Analityk
# Zuzanna        Pa�ka    35     1    0.00     4000    K      ��d�    Ksi�gowy

#po imieniu wyciagamy dane...
print(df2.loc['Janusz'])

# Nazwisko        Kocio�
# Wiek                44
# Staz                 7
# Premia            0.08
# Zarobki           6000
# Plec                 M
# Miasto        Warszawa
# Zawod       Sprzedawca
# Name: Janusz, dtype: object

print("\n")
print(df2.loc['Janusz','Zarobki'])
#6000


#Trzeba pamiętać o spacjach aby ich nie było przed dwukropkiem i za nim
print("\n")
print(df2.loc['Janusz':'Jolanta','Miasto':'Zawod'])

#            Miasto       Zawod
# Imie                         
# Janusz   Warszawa  Sprzedawca
# Jolanta  Warszawa   Kierownik