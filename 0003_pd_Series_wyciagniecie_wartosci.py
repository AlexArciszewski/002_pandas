import numpy as np
import pandas as pd


some_series = pd.Series([1, 2, 3, 4, 5], index =['a', 'b', 'c', 'd', 'e'])
print(some_series)

# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64
#z lewej etykiety przypisane z index  z prawej wartości

print(some_series.values)
#[1 2 3 4 5]

print(some_series.index)
#Index(['a', 'b', 'c', 'd', 'e'], dtype='object')


#pierwszy el z some_series przypisany do a
print(some_series[0])
#1














