# Przydatne funkcje w pandas (apply,groupby)

import pandas as pd
df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\zawody.xlsx", sheet_name ='Arkusz1',names=['Imie', 'Rzut','Skok', 'Czas biegu', 'Plec',  'Zawody','Miasto', 'Wzrost'])
print(df.head(2))

# Zadanie 1. Zbuduj funkcję, która będzie przypisywała osobie wartość "Osoba wysoka" jeśli ma ponad 185 cm wzrostu, za to jeśli ma mniej niż 185 cm wzrostu funkcja zwróci wartość "Osoba nie jest wysoka". Za pomocą apply użyj funkcji na df.

df['wzrost osoby'] = 0

def height(df):
    if df['Wzrost'] > 185:
        return 'osoba wysoka'
    else:
        return 'osoba niewysoka'

df['wzrost osoby'] = df.apply(height, axis=1)
print(df.head(1))

#        Imi�  Rzut  Skok  Czas biegu       P�e� Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188


# Zadanie 2. Dodaj kolumnę o nazwie "Wysokość", która ma zostać uzupełniona wynikami z zadania 1.

df['Wysokość'] = df.apply(height, axis=1)
df.drop(columns=["wzrost osoby"], inplace= True)
print(df.head(1))
#        Imi�  Rzut  Skok  Czas biegu  ... Zawody    Miasto Wzrost      Wysoko��
# 0  Karolina  8.03  3.13        2.11  ...    Tak  Warszawa    188  osoba wysoka

# [1 rows x 9 columns]


# Zadanie 3. Wykonaj Zadanie 1 za pomocą funkcji lambda.

df["wysoko z lambda"] = df.Wzrost.apply(lambda x: 'osoba wysoka'if x>185 else 'osoba niewysoka')
print(df.head(3))

#        Imi�  Rzut  Skok  ...  Wzrost         Wysoko��  wysoko z lambda
# 0  Karolina  8.03  3.13  ...     188     osoba wysoka     osoba wysoka
# 1   Mateusz  8.11  3.22  ...     178  osoba niewysoka  osoba niewysoka
# 2   Paulina  7.44  2.98  ...     182  osoba niewysoka  osoba niewysoka

# [3 rows x 10 columns]

# Zadanie 4. Zdefiniuj funkcję, która zsumuje wynik "Rzut" oraz "Skok" i zwróci wartość "Dobry wynik" jeśli ich suma będzie większa od 11,5, za to jeśli będzie mniejsza lub równa to ma zwrócić "Zły wynik".

# WSKAZÓWKA: Do funkcji podaj tylko jeden argument, który będzie listą dwóch argumentów - Rzut oraz Skok.


df["osiagi"] = 0

def summary(df):
    if df['Rzut'] + df['Skok'] > 11.5:
        return "Dobry wynik"
    else:
        return "Słaby wynik"
    

df['osiagi'] = df.apply(summary, axis=1)

print(df.head(1))

# Zadanie 5. Wykonaj Zadanie 4. za pomocją funkcji lambda.
df['osiagi z lambda'] = 0
df['osiagi z lambda'] = df.apply(lambda x: "Dobry wynik" if x['Rzut'] + x['Skok'] > 11.5 else 'Zły wynik', axis=1)

print(df.head(1))

#        Imi�  Rzut  Skok  ...  wysoko z lambda       osiagi osiagi z lambda
# 0  Karolina  8.03  3.13  ...     osoba wysoka  S�aby wynik       Z�y wynik

# Zadanie 6. Wydrukuj tablicę danych pogrupowaną względem kolumny "Miasto". Zlicz wystąpienia pozostałych kolumn.

print(df.groupby('Miasto').count())

#           Imi�  Rzut  Skok  ...  wysoko z lambda  osiagi  osiagi z lambda
# Miasto                      ...                                          
# Gda�sk       2     2     2  ...                2       2                2
# Krak�w       3     3     3  ...                3       3                3
# Warszawa     5     5     5  ...                5       5                5

# [3 rows x 11 columns]

# Zadanie 7. Wyznacz średnią czasu biegu mieszkańców poszczególnych miast.-Agregacje dla wielu kolumn

print(df.groupby('Miasto').agg({'Czas biegu':['mean']}))

#          Czas biegu
#                mean
# Miasto             
# Gda�sk     2.600000
# Krak�w     2.223333
# Warszawa   2.200000

# Zadanie 8. Oblicz średni skok kobiet i mężczyzn.

#Proste agregacje dla jednej kolumny
print(df.groupby('Plec')['Skok'].mean())

# Plec
# Kobieta      3.0950
# M�czyzna    3.2125
# Name: Skok, dtype: float64


#Zadanie 9. Policz średni rzut, maksymalny rzut, średni czas biegu oraz minimalny czas biegu dla kobiet i mężczyzn.

print(df.groupby('Plec').agg({"Rzut":["mean","max"],"Czas biegu":["mean","min"]}))

#             Rzut       Czas biegu      
#             mean   max       mean   min
# Plec                                   
# Kobieta    7.725  8.88   2.213333  2.04
# M�czyzna  7.515  8.11   2.397500  2.07


# Zadanie 10. Oblicz minimalny i maksymalny czas biegu dla osób z różnych miast, które miały maksymalny skok na poziomie 3,1.


print(df[df['Skok']<=3.1].groupby('Miasto').agg({'Czas biegu':['min','max']}))


#          Czas biegu      
#                 min   max
# Miasto                   
# Gda�sk         2.98  2.98
# Krak�w         2.08  2.52
# Warszawa       2.04  2.11
