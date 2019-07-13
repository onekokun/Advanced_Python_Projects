from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from matplotlib import style

read = pd.read_csv('/home/physis/Desktop/Linear_Regression_Project/file.csv')
year = read['year'].values
GDP = read['GDP(in billion USD)'].values
share = read['share of world GDP'].values
growth = read['GDP(growth)'].values


y = list(year)
s = list(share)

yb = sum(y)/len(y)
sb = sum(s)/len(y)

ymyb = list(map(lambda x : x - yb,y))
smsb = list(map(lambda x : x - sb,s))


pmny_s = []

for i in range(len(y)):
    mny_s = ymyb[i]*smsb[i]
    pmny_s.append(mny_s)
    


   

symyb = list(map(lambda x: x**2,ymyb))

my_s = sum(pmny_s)/sum(symyb)


print(my_s)




plt.xlabel = 'year'
plt.ylabel = 'share of world GDP)'
plt.title('share of world GDP')
plt.scatter(year,share,color = 'k')
plt.show()


