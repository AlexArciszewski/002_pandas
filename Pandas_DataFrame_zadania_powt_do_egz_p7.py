#Przeprowadzanie zmian na kolumnach

import pandas as pd

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\zawody.xlsx", sheet_name='Arkusz1', names=['Imie', 'Rzut','Skok', 'Czas biegu', 'Plec',  'Zawody','Miasto', 'Wzrost'])


# Zadanie 1. Stwórz nową kolumnę o nazwie "Dobry czas" i każdej osobie przypisz wartość 0.

df['Dobry czas'] = 0
print(df.head())

#        Imi�  Rzut  Skok  Czas biegu  ... Zawody    Miasto Wzrost  Dobry czas
# 0  Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188           0
# 1   Mateusz  8.11  3.22        2.07  ...    Tak    Krak�w    178           0
# 2   Paulina  7.44  2.98        2.08  ...    Nie    Krak�w    182           0
# 3  Zdzis�aw  7.38  3.14        2.32  ...    Nie  Warszawa    188           0
# 4    Janusz  7.98  3.55        2.22  ...    Tak    Gda�sk    192           0


# Zadanie 2. Przypisz Agnieszce wartość "TAK" w kolumnie "Dobry czas"


df.loc[df['Imie'] == 'Agnieszka','Dobry czas'] = 'TAK'
print(df)
#1-najpierw maska który wiersz df['Imie'] == 'Agnieszka','Dobry czas']
#2-która komórka - 'Dobry czas'
#3robimy loc-df.loc
#4-wartosc -= 'TAK'


# 0   Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188           0
# 1    Mateusz  8.11  3.22        2.07  ...    Tak    Krak�w    178           0
# 2    Paulina  7.44  2.98        2.08  ...    Nie    Krak�w    182           0
# 3   Zdzis�aw  7.38  3.14        2.32  ...    Nie  Warszawa    188           0
# 4     Janusz  7.98  3.55        2.22  ...    Tak    Gda�sk    192           0
# 5       Ania  7.44  3.68        2.42  ...    Nie  Warszawa    190           0
# 6  Agnieszka  7.33  3.04        2.52  ...    Nie    Krak�w    191         TAK
# 7    Natalia  7.23  2.74        2.11  ...    Tak  Warszawa    179           0
# 8      Kamil  6.59  2.94        2.98  ...    Nie    Gda�sk    178           0
# 9        Ewa  8.88  3.00        2.04  ...    Tak  Warszawa    182           0

# Zadanie 3. Przypisz osobom, które mają czas biegu krótszy niż 2.2 wartość "TAK" w kolumnie "Dobry czas". Pozostałym osobom wpisz wartość "NIE".

df.loc[df['Czas biegu'] < 2.2,'Dobry czas'] = 'TAK'
df.loc[df['Czas biegu'] > 2.2,'Dobry czas'] = 'NIE'
print(df.head())
#        Imie  Rzut  Skok  Czas biegu  ... Zawody    Miasto Wzrost  Dobry czas
# 0  Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188         TAK
# 1   Mateusz  8.11  3.22        2.07  ...    Tak    Krak�w    178         TAK
# 2   Paulina  7.44  2.98        2.08  ...    Nie    Krak�w    182         TAK
# 3  Zdzis�aw  7.38  3.14        2.32  ...    Nie  Warszawa    188         NIE
# 4    Janusz  7.98  3.55        2.22  ...    Tak    Gda�sk    192         NIE

# [5 rows x 9 columns]
# Zadanie 4. Zmień nazwę kolumny "Miasto" na "Miejscowość" oraz "Czas biegu" na "Bieg"

df.rename(columns={"Czas biegu":"Bieg",'Miasto':'Miejscowość'}, inplace=True)
print(df.columns)
# Index(['Imie', 'Rzut', 'Skok', 'Bieg', 'Plec', 'Zawody', 'Miejscowo��',
#        'Wzrost', 'Dobry czas'],
#       dtype='object')

# Zadanie 5. Skasuj kolumnę "Dobry czas", używając argumentu inplace=True.

df.drop(columns=['Dobry czas'], inplace=True)
print(df.head())

#        Imie  Rzut  Skok  Bieg       Plec Zawody Miejscowo��  Wzrost
# 0  Karolina  8.03  3.13  2.11    Kobieta    Tak    Warszawa     188
# 1   Mateusz  8.11  3.22  2.07  M�czyzna    Tak      Krak�w     178
# 2   Paulina  7.44  2.98  2.08    Kobieta    Nie      Krak�w     182
# 3  Zdzis�aw  7.38  3.14  2.32  M�czyzna    Nie    Warszawa     188
# 4    Janusz  7.98  3.55  2.22  M�czyzna    Tak      Gda�sk     192

# Zadanie 6. Połącz kolumny "Imię" oraz "Płeć". Między połączone wartości wstaw dodatkową spację. Nową kolumnę nazwij "Imię + Płeć".
df['Imie + Plec'] = df['Imie'] + " " + df['Plec']
print(df) 

#         Imie  Rzut  Skok  Bieg  ... Zawody Miejscowo�� Wzrost         Imie + Plec
# 0   Karolina  8.03  3.13  2.11  ...    Tak    Warszawa    188    Karolina Kobieta
# 1    Mateusz  8.11  3.22  2.07  ...    Tak      Krak�w    178   Mateusz M�czyzna


# Zadanie 7. Z powrotem rozdziel kolumnę "Imię + Płeć" na dwie oddzielne kolumny. Nazwij pierwszą kolumnę "Rozdzielone Imię" a drugą "Rozdzielona Płeć".
df[['Imie_r','Plec_r']] = df['Imie + Plec'].str.split(" ", expand=True)
print(df.head())

#      Imie  Rzut  Skok  Bieg  ... Wzrost         Imie + Plec    Imie_r     Plec_r
# 0  Karolina  8.03  3.13  2.11  ...    188    Karolina Kobieta  Karolina    Kobieta