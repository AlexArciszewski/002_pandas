import pandas as pd
import numpy as np

#Series dane jednowymiarowe

some_series = pd.Series([1, 2, 3, 4, 5])
print(some_series)

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

#z lewej etykiety przypisane automatycznie  z prawej wartości

some_series = pd.Series([1, 2, 3, 4, 5], index =['a', 'b', 'c', 'd', 'e'])
print(some_series)

# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64
#z lewej etykiety przypisane z index  z prawej wartości
