import pandas as pd

df2 = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
df2 = df2.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
df2.set_index(['brand','model', 'color'],inplace=True)
print(df2.index)
idx = pd.IndexSlice
score = df2.loc[idx['ford','mustang','red'], :]
print(score)
# brand model   color               ...                       
# ford  mustang red    21900  2018  ...     usa    2 days left
#               red    22000  2018  ...     usa    2 days left
#               red    21500  2019  ...     usa    2 days left
#               red    35100  2019  ...     usa  21 hours left
#               red    34100  2019  ...     usa  21 hours left
#               red    27000  2020  ...     usa    2 days left
#               red    15500  2019  ...     usa  19 hours left
