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