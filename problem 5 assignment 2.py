''' Problem 5 assignment 2
Shooting method for freefall diff eq
NAME: SAGAR DAM;    DNAP
'''

import numpy as np
import matplotlib.pyplot as plt

#defining variables:
a=0
b=60
g=10
h=0.01
t1=10
xend=0
err=0.001
t=np.arange(0,t1,h)
x=np.ones(len(t))
x[0]=0
v=np.zeros(len(t))

#defining function for euler technique in shooting loop
def f(t,x,v):
    return v
def f1(t,x,v):
    return -g

# Introducing Shooting condition:

while (abs(x[len(t)-1]-xend)>err):
    r=(a+b)/2    
    v[0]=r
    x[0]=0
# Doing the Euler solution:
    for i in range(len(t)-1):
        v[i+1]=v[i]+h*f1(t[i],x[i],v[i])
        x[i+1]=x[i]+h*f(t[i],x[i],v[i])
    if(x[len(t)-1]<xend):
        a=r
    elif(x[len(t)-1]>xend):
        b=r  
    plt.plot(t,x,'y')

      
plt.plot(t,x,'b',label='solution with given accuracy')
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('x')
plt.show()
print()
print("value of x'(0) to get ultimate accuracy: ",r)