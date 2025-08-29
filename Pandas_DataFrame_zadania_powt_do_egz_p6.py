# Maski - narzędzie do wyświetlania i modyfikowania wierszy na bazie wartości kolumn
import pandas as pd
df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\zawody.xlsx", sheet_name='Arkusz1')

print(df)

# Zadanie 1. Za pomocą maski sprawdź, które osoby są z Warszawy.
print(df[df['Miasto'] == 'Warszawa'])
#       Imi�  Rzut  Skok  Czas biegu       P�e� Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
# 3  Zdzis�aw  7.38  3.14        2.32  M�czyzna    Nie  Warszawa     188
# 5      Ania  7.44  3.68        2.42    Kobieta    Nie  Warszawa     190
# 7   Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
# 9       Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182

#Zadanie 2. Wyświetl jedynie kobiety z Warszawy.

print(df[(df['Miasto'] == 'Warszawa') & (df['Płeć'] =='Kobieta')])
#        Imi�  Rzut  Skok  Czas biegu     P�e� Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11  Kobieta    Tak  Warszawa     188
# 5      Ania  7.44  3.68        2.42  Kobieta    Nie  Warszawa     190
# 7   Natalia  7.23  2.74        2.11  Kobieta    Tak  Warszawa     179
# 9       Ewa  8.88  3.00        2.04  Kobieta    Tak  Warszawa     182

# Zadanie 3. Wyświetl jedynie osoby, które mają skok krótszy niż 3,1 oraz są z Warszawy.

print(df[(df['Miasto'] == 'Warszawa') & (df['Skok'] < 3.1) ])

#       Imi�  Rzut  Skok  Czas biegu     P�e� Zawody    Miasto  Wzrost
# 7  Natalia  7.23  2.74        2.11  Kobieta    Tak  Warszawa     179
# 9      Ewa  8.88  3.00        2.04  Kobieta    Tak  Warszawa     182

# Zadanie 4. Wyświetl osoby, które mają mniej niż 188 cm wzrostu lub osoby, które mają czas biegu dłuższy niz 2,4.


print(df[(df['Wzrost'] < 180) | (df['Czas biegu'] < 2.4) ])

#        Imi�  Rzut  Skok  Czas biegu       P�e� Zawody    Miasto  Wzrost
# 0  Karolina  8.03  3.13        2.11    Kobieta    Tak  Warszawa     188
# 1   Mateusz  8.11  3.22        2.07  M�czyzna    Tak    Krak�w     178
# 2   Paulina  7.44  2.98        2.08    Kobieta    Nie    Krak�w     182
# 3  Zdzis�aw  7.38  3.14        2.32  M�czyzna    Nie  Warszawa     188
# 4    Janusz  7.98  3.55        2.22  M�czyzna    Tak    Gda�sk     192
# 7   Natalia  7.23  2.74        2.11    Kobieta    Tak  Warszawa     179
# 8     Kamil  6.59  2.94        2.98  M�czyzna    Nie    Gda�sk     178
# 9       Ewa  8.88  3.00        2.04    Kobieta    Tak  Warszawa     182

#Zadanie 6. Wyświetl osoby, które są z Krakowa oraz mają czas biegu krótszy niż 2,2 lub mężczyzn, którzy mają ponad 190 cm wzrostu.
print(df[ ((df['Miasto'] == 'Kraków') & (df['Czas biegu'] < 2.2)) | ((df['Płeć'] == 'Mężczyzna') & (df['Wzrost'] > 190))])

#       Imi�  Rzut  Skok  Czas biegu       P�e� Zawody  Miasto  Wzrost
# 1  Mateusz  8.11  3.22        2.07  M�czyzna    Tak  Krak�w     178
# 2  Paulina  7.44  2.98        2.08    Kobieta    Nie  Krak�w     182
# 4   Janusz  7.98  3.55        2.22  M�czyzna    Tak  Gda�sk     192




