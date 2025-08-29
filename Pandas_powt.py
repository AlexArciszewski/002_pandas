import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Dane\2_Python_Data\998_Databases\2_db_cars_csv\mod_cars2.csv")
print(df.head())

print(df.columns)
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
print(df.columns)

df.rename(columns={'condition':'ends in'}, inplace=True)
print(df.columns)
# df.drop(columns=['was crashed'], inplace=True)
df["was_crashed"] = 0
print(df.head())

df.loc[df['model'] == 'se','was_crashed'] = 'Yes'
print(df.head())

def was_crashed(was_crashed):
    if was_crashed == 0:
        return 'No'
    elif was_crashed == 'Yes':
        return 'Yes'
    else:
        return 'Yes'

df['was_crashed'] = df['was_crashed'].apply(was_crashed)
print(df.head())

df['split_test'] = 'split test'
print(df.head())


def divide(df):
    df['split'], df['test'] = df.split_test.split(" ")
    return df

df = df.apply(divide,axis=1)

print(df.head())
print(df.columns)


#    price      brand    model  year  ... was_crashed  split_test  split  test
# 0   6300     toyota  cruiser  2008  ...          No  split test  split  test
# 1   2899       ford       se  2011  ...         Yes  split test  split  test
# 2   5350      dodge      mpv  2018  ...          No  split test  split  test
# 3  25000       ford     door  2014  ...          No  split test  split  test
# 4  27700  chevrolet     1500  2018  ...          No  split test  split  test


print(df.groupby('brand').count())

#                  price  model  year  ...  split_test  split  test
# brand                                ...                         
# acura                3      3     3  ...           3      3     3
# audi                 4      4     4  ...           4      4     4
# bmw                 17     17    17  ...          17     17    17
# buick               13     13    13  ...          13     13    13
# cadillac            10     10    10  ...          10     10    10
# chevrolet          297    297   297  ...         297    297   297
# chrysler            18     18    18  ...          18     18    18
# dodge              432    432   432  ...         432    432   432
# ford              1235   1235  1235  ...        1235   1235  1235
# gmc                 42     42    42  ...          42     42    42
# harley-davidson      1      1     1  ...           1      1     1
# heartland            5      5     5  ...           5      5     5
# honda               12     12    12  ...          12     12    12
# hyundai             15     15    15  ...          15     15    15
# infiniti            12     12    12  ...          12     12    12
# jaguar               1      1     1  ...           1      1     1
# jeep                30     30    30  ...          30     30    30
# kia                 13     13    13  ...          13     13    13
# land                 4      4     4  ...           4      4     4
# lexus                2      2     2  ...           2      2     2
# lincoln              2      2     2  ...           2      2     2
# maserati             1      1     1  ...           1      1     1
# mazda                2      2     2  ...           2      2     2
# mercedes-benz       10     10    10  ...          10     10    10
# nissan             312    312   312  ...         312    312   312
# peterbilt            4      4     4  ...           4      4     4
# ram                  1      1     1  ...           1      1     1
# toyota               1      1     1  ...           1      1     1


print(df.groupby('brand').agg({
    'price':['min','max','mean'],
    'mileage':['min','max','mean']}))

