import pandas as pd

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx", engine='openpyxl')

df.index +=1
print(df)

# [18 rows x 9 columns]
#          Imie   Nazwisko  Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
# 1    Adrianna       Bono    23     2  ...     5000     K  Warszawa    Analityk
# 2   Agnieszka   Anielska    31     2  ...     7000     K  Warszawa  Sprzedawca
# 3     Andrzej        Lis    32    11  ...    13000     M    Krak�w   Kierownik
# 4     Gracjan      Pa�ka    33     8  ...     6000     M    Gda�sk    Ksi�gowy
# 5      Janusz     Kocio�    44     7  ...     6000     M  Warszawa  Sprzedawca
# 6     Jolanta  Bara�czyk    38    10  ...    17000     K  Warszawa   Kierownik
# 7    Karolina     Zgrzyt    24     2  ...     4000     K    Krak�w    Ksi�gowy
# 8       �ucja    Zaremba    29     1  ...     5000     K      ��d�    Analityk
# 9      Micha�  Bara�czyk    30     3  ...     9000     M    Krak�w    Analityk
# 10    Miko�aj   Kowalski    41    10  ...    15000     M      ��d�   Kierownik
# 11     Monika   Adamczyk    30     3  ...     5500     K    Gda�sk  Sprzedawca
# 12      Oskar      Nowak    39     6  ...     4500     M      ��d�    Ksi�gowy
# 13      Pawe�  Niebieski    33     2  ...     6000     M  Warszawa  Sprzedawca
# 14      Piotr  Ostrowski    40     8  ...    12000     M    Krak�w   Kierownik
# 15     Szymon   Kowalski    33     5  ...     5000     M  Warszawa  Sprzedawca
# 16     Tomasz      Kowal    50    15  ...     8000     M  Warszawa    Ksi�gowy
# 17   Weronika     Lipska    31     5  ...    10000     K  Warszawa    Analityk
# 18    Zuzanna      Pa�ka    35     1  ...     4000     K      ��d�    Ksi�gowy

#df2 = df.set_index('Imie')
print("\n")
#Czy w kolumnie Zawod jest Sprzedawca albo Kierownik zwraca bool
print(df['Zawod'].isin(['Sprzedawca','Kierownik']))
# [18 rows x 9 columns]
# 1     False
# 2      True
# 3      True
# 4     False
#...
# Name: Zawod, dtype: bool
print("\n")
#Czy tekst zawiera daną frazę (działa tylko na kolumnach typu tekstowego).
print(df['Miasto'].str.contains('Warsz'))
# df['Miasto'].str.contains('warsz', case=False)  #ignorowanie wielkosci liter
# 1      True
# 2      True
# 3     False
# ......
# 18    False
# Name: Miasto, dtype: bool

print("\n")
#between Sprawdza, czy wartość liczbową mieści się w przedziale.

print(df['Wiek'].between(30, 40))

# 1     False
# 2      True
# 3      True
# 4      True
#......
# Name: Wiek, dtype: bool

print("\n")
#Sprawdza, czy wartość jest NaN (brakuje jej).

print(df['Staz'].isnull())     # brak danych

# 1     False
# 2     False
# 3     False
# 4     False

# Name: Staz, dtype: bool

print("\n")
print(df['Staz'].notnull())    # są dane

# 1     True
# 2     True
# 3     True

# 16    True
# 17    True
# 18    True
# Name: Staz, dtype: bool

print("\n")

#Zduplikowane wiersze
print(df.duplicated(subset =['Imie','Nazwisko']))

# 1     False
# 2     False
# 3     False
# ...........
# 18    False
# dtype: bool

print("\n")

# str.startswith() / str.endswith()

print(df['Miasto'].str.startswith('W'))

# 1      True
# 2      True
# 3     False
#........
# Name: Miasto, dtype: bool

print("\n")
print(df['Miasto'].str.endswith('awa'))


# 1      True
# 2      True
#.......
# 18    False
# Name: Miasto, dtype: bool

print("\n")
#Daje pełną kontrolę – możesz napisać własny warunek.
print(df['Wiek'].apply(lambda x: x % 2 == 0)) 


# 1     False
# 2     False
# 3      True
# .......
# Name: Wiek, dtype: bool










