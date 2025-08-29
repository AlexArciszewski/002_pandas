import pandas as pd


df =pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")

print(df.columns)
# Index(['Unnamed: 0.1', 'Unnamed: 0', 'price', 'brand', 'model', 'year',
#        'title_status', 'mileage', 'color', 'vin', 'lot', 'state', 'country',
#        'condition'],
#       dtype='object')
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.columns)
# Index(['price', 'brand', 'model', 'year', 'title_status', 'mileage', 'color',
#        'vin', 'lot', 'state', 'country', 'condition'],
#       dtype='object')
df['make and model'] = df['brand'] + " " + df['model']
print(df.head())
#    price      brand    model  ...  country      condition  make and model
# 0   6300     toyota  cruiser  ...      usa   10 days left  toyota cruiser
# 1   2899       ford       se  ...      usa    6 days left         ford se
# 2   5350      dodge      mpv  ...      usa    2 days left       dodge mpv
# 3  25000       ford     door  ...      usa  22 hours left       ford door
# 4  27700  chevrolet     1500  ...      usa  22 hours left  chevrolet 1500
df.rename(columns={'condition':'ends in'}, inplace=True)
print(df.head())
#    price      brand    model  ...  country        ends in  make and model
# 0   6300     toyota  cruiser  ...      usa   10 days left  toyota cruiser
# 1   2899       ford       se  ...      usa    6 days left         ford se
# 2   5350      dodge      mpv  ...      usa    2 days left       dodge mpv
# 3  25000       ford     door  ...      usa  22 hours left       ford door
# 4  27700  chevrolet     1500  ...      usa  22 hours left  chevrolet 1500

# [5 rows x 13 columns]
df.drop(columns=['make and model'], inplace=True)

print(df.head())

#    price      brand    model  ...       state country        ends in
# 0   6300     toyota  cruiser  ...  new jersey     usa   10 days left
# 1   2899       ford       se  ...   tennessee     usa    6 days left
# 2   5350      dodge      mpv  ...     georgia     usa    2 days left
# 3  25000       ford     door  ...    virginia     usa  22 hours left
# 4  27700  chevrolet     1500  ...     florida     usa  22 hours left

# [5 rows x 12 columns]

df['crashed'] = 0
print(df.head())
#    price      brand    model  year  ...       state  country        ends in crashed
# 0   6300     toyota  cruiser  2008  ...  new jersey      usa   10 days left       0
# 1   2899       ford       se  2011  ...   tennessee      usa    6 days left       0
# 2   5350      dodge      mpv  2018  ...     georgia      usa    2 days left       0
# 3  25000       ford     door  2014  ...    virginia      usa  22 hours left       0
# 4  27700  chevrolet     1500  2018  ...     florida      usa  22 hours left       0

# [5 rows x 13 columns]
df.drop(columns=['crashed'], inplace=True)
print(df.head())
#    price      brand    model  ...       state country        ends in
# 0   6300     toyota  cruiser  ...  new jersey     usa   10 days left
# 1   2899       ford       se  ...   tennessee     usa    6 days left
# 2   5350      dodge      mpv  ...     georgia     usa    2 days left
# 3  25000       ford     door  ...    virginia     usa  22 hours left
# 4  27700  chevrolet     1500  ...     florida     usa  22 hours left

# [5 rows x 12 columns]


df['crashed'] = 0
print(df.head())
#    price      brand    model  year  ...       state  country        ends in crashed
# 0   6300     toyota  cruiser  2008  ...  new jersey      usa   10 days left       0
# 1   2899       ford       se  2011  ...   tennessee      usa    6 days left       0
# 2   5350      dodge      mpv  2018  ...     georgia      usa    2 days left       0
# 3  25000       ford     door  2014  ...    virginia      usa  22 hours left       0
# 4  27700  chevrolet     1500  2018  ...     florida      usa  22 hours left       0


df.drop('crashed',axis=1, inplace=True)
print(df.head())

# [5 rows x 13 columns]
#    price      brand    model  ...       state country        ends in
# 0   6300     toyota  cruiser  ...  new jersey     usa   10 days left
# 1   2899       ford       se  ...   tennessee     usa    6 days left
# 2   5350      dodge      mpv  ...     georgia     usa    2 days left
# 3  25000       ford     door  ...    virginia     usa  22 hours left
# 4  27700  chevrolet     1500  ...     florida     usa  22 hours left

# [5 rows x 12 columns]

print(df.columns)
#tworze kolumne z brand i model

df['make and model'] = df['brand'] + " " + df['model']
print(df.head())
print(df.columns)

#    price      brand    model  ...  country        ends in  make and model
# 0   6300     toyota  cruiser  ...      usa   10 days left  toyota cruiser
# 1   2899       ford       se  ...      usa    6 days left         ford se

df.drop(columns=['brand','model'], inplace=True)
print(df.head())
print(df.columns)

#usuniecie brand i model

df[['brand','model']] = df['make and model'].str.split(' ', expand=True)
print(df.head())
print(df.columns)

#   price  year   title_status  ...  make and model      brand    model
#0   6300  2008  clean vehicle  ...  toyota cruiser     toyota  cruiser

# Index(['price', 'year', 'title_status', 'mileage', 'color', 'vin', 'lot',
#        'state', 'country', 'ends in', 'make and model', 'brand', 'model'],
#       dtype='object')
#uporzadkowanie kolumn 
new_order = ['brand', 'model', 'price', 'year', 'title_status', 'mileage', 'color', 'vin', 'lot','state', 'country', 'ends in']

df = df[new_order]
print(df.head())

#        brand    model  price  ...       state country        ends in
# 0     toyota  cruiser   6300  ...  new jersey     usa   10 days left








