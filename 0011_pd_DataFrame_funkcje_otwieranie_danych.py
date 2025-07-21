import pandas as pd

#przykładowe funkcje odczytu:
# read_excel()

# read_csv()

# read_sql()

# read_json()

# read_pickle()

#przykładowe funkcje zapisu:

# to_excel()

# to_csv()

# to_sql()

# to_json()

# to_pickle()

df = pd.read_excel(r"C:\Dane\2_Python_Data\999_Zbiory danych\002_iris.xlsx")
print(df)

#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 0             0  4.9  3.0  1.4  0.2     Iris-setosa
# 1             1  4.7  3.2  1.3  0.2     Iris-setosa
# 2             2  4.6  3.1  1.5  0.2     Iris-setosa
# 3             3  5.0  3.6  1.4  0.2     Iris-setosa
# 4             4  5.4  3.9  1.7  0.4     Iris-setosa
# ..          ...  ...  ...  ...  ...             ...
# 144         144  6.7  3.0  5.2  2.3  Iris-virginica
# 145         145  6.3  2.5  5.0  1.9  Iris-virginica
# 146         146  6.5  3.0  5.2  2.0  Iris-virginica
# 147         147  6.2  3.4  5.4  2.3  Iris-virginica
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica

# [149 rows x 6 columns]

df2 = pd.read_excel("C:/Dane/2_Python_Data/999_Zbiory danych/002_iris.xlsx", sheet_name='kwiatki')
print(f"To z nazwą arkusza\n{df2}")

# [149 rows x 6 columns]
#      Unnamed: 0  5.1  3.5  1.4  0.2     Iris-setosa
# 0             0  4.9  3.0  1.4  0.2     Iris-setosa
# 1             1  4.7  3.2  1.3  0.2     Iris-setosa
# 2             2  4.6  3.1  1.5  0.2     Iris-setosa
# 3             3  5.0  3.6  1.4  0.2     Iris-setosa
# 4             4  5.4  3.9  1.7  0.4     Iris-setosa
# ..          ...  ...  ...  ...  ...             ...
# 144         144  6.7  3.0  5.2  2.3  Iris-virginica
# 145         145  6.3  2.5  5.0  1.9  Iris-virginica
# 146         146  6.5  3.0  5.2  2.0  Iris-virginica
# 147         147  6.2  3.4  5.4  2.3  Iris-virginica
# 148         148  5.9  3.0  5.1  1.8  Iris-virginica

# [149 rows x 6 columns]














