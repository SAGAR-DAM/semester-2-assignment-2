''' Problem assignment 2 part 3
BVP problem
NAME: SAGAR DAM;   DNAP'''

from scipy.integrate import *
from matplotlib import pyplot as plt
import numpy as np

#3rd problem
a=np.pi/4
b=np.pi/3
def fun(x,y):
    return np.vstack((y[1],-(2*(y[1])**3 +(y[0]**2)*y[1])/np.cos(x)))
def bc(ya,yb):
    return np.array([ya[0]-(2**(-0.25)),yb[0]-(0.5*(12**0.25))])
x=np.linspace(a,b,100)       
y=np.zeros((2,x.size))
y[0]=1              
sol=solve_bvp(fun,bc,x,y)         
y1=np.loadtxt("bvp3.txt",usecols=0)    


plt.plot(x,sol.sol(x)[0],'g',label='using bvp')
plt.plot(x,y1,'ko',markersize=2,label='from mathematica')
plt.title('numerical and analytical (from mathematica) solutions')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

'''
Acknowledgement:
I thank to my friend Akashdeep for problem no 8. In my machine Mathematica is not working 
(and wolfram alpha is not able for 2nd order nonlinear eqn), hence I can't solve the 2nd order 
nonlinear eqns given in problem 8. As other time we generally get a chance to discuss and 
then do like own way, this time that's not possible. Even it was also not possible to use 
some other's computer. We all are at different places. However he helped me with 
the mathematica file to plot the analytic solution. I am greatly thankful to him.'''