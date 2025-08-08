import pandas as pd

df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\dane.xlsx",sheet_name='Zarzad')
print(df)
#błąd zamiast Waga powinno być Płeć
#         Imie  Wiek  Wzrost    Miasto       Waga
# 0   Karolina    38     180    Gda�sk    Kobieta
# 1    Jolanta    19     182    Krak�w    Kobieta
# 2      �ucja    42     177    Krak�w    Kobieta
# 3  Agnieszka    55     162  Warszawa    Kobieta
# 4      Agata    42     168      ��d�    Kobieta
# 5     Marcel    44     169  Warszawa  M�czyzna
# 6     Janusz    39     177    Krak�w  M�czyzna


df = pd.read_excel(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\dane.xlsx",sheet_name='Zarzad',
                   names=['Imie', 'Wiek', 'Wzrost', 'Miasto', 'Plec'])
print(df)

#         Imie  Wiek  Wzrost    Miasto       Plec
# 0   Karolina    38     180    Gda�sk    Kobieta
# 1    Jolanta    19     182    Krak�w    Kobieta
# 2      �ucja    42     177    Krak�w    Kobieta
# 3  Agnieszka    55     162  Warszawa    Kobieta
# 4      Agata    42     168      ��d�    Kobieta
# 5     Marcel    44     169  Warszawa  M�czyzna
# 6     Janusz    39     177    Krak�w  M�czyzna                   

print("\nzmiana nazwy już zaimportowanych danych")

df.rename(columns={"Plec": "Plec_pracownika"}, inplace=True)

print(df)

# zmiana nazwy ju� zaimportowanych danych
#         Imie  Wiek  Wzrost    Miasto Plec_pracownika
# 0   Karolina    38     180    Gda�sk         Kobieta
# 1    Jolanta    19     182    Krak�w         Kobieta
# 2      �ucja    42     177    Krak�w         Kobieta
# 3  Agnieszka    55     162  Warszawa         Kobieta
# 4      Agata    42     168      ��d�         Kobieta
# 5     Marcel    44     169  Warszawa       M�czyzna
# 6     Janusz    39     177    Krak�w       M�czyzna

