import pandas as pd


#załadowanie danych i ustawienie indeksów z użyciem Series i DataFrame
data_dict = {
    'Voivodeship': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'], index=[1, 2, 3, 4, 5]),
    'Capital': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'Population': [5.42, 1.42, 1.18, 2.35, 3.41]
}

data = pd.DataFrame(data_dict)

print(data)
#            Voivodeship    Capital  Population
# 1          Mazowieckie   Warszawa        5.42
# 2  Warminsko-Mazurskie    Olsztyn        1.42
# 3            Podlaskie  Bia�ystok        1.18
# 4            Pomorskie     Gda�sk        2.35
# 5          ma�opolskie     Krak�w        3.41

print("\n Opcja nr 2 index w innym miejscu \n")
data_dict2 = {
    'Voivodeship': ['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'],
    'Capital': pd.Series(['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'], index=[1, 2, 3, 4, 5]),
    'Population': [5.42, 1.42, 1.18, 2.35, 3.41]
}

df2 = pd.DataFrame(data_dict2)
print(df2)










