import pandas as pd


df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\zawodnicy.xlsx",sheet_name='Arkusz1',names=['Imie', 'Liczba goli',	'Pozycja','Liczba meczy','Pierwszy sklad','Wartosc zawodnika','Zdjecie zawodnika'])

# 1. jak można przeglad danych
print(df)

print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 11 entries, 0 to 10
# Data columns (total 7 columns):
#  #   Column             Non-Null Count  Dtype 
# ---  ------             --------------  ----- 
#  0   Imi�               11 non-null     object
#  1   Liczba goli        11 non-null     object
#  2   Pozycja            11 non-null     object
#  3   Liczba meczy       11 non-null     object
#  4   Pierwszy sk�ad     11 non-null     object
#  5   Warto�� zawodnika  11 non-null     object
#  6   Zdjecie zawodnika  11 non-null     object
# dtypes: object(7)
# memory usage: 748.0+ bytes
#mamy większosc Dtype jako object to żle bo to stringi nie da się policzyć srredniej goli a ni nic innego

#2 usuwamy wiersz pierwszy i ostatnia kolumna bo nie sa potrzebne

df.drop(0,inplace=True)
df.drop('Zdjecie zawodnika',axis=1, inplace=True) #axis=1 bo to kolumna

print(df)


#          Imi� Liczba goli  ... Pierwszy sk�ad Warto�� zawodnika
# 1         Jan           3  ...            Tak               3.1
# 2        Adam           2  ...            Tak              3.89
# 3       Karol           1  ...            Tak               4.1
# 4     Miko�aj           4  ...            Nie               3.8
# 5      Micha�           6  ...            Tak               1.7
# 6   Tymoteusz          12  ...            Tak               3.3
# 7      Szymon           3  ...            Nie             2.978
# 8       Jacek           2  ...            Tak              2.11
# 9   Klaudiusz           1  ...            Nie               3.8
# 10       Igor           4  ...            Nie               4.5

# [10 rows x 6 columns]


df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 6 columns):
#  #   Column             Non-Null Count  Dtype 
# ---  ------             --------------  ----- 
#  0   Imi�               10 non-null     object
#  1   Liczba goli        10 non-null     object
#  2   Pozycja            10 non-null     object
#  3   Liczba meczy       10 non-null     object
#  4   Pierwszy sk�ad     10 non-null     object
#  5   Warto�� zawodnika  10 non-null     object
# dtypes: object(6)
# memory usage: 612.0+ bytes

#3 Zmiana ze stringu czyli object na wartosci numeryczne

df['Liczba meczy'] = pd.to_numeric(df['Liczba meczy'])
df['Liczba goli'] = pd.to_numeric(df['Liczba goli'])
df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 6 columns):
#  #   Column             Non-Null Count  Dtype 
# ---  ------             --------------  ----- 
#  0   Imi�               10 non-null     object
#  1   Liczba goli        10 non-null     int64 
#  2   Pozycja            10 non-null     object
#  3   Liczba meczy       10 non-null     int64 
#  4   Pierwszy sk�ad     10 non-null     object
#  5   Warto�� zawodnika  10 non-null     object
# dtypes: int64(1), object(5)
# memory usage: 612.0+ bytes

df['Wartosc zawodnika'] = df['Wartosc zawodnika'].astype('float64')

df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 6 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   Imie               10 non-null     object 
#  1   Liczba goli        10 non-null     int64  
#  2   Pozycja            10 non-null     object 
#  3   Liczba meczy       10 non-null     int64  
#  4   Pierwszy sk�ad     10 non-null     object 
#  5   Wartosc zawodnika  10 non-null     float64
# dtypes: float64(1), int64(2), object(3)
# memory usage: 612.0+ bytes

def logic(kolumna):
    if kolumna == 'Nie':
        return False
    elif kolumna == 'Tak':
        return True
    else:
        return False


df['Pierwszy sklad'] = df['Pierwszy sklad'].apply(logic)

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 1 to 10
# Data columns (total 6 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   Imie               10 non-null     object 
#  1   Liczba goli        10 non-null     int64  
#  2   Pozycja            10 non-null     object 
#  3   Liczba meczy       10 non-null     int64  
#  4   Pierwszy sklad     10 non-null     bool   
#  5   Wartosc zawodnika  10 non-null     float64
# dtypes: bool(1), float64(1), int64(2), object(2)
# memory usage: 542.0+ bytes


def logic2(kolumna):
    if kolumna == 'Nie':
        return False
    elif kolumna == 'Tak':
        return True
    else:
        return False

df2 = pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\zawodnicy.xlsx", 
    sheet_name='Arkusz1',
    names=['Imie', 'Liczba goli','Pozycja','Liczba meczy','Pierwszy sklad','Wartosc zawodnika','Zdjecie zawodnika'],
    skiprows=[1], #Skiprows – pozwala na wskazanie wierszy, które należy pominąć przy importowaniu danych
    dtype={                      #Dtype – pozwala na zdefiniowanie typu danych, które importujemy
        'Liczba goli':'int64',
        'Liczba meczy':'int64',
        'Wartosc zawodnika': 'float64'},
    usecols=['Imie', 'Liczba goli','Pozycja','Liczba meczy','Pierwszy sklad','Wartosc zawodnika'], #Usecols – pozwala na zdefiniowanie kolumn, które chcemy zaimportować nie bierzemy Zdjecia zawodnika
    converters = {'Pierwszy sklad': logic2}                #Converters – pozwala na wskazanie kolumn, które mają zostać poddane apply
    )

df2.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 7 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   Imie               10 non-null     object 
#  1   Liczba goli        10 non-null     int64  
#  2   Pozycja            10 non-null     object 
#  3   Liczba meczy       10 non-null     int64  
#  4   Pierwszy sklad     10 non-null     bool   
#  5   Wartosc zawodnika  10 non-null     float64
#  6   Zdjecie zawodnika  10 non-null     object 
# dtypes: bool(1), float64(1), int64(2), object(3)
# memory usage: 622.0+ bytes



