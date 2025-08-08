import pandas as pd
import numpy as np

print("sposób nr 1 slownik")

dict_data:dict = {
    'Imie': pd.Series(['Ania', 'Szymon', 'Paulina'], index=['Pierwsza osoba','Druga osoba','Trzecia osoba']),
    'Wiek':pd.Series([18,22,33], index=['Pierwsza osoba','Druga osoba','Trzecia osoba'])
    }
tab_1 = pd.DataFrame(dict_data)
print(tab_1)
# #                    Imie  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33

print("sposób nr 2 lista slownikow")

data_list_dict = [
    {'Imię':'Ania','Wiek':18},
    {'Imię':'Szymon','Wiek':22},
    {'Imię':'Paulina','Wiek':33}
]

tab_2 = pd.DataFrame(data_list_dict,index=['Pierwsza osoba','Druga osoba','Trzecia osoba'])
print(tab_2)

#                    Imi�  Wiek
# Pierwsza osoba     Ania    18
# Druga osoba      Szymon    22
# Trzecia osoba   Paulina    33


print("sposób nr 3 ndarray")

my_arr = np.array([
    ['Ania', 18],
    ['Szymon', 22],
    ['Paulina', 33]
])
tab_3 = pd.DataFrame(my_arr,columns=['Imie','Wiek'], index=['Pierwsza osoba','Druga osoba','Trzecia osoba'])
print(tab_3)
