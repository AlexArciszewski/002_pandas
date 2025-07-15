import numpy as np
import pandas as pd


tab = pd.Series({"a":1, "b":2, "c":3, "d":4, "e":5})
print(tab)

# a    1
# b    2
# c    3
# d    4
# e    5


print(tab.max())

# dtype: int64
# 5


print(tab.min())
# 1


print(np.sin(tab))

# a    0.841471
# b    0.909297
# c    0.141120
# d   -0.756802
# e   -0.958924
# dtype: float64























