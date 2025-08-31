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

dane_lacznie = dane2.join(dane1, lsuffix="_1", rsuffix="_2")
print(dane_lacznie)



#    Imie_1  Waga  Imie_2    Miasto
# 0  Monika    90   Zosia  Warszawa
# 1  Michal    80  Michal    Krakow
# 2  Szymon    75    Ania   Olsztyn
# 3   Jezus    70  Szymon  Warszawa