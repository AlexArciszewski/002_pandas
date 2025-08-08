import pandas as pd

df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\USA_cars_datasets.csv")
print(df.head())
df_cars = df
df_cars.rename(columns={'condition':'time left'}, inplace=True)
df_cars.drop(columns=['Unnamed: 0'], inplace=True)
df_cars = df_cars.sort_values(by='brand', ascending=True)
df_cars = df_cars.reset_index(drop=True)
df_cars.index += 1
print(df_cars.head())

#   price  brand model  year  ...        lot      state country      time left
# 1  16900  acura   mdx  2014  ...  167775829    florida     usa    1 days left
# 2   3900  acura  door  2009  ...  167389316      texas     usa   2 hours left
# 3   1000  acura  door  2008  ...  167362709   michigan     usa    2 days left
# 4     25   audi  door  2008  ...  167417202      texas     usa  17 hours left
# 5  36400   audi     5  2015  ...  167780470  wisconsin     usa    2 days left


