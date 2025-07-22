import pandas as pd

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx")

df.index +=1


print(df)
df['Staz/Wiek'] = df['Staz'] / df['Wiek']
print(df.head())

# [18 rows x 9 columns]
#         Imie  Nazwisko  Wiek  Staz  ...  Plec    Miasto       Zawod Staz/Wiek
# 1   Adrianna      Bono    23     2  ...     K  Warszawa    Analityk  0.086957
# 2  Agnieszka  Anielska    31     2  ...     K  Warszawa  Sprzedawca  0.064516
# 3    Andrzej       Lis    32    11  ...     M    Krak�w   Kierownik  0.343750
# 4    Gracjan     Pa�ka    33     8  ...     M    Gda�sk    Ksi�gowy  0.242424
# 5     Janusz    Kocio�    44     7  ...     M  Warszawa  Sprzedawca  0.159091

df['Imie i nazwisko'] = df['Imie'] +" "+ df['Nazwisko']

print(df.head())

# [5 rows x 10 columns]
#         Imie  Nazwisko  Wiek  ...       Zawod  Staz/Wiek     Imie i nazwisko
# 1   Adrianna      Bono    23  ...    Analityk   0.086957       Adrianna Bono
# 2  Agnieszka  Anielska    31  ...  Sprzedawca   0.064516  Agnieszka Anielska
# 3    Andrzej       Lis    32  ...   Kierownik   0.343750         Andrzej Lis
# 4    Gracjan     Pa�ka    33  ...    Ksi�gowy   0.242424       Gracjan Pa�ka
# 5     Janusz    Kocio�    44  ...  Sprzedawca   0.159091       Janusz Kocio