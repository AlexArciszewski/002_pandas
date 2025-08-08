import pandas as pd


df_data = pd.read_csv(r"C:\Dane\2_ML_Projekty\003_programowanie_ML_zadanka_kurs_wprowadzenie\Moduł 2\Zbiory danych\danecsv.csv")
print(df_data)


#         Imie  Wiek  Wzrost    Miasto
# 0    Zuzanna    33     170  Warszawa
# 1    Andrzej    22     166  Warszawa
# 2     Michal    19     180   Olsztyn
# 3     Szymon    38     190   Ostroda
# 4     Konrad    43     167    Krakow
# 5  Agnieszka    18     181    Gdansk


df_data.to_excel("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/Moduł 2/Zbiory danych/new_data.xlsx", sheet_name ='dane')

#powstał plik xlsx new_data.xlsx z arkuszem dane