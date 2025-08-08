# Opis sytuacji:

# Otrzymałeś/aś dwa pliki CSV: jeden z danymi sprzedażowymi za ostatni kwartał i drugi z aktualnym katalogiem produktów i ich cenami katalogowymi. Twoim zadaniem jest szybko przeanalizować te dane i odpowiedzieć na kluczowe pytania zarządu, uwzględniając potencjalne niezgodności między raportem sprzedaży a katalogiem.


# Zadanie nr 1
# 1. Połącz dane sprzedażowe z katalogiem produktów. Ile unikalnych transakcji z pliku raport_kwartalny_sprzedaz.csv nie ma swojego odpowiednika w katalog_produktow.csv na podstawie kolumn ID produktu?

import pandas as pd

sales_df = pd.read_csv(r"C:\Dane\2_Python_Data\1001_rekrutacje\03_rekrutacja\raport_kwartalny_sprzedaz.csv", encoding='utf-8')
catalog_df = pd.read_csv(r"C:\Dane\2_Python_Data\1001_rekrutacje\03_rekrutacja\katalog_produktow.csv", encoding='utf-8')


print(sales_df.head())
print(catalog_df.head())


print(sales_df.shape)
print(catalog_df.shape)

# print(sales_df.tail())
# print(catalog_df.tail())

print("\nInfo\n")
print(sales_df.info())
print("\n")
print(catalog_df.info())

# print(sales_df.dtypes)
# print(catalog_df.dtypes)


# print(sales_df.columns)
# print(catalog_df.columns)









