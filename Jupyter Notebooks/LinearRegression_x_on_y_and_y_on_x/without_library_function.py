# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:02:44 2019

@author: preya
"""

#function to find M
def findM(x,y):
    Exy = 0
    for i in range(len(x)):
        Exy = Exy + x[i]*y[i]
    Ex2 = 0
    for i in range(len(x)):
        Ex2 = Ex2 + x[i]**2        
    return ((len(x)*Exy) - (sum(x)*sum(y)))/((len(x)*Ex2)-(sum(x)*sum(x)))

#function to find C    
def findC(x,y):
    return (sum(y)- findM(x,y)*sum(x))/len(x)    

#function to find Y
def findY(x,y,x1):
    return (findM(x,y)*x1) + findC(x,y)

#dataset
x = [376.9, 371.8, 355.1, 335.2, 332, 335.5, 340.8, 352.7, 352.4, 338.9, 336.6, 356.3]
y = [67.3, 52.8, 50.9, 48.6, 44.2, 51.9, 50.3, 46.8, 49.6, 51.4, 48, 50.9]

#calling the fuction
print(findY(x,y,4))

#data preperation for base line
y1 = []
for i in range(len(x)):
    y1.append(findY(x,y,x[i]))
x1 = []
for i in range(len(x)):
    x1.append(findY(x,y,y[i]))

#data visualization for y on x
import matplotlib.pyplot as plt
plt.plot(x,y1, label="Best Fit Line")
plt.scatter(x,y,color="r", label="Data Points")
plt.scatter(8,findY(x1,y,8),color="g", label="Predicated Value")
for i in range(len(x)):
    if i == 0:
            plt.plot([x[i],x[i]],[y[i],y1[i]],color='k',linestyle='-',linewidth="2", label="Residual Value")
    else: 
            plt.plot([x[i],x[i]],[y[i],y1[i]],color='k',linestyle='-',linewidth="2")
plt.xlabel("Hours")
plt.ylabel("No of IceCreem Sold")
plt.title("Hour wise IceCreem Sold Y on X")
plt.legend()
plt.show()

#data visualization for x on y
import matplotlib.pyplot as plt
plt.plot(x1,y, label="Best Fit Line")
plt.scatter(x,y,color="r", label="Data Points")
plt.scatter(8,findY(x,y,8),color="g", label="Predicated Value")
for i in range(len(x)):
    if i == 0:
            plt.plot([x[i],x1[i]],[y[i],y[i]],color='k',linestyle='-',linewidth="2", label="Residual Value")
    else: 
            plt.plot([x[i],x1[i]],[y[i],y[i]],color='k',linestyle='-',linewidth="2")
plt.xlabel("No of IceCreem Sold")
plt.ylabel("Hours")
plt.title("Hour wise IceCreem Sold x on y")
plt.legend()
plt.show()