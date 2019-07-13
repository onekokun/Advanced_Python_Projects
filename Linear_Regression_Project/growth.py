from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style

read = pd.read_csv('/home/physis/Desktop/Linear_Regression_Project/file.csv')
year = read['year'].values
GDP = read['GDP(in billion USD)'].values
share = read['share of world GDP'].values
growth = read['GDP(growth)']

y = list(year)
g = list(growth)


yb = sum(y)/len(y)
gb = sum(g)/len(y)


ymyb = list(map(lambda x : x - yb,y))
gmgb = list(map(lambda x : x - gb,g))

pmny_g = []

for i in range(len(y)):
    mny_g = ymyb[i]*gmgb[i]
    pmny_g.append(mny_g)
    
symyb = list(map(lambda x: x**2,ymyb))

my_g = sum(pmny_g)/sum(symyb)




cy_g = yb - gb*my_g

X = [1980,2018]
Y = [my_g*1980+cy_g,my_g*2018+cy_g]

plt.xlabel = 'x_values'
plt.ylabel = 'y_values'
plt.title('growth of GDP')
plt.plot(X,Y,color ='c' )
plt.scatter(year,growth,color = 'r',label = 'graph')
plt.legend()

plt.show()

