''' PROBLEM 10 ASSIGNMENT 2
 RK4 method over o to infinity
 NAME: SAGAR DAM; DNAP'''
 
import numpy as np
from matplotlib import pyplot as plt
def f(t,y):
    z=1/(t**2+y**2)
    return  z

a=0
b=100
h=0.1
n=(b-a)/h
t=np.arange(a,b,h)
y=np.zeros(len(t))
y[0]=1

#Rk4
for i in range(len(y)-1):
    
    k1=h*f(t[i],y[i])
    k2=h*f(t[i]+h/2,y[i]+k1/2)
    k3=h*f(t[i]+h/2,y[i]+k2/2)
    k4=h*f(t[i]+h,y[i]+k3)
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
v=y[len(t)-1]   
plt.plot(t,y)
plt.suptitle('plot for a small range')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()

a=100
b=5e6
h=10
n=(b-a)/h
t=np.arange(a,b,h)
y=np.zeros(len(t))
y[0]=v
#Rk4
for i in range(len(y)-1):
    
    k1=h*f(t[i],y[i])
    k2=h*f(t[i]+h/2,y[i]+k1/2)
    k3=h*f(t[i]+h/2,y[i]+k2/2)
    k4=h*f(t[i]+h,y[i]+k3)
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
    
p=int((3.5e6-100)/10)
plt.plot(t,y)
plt.suptitle('plot for wide range')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()
print("value of x at t=",t[p],"is: ",y[p])