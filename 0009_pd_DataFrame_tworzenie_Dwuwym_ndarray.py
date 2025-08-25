import pandas as pd





dict_list = [
    {'wojewodztwo':'mazowieckie', 'stolica':'Warszawa' ,'l_ludnosci':5.42 },
    {'wojewodztwo':'warminsko-mazurskie', 'stolica':"Olsztyn" ,'l_ludnosci':1.42},
    {'wojewodztwo':'podlaskie', 'stolica':'Bialystok' ,'l_ludnosci':1.18 },
    {'wojewodztwo':'pomorskie', 'stolica':'Gdansk ' ,'l_ludnosci':2.35 },
    {'wojewodztwo':'malopolskie', 'stolica':'Krakow' ,'l_ludnosci':3.41}   
]
df = pd.DataFrame(dict_list)
print(df)
#            wojewodztwo    stolica  l_ludnosci
# 0          mazowieckie   Warszawa        5.42
# 1  warminsko-mazurskie    Olsztyn        1.42
# 2            podlaskie  Bialystok        1.18
# 3            pomorskie    Gdansk         2.35
# 4          malopolskie     Krakow        3.41
df.index += 1
df.columns = ['nazwa_woj', 'stolica_woj','populacja' ]
print(df)
#              nazwa_woj stolica_woj  populacja
# 1          mazowieckie    Warszawa       5.42
# 2  warminsko-mazurskie     Olsztyn       1.42
# 3            podlaskie   Bialystok       1.18
# 4            pomorskie     Gdansk        2.35
# 5          malopolskie      Krakow       3.41














