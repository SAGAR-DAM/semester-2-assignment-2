'''Problem 13 assignment 2
EULER method for 2nd order diff eq
NAME: SAGAR DAM;  DNAP'''

import numpy as np
import matplotlib.pyplot as plt

#defining variables
a=1
b=2
n=1000
h=(b-a)/n
t=np.arange(a,b,h)
y=np.zeros(len(t))
z=np.zeros(len(t))
ytrue=np.zeros(len(t))
z[0]=0
y[0]=1
ytrue[0]=y[0]

#defining functions
def f(x,y,z):
    return z
def g(t,y,z):
    w=(2*t*z-2*y+t**3*(np.log(t)))/t**2
    return w

#running loop for numerical calculation
for i in range(len(y)-1):
    y[i+1]=y[i]+h*f(t[i],y[i],z[i])
    z[i+1]=z[i]+h*g(t[i],y[i],z[i])
    
    ytrue[i+1]=7*t[i+1]/4+t[i+1]**3*np.log(t[i+1])/2-3*t[i+1]**3/4
    
#plotting
plt.plot(t,ytrue,label='true solution')    
plt.plot(t,y,label='numerical solution')  
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.show()  