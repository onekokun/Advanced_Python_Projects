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
G = list(GDP)


yb = sum(y)/len(y)
Gb = sum(G)/len(y)

ymyb = list(map(lambda x : x - yb,y))
GmGb = list(map(lambda x : x - Gb,G))





pmny_G = []

for i in range(len(y)):
    mny_G = ymyb[i]*GmGb[i]
    pmny_G.append(mny_G)
    


   

symyb = list(map(lambda x: x**2,ymyb))

my_G = sum(pmny_G)/sum(symyb)


print(my_G)


plt.xlabel = 'year'
plt.ylabel = 'GDP(in billion USD)'
plt.title('GDP of India(in billion USD)')
plt.plot(year,GDP,color = 'k')
plt.show()




