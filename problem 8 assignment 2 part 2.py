''' Problem assignment 2 part 2
BVP problem
NAME: SAGAR DAM;   DNAP'''

from scipy.integrate import *
from matplotlib import pyplot as plt
import numpy as np

#2nd problem
a=0
b=np.pi/2
def fun(x,y):
    return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))
def bc(ya,yb):
    return np.array([ya[0]-1,yb[0]-np.exp(1)])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=solve_bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp2.txt",usecols=0)   
   
plt.plot(x,sol.sol(x)[0],'g',label='using bvp')
plt.plot(x,y1,'ko',markersize=2,label='from mathematica')
plt.title('numerical and analytical (from mathematica) solutions')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()