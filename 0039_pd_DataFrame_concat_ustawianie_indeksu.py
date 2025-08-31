import pandas as pd

zbior_1 =pd.DataFrame({'Imie':['Agnieszka','Ania','Michał','Zosia'],
                       'Wzrost':[190, 180, 166, 192]})

print(zbior_1)
#         Imie  Wzrost
# 0  Agnieszka     190
# 1       Ania     180
# 2     Micha�     166
# 3      Zosia     192

zbior_2 =pd.DataFrame({'Imie':['Konstanty','Janusz'],
                       'Wzrost':[173, 166,]})


Zbior_fin = pd.concat([zbior_1, zbior_2])
print(Zbior_fin)

# 0  Agnieszka     190
# 1       Ania     180
# 2     Micha�     166
# 3      Zosia     192
# 0  Konstanty     173
# 1     Janusz     166
print("\nreset_index\n")
Zbior_fin = Zbior_fin.reset_index(drop=True)
print(Zbior_fin)

#         Imie  Wzrost
# 0  Agnieszka     190
# 1       Ania     180
# 2     Micha�     166
# 3      Zosia     192
# 4  Konstanty     173
# 5     Janusz     166


print("\nignore index\n")
Zbior_fin_2 = pd.concat([zbior_1, zbior_2], ignore_index=True)
print(Zbior_fin_2)

#         Imie  Wzrost
# 0  Agnieszka     190
# 1       Ania     180
# 2     Micha�     166
# 3      Zosia     192
# 4  Konstanty     173
# 5     Janusz     166

#ułozenie zbioru danych jeden obok drugiego
print("\nAxis\n")
Zbior_fin_3 = pd.concat([zbior_1, zbior_2], axis=1)
print(Zbior_fin_3)
#         Imie  Wzrost       Imie  Wzrost
# 0  Agnieszka     190  Konstanty   173.0
# 1       Ania     180     Janusz   166.0
# 2     Micha�     166        NaN     NaN
# 3      Zosia     192        NaN     NaN


print("\nkeys\n")
Zbior_fin_4 = pd.concat([zbior_1, zbior_2], keys=['zbior_1','zbior_2'])
print(Zbior_fin_4)

#                 Imie  Wzrost
# zbior_1 0  Agnieszka     190
#         1       Ania     180
#         2     Micha�     166
#         3      Zosia     192
# zbior_2 0  Konstanty     173
#         1     Janusz     166


print("\nNaN w meijscu brakow\n")

dane1 = pd.DataFrame(
    {
        'Nazwisko':['Kowalski','Nowak','Buła'],
        'Wzrost':[190,180,145]
        }
    ) 

dane2 = pd.DataFrame(
    {
        'Imię':['jan','Maria','Piotr'],
        'Waga':[90 ,80, 75]
        }
    ) 

dane3 = pd.concat([dane1, dane2], ignore_index=True)
print(dane3)

# NaN w meijscu brakow

#    Nazwisko  Wzrost   Imi�  Waga
# 0  Kowalski   190.0    NaN   NaN
# 1     Nowak   180.0    NaN   NaN
# 2      Bu�a   145.0    NaN   NaN
# 3       NaN     NaN    jan  90.0
# 4       NaN     NaN  Maria  80.0
# 5       NaN     NaN  Piotr  75.0



