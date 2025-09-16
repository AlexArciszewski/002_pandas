import pandas as pd


df =pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\zledane.xlsx", 
    sheet_name='Arkusz1', 
    names=["Imie", "Rzut", "Skok", "Czas biegu", "Plec", "Zawody", "Miasto", "Wzrost"]
)
print(df)

#  	Imie 	Rzut 	Skok 	Czas biegu 	Plec 	Zawody 	Miasto 	Wzrost
# 0 	String 	Float64 	Float64 	Float64 	String 	String 	String 	Int64
# 1 	Karolina 	8.03 	3.13 	2.11 	Kobieta 	Tak 	Warszawa 	188
# 2 	Mateusz 	8.11 	3.22 	2.07 	Mężczyzna 	Tak 	Kraków 	178
# 3 	Paulina 	7.44 	2.98 	2.08 	Kobieta 	Nie 	Kraków 	182
# 4 	Zdzisław 	7.38 	3.14 	2.32 	Mężczyzna 	Nie 	Warszawa 	188
# 5 	Janusz 	7.98 	3.55 	2.22 	Mężczyzna 	Tak 	Gdańsk 	192
# 6 	Ania 	7.44 	3.68 	2.42 	Kobieta 	Nie 	Warszawa 	190
# 7 	Agnieszka 	7.33 	3.04 	2.52 	Kobieta 	Nie 	Kraków 	191
# 8 	Natalia 	7.23 	2.74 	2.11 	Kobieta 	Tak 	Warszawa 	179
# 9 	Kamil 	6.59 	2.94 	2.98 	Mężczyzna 	Nie 	Gdańsk 	178
# 10 	Ewa 	8.88 	3 	2.04 	Kobieta 	Tak 	Warszawa 	182


# Zadanie 1. Sprawdź typy danych poszczególnych kolumn w DataFrame
df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 11 entries, 0 to 10
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   Imie        11 non-null     object
#  1   Rzut        11 non-null     object
#  2   Skok        11 non-null     object
#  3   Czas biegu  11 non-null     object
#  4   Plec        11 non-null     object
#  5   Zawody      11 non-null     object
#  6   Miasto      11 non-null     object
#  7   Wzrost      11 non-null     object
# dtypes: object(8)
# memory usage: 836.0+ bytes

# Kliknij dwa razy tutaj aby zobaczyć rozwiązanie



# Zadanie 2. Usuń pierwszy wiersz zawierający typy danych.
df.drop([0], inplace=True)
df.head(2)

#  	Imie 	Rzut 	Skok 	Czas biegu 	Plec 	Zawody 	Miasto 	Wzrost
# 1 	Karolina 	8.03 	3.13 	2.11 	Kobieta 	Tak 	Warszawa 	188
# 2 	Mateusz 	8.11 	3.22 	2.07 	Mężczyzna 	Tak 	Kraków 	178





# Zadanie 3. Zamień kolumny "Rzut", "Skok" oraz "Czas biegu" na float64 za pomocą *astype*.

df['Rzut'] = df['Rzut'].astype('float64')
df['Skok'] = df['Skok'].astype('float64')
df['Czas biegu'] = df['Czas biegu'].astype('float64')
df.info()


# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   Imie        10 non-null     object 
#  1   Rzut        10 non-null     float64
#  2   Skok        10 non-null     float64
#  3   Czas biegu  10 non-null     float64
#  4   Plec        10 non-null     object 
#  5   Zawody      10 non-null     object 
#  6   Miasto      10 non-null     object 
#  7   Wzrost      10 non-null     object 
# dtypes: float64(3), object(5)
# memory usage: 772.0+ bytes


# Zadanie 4. Zamień typ zmiennej wzrost na jej odpowiedni typ za pomocą to_numeric.

df['Wzrost'] = pd.to_numeric(df['Wzrost'])
df.info()



# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   Imie        10 non-null     object 
#  1   Rzut        10 non-null     float64
#  2   Skok        10 non-null     float64
#  3   Czas biegu  10 non-null     float64
#  4   Plec        10 non-null     object 
#  5   Zawody      10 non-null     object 
#  6   Miasto      10 non-null     object 
#  7   Wzrost      10 non-null     int64  
# dtypes: float64(3), int64(1), object(4)
# memory usage: 772.0+ bytes


# Zadanie 5. Zbuduj funkcję, za pomocą której przekształcisz wartości "Tak" na True i wartości "Nie" na False


def to_bool(column):
    if column == 'Tak':
        return True
    elif column == 'Nie':
        return False
    else:
        return False
    
    
    
#Zadanie 6. Użyj powyższej funkcji na kolumnie "Zawody" naszej tabeli danych. Sprawdź czy typ danych zmienił się na bool
    
df['Zawody'] = df['Zawody'].apply(to_bool)
df.info()
    
        
#     <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   Imie        10 non-null     object 
#  1   Rzut        10 non-null     float64
#  2   Skok        10 non-null     float64
#  3   Czas biegu  10 non-null     float64
#  4   Plec        10 non-null     object 
#  5   Zawody      10 non-null     bool   
#  6   Miasto      10 non-null     object 
#  7   Wzrost      10 non-null     int64  
# dtypes: bool(1), float64(3), int64(1), object(3)
# memory usage: 702.0+ bytes
    
# Zadanie 7. Dokonaj wczytania danych po raz kolejny, wykonując wszystkie operację z zadań 1-6 na etapie importowania.    
    
    df = pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\zledane.xlsx", 
    sheet_name='Arkusz1', 
    names=["Imie", "Rzut", "Skok", "Czas biegu", "Plec", "Zawody", "Miasto", "Wzrost"],
    skiprows =[1],
    dtype ={
        'Rzut':'float64',
        'Skok':'float64',
        'Czas biegu':'float64',
        'Zawody':'bool',
        'Wzrost':'int64'
    },
    usecols=["Imie", "Rzut", "Skok", "Czas biegu", "Plec", "Zawody", "Miasto", "Wzrost"],
    converters = {'Zawody':to_bool}
)
df.info()
    
#     <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   Imie        10 non-null     object 
#  1   Rzut        10 non-null     float64
#  2   Skok        10 non-null     float64
#  3   Czas biegu  10 non-null     float64
#  4   Plec        10 non-null     object 
#  5   Zawody      10 non-null     bool   
#  6   Miasto      10 non-null     object 
#  7   Wzrost      10 non-null     int64  
# dtypes: bool(1), float64(3), int64(1), object(3)
# memory usage: 702.0+ bytes

#gdy dane np cena ma znak doalra przecinki i inne
#df["Price"] = df["Price"].str.replace('[\$\,\.]', '').astype(int)
#df["Price"] = df["Price"].str.replace('[\\$,.]', '', regex=True)
# df["Price"] = df["Price"].str.replace(r'[\$\,\.]', '', regex=True)
#df["Price"] = df["Price"].astype(int)     
    
    
    
    
    
    
    