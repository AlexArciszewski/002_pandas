import pandas as pd

slownik = {
    'wojewodztwo': ['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'],
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}


df = pd.DataFrame(slownik)

print(df)

#            wojewodztwo    stolica  l_ludnosci
# 0          Mazowieckie   Warszawa        5.42
# 1  Warminsko-Mazurskie    Olsztyn        1.42
# 2            Podlaskie  Bia�ystok        1.18
# 3            Pomorskie     Gda�sk        2.35
# 4          ma�opolskie     Krak�w        3.41

#klucze to kolumny awartości tablicy to wartości ze słownika


#Przypisanie indeksow  po załadowaniu z użyciem df index

df.index = [1, 2, 3, 4, 5]
print(df.index)

print(df)

#            wojewodztwo    stolica  l_ludnosci
# 1          Mazowieckie   Warszawa        5.42
# 2  Warminsko-Mazurskie    Olsztyn        1.42
# 3            Podlaskie  Bia�ystok        1.18
# 4            Pomorskie     Gda�sk        2.35
# 5          ma�opolskie     Krak�w        3.41


#Przypisanie indeksow w trakcie ładowania z użyciem Series


slownik_2 = {
    'wojewodztwo': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'], index=[1, 2, 3, 4, 5]),
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}
df2 = pd.DataFrame(slownik_2)



print(df2)

#            wojewodztwo    stolica  l_ludnosci
# 1          Mazowieckie   Warszawa        5.42
# 2  Warminsko-Mazurskie    Olsztyn        1.42
# 3            Podlaskie  Bia�ystok        1.18
# 4            Pomorskie     Gda�sk        2.35
# 5          ma�opolskie     Krak�w        3.41

