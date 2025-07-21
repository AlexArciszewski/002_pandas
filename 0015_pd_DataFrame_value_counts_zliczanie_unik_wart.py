import pandas as pd

#Załadowanie danych i zmiana indeksu
df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\dane.xlsx")
print(df)
#         Imie  Wiek  Wzrost    Miasto
# 0    Zuzanna    33     170  Warszawa
# 1    Andrzej    22     166  Warszawa
# 2     Michal    19     180   Olsztyn
# 3     Szymon    38     190   Ostr�da
# 4     Konrad    43     167    Krak�w
# 5  Agnieszka    18     181    Gda�sk
#sortowanie od 1
df.index = df.index + 1
print("\n")

print(df['Miasto'].value_counts())

# Miasto
# Warszawa    2
# Olsztyn     1
# Ostr�da     1
# Krak�w      1
# Gda�sk      1
# Name: count, dtype: int64
