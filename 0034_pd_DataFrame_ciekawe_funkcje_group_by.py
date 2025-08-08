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

print(df.groupby('Miasto').count())

#         Imie  Nazwisko  Wiek  Staz  Premia  Zarobki  Plec  Zawod
# Miasto                                                            
# Gda�sk       2         2     2     2       2        2     2      2
# Krak�w       4         4     4     4       4        4     4      4
# Warszawa     8         8     8     8       8        8     8      8
# ��d�         4         4     4     4       4        4     4      4
print("\n")

# zliczamy po nazwisku nie potrzebujemy wszystkich danych z tabeli:
print(df.groupby('Miasto')['Nazwisko'].count())


# Miasto
# Gda�sk      2
# Krak�w      4
# Warszawa    8
# ��d�        4
# Name: Nazwisko, dtype: int64
print("\n")
#Średnie arobki w zależnosci od miasta
print(df.groupby('Miasto')['Zarobki'].mean())


# Miasto
# Gda�sk      5750.0
# Krak�w      9500.0
# Warszawa    8000.0
# ��d�        7125.0
# Name: Zarobki, dtype: float64
print("\n")




#Średnie arobki w zależnosci od miasta
print(df.groupby(['Miasto','Zawod']).Zarobki.mean())


# Miasto    Zawod     
# Gda�sk    Ksi�gowy       6000.0
#           Sprzedawca     5500.0
# Krak�w    Analityk       9000.0
#           Kierownik     12500.0
#           Ksi�gowy       4000.0
# Warszawa  Analityk       7500.0
#           Kierownik     17000.0
#           Ksi�gowy       8000.0
#           Sprzedawca     6000.0
# ��d�      Analityk       5000.0
#           Kierownik     15000.0
#           Ksi�gowy       4250.0
# Name: Zarobki, dtype: float64