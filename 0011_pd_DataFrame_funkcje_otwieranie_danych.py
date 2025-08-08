import pandas as pd

#przykładowe funkcje odczytu:
# read_excel()

# read_csv()

# read_sql()

# read_json()

# read_pickle()

#przykładowe funkcje zapisu:

# to_excel()

# to_csv()

# to_sql()

# to_json()

# to_pickle()

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\002_iris.xlsx")
print(df)

#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 0             0  4.9  3.0  1.4  0.2     Iris-setosa
# 1             1  4.7  3.2  1.3  0.2     Iris-setosa
# 2             2  4.6  3.1  1.5  0.2     Iris-setosa
# 3             3  5.0  3.6  1.4  0.2     Iris-setosa
# 4             4  5.4  3.9  1.7  0.4     Iris-setosa
# ..          ...  ...  ...  ...  ...             ...
# 144         144  6.7  3.0  5.2  2.3  Iris-virginica
# 145         145  6.3  2.5  5.0  1.9  Iris-virginica
# 146         146  6.5  3.0  5.2  2.0  Iris-virginica
# 147         147  6.2  3.4  5.4  2.3  Iris-virginica
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica

# [149 rows x 6 columns]

df2 = pd.read_excel("C:/Dane/2_Python_Data/999_Zbiory danych/002_iris.xlsx", sheet_name='kwiatki')
print(f"To z nazwą arkusza\n{df2}")

# [149 rows x 6 columns]
#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 0             0  4.9  3.0  1.4  0.2     Iris-setosa
# 1             1  4.7  3.2  1.3  0.2     Iris-setosa
# 2             2  4.6  3.1  1.5  0.2     Iris-setosa
# 3             3  5.0  3.6  1.4  0.2     Iris-setosa
# 4             4  5.4  3.9  1.7  0.4     Iris-setosa
# ..          ...  ...  ...  ...  ...             ...
# 144         144  6.7  3.0  5.2  2.3  Iris-virginica
# 145         145  6.3  2.5  5.0  1.9  Iris-virginica
# 146         146  6.5  3.0  5.2  2.0  Iris-virginica
# 147         147  6.2  3.4  5.4  2.3  Iris-virginica
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica

# [149 rows x 6 columns]


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

df_data = pd.read_csv(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\danecsv.csv")
print(df_data)


#         Imie  Wiek  Wzrost    Miasto
# 0    Zuzanna    33     170  Warszawa
# 1    Andrzej    22     166  Warszawa
# 2     Michal    19     180   Olsztyn
# 3     Szymon    38     190   Ostroda
# 4     Konrad    43     167    Krakow
# 5  Agnieszka    18     181    Gdansk







