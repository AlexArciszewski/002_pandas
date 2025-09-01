#Łączenie zbiorów danych za pomocą concat, merge i join

import pandas as pd

zbior1 = pd.DataFrame({'Imie':['Szymon','Andrzej','Jan','Albert'], 'Waga':[88,92,77,105], 'Wzrost': [175, 192, 180, 185]})

zbior2 = pd.DataFrame({'Imie':['Patryk','Paweł','Adam'], 'Waga':[83,115,104]})

zbior3 = pd.DataFrame({'Imie':['Andrzej','Janusz','Paweł','Szymon','Paulina','Monika'], 'Miasto':['Warszawa','Kraków','Olsztyn','Warszawa','Kraków','Łódź']})

# Zadanie 1. Połącz zbior1 i zbior2 tak aby obserwacje jednego znajdowały się nad obserwacjami drugiego (uwzględnij wszystkie obserwacje). Nazwij to zbior_scalony.

zbior_scalony = pd.concat([zbior1,zbior2], ignore_index=True)
print(zbior_scalony)

#       Imi�  Waga  Wzrost
# 0   Szymon    88   175.0
# 1  Andrzej    92   192.0
# 2      Jan    77   180.0
# 3   Albert   105   185.0
# 4   Patryk    83     NaN
# 5    Pawe�   115     NaN
# 6     Adam   104     NaN


#Zadanie 2. Połącz zbiór1 i zbiór2 jeszcze raz, tym razem dodając nazwy zbiorów skąd pochodzą wartości za pomocą argumentu keys.


zbior_scalony2 = pd.concat([zbior1,zbior2], keys =['zbior_1','zbior_2'])
print(zbior_scalony2)

#               Imi�  Waga  Wzrost
# zbior_1 0   Szymon    88   175.0
#         1  Andrzej    92   192.0
#         2      Jan    77   180.0
#         3   Albert   105   185.0
# zbior_2 0   Patryk    83     NaN
#         1    Pawe�   115     NaN
#         2     Adam   104     NaN


# Zadanie 3. Połącz zbior_scalony razem ze zbiorem 3 na podstawie imion, tak aby zostały użyte jedynie obserwacje, które znajdują się w obu zbiorach jednocześnie.



# Funkcja merge przyjmuje cztery podstawowe argumenty:
# • Pierwszym argumentem jest pierwszy zbiór, który chcemy połączyć,
# • Drugim argumentem jest drugi zbiór, który chcemy połączyć,
# • Trzecim argumentem jest on, które definiuje na podstawie jakiej kolumny chcemy połączyć zbiory
# • Czwartym argumentem jest how, które definiuje w jaki sposób chcemy połączyć nasze zbiory. Przyjmuje cztery możliwe wartości: inner, outer, left oraz right.



inner_join = pd.merge(zbior_scalony,zbior2, on='Imie', how='inner')
print(inner_join)

#      Imie  Waga_x  Wzrost  Waga_y
# 0  Patryk      83     NaN      83
# 1   Pawe�     115     NaN     115
# 2    Adam     104     NaN     104

# Zadanie 4. Połącz zbior_scalony razem ze zbiorem 3 na podstawie imion, tak aby zostały użyte jedynie obserwacje, które znajdują się w zbiorze scalonym.


left_join = pd.merge(zbior_scalony,zbior3, on='Imie', how='left')
print(left_join)

#       Imie  Waga  Wzrost    Miasto
# 0   Szymon    88   175.0  Warszawa
# 1  Andrzej    92   192.0  Warszawa
# 2      Jan    77   180.0       NaN
# 3   Albert   105   185.0       NaN
# 4   Patryk    83     NaN       NaN
# 5    Pawe�   115     NaN   Olsztyn
# 6     Adam   104     NaN       NaN


# Zadanie 5. Połącz zbior_scalony razem ze zbiorem 3 na podstawie imion, tak aby zostały użyte wszystkie obserwacje.


right_join = pd.merge(zbior_scalony,zbior3, on='Imie', how='right')
print(right_join)

#       Imie   Waga  Wzrost    Miasto
# 0  Andrzej   92.0   192.0  Warszawa
# 1   Janusz    NaN     NaN    Krak�w
# 2    Pawe�  115.0     NaN   Olsztyn
# 3   Szymon   88.0   175.0  Warszawa
# 4  Paulina    NaN     NaN    Krak�w
# 5   Monika    NaN     NaN      ��d�

# Zadanie 6. Zresetuj indeks w zbiorze_scalonym za pomocą odpowiedniej metody (użyj argumentu drop=True aby nie dodawać nowych kolumn powstałych z indeksu). Następnie stwórz podzbiór zbioru_scalonego wybierając jedynie rekordy, gdzie Waga > 90. Zapisz zbiór do zmiennej podzbior. Na powstałym podzbiorze wylicz bmi osób za pomocą wzoru: Waga/(Wzrost w m)^2 i zapisz do zmiennej bmi.


zbior_scalony = zbior_scalony.reset_index(drop=True)
print(zbior_scalony)


#       Imie  Waga  Wzrost
# 0   Szymon    88   175.0
# 1  Andrzej    92   192.0
# 2      Jan    77   180.0
# 3   Albert   105   185.0
# 4   Patryk    83     NaN
# 5    Pawe�   115     NaN
# 6     Adam   104     NaN


podzbior = zbior_scalony[zbior_scalony['Waga'] >90].copy()
print(podzbior)

#      Imie  Waga  Wzrost
# 1  Andrzej    92   192.0
# 3   Albert   105   185.0
# 5    Pawe�   115     NaN
# 6     Adam   104     NaN

podzbior['bmi'] = podzbior['Waga']/(podzbior['Wzrost']**2)
print(podzbior['bmi'])

# 1    0.002496
# 3    0.003068
# 5         NaN
# 6         NaN
# Name: bmi, dtype: float64

# Zadanie 7. Do zbioru zbior_scalony dołącz kolumnę bmi ze zbioru podzbior po indeksach.

zbior_final = zbior_scalony.join(podzbior['bmi'])
print(zbior_final)


#      Imie  Waga  Wzrost       bmi
# 0   Szymon    88   175.0       NaN
# 1  Andrzej    92   192.0  0.002496
# 2      Jan    77   180.0       NaN
# 3   Albert   105   185.0  0.003068
# 4   Patryk    83     NaN       NaN
# 5    Pawe�   115     NaN       NaN
# 6     Adam   104     NaN       NaN