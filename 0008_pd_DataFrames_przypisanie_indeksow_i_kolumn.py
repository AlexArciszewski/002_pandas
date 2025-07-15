import pandas as pd


#załadowanie danych i ustawienie indeksów z użyciem Series i DataFrame
data_dict = {
    'Voivodeship': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'], index=[1, 2, 3, 4, 5]),
    'Capital': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'Population': [5.42, 1.42, 1.18, 2.35, 3.41]
}
print(data_dict)
#      Capital  Population          Voivodeship
# 1   Warszawa        5.42          Mazowieckie
# 2    Olsztyn        1.42  Warminsko-Mazurskie
# 3  Bia�ystok        1.18            Podlaskie
# 4     Gda�sk        2.35            Pomorskie
# 5     Krak�w        3.41          ma�opolskie

df = pd.DataFrame(data_dict, columns=['Capital', 'Population', 'Voivodeship'])

print(df)
