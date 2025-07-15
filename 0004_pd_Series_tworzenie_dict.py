import numpy as np
import pandas as pd


tab = pd.Series({"a":1, "b":2, "c":3})
print(tab)

# a    1
# b    2
# c    3
# dtype: int64

print(tab[0])
#1
print(tab["a"])
#1


print(tab[1:])
#b    2
#c    3

tab["a"] =72349047239049
print(tab)

# a    72349047239049
# b                 2
# c                 3
# dtype: int64

print(tab)

tab["swaped_index"] = tab.pop("a")

print(tab)

# b                            2
# c                            3
# swaped_index    72349047239049
# dtype: int64

