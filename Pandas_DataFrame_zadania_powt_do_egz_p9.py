#Tabele przestawne (Pivot table)


import pandas as pd



df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\zawody.xlsx",sheet_name="Arkusz1")
print(df.head(2))

#        Imi�  Rzut  Skok  Czas biegu       P�e� Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
# 1   Mateusz  8.11  3.22        2.07  M�czyzna    Tak    Krak�w     178


# Zadanie 1. Pogrupuj powyższy zbiór danych względem Płci oraz Miasta. Dla otrzymanej tabeli znajdź przeciętny wzrost osób.

print(df.groupby(["Płeć", "Miasto"]).agg({'Wzrost':'mean'}))

#                     Wzrost
# P�e�      Miasto          
# Kobieta   Krak�w    186.50
#           Warszawa  184.75
# M�czyzna Gda�sk    185.00
#           Krak�w    178.00
#           Warszawa  188.00


#Zadanie 2. Odpakuj powyższy obiekt za pomocą metody .unstack

print(df.unstack())

# Imię    0    Karolina
#         1     Mateusz
#         2     Paulina
#         3    Zdzisław
#         4      Janusz
#                ...   
# Wzrost  5         190
#         6         191
#         7         179
#         8         178
#         9         182
# Length: 80, dtype: object


#Zadanie 3. Zbuduj identyczną tabelę jak ta z zadania 2 za pomocą pd.pivot_table().

dane = pd.pivot_table(df, index="Płeć",columns="Miasto",values="Wzrost",aggfunc='mean')
print(dane)

# Miasto     Gda�sk  Krak�w  Warszawa
# P�e�                               
# Kobieta       NaN   186.5    184.75
# M�czyzna   185.0   178.0    188.00


# Zadanie 4. Zbuduj tabelę pivot table taką jak powyżej w zadaniu 3, ale zamiast wypisanych średnich wzrostów chcemy dostać napis "Wysoka osoba" jeśli osoba ma 185 cm wzrostu lub więcej oraz "Zwykła osoba" jeśli ma mniej niż 185 cm wzrostu.

def ocena(wzrost):
    if wzrost > 185: return "wysoka osoba"
    else: return "niska osoba"
dane_ocena = dane.applymap(ocena)
print(dane_ocena)

# Miasto          Gda�sk        Krak�w      Warszawa
# P�e�                                              
# Kobieta    niska osoba  wysoka osoba   niska osoba
# M�czyzna  niska osoba   niska osoba  wysoka osoba





