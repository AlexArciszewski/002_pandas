import pandas as pd

# Funkcja merge przyjmuje cztery podstawowe argumenty:
# • Pierwszym argumentem jest pierwszy zbiór, który chcemy połączyć,
# • Drugim argumentem jest drugi zbiór, który chcemy połączyć,
# • Trzecim argumentem jest on, które definiuje na podstawie jakiej kolumny chcemy połączyć zbiory
# • Czwartym argumentem jest how, które definiuje w jaki sposób chcemy połączyć nasze zbiory. Przyjmuje cztery możliwe wartości: inner, outer, left oraz right.



dane1 = pd.DataFrame(
    {
        'nazwisko':['Kowalska','Kot','Sienkiewicz','Nowak'],
        'Miasto':['Warszawa','Krakow','Olsztyn','Warszawa']
                             }
    )
print('zawartosc dane1')
print(dane1)


# zawartosc dane1
#       nazwisko    Miasto
# 0     Kowalska  Warszawa
# 1          Kot    Krakow
# 2  Sienkiewicz   Olsztyn
# 3        Nowak  Warszawa

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

print("/nlaczeniepo indeksach/n")
fin = dane1.join(dane2)
print(fin)

#       nazwisko    Miasto    Imie  Waga
# 0     Kowalska  Warszawa  Monika    90
# 1          Kot    Krakow  Michal    80
# 2  Sienkiewicz   Olsztyn  Szymon    75
# 3        Nowak  Warszawa   Jezus    70

#jak taki blad sie pojawia to znaczy żew dwoch zbiorach danych sa takie same kolumny poza indeksem i nie wiemy po czym skaldac

#ValueError: columns overlap but no suffix specified: Index(['Imie'], dtype='object')