import pandas as pd
import numpy as np
# Zadanie 1. Stwórz tabelę danych, która wygląda następująco:
#                    Imi�  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33
# Nazwij tą tabelę *x*

data_dict = {
    'Imię': pd.Series(['Ania', 'Szymon', 'Paulina'], index=['Pierwsza osoba','Druga osoba','Trzecia osoba']),
    'Wiek':pd.Series([18,22,33], index=['Pierwsza osoba','Druga osoba','Trzecia osoba'])
}
x = pd.DataFrame(data_dict)
print(x)
#                    Imi�  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33

print("Opcja z listą słowników")
data_list_dict = [
    {'Imię':'Ania','Wiek':18},
    {'Imię':'Szymon','Wiek':22},
    {'Imię':'Paulina','Wiek':33}

]

y = pd.DataFrame(data_list_dict,index=['Pierwsza osoba','Druga osoba','Trzecia osoba'])
print(y)

#                    Imi�  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33


# Zadanie 2. Stwórz drugą tabelę, która będzie wyglądała w następujący sposób:
#                    Imie  Wiek
# Czwarta osoba   Paulina,   NaN
# Druga osoba       Szymon  22.0
# Pierwsza osoba      Ania  18.0
# Trzecia osoba        NaN  33.0
# Nazwij ją *df2*. (wskazówka: wystarczy tylko trochę zmienić kod z zadania 1)


import pandas as pd


my_data = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', None], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
    'Wiek': pd.Series([None, 22.0, 18.0, 33.0], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba'])
}
df2 =pd.DataFrame(my_data)
print(df2)

#                     Imie  Wiek
# Czwarta osoba   Paulina,   NaN
# Druga osoba       Szymon  22.0
# Pierwsza osoba      Ania  18.0
# Trzecia osoba       None  33.0

#jest NaN a nie none trze zaimportowac numpy i użyć np.nan

import pandas as pd
import numpy as np


my_data_2 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba'])
}
df2 =pd.DataFrame(my_data_2)
print(df2)

#                    Imie  Wiek
# Czwarta osoba   Paulina,   NaN
# Druga osoba       Szymon  22.0
# Pierwsza osoba      Ania  18.0
# Trzecia osoba        NaN  33.0


# Zadanie 3. Stwórz *ndarray*, który ma wyglądać w następujący sposób:
# [[10 10 10]
#  [20 20 20]
#  [30 30 30]]

# Po czym na podstawie tego *ndarray* stwórz *df*, które będzie wyglądało w następujący sposób:
#     k1  k2  k3
# w1  10  10  10
# w2  20  20  20
# w3  30  30  30

# Nazwij tą tabelę *tablica*.

ndarray = np.array([
    [10,10,10],
    [20,20,20],
    [30,30,30]
    ])
print(ndarray)

df = pd.DataFrame(ndarray)
print(df)
#     0   1   2
# 0  10  10  10
# 1  20  20  20
# 2  30  30  30
df = pd.DataFrame(ndarray,columns=['k1','k2','k3'], index=['w1','w2','w3'])
print(df)

#     k1  k2  k3
# w1  10  10  10
# w2  20  20  20
# w3  30  30  30



























