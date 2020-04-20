''' Problem 1 ASSIGNMENT 2 part 1
implicit integration programme
Name: SAGAR DAM;  DNAP'''

import numpy as np
from matplotlib import pyplot as plt

a=0
b=1
n=100
h=(b-a)/n

y=np.zeros(n)
t=np.zeros(n)
ytrue=np.zeros(n)
t[0]=0
y[0]=np.exp(1)
ytrue[0]=y[0]

for j in range (len(y)-1):
    t[j+1]=t[j]+h
    y[j+1]=y[j]/(1+9*h)
    ytrue[j+1]=np.exp(1-9*t[j+1])

plt.plot(t,y,label='numerical solution')
plt.plot(t,ytrue,label='true solution')
plt.xlabel('t')
plt.ylabel('y') 
plt.legend()
plt.grid() 
plt.show()