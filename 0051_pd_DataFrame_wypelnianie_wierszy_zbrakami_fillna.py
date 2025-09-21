import pandas as pd

df = pd.read_csv(r"C:\Dane\2_ML\00001_sample_project\car-sales-missing-data.csv")

print(df)

#      Make Colour  Odometer  Doors    Price
# 0  Toyota  White  150043.0    4.0   $4,000
# 1   Honda    Red   87899.0    4.0   $5,000
# 2  Toyota   Blue       NaN    3.0   $7,000
# 3     BMW  Black   11179.0    5.0  $22,000
# 4  Nissan  White  213095.0    4.0   $3,500
# 5  Toyota  Green       NaN    4.0   $4,500
# 6   Honda    NaN       NaN    4.0   $7,500
# 7   Honda   Blue       NaN    4.0      NaN
# 8  Toyota  White   60000.0    NaN      NaN
# 9     NaN  White   31600.0    4.0   $9,700

print(df["Odometer"].mean())
# 92302.66666666667

#wypelnainei wartosciami średnimi
df["Odometer"].fillna(df["Odometer"].mean(), inplace=True)

print(df)

#      Make Colour       Odometer  Doors    Price
# 0  Toyota  White  150043.000000    4.0   $4,000
# 1   Honda    Red   87899.000000    4.0   $5,000
# 2  Toyota   Blue   92302.666667    3.0   $7,000
# 3     BMW  Black   11179.000000    5.0  $22,000
# 4  Nissan  White  213095.000000    4.0   $3,500
# 5  Toyota  Green   92302.666667    4.0   $4,500
# 6   Honda    NaN   92302.666667    4.0   $7,500
# 7   Honda   Blue   92302.666667    4.0      NaN
# 8  Toyota  White   60000.000000    NaN      NaN
# 9     NaN  White   31600.000000    4.0   $9,700