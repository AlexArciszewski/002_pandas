import pandas as pd

df = pd.read_excel(r'C:\Dane\2_Python_Data\999_Zbiory danych\zawody.xlsx',names=['Imie','Rzut', 'Skok', 'Czas biegu', 'Plec', 'Zawody','Miasto','Wzrost'])
print(df.head())

# Zadanie 1. Wyświetl czas biegu oraz miasto dla 5 pierwszych osób za pomocą indeksowania prostego.

# #        Imie  Rzut  Skok  Czas biegu       Plec Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
# 1   Mateusz  8.11  3.22        2.07  M�czyzna    Tak    Krak�w     178
# 2   Paulina  7.44  2.98        2.08    Kobieta    Nie    Krak�w     182
# 3  Zdzis�aw  7.38  3.14        2.32  M�czyzna    Nie  Warszawa     188
# 4    Janusz  7.98  3.55        2.22  M�czyzna    Tak    Gda�sk     192

print(df[['Czas biegu','Miasto']][:5])

#    Czas biegu    Miasto
# 0        2.11  Warszawa
# 1        2.07    Krak�w
# 2        2.08    Krak�w
# 3        2.32  Warszawa
# 4        2.22    Gda�sk
# Zadanie 2. Wyświetl Imię oraz Wzrost trzech ostatnich osób.
# print(df.tail())
print(df[['Imie','Wzrost']][-3:])

#       Imie  Wzrost
# 7  Natalia     179
# 8    Kamil     178
# 9      Ewa     182
#wiersz z Januszem
#      Imie  Rzut  Skok  Czas biegu       Plec Zawody  Miasto  Wzrost
# 4  Janusz  7.98  3.55        2.22  M�czyzna    Tak  Gda�sk     192 
print(df[df['Imie'] == 'Janusz'])


#Zadanie 3. Ustaw imiona jako indeks naszej tabeli.

df2=df
df2=df2.set_index('Imie')
print(df2)
#            Rzut  Skok  Czas biegu       Plec Zawody    Miasto  Wzrost
# Imie                                                                 
# Karolina   8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
# Mateusz    8.11  3.22        2.07  M�czyzna    Tak    Krak�w     178
# Paulina    7.44  2.98        2.08    Kobieta    Nie    Krak�w     182
# Zdzis�aw   7.38  3.14        2.32  M�czyzna    Nie  Warszawa     188
# Janusz     7.98  3.55        2.22  M�czyzna    Tak    Gda�sk     192
# Ania       7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
# Agnieszka  7.33  3.04        2.52    Kobieta    Nie    Krak�w     191
# Natalia    7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
# Kamil      6.59  2.94        2.98  M�czyzna    Nie    Gda�sk     178
# Ewa        8.88  3.00        2.04    Kobieta    Tak  Warszawa     182

# Zadanie 4. Za pomocą *loc* sprawdź wszystkie informacje o Kamilu.
print(df2.loc['Kamil'])

# Rzut               6.59
# Skok               2.94
# Czas biegu         2.98
# Plec          M�czyzna
# Zawody              Nie
# Miasto           Gda�sk
# Wzrost              178
# Name: Kamil, dtype: object

# Zadanie 5. Za pomocą *loc* ustaw wzrost Janusza na 170 cm.

df2.loc['Janusz','Wzrost'] = 170
print(df2.loc['Janusz'])
# Rzut               7.98
# Skok               3.55
# Czas biegu         2.22
# Plec          M�czyzna
# Zawody              Tak
# Miasto           Gda�sk
# Wzrost              170
# Name: Janusz, dtype: object

print(df2.loc[['Janusz']])
#         Rzut  Skok  Czas biegu       Plec Zawody  Miasto  Wzrost
# Imie                                                            
# Janusz  7.98  3.55        2.22  M�czyzna    Tak  Gda�sk     170

#Zadanie 6. Za pomocą *iloc* wydrukuj dokładny wzrost Ewy.

print(df2.iloc[-1]['Wzrost'])
#182
print(df2.iloc[9,6])
#182

# Zadanie 7.Za pomocą *iloc* zmień wzrost ostatnich trzech osób na 180 cm, 170 cm oraz 190 cm.
df2.iloc[7:,6]=[180,170,190]
print(df2)

# Natalia    7.23  2.74        2.11    Kobieta    Tak  Warszawa     180
# Kamil      6.59  2.94        2.98  M�czyzna    Nie    Gda�sk     170
# Ewa        8.88  3.00        2.04    Kobieta    Tak  Warszawa     190