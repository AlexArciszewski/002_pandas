import pandas as pd



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
# zawartosc dane2
#     Imie  Waga
# 0  Monika    90
# 1  Michal    80
# 2  Szymon    75
# 3   Jezus    70
#imie jako indeks
print(dane2.set_index('Imie').join(dane1.set_index('Imie'), on='Imie'))

#         Waga    Miasto
# Imie                  
# Monika    90      Lodz
# Michal    80    Krakow
# Szymon    75  Warszawa
# Jezus     70       NaN


#bez indeksu jako imie
dane_lacznie = dane2.join(dane1.set_index("Imie"), on='Imie')
print(dane_lacznie)

#      Imie  Waga    Miasto
# 0  Monika    90      Lodz
# 1  Michal    80    Krakow
# 2  Szymon    75  Warszawa
# 3   Jezus    70       NaN
