import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\DanePD.xlsx")

df.index += 1

print(df)
print('\n')

print(df.duplicated())
print('\n')


# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6    False
# 7     True
# dtype: bool
#7 wiersz jest duplikatem innego

#sumwoanie dupliaktów
print(df.duplicated().sum())
#1 zdublowany element

#usuwanie duplikatu z nadpisaniem go dzieki inplace


#przypisanie nowych danych do zmiennej bez inplace

df2 = df.drop_duplicates()
print(df2)
#         Imi�  Wiek   Waga       P�e�
# 1  Agnieszka    19   72.0    Kobieta
# 2     Marcel    18  400.0  M�czyzna
# 3    Jolanta    33   80.0    Kobieta
# 4     Bartek    29   66.0        fff
# 5      Karol    22  102.0        NaN
# 6       Adam    10    NaN  M�czyzna
print('\n')
#opcja bez przypisania nowychd anych do zmiennej
df.drop_duplicates(inplace=True)
print(df)

#         Imi�  Wiek   Waga       P�e�
# 1  Agnieszka    19   72.0    Kobieta
# 2     Marcel    18  400.0  M�czyzna
# 3    Jolanta    33   80.0    Kobieta
# 4     Bartek    29   66.0        fff
# 5      Karol    22  102.0        NaN
# 6       Adam    10    NaN  M�czyzna


