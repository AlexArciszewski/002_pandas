# Funkcja agg pozwala na obliczenie wielu różnych statystyk opisowych dla określonych zmiennych.


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


print(df.groupby('Miasto').agg({"Zarobki":['min','max']}) )


#          Zarobki       
#              min    max
# Miasto                 
# Gda�sk      5500   6000
# Krak�w      4000  13000
# Warszawa    5000  17000
# ��d�        4000  15000

print(df)
#Analizuję osoby w wieku poniżej 40 lat grupując je po miastach skąd pochodzą chce wyznaczyć min max i sredni staż oraz zarobki 
# wyciagam osoby w wieku ponizej 40
# Grupuje je wg miasta
# Wyciagam Zarobki i Staż
# Obliczam min max i srednią
print(df[df['Wiek']<40].groupby(['Miasto'])[['Zarobki','Staz']].agg(['mean','max','min']) ) 


#               Zarobki                   Staz        
#                  mean    max   min      mean max min
# Miasto                                              
# Gda�sk    5750.000000   6000  5500  5.500000   8   3
# Krak�w    8666.666667  13000  4000  5.333333  11   2
# Warszawa  8333.333333  17000  5000  4.333333  10   2
# ��d�      4500.000000   5000  4000  2.666667   6   1                                                       
