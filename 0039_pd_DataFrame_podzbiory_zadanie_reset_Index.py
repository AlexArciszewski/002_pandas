# Zadanie 6. Zresetuj indeks w zbiorze_scalonym za pomocą odpowiedniej metody (użyj argumentu drop=True aby nie dodawać nowych kolumn 
# powstałych z indeksu). Następnie stwórz podzbiór zbioru_scalonego wybierając jedynie rekordy, gdzie Waga > 90. Zapisz zbiór do zmiennej podzbior. 
# Na powstałym podzbiorze wylicz bmi osób za pomocą wzoru: Waga/(Wzrost w m)^2 i zapisz do zmiennej bmi.


import pandas as pd


zbior1 = pd.DataFrame({'Imię':['Szymon','Andrzej','Jan','Albert'], 'Waga':[88,92,77,105], 'Wzrost': [175, 192, 180, 185]})

zbior2 = pd.DataFrame({'Imię':['Patryk','Paweł','Adam'], 'Waga':[83,115,104]})

zbior3 = pd.DataFrame({'Imię':['Andrzej','Janusz','Paweł','Szymon','Paulina','Monika'], 'Miasto':['Warszawa','Kraków','Olsztyn','Warszawa','Kraków','Łódź']})
zbior_scalony = pd.concat([zbior1, zbior2, zbior3],ignore_index=True)
#        Imi�   Waga  Wzrost    Miasto
# 0    Szymon   88.0   175.0       NaN
# 1   Andrzej   92.0   192.0       NaN
# 2       Jan   77.0   180.0       NaN
# 3    Albert  105.0   185.0       NaN
# 4    Patryk   83.0     NaN       NaN
# 5     Pawe�  115.0     NaN       NaN
# 6      Adam  104.0     NaN       NaN
# 7   Andrzej    NaN     NaN  Warszawa
# 8    Janusz    NaN     NaN    Krak�w
# 9     Pawe�    NaN     NaN   Olsztyn
# 10   Szymon    NaN     NaN  Warszawa
# 11  Paulina    NaN     NaN    Krak�w
# 12   Monika    NaN     NaN      ��d�

zbior_scalony.reset_index(drop=True)
print(zbior_scalony)
podzbior = zbior_scalony[zbior_scalony['Waga']>90].copy() 
print(podzbior)
#       Imi�   Waga  Wzrost Miasto
# 1  Andrzej   92.0   192.0    NaN
# 3   Albert  105.0   185.0    NaN
# 5    Pawe�  115.0     NaN    NaN
# 6     Adam  104.0     NaN    NaN

podzbior['bmi'] = podzbior['Waga']/((podzbior['Wzrost']/100)**2)
print(podzbior['bmi'])

# 1    24.956597
# 3    30.679328
# 5          NaN
# 6          NaN
# Name: bmi, dtype: float64
