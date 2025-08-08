import pandas as pd
import numpy as np
#Stworzyć tabelę
#                    Imie  Wiek
# Czwarta osoba   Paulina,   NaN
# Druga osoba       Szymon  22.0
# Pierwsza osoba      Ania  18.0
# Trzecia osoba        NaN  33.0

my_data_2 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0], index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba'])
}
df2 =pd.DataFrame(my_data_2)
print(df2)

#                    Imie  Wiek
# Czwarta osoba   Paulina,   NaN
# Druga osoba       Szymon  22.0
# Pierwsza osoba      Ania  18.0
# Trzecia osoba        NaN  33.0

print("Opcja nr3")
my_data_3 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan]),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0]),
    'Wzrost': pd.Series([np.nan, np.nan, np.nan, np.nan])
    
}
df3 =pd.DataFrame(my_data_3,columns =['Imie','Wiek','Wzrost'])

print(df3)

#        Imie  Wiek  Wzrost
# 0  Paulina,   NaN     NaN
# 1    Szymon  22.0     NaN
# 2      Ania  18.0     NaN
# 3       NaN  33.0     NaN


print("Opcja nr4")
my_data_4 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan],index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0],index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba']),
    'Wzrost': pd.Series([np.nan, np.nan, np.nan, np.nan],index=['Czwarta osoba', 'Druga osoba', 'Pierwsza osoba', 'Trzecia osoba'])
    
}
df4 =pd.DataFrame(my_data_4, columns =['Imie','Wiek','Wzrost'])

print(df4)

# df4 =pd.DataFrame(my_data_4, columns =['Imie','Wiek','Wzrost'])
# print(df4)

# Opcja nr4
#                     Imie  Wiek  Wzrost
# Czwarta osoba   Paulina,   NaN     NaN
# Druga osoba       Szymon  22.0     NaN
# Pierwsza osoba      Ania  18.0     NaN
# Trzecia osoba        NaN  33.0     NaN

# df4 =pd.DataFrame(my_data_4)
# print(df4)

#                     Imie  Wiek  Wzrost
# Czwarta osoba   Paulina,   NaN     NaN
# Druga osoba       Szymon  22.0     NaN
# Pierwsza osoba      Ania  18.0     NaN
# Trzecia osoba        NaN  33.0     NaN

#USUNIECIE columns NIE DAJE ZMIAN WYSWIETLANEJ TABLICY JESLI MAMY  INDEX



print("Opcja nr5")
my_data_5 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan]),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0]),
    'Wzrost': pd.Series([np.nan, np.nan, np.nan, np.nan])
    
}

df5 =pd.DataFrame(my_data_5, columns =['Imie','Wiek','Wzrost'])

print(df5)

#       Imie  Wiek  Wzrost
# 0  Paulina,   NaN     NaN
# 1    Szymon  22.0     NaN
# 2      Ania  18.0     NaN
# 3       NaN  33.0     NaN

#Brak indeksów wpd.Series powoduje powstanei autoamtyczne zliczanei od zera.
#columns jest niekoneicznie ptorzebne
print("Opcja nr6")
my_data_6 = {
    'Imie': pd.Series(['Paulina,', 'Szymon', 'Ania', np.nan]),
    'Wiek': pd.Series([np.nan, 22.0, 18.0, 33.0]),
    'Wzrost': pd.Series([np.nan, np.nan, np.nan, np.nan])
    
}

df6 =pd.DataFrame(my_data_6)

print(df6)

#        Imie  Wiek  Wzrost
# 0  Paulina,   NaN     NaN
# 1    Szymon  22.0     NaN
# 2      Ania  18.0     NaN
# 3       NaN  33.0     NaN