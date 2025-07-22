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

df= df.rename(columns={'Premia':'Bonus'})

print(df.head())


#         Imie  Nazwisko  Wiek  Staz  Bonus  Zarobki Plec    Miasto       Zawod
# 1   Adrianna      Bono    23     2   0.00     5000    K  Warszawa    Analityk
# 2  Agnieszka  Anielska    31     2   0.05     7000    K  Warszawa  Sprzedawca
# 3    Andrzej       Lis    32    11   0.02    13000    M    Krak�w   Kierownik
# 4    Gracjan     Pa�ka    33     8   0.00     6000    M    Gda�sk    Ksi�gowy
# 5     Janusz    Kocio�    44     7   0.08     6000    M  Warszawa  Sprzedawca

print("\n")
df.rename(columns={'Bonus':'Premia'},inplace=True)
print(df.head())

#         Imie  Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
# 1   Adrianna      Bono    23     2    0.00     5000    K  Warszawa    Analityk
# 2  Agnieszka  Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca
# 3    Andrzej       Lis    32    11    0.02    13000    M    Krak�w   Kierownik
# 4    Gracjan     Pa�ka    33     8    0.00     6000    M    Gda�sk    Ksi�gowy
# 5     Janusz    Kocio�    44     7    0.08     6000    M  Warszawa  Sprzedawca