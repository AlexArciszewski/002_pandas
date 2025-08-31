import pandas as pd

# Funkcja merge przyjmuje cztery podstawowe argumenty:
# • Pierwszym argumentem jest pierwszy zbiór, który chcemy połączyć,
# • Drugim argumentem jest drugi zbiór, który chcemy połączyć,
# • Trzecim argumentem jest on, które definiuje na podstawie jakiej kolumny chcemy połączyć zbiory
# • Czwartym argumentem jest how, które definiuje w jaki sposób chcemy połączyć nasze zbiory. Przyjmuje cztery możliwe wartości: inner, outer, left oraz right.



zamieszkanie = pd.DataFrame(
    {
        'Imie':['Zosia','Michal','Ania','Szymon','Paulina','Monika'],
        'Miasto':['Warszawa','Krakow','Olsztyn','Warszawa','Krakow','Lodz']
                             }
    )
print('zbior1zameiszkanie')
print(zamieszkanie)

#       Imi�    Miasto
# 0    Zosia  Warszawa
# 1   Micha�    Krak�w
# 2     Ania   Olsztyn
# 3   Szymon  Warszawa
# 4  Paulina    Krak�w
# 5   Monika      ��d�



print("\nmerge\n")
dane2 = pd.DataFrame(
    {
        'Imie':['Monika','Michal','Szymon'],
        'Waga':[90 ,80, 75]
        }
    ) 
print("zbior dane2")
print(dane2)

print(pd.merge(zamieszkanie, dane2))


#      Imi�    Miasto  Waga
# 0  Micha�    Krak�w    80
# 1  Szymon  Warszawa    75
# 2  Monika      ��d�    90


#inner join ywciaga ze zbioru miasta i wrzuca je do zbioru 2. kolejnosc osob ze zbioru nr1

print("\ninner join tylko osoby których imiona znajdują sie w zbiorze dane2\n")
print(pd.merge(zamieszkanie, dane2, on='Imie',how="inner"))

# inner join
#      Imie    Miasto  Waga
# 0  Michal    Krakow    80
# 1  Szymon  Warszawa    75
# 2  Monika      Lodz    90


#Outer

print("\nouter wszystkie możliwe wartości występujące w obu zbiorach\n")

print(pd.merge(zamieszkanie, dane2, on='Imie',how="outer"))

#       Imie    Miasto  Waga
# 0     Ania   Olsztyn   NaN
# 1   Michal    Krakow  80.0
# 2   Monika      Lodz  90.0
# 3  Paulina    Krakow   NaN
# 4   Szymon  Warszawa  75.0
# 5    Zosia  Warszawa   NaN



print("\n left laczenie po wszystkich elementach z pierwszegoz bioru\n")


print(pd.merge(zamieszkanie, dane2, on='Imie',how="left"))


#       Imie    Miasto  Waga
# 0    Zosia  Warszawa   NaN
# 1   Michal    Krakow  80.0
# 2     Ania   Olsztyn   NaN
# 3   Szymon  Warszawa  75.0
# 4  Paulina    Krakow   NaN
# 5   Monika      Lodz  90.0