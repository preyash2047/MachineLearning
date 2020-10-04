# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:00:26 2019

@author: preya
"""
#modules
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Q: pridict x on y when y = 70
#Q: pridict y on x when x = 370
#dataset
x = [376.9, 371.8, 355.1, 335.2, 332, 335.5, 340.8, 352.7, 352.4, 338.9, 336.6, 356.3]
y = [67.3, 52.8, 50.9, 48.6, 44.2, 51.9, 50.3, 46.8, 49.6, 51.4, 48, 50.9]
testx = 370
testy = 70
#data preperation
x = np.array(x).reshape(-1,1)

#creating model
model = LinearRegression()
model.fit(x,y)
m = model.coef_[0]
c = model.intercept_

#y on x
#test y
y1 = []
for i in range(len(x)):
    y1.append(m*x[i] + c)

print("when x = "+str(testx) + " then y will be "+ str(m*testx + c))

#data visualization
plt.plot(x,y1,color="g",label='Base Line')
plt.scatter(x,y,color='b',label='Data Points')
for i in range(len(x)):
    if i == 0: plt.plot([x[i],x[i]],[y[i],y1[i]],label='Residual',color='red')
    else: plt.plot([x[i],x[i]],[y[i],y1[i]],color='red')
plt.scatter(testx,(m*370 + c),color='k',linestyle='-',linewidth='3',label="Predicated Y")
plt.title("y on x")
plt.legend()
plt.show()

#x on y
#test y
x1 = []
for i in range(len(x)):
    x1.append(m*y[i] + c)

print("when y = "+str(testy) + " then x will be "+ str(m*testy + c))

#data visualization
plt.plot(x1,y,color="g",label='Base Line')
plt.scatter(x,y,color='b',label='Data Points')
for i in range(len(x)):
    if i == 0: plt.plot([x1[i],x[i]],[y[i],y[i]],label='Residual',color='red')
    else: plt.plot([x1[i],x[i]],[y[i],y[i]],color='red')
plt.scatter((m*testy + c),testy,color='k',linestyle='-',linewidth='3',label="Predicated Y")
plt.title("x on y")
plt.legend()
plt.show()