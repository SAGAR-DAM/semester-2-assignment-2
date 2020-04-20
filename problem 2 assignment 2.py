'''Problem 2 assignment 2
Euler method for differential eqn
Name: SAGAR DAM;   DNAP'''

import numpy as np
from matplotlib import pyplot as plt
def f(t,y):
    z=(y/t)-(y/t)**2
    return  z

a=1
b=2
h=0.1
n=(b-a)/h
t=np.arange(a,b,h)
y=np.zeros(len(t))
y[0]=1
ysol=t/(1+np.log(t))

# Solving the given eqn
for i in range(len(y)-1):
    y[i+1]=y[i]+h*f(t[i],y[i])
plt.plot(t,y,label='Euler solution')  
plt.plot(t,ysol,label='true solution')
plt.suptitle('plotting of t vs y for actual and euler curve')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()  

# calculating absolute errors
err=np.zeros(len(t))
for i in range(len(t)):
    err[i]=abs(y[i]-ysol[i])
plt.bar(t,err,width=0.05)
plt.xlabel('t value')
plt.ylabel('absolute error at that mesh point t(i)')
plt.suptitle('plotting the absolute error for different mesh points')
plt.show()

# calculating relative errors
for i in range(len(t)-1):
    err[i+1]=abs(ysol[i+1]-y[i+1])/ysol[i+1]
plt.bar(t,err,width=0.05)
plt.xlabel('t value')
plt.ylabel('relative error at that mesh point t(i)')
plt.suptitle('plotting the relative error for different mesh points')
plt.show()