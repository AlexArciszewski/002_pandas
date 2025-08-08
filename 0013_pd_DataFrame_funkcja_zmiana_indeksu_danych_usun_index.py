import pandas as pd


df1 = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\USA_cars_datasets.csv")

print(df1.head())

#    Unnamed: 0  price      brand  ...       state  country      condition
# 0           0   6300     toyota  ...  new jersey      usa   10 days left
# 1           1   2899       ford  ...   tennessee      usa    6 days left
# 2           2   5350      dodge  ...     georgia      usa    2 days left
# 3           3  25000       ford  ...    virginia      usa  22 hours left
# 4           4  27700  chevrolet  ...     florida      usa  22 hours left


df1 = df1.reset_index(drop=True)
df1.index += 1
print(df1)

# [5 rows x 13 columns]
#       Unnamed: 0  price      brand  ...       state  country      condition
# 1              0   6300     toyota  ...  new jersey      usa   10 days left
# 2              1   2899       ford  ...   tennessee      usa    6 days left
# 3              2   5350      dodge  ...     georgia      usa    2 days left
# 4              3  25000       ford  ...    virginia      usa  22 hours left
# 5              4  27700  chevrolet  ...     florida      usa  22 hours left
# ...          ...    ...        ...  ...         ...      ...            ...
# 2495        2494   7800     nissan  ...  california      usa    1 days left
# 2496        2495   9200     nissan  ...     florida      usa  21 hours left
# 2497        2496   9200     nissan  ...     florida      usa  21 hours left
# 2498        2497   9200     nissan  ...     florida      usa    2 days left
# 2499        2498   9200     nissan  ...     florida      usa  21 hours left





