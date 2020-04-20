'''problem 7 assignment 2 part 3
Using scipy.integrate.solve_ivp
Name: Sagar Dam, Dept: Dnap'''

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt


'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

'''PART 3: f(t,y)=1+y/t  '''
#defining the function:
def f(t,y):
    fy=1+y/t
    return fy

#solving numerically using scipy.integrate:
t=np.linspace(1,2,1000)
s=solve_ivp( f,[1,2],[2],t=np.linspace(1,2,1000),dense_output="True")

#exact solution (using mathematica):
def ytrue(t):
    true= t*(2+np.log(t))
    return true
plt.plot(t,s.sol(t).T, label='using scipy')
plt.plot( t, ytrue(t), label='exact solutin' )
plt.title( "Solving initial value problem using scipy.integrate.solve_ivp" )
plt.xlabel('t')
plt.ylabel('y(t)')
plt.suptitle('for f(t,y)=1+y/t')
plt.legend()
plt.grid()
plt.show()