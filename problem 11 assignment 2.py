''' problem 11 assignment 2 
Coupled diff eqn with RK(4) method
Name: SAGAR DAM;  DNAP'''

import numpy as np
import matplotlib.pyplot as plt

#defining variables
a=0
b=1
n=1000
h=(b-a)/n
t=np.arange(a,b,h)
x=np.zeros(len(t))
y=np.zeros(len(t))
z=np.zeros(len(t))
x[0]=3
z[0]=-1
y[0]=1

def e(t,x,y,z):
    return (x+2*y-2*z+np.exp(-t))
def f(t,x,y,z):
    return (y+z-2*np.exp(-t))
def g(t,x,y,z):
    return (x+2*y+np.exp(-t))

# The RK 4 method implementation....
for i in range(len(y)-1):
    n1=h*e(t[i],x[i],y[i],z[i])
    k1=h*f(t[i],x[i],y[i],z[i])
    l1=h*g(t[i],x[i],y[i],z[i])
    
    n2=h*e(t[i]+h/2,x[i]+n1/2,y[i]+k1/2,z[i]+l1/2)
    k2=h*f(t[i]+h/2,x[i]+n1/2,y[i]+k1/2,z[i]+l1/2)
    l2=h*g(t[i]+h/2,x[i]+n1/2,y[i]+k1/2,z[i]+l1/2)
    
    n3=h*e(t[i]+h/2,x[i]+n2/2,y[i]+k2/2,z[i]+l2/2)
    k3=h*f(t[i]+h/2,x[i]+n2/2,y[i]+k2/2,z[i]+l2/2)
    l3=h*g(t[i]+h/2,x[i]+n2/2,y[i]+k2/2,z[i]+l2/2)
    
    n4=h*e(t[i]+h,x[i]+n3,y[i]+k3,z[i]+l3)
    k4=h*f(t[i]+h,x[i]+n3,y[i]+k3,z[i]+l3)
    l4=h*g(t[i]+h,x[i]+n3,y[i]+k3,z[i]+l3)
    
    x[i+1]=x[i]+(n1+2*n2+2*n3+n4)/6
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
    z[i+1]=z[i]+(l1+2*l2+2*l3+l4)/6
    
#plotting the graph
plt.plot(t,x,label='u1')
plt.plot(t,y,label='u2')  
plt.plot(t,z,label='u3')  
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('plot of x vs y')
plt.grid()
plt.show()  