# Maski – narzędzie do wyświetlania i modyfikacji wierszy na bazie wartości kolumn zamiast and jest & a zamiast or |


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

#sprawdzenie danych:

print(df['Miasto'] == 'Warszawa')

# [18 rows x 9 columns]
# 1      True
# 2      True
# 3     False
# 4     False
# 5      True
# 6      True
# 7     False
# 8     False
# 9     False
# 10    False
# 11    False
# 12    False
# 13     True
# 14    False
# 15     True
# 16     True
# 17     True
# 18    False
# Name: Miasto, dtype: bool

print("\n")
print(df[df['Miasto'] == 'Warszawa'])

#          Imie   Nazwisko  Wiek  Staz  ...  Zarobki  Plec    Miasto       Zawod
# 1    Adrianna       Bono    23     2  ...     5000     K  Warszawa    Analityk
# 2   Agnieszka   Anielska    31     2  ...     7000     K  Warszawa  Sprzedawca
# 5      Janusz     Kocio�    44     7  ...     6000     M  Warszawa  Sprzedawca
# 6     Jolanta  Bara�czyk    38    10  ...    17000     K  Warszawa   Kierownik
# 13      Pawe�  Niebieski    33     2  ...     6000     M  Warszawa  Sprzedawca
# 15     Szymon   Kowalski    33     5  ...     5000     M  Warszawa  Sprzedawca
# 16     Tomasz      Kowal    50    15  ...     8000     M  Warszawa    Ksi�gowy
# 17   Weronika     Lipska    31     5  ...    10000     K  Warszawa    Analityk

#albo Ci co nie są z Warszawy 
#print(df[df['Miasto'] != 'Warszawa'])


print("\n")
for index, row in df.iterrows():
    if row['Miasto'] == 'Warszawa':
        print(f"{row['Imie']} {row['Nazwisko']} jest z Warszawy.")

# Name: Miasto, dtype: bool
# Adrianna Bono jest z Warszawy.
# Agnieszka Anielska jest z Warszawy.
# Janusz Kocio� jest z Warszawy.
# Jolanta Bara�czyk jest z Warszawy.
# Pawe� Niebieski jest z Warszawy.
# Szymon Kowalski jest z Warszawy.
# Tomasz Kowal jest z Warszawy.
# Weronika Lipska jest z Warszawy.
#print(df[df['Miasto'] != 'Warszawa'])
print("\n")
print(  df[  ( df['Miasto'] == 'Warszawa' ) & ( df['Imie'] == 'Janusz' ) ]  )
        # df od (df)&(df)
#      Imie Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
# 5  Janusz   Kocio�    44     7    0.08     6000    M  Warszawa  Sprzedawca


print(df['Zawod'].isin(['Sprzedawca','Kierownik']))

# 1     False
# 2      True
# 3      True
# 4     False
# 5      True
# 6      True
# 7     False
# 8     False
# 9     False
# 10     True
# 11     True
# 12    False
# 13     True
# 14     True
# 15     True
# 16    False
# 17    False
# 18    False
# Name: Zawod, dtype: bool

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx")

df.index += 1 
df2 = df.set_index('Imie')

print(df2)

#             Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
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

print(df2[(df2['Wiek']< 25)])
print("\n")
# Imie                                                                   
# Adrianna     Bono    23     2     0.0     5000    K  Warszawa  Analityk
# Karolina   Zgrzyt    24     2     0.0     4000    K    Krak�w  Ksi�gowy

#osoby, które pochodzą z Warszawy i mają wiek 33 lub osoby, których zawód to sprzedawca.
#             Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod

print(df2[(df2['Miasto'] == "Warszawa") & (df2['Wiek']< 30)])                                                                
# Imie                                                                   
# Adrianna     Bono    23     2     0.0     5000    K  Warszawa  Analityk

print( df2[((df2['Miasto'] == "Warszawa") & (df2['Wiek']< 30)) | (df2['Zawod'] == "Sprzedawca" )])    
#( (WARUNEK 1) & (WARUNEK 2) ) | (WARUNEK 3)
# Imie                                                                        
# Adrianna        Bono    23     2    0.00     5000    K  Warszawa    Analityk
# Agnieszka   Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca
# Janusz        Kocio�    44     7    0.08     6000    M  Warszawa  Sprzedawca
# Monika      Adamczyk    30     3    0.07     5500    K    Gda�sk  Sprzedawca
# Pawe�      Niebieski    33     2    0.10     6000    M  Warszawa  Sprzedawca
# Szymon      Kowalski    33     5    0.10     5000    M  Warszawa  Sprzedawca