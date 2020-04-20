'''problem 7 assignment 2 part 2
Using scipy.integrate.solve_ivp
Name: Sagar Dam, Dept: Dnap'''

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt


'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

'''PART 2: f(t,y)=1-(t-y)**2  '''
#defining the function:
def f(t,y):
    fy=1-(t-y)**2
    return fy

#solving numerically using scipy.integrate:
t=np.linspace(2,2.99,1000)
s=solve_ivp( f,[2,2.99],[1],t=np.linspace(2,3,1000),dense_output="True")

#exact solution (using mathematica):
def ytrue(t):
    true= (t**2-3*t+1)/(t-3)
    return true
plt.plot(t,s.sol(t).T, label='using scipy')
plt.plot( t, ytrue(t), label='exact solutin' )
plt.title( "Solving initial value problem using scipy.integrate.solve_ivp" )
plt.xlabel('t')
plt.ylabel('y(t)')
plt.suptitle('for f(t,y)=1-(t-y)**2')
plt.grid()
plt.legend()
plt.show()

'''AS THE SOLUTION IS GOING TO DIVERGE AT t=3 SO FIRSTLY I'VE PLOTTED
   FOR t in range (2,2.99).'''
   