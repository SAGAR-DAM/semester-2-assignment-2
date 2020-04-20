'''problem 7 assignment 2 part 4
Using scipy.integrate.solve_ivp
Name: Sagar Dam, Dept: Dnap'''

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt


'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

'''PART 3: f(t,y)=cos(2t)+sin(3t)  '''
#defining the function:
def f(t,y):
    fy=np.cos(2*t)+np.sin(3*t)
    return fy

#solving numerically using scipy.integrate:
t=np.linspace(0,1,1000)
s=solve_ivp( f,[0,1],[1],t=np.linspace(0,1,1000),method='RK45',dense_output="True")

#exact solution (using mathematica):
def ytrue(t):
    true= (3*np.sin(2*t)-2*np.cos(3*t)+8)/6
    return true
plt.plot(t,s.sol(t).T, label='using scipy')
plt.plot( t, ytrue(t), label='exact solutin' )
plt.title( "Solving initial value problem using scipy.integrate.solve_ivp" )
plt.xlabel('t')
plt.ylabel('y(t)')
plt.suptitle('for f(t,y)=cos(2t)+sin(3t)')
plt.legend()
plt.grid()
plt.show()