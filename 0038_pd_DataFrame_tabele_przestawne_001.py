import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\pracownicy.xlsx", sheet_name="Arkusz1", names=["Imie","Nazwisko", "Wiek", "Staz", "Premia", "Zarobki", "Plec", "Miasto", "Zawod"])
print(df.head(2))

#         Imie  Nazwisko  Wiek  Staz  Premia  Zarobki Plec    Miasto       Zawod
# 0   Adrianna      Bono    23     2    0.00     5000    K  Warszawa    Analityk
# 1  Agnieszka  Anielska    31     2    0.05     7000    K  Warszawa  Sprzedawca

#grupujemy po masto i Kolor oczu

print(df.groupby(['Miasto','Wiek']).agg({'Zarobki':'mean'}))


# Miasto   Wiek         
# Gda�sk   30     5500.0
#          33     6000.0
# Krak�w   24     4000.0
#          30     9000.0
#          32    13000.0
#          40    12000.0
# Warszawa 23     5000.0
#          31     8500.0
#          33     5500.0
#          38    17000.0
#          44     6000.0
#          50     8000.0
# ��d�     29     5000.0
#          35     4000.0
#          39     4500.0
#          41    15000.0
print("tabela przestawna\n")
print(df.unstack())

# Imie   0       Adrianna
#        1      Agnieszka
#        2        Andrzej
#        3        Gracjan
#        4         Janusz
#                 ...    
# Zawod  13     Kierownik
#        14    Sprzedawca
#        15      Ksi�gowy
#        16      Analityk
#        17      Ksi�gowy
# Length: 162, dtype: object
print("Tworzymy tabele przestawną")
dane = pd.pivot_table(df,
                      index="Miasto",
                      columns='Wiek',
                      values='Zarobki',
                      aggfunc='mean')
print(dane)
# Wiek          23      24      29      30  ...       40       41      44      50
# Miasto                                    ...                                  
# Gda�sk       NaN     NaN     NaN  5500.0  ...      NaN      NaN     NaN     NaN
# Krak�w       NaN  4000.0     NaN  9000.0  ...  12000.0      NaN     NaN     NaN
# Warszawa  5000.0     NaN     NaN     NaN  ...      NaN      NaN  6000.0  8000.0
# ��d�         NaN     NaN  5000.0     NaN  ...      NaN  15000.0     NaN     NaN

# [4 rows x 14 columns]


def ocena(wzrost):
    if wzrost > 185: return "wysoka osoba"
    else: return "niska osoba"
dane_ocena = dane.applymap(ocena)
print(dane_ocena)
# Wiek                23            24  ...            44            50
# Miasto                                ...                            
# Gda�sk     niska osoba   niska osoba  ...   niska osoba   niska osoba
# Krak�w     niska osoba  wysoka osoba  ...   niska osoba   niska osoba
# Warszawa  wysoka osoba   niska osoba  ...  wysoka osoba  wysoka osoba
# ��d�       niska osoba   niska osoba  ...   niska osoba   niska osoba
        