import pandas as pd

# Funkcja merge przyjmuje cztery podstawowe argumenty:
# • Pierwszym argumentem jest pierwszy zbiór, który chcemy połączyć,
# • Drugim argumentem jest drugi zbiór, który chcemy połączyć,
# • Trzecim argumentem jest on, które definiuje na podstawie jakiej kolumny chcemy połączyć zbiory
# • Czwartym argumentem jest how, które definiuje w jaki sposób chcemy połączyć nasze zbiory. Przyjmuje cztery możliwe wartości: inner, outer, left oraz right.



dane1 = pd.DataFrame(
    {
        'Imie':['Zosia','Michal','Ania','Szymon','Paulina','Monika','Hose'],
        'Miasto':['Warszawa','Krakow','Olsztyn','Warszawa','Krakow','Lodz','Costa Brava']
                             }
    )
print('zawartosc dane1')
print(dane1)


# zawartosc dane1
#       Imie    Miasto
# 0    Zosia  Warszawa
# 1   Michal    Krakow
# 2     Ania   Olsztyn
# 3   Szymon  Warszawa
# 4  Paulina    Krakow
# 5   Monika      Lodz
# 6  Hose     Costa Brava 
dane2 = pd.DataFrame(
    {
        'Imie':['Monika','Michal','Szymon',"Jezus"],
        'Waga':[90 ,80, 75,70]
        }
    ) 


print("\nzawartosc2 dane2\n")

print(dane2)

#     Imie  Waga
# 0  Monika    90
# 1  Michal    80
# 2  Szymon    75
# 3   Jezus    70



print("\ninner join tylko osoby których imiona znajdują sie w zbiorze dane2\n")
print(pd.merge(dane1, dane2, on='Imie',how="inner"))


# zbor dane1
#       Imie       Miasto
# 0    Zosia     Warszawa
# 1   Michal       Krakow
# 2     Ania      Olsztyn
# 3   Szymon     Warszawa
# 4  Paulina       Krakow
# 5   Monika         Lodz
# 6     Hose  Costa Brava

#zbior dane2
#     Imie  Waga
# 0  Monika    90
# 1  Michal    80
# 2  Szymon    75
# 3   Jezus    70
#do osob ze zbioru dane 2 wyciagnelismy z dane 1 miasto w kolejnosci w jakiej wystepuja w dane1 po usunieciu rekordów bez wagi
#====================WYNIK===================================================
#      Imie    Miasto  Waga
# 0  Michal    Krakow    80
# 1  Szymon  Warszawa    75
# 2  Monika      Lodz    90