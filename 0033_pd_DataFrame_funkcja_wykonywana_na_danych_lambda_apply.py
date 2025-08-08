import pandas as pd


df = pd.DataFrame({
    'Person':['Jacek Kowalski','Agnieszka Wiśniewska', 'Paweł Nowak'],
    'Age': [17,33,45]
})
df.index +=1
print(f"{df} \n")
#
#                  Person  Age
# 1        Jacek Kowalski   17
# 2  Agnieszka Wi�niewska   33
# 3           Pawe� Nowak   45

#Tworzymy funkcję do wykonania na zbiorze danych


df['adult or a kid'] = df.Age.apply(lambda x:'adult'if x>=18 else 'a kid')

print(df)

#                  Person  Age adult or a kid
# 1        Jacek Kowalski   17          a kid
# 2  Agnieszka Wi�niewska   33          adult
# 3           Pawe� Nowak   45          adult


















