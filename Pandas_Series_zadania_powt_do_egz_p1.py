import pandas as pd
import numpy as np

# Zadanie 1. Stwórz *series* składającą się z liczb od 5 do 10. Przypisz nazwy indeksów "a,b,c,d,e,f". Przypisz tą tablicę do zmiennej *x* (nie używaj słownika).

x = pd.Series([5, 6, 7, 8, 9, 10], index=['a','b','c','d','e','f'])
print(x)


#Zadanie 2. Wydrukuj wartości znajdujące się w w tabeli *x*.

print(f"Values:{x.values}, Indexes {x.index}")
#Values:[ 5  6  7  8  9 10], Indexes Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')


# Zadanie 3. Wydrukuj indeksy znajdujące się w tabeli *x*.

print(x.index)
# Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')

# Zadanie 4. Zbuduj dokładnie taką samą tablicę jak wyżej używając słownika. Przypisz tablicę do zmiennej *y*.

data = {
    'a': 5,
    'b': 6,
    'c': 7,
    'd': 8,
    'e': 9,
    'f': 10
}

y = pd.Series(data)
print(y)
# a     5
# b     6
# c     7
# d     8
# e     9
# f    10
# dtype: int64

#Zadanie 5. Wydrukuj trzy pierwsze elementy tablicy *y*.

print(y[:3])
# a    5
# b    6
# c    7
# dtype: int64

# Zadanie 6. Wydrukuj element odpowiadający indeksowi a oraz b.

print(y['a'])
print(y['b'])

#5
#6

#Zadanie 7. Zmień wartość przypisaną do indeksu "a" na wartość 100.

y['a'] = 100 
print(y)

# a    100
# b      6
# c      7
# d      8
# e      9
# f     10
# dtype: int64



# Zadanie 8. Zmień indeks "d" na "xyz".

y['xyz'] = y.pop('d')

print(y)

# a      100
# b        6
# c        7
# e        9
# f       10
# xyz      8
# dtype: int64

#Zadanie 9. Znajdź maksimum tabeli *y*.

print(y.max())

#100

# Zadanie 10. Znajdź minimuim tabeli *x*.

print(x.min())

#5