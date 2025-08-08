import pandas as pd


df = pd.DataFrame({
    'Person':['Jacek Kowalski','Agnieszka Wiśniewska', 'Paweł Nowak'],
    'Age': [18,33,45]
})
df.index +=1
print(f"{df} \n")
#
#                  Person  Age
# 1        Jacek Kowalski   18
# 2  Agnieszka Wi�niewska   33
# 3           Pawe� Nowak   45

#Tworzymy funkcję do wykonania na zbiorze danych

def is_adult(Age):
    if Age > 18:
        return "Adult person"
    else:
        return "A kid"
#nałozenie funkcji na kolumnę 'Age' w apply kolumna bez ''
df.Age.apply(is_adult)

df['Adult or Kid'] = df.Age.apply(is_adult)

print(f"{df} \n")

#                  Person  Age  Adult or Kid
# 1        Jacek Kowalski   18         A kid
# 2  Agnieszka Wi�niewska   33  Adult person
# 3           Pawe� Nowak   45  Adult person

#funkcja rozdzielajaca person na name i last name


def split(data):
    data['Name'], data['Last name'] = data.Person.split(' ')
    return data

df = df.apply(split,axis=1)

print(f"{df} \n")

#                  Person  Age  Adult or Kid       Name   Last name
# 1        Jacek Kowalski   18         A kid      Jacek    Kowalski
# 2  Agnieszka Wi�niewska   33  Adult person  Agnieszka  Wi�niewska
# 3           Pawe� Nowak   45  Adult person      Pawe�       Nowak

df = df[['Name', 'Last name', 'Age', 'Adult or Kid','Person']]
df.drop('Person',axis=1, inplace=True)

print(f"{df} \n")
#         Name   Last name  Age  Adult or Kid
# 1      Jacek    Kowalski   18         A kid
# 2  Agnieszka  Wi�niewska   33  Adult person
# 3      Pawe�       Nowak   45  Adult person


