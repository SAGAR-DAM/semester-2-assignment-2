''' Problem 1 ASSIGNMENT 2 part 2
implicit integration programme
Name: SAGAR DAM;  DNAP'''

import numpy as np
from matplotlib import pyplot as plt

a=0
b=1
n=100
h=(b-a)/n

y=np.zeros(n)
z=np.zeros(n)
t=np.zeros(n)
t[0]=0
y[0]=1/3
z[0]=1/3

for j in range (len(y)-1):
    t[j+1]=t[j]+h
    a=1+20*h
    b=-40*h*t[j+1]
    c=20*h*(t[j+1])**2-y[j]
    y[j+1]=(-b+np.sqrt(b**2-4*a*c))/(2*a)
    z[j+1]=(-b-np.sqrt(b**2-4*a*c))/(2*a)

plt.plot(t,y,'r',label='plotted with + sign in quadratic algebric eq')
plt.plot(t,z,'g',label='plotted with - sign in quadratic algebric eq')
plt.suptitle('solving the given differential equation')
plt.title('(with the algebric quadratic eqn with both + and - sign)')
plt.xlabel('t')
plt.ylabel('y')  
plt.legend()
plt.grid()
plt.show()
