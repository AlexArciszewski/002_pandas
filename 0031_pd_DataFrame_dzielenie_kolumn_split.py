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

df['Imie i Nazwisko'] = df['Imie'] +" "+ df['Nazwisko']
df.drop('Imie', axis=1, inplace=True)
df.drop("Nazwisko",axis=1, inplace=True)
print(df.head())

#    Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod     Imie i nazwisko
# 1    23     2    0.00     5000    K  Warszawa    Analityk       Adrianna Bono
# 2    31     2    0.05     7000    K  Warszawa  Sprzedawca  Agnieszka Anielska
# 3    32    11    0.02    13000    M    Krak�w   Kierownik         Andrzej Lis
# 4    33     8    0.00     6000    M    Gda�sk    Ksi�gowy       Gracjan Pa�ka
# 5    44     7    0.08     6000    M  Warszawa  Sprzedawca       Janusz Kocio�
print("\n")
print(df.columns)
#ndex(['Wiek', 'Staz', 'Premia', 'Zarobki', 'Plec', 'Miasto', 'Zawod','Imie i nazwisko'],dtype='object')
#Zmiana położenai kolumny Imie i nazwisko

df = df[['Imie i Nazwisko', 'Wiek', 'Staz', 'Premia', 'Zarobki', 'Plec', 'Miasto', 'Zawod']]
print(df.head())
print("\n")
#przeniesienie kolumny na wybraną pozycję na pozycję po imie i nazwisko rpzesuwam Plec


col_to_move = "Plec"
target_position = 1

col = df.pop(col_to_move)
df.insert(target_position, col_to_move, col)
print("\n")
print(df.head())
print("\n")
#dzielenie split

df[['Imie', 'Nazwisko']] = df['Imie i Nazwisko'].str.split(' ',expand=True)
print(df.head())
print("\n")

#zrzucenie polaczonej kolumny
df.drop('Imie i Nazwisko', axis=1, inplace=True)

#przesuneicie na poczatek imienia i nazwiska
df = df[['Imie', 'Nazwisko', 'Wiek', 'Staz', 'Premia', 'Zarobki', 'Plec', 'Miasto', 'Zawod']]
print(df.head())