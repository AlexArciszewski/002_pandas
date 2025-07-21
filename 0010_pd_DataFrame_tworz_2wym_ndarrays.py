import pandas as pd
import numpy as np

#pd.Series
data_dict = {
    'Voivodeship': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'], index=[1, 2, 3, 4, 5]),
    'Capital': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'Population': [5.42, 1.42, 1.18, 2.35, 3.41]
}
# z pd.Series DataFrames
data = pd.DataFrame(data_dict)
print(data)
#            Voivodeship    Capital  Population
# 1          Mazowieckie   Warszawa        5.42
# 2  Warminsko-Mazurskie    Olsztyn        1.42
# 3            Podlaskie  Bia�ystok        1.18
# 4            Pomorskie     Gda�sk        2.35
# 5          ma�opolskie     Krak�w        3.41


#df z numpy.array([[]])

x = np.array([['Mazowieckie', 'Warszawa', 5.42],
            ['Warminsko-Mazurskie', 'Olsztyn', 	1.42],
            ['Podlaskie', 'Białystok', 	1.18],
            ['Pomorskie', 'Gdańsk', 	2.35],
            ['Małopolskie', 'Kraków', 	3.41]]
        )

#z numpy.array DataFrames
df = pd.DataFrame(x)

print(df)

#                      0          1     2
# 0          Mazowieckie   Warszawa  5.42
# 1  Warminsko-Mazurskie    Olsztyn  1.42
# 2            Podlaskie  Bia�ystok  1.18
# 3            Pomorskie     Gda�sk  2.35
# 4          Ma�opolskie     Krak�w  3.41

print("\n oznaczenie  kolumn \n")

#dodanie nazw kolumn
df = pd.DataFrame(x, columns=['Voivodeship', 'Capital',  'Population']), 

print(df)
#            Voivodeship    Capital Population
# 0          Mazowieckie   Warszawa       5.42
# 1  Warminsko-Mazurskie    Olsztyn       1.42
# 2            Podlaskie  Bia�ystok       1.18
# 3            Pomorskie     Gda�sk       2.35
# 4          Ma�opolskie     Krak�w       3.41


df = pd.DataFrame(x, columns=['Voivodeship', 'Capital',  'Population'], index=['Maz', 'WM', 'POD','POM', 'MAL'])

#              Voivodeship    Capital Population
# Maz          Mazowieckie   Warszawa       5.42
# WM   Warminsko-Mazurskie    Olsztyn       1.42
# POD            Podlaskie  Bia�ystok       1.18
# POM            Pomorskie     Gda�sk       2.35
# MAL          Ma�opolskie     Krak�w       3.41



