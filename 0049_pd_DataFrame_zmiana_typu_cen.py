#Dzielenie przez 100
df["Price"] = df["Price"] // 100    # wynik jako int
# lub
df["Price"] = df["Price"] / 100     # wynik jako float

#iine tpy nie int a str
df["Price"] = (
    df["Price"]
    .str.replace(r'[\$,]', '', regex=True)  # usuń $, przecinki
    .str.replace(r'\.00', '', regex=True)   # usuń .00 z końca
    .astype(int)                            # konwersja na liczbę całkowitą
#Usuwanie dwoch sotatnich znaków
df["Price"] = df["Price"].astype(str).str[:-2]


df["Price"] = df["Price"].str.replace(r'[\$\,\.]', '', regex=True)