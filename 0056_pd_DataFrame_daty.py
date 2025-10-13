import pandas as pd

df = pd.read_csv(r"C:\Dane\2_Python_Data\999_Zbiory danych\car-sales.csv")

print(df.head())
#      Make Colour  Odometer (KM)  Doors       Price
# 0  Toyota  White         150043      4   $4,000.00
# 1   Honda    Red          87899      4   $5,000.00
# 2  Toyota   Blue          32549      3   $7,000.00
# 3     BMW  Black          11179      5  $22,000.00
# 4  Nissan  White         213095      4   $3,500.00

#konwersja stringa z cenami:
df["Price"] = df["Price"].str.replace(r'[\$\,\.]', '', regex=True)
print(df.head())
#      Make Colour  Odometer (KM)  Doors    Price
# 0  Toyota  White         150043      4   400000
# 1   Honda    Red          87899      4   500000
# 2  Toyota   Blue          32549      3   700000
# 3     BMW  Black          11179      5  2200000
# 4  Nissan  White         213095      4   350000

#ucinamy dwa zera
df["Price"] = df["Price"].astype(str).str[:-2]
print(df.head())
#      Make Colour  Odometer (KM)  Doors  Price
# 0  Toyota  White         150043      4   4000
# 1   Honda    Red          87899      4   5000
# 2  Toyota   Blue          32549      3   7000
# 3     BMW  Black          11179      5  22000
# 4  Nissan  White         213095      4   3500

#zmiana prie na int
# df["Price"].astype(int)
df['Price'] = pd.to_numeric(df['Price'])
#Tworzenie nowej kolumny do zliczania cen:
df['Total_Sale'] = 0
df['Total_Sale'].astype(int) 

df['Total_Sale'] = df['Price'].cumsum()
df['Total_Sale']

print(df.head())
#      Make Colour  Odometer (KM)  Doors  Price  Total_Sale
# 0  Toyota  White         150043      4   4000        4000
# 1   Honda    Red          87899      4   5000        9000
# 2  Toyota   Blue          32549      3   7000       16000
# 3     BMW  Black          11179      5  22000       38000
# 4  Nissan  White         213095      4   3500       41500


# Add a column called 'Sale Date' which lists a series of successive dates starting from today (your today)
df["Sale Date"] = pd.date_range(start=pd.Timestamp.today().normalize(), periods=len(df), freq="D")

print(df)
#      Make Colour  Odometer (KM)  Doors  Price  Total_Sale  Sale Date
# 0  Toyota  White         150043      4   4000        4000 2025-10-13
# 1   Honda    Red          87899      4   5000        9000 2025-10-14
# 2  Toyota   Blue          32549      3   7000       16000 2025-10-15
# 3     BMW  Black          11179      5  22000       38000 2025-10-16
# 4  Nissan  White         213095      4   3500       41500 2025-10-17
# 5  Toyota  Green          99213      4   4500       46000 2025-10-18
# 6   Honda   Blue          45698      4   7500       53500 2025-10-19
# 7   Honda   Blue          54738      4   7000       60500 2025-10-20
# 8  Toyota  White          60000      4   6250       66750 2025-10-21
# 9  Nissan  White          31600      4   9700       76450 2025-10-22

# pd.Timestamp.today() — zwraca aktualną datę i godzinę.
# .normalize() — ustawia godzinę na 00:00:00 (żeby była czysta data).
# periods=len(df) — liczba dat = liczba wierszy w DataFrame.
# freq="D" — kolejne dni (można też dać "W" dla tygodni, "M" dla miesięcy itp.).