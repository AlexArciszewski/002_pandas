import pandas as pd

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\DanePD.xlsx")

print(df)
print("\n")
#        Imi�  Wiek   Waga       P�e�
# 0  Agnieszka    19   72.0    Kobieta
# 1     Marcel    18  400.0  M�czyzna
# 2    Jolanta    33   80.0    Kobieta
# 3     Bartek    29   66.0        fff
# 4      Karol    22  102.0        NaN
# 5       Adam    10    NaN  M�czyzna
# 6     Marcel    18  400.0  M�czyzna

print(df.isnull())
print("\n")
# 0  False  False  False  False
# 1  False  False  False  False
# 2  False  False  False  False
# 3  False  False  False  False
# 4  False  False  False   True
# 5  False  False   True  False
# 6  False  False  False  False


print(df.isnull().sum())
print("\n")
# Imi�    0
# Wiek    0
# Waga    1
# P�e�    1
# dtype: int64