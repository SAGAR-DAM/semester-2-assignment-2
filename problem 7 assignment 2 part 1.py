'''problem 7 assignment 2 part 1
Using scipy.integrate.solve_ivp
Name: Sagar Dam, Dept: Dnap'''

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt

'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

'''PART 1: f(t,y)=t*np.exp(3*t)-2*y  '''
#defining the function:
def f1(t,y):
    fy=t*np.exp(3*t)-2*y
    return fy

#solving numerically using scipy.integrate:
t=np.linspace(0,1,100)
s1=solve_ivp( f1,[0,1],[0],t=np.linspace(0,1,100),dense_output="True")

#exact solution (using mathematica):
def ytrue(t):
    true= (1/25)*(np.exp(-2*t))*(1-np.exp(5*t)+5*t*np.exp(5*t))
    return true
plt.plot(t,s1.sol(t).T, label='using scipy')
plt.plot( t, ytrue(t), label='exact solutin' )
plt.title( "Solving initial value problem using scipy.integrate.solve_ivp" )
plt.xlabel('t')
plt.ylabel('y(t)')
plt.suptitle('for f(t,y)=t*np.exp(3*t)-2*y')
plt.legend()
plt.grid()
plt.show()