#                  price                        mileage                          
#                    min    max          mean       min        max           mean
# brand                                                                          
# acura             1000  16900   7266.666667   63500.0   179389.0  120379.666667
# audi                 0  36400  13981.250000   47213.0   181896.0  118091.000000
# bmw                  0  61200  26397.058824    7509.0   216657.0   47846.411765
# buick                0  37500  19715.769231   12406.0   137464.0   37926.846154
# cadillac             0  47500  24941.000000   16013.0   105169.0   40195.900000
# chevrolet            0  63200  18669.952862       0.0   507985.0   65124.461279
# chrysler            25  29100  13686.111111    2473.0   231240.0   73004.000000
# dodge                0  67000  17781.988426    1091.0   239822.0   44184.863426
# ford                 0  74000  21666.888259       0.0   999999.0   52084.304453
# gmc                  0  48500  10657.380952       0.0   235348.0   58548.738095
# harley-davidson  54680  54680  54680.000000    9502.0     9502.0    9502.000000
# heartland            0   6680   2966.000000       1.0        1.0       1.000000
# honda                0  17200   6127.500000   16702.0   217290.0   91599.000000
# hyundai           3250   9800   5203.200000   25847.0   142106.0   56683.866667
# infiniti         10050  18500  13098.333333   11047.0    71967.0   25023.166667
# jaguar            2800   2800   2800.000000   20849.0    20849.0   20849.000000
# jeep                25  21100  10933.833333    8395.0   226972.0   38723.266667
# kia                  0  21500  11123.846154   11451.0   148463.0   56609.461538
# land             22500  46900  28900.000000   20103.0    32387.0   26613.750000
# lexus            10840  55600  33220.000000    8186.0    36596.0   22391.000000
# lincoln              0  36300  18150.000000   14541.0    89705.0   52123.000000
# maserati         30300  30300  30300.000000   37021.0    37021.0   37021.000000
# mazda                0  16000   8000.000000   47753.0   117541.0   82647.000000
# mercedes-benz    10740  84900  28704.000000   19427.0   110907.0   54597.000000
# nissan             375  36300  12065.820513       1.0   234792.0   42426.230769
# peterbilt            0   1025    400.000000       0.0  1017936.0  725615.750000
# ram              11050  11050  11050.000000   30421.0    30421.0   30421.000000
# toyota            6300   6300   6300.000000  274117.0   274117.0  274117.000000


print(
    df[(df['brand'] == 'ford') & (df['model'] == 'mustang')]
      .groupby('brand')
      .agg({
          'price': ['min', 'max', 'mean'],
          'mileage': ['min', 'max', 'mean']
      })
)

#        price                      mileage                       
#          min    max          mean     min      max          mean
# brand                                                           
# ford   15500  49000  25841.758621   878.0  41147.0  21551.931034

print(
    df.groupby(['brand', 'model'])
      .agg({
          'price': ['min', 'max', 'mean'],
          'mileage': ['min', 'max', 'mean']
      })
      .loc[('ford', 'mustang')])

# price    min     15500.000000
#          max     49000.000000
#          mean    25841.758621
# mileage  min       878.000000
#          max     41147.000000
#          mean    21551.931034
# Name: (ford, mustang), dtype: float64
print((df['price'] < 1000).any())
#czy sa auta ponizej 1000

print(df[df['price'] < 1000])
#wyswietl je
print(df[df['price'] < 1000].groupby(['brand']))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000029C0C5C3F90>
print(df[df['price'] < 1000].groupby(['brand'])[['brand','model','year', 'price']])
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000027BEA83E450>
print(df[df['price'] < 1000].groupby(['brand'])[['brand','model','year', 'price']].agg(['min','max']))
#                brand                model            year       price     
#                  min        max       min       max   min   max   min  max
# brand                                                                     
# audi            audi       audi      door      door  2005  2008     0   25
# bmw              bmw        bmw      door      door  2000  2000     0    0
# buick          buick      buick      door      door  2006  2006     0    0
# cadillac    cadillac   cadillac     coupe     coupe  2000  2000     0    0
# chevrolet  chevrolet  chevrolet     coupe    vehicl  1995  2020     0  450
# chrysler    chrysler   chrysler      door      door  2000  2005    25  175
# dodge          dodge      dodge      door       van  2007  2014     0  950
# ford            ford       ford   chassis     wagon  1984  2017     0  950
# gmc              gmc        gmc      door      door  1993  2018     0  500
# heartland  heartland  heartland  sundance  sundance  2009  2009     0    0
# honda          honda      honda      door      door  2003  2003     0    0
# jeep            jeep       jeep      door      door  1999  2001    25  200
# kia              kia        kia     wagon     wagon  2008  2008     0    0
# lincoln      lincoln    lincoln      door      door  2005  2005     0    0
# mazda          mazda      mazda      door      door  2009  2009     0    0
# nissan        nissan     nissan      door    sentra  2012  2018   375  925
# peterbilt  peterbilt  peterbilt     truck     truck  2009  2012     0  475

df[]