import pandas as pd

# Zadanie 1. Zaimportuj drugi arkusz "zarzad" z pliku *pracadomowa.xlsx*. Przy importowaniu podaj nazwy kolumn "Imię, Nazwisko, Wzrost, Kolor oczu". Wyświetl tą tabelę.


df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\pracadomowa.xlsx", names=['Imie', 'Wiek', 'Wzrost', 'Kolor oczu'])
print(df)
#         Imie   Wiek  Wzrost  Kolor oczu
# 0      �ucja    Lis     180  Niebieskie
# 1       Adam   Zi�b     177       Szare
# 2  Agnieszka   K�os     156       Szare
# 3    Paulina  Zgryz     199     Zielone

df.rename(columns={'Kolor oczu':'Oczy'}, inplace=True)
print(df.head())

#         Imie   Wiek  Wzrost        Oczy
# 0      �ucja    Lis     180  Niebieskie
# 1       Adam   Zi�b     177       Szare
# 2  Agnieszka   K�os     156       Szare
# 3    Paulina  Zgryz     199     Zielone

# Zadanie 2. Zaimportuj dane będące w pliku *homework.csv*. Po zaimportowaniu danych zmień nazwy kolumn na: Imię, Nazwisko, Wzrost oraz Kolor oczu.
df2 =pd.read_csv(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\homework.csv", names=['Imię', 'Nazwisko', 'Wzrost','Kolor oczu'])
print(df2)

#         Imi� Nazwisko  Wzrost  Kolor oczu
# 0     Nazwa1   Nazwa2  Nazwa3      Nazwa4
# 1      Lucja      Lis     180  Niebieskie
# 2       Adam     Ziab     177       Szare
# 3  Agnieszka     Klos     156       Szare
# 4    Paulina    Zgryz     199     Zielone

# Zadanie 3. Zapisz utworzoną tabelkę w zadaniu 2 do excela. Ustaw nazwę pliku na *pdexcel*. Nazwij arkusz excela "Pracownicy".

df2.to_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\pdexcel.xlsx", sheet_name ='Pracownicy',index=False)

#powstał plik w katalogu o nazwie pdexcel.xlsx z akruszem Pracownicy
# index=False zapobiega zapisywaniu indeksu jako osobnej kolumny
