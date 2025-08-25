import pandas as pd

slownik_2 = {
    'wojewodztwo': pd.Series(['Mazowieckie','Warminsko-Mazurskie', 'Podlaskie','Pomorskie', 'małopolskie'], index=[1, 2, 3, 4, 5]),
    'stolica': ['Warszawa', 'Olsztyn', 'Białystok', 'Gdańsk', 'Kraków'],
    'l_ludnosci': [5.42, 1.42, 1.18, 2.35, 3.41]
}
df = pd.DataFrame(slownik_2)
#zmiana nazwy indeksu uzycie rename
df=df.rename(
    columns={
    'stolica':'stolica_woj',
    'l_ludnosci':'populacja'
}
    )
print(df)

#            wojewodztwo stolica_woj  populacja
# 1          Mazowieckie    Warszawa       5.42
# 2  Warminsko-Mazurskie     Olsztyn       1.42
# 3            Podlaskie   Bia�ystok       1.18
# 4            Pomorskie      Gda�sk       2.35
# 5          ma�opolskie      Krak�w       3.41

#zmiana nazwy indeksu prosciej

df.columns = ['vwojewodztwo', 'stolica_woj', 'populacja_miasta']
print(df)

#           vwojewodztwo stolica_woj  populacja_miasta
# 1          Mazowieckie    Warszawa              5.42
# 2  Warminsko-Mazurskie     Olsztyn              1.42
# 3            Podlaskie   Bia�ystok              1.18
# 4            Pomorskie      Gda�sk              2.35
# 5          ma�opolskie      Krak�w              3.41