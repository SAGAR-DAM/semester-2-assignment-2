'''Problem 3 assignment 2
RK 4 method for 2nd order diff eq
NAME: SAGAR DAM;  DNAP'''

import numpy as np
import matplotlib.pyplot as plt

#defining variables
a=0
b=1
n=100
h=(b-a)/n
t=np.arange(a,b,h)
y=np.zeros(len(t))
z=np.zeros(len(t))
z[0]=0
y[0]=0

def f(x,y,z):
    return z
def g(x,y,z):
    return (2*z-y+x*np.exp(x)-x)

# The RK 4 method implementation....
for i in range(len(y)-1):
    k1=h*f(t[i],y[i],z[i])
    l1=h*g(t[i],y[i],z[i])
    
    k2=h*f(t[i]+h/2,y[i]+k1/2,z[i]+l1/2)
    l2=h*g(t[i]+h/2,y[i]+k1/2,z[i]+l1/2)
    
    k3=h*f(t[i]+h/2,y[i]+k2/2,z[i]+l2/2)
    l3=h*g(t[i]+h/2,y[i]+k2/2,z[i]+l2/2)
    
    k4=h*f(t[i]+h,y[i]+k3,z[i]+l3)
    l4=h*g(t[i]+h,y[i]+k3,z[i]+l3)
    
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
    z[i+1]=z[i]+(l1+2*l2+2*l3+l4)/6
    
#plotting the graph
plt.plot(t,y)  
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot of x vs y')
plt.grid()
plt.show()  