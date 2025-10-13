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
# df["Sale Date"] = pd.date_range(start=pd.Timestamp.today().normalize(), periods=len(df), freq="D")