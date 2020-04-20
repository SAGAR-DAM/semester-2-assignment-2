'''problem 6 assignment 2
RELAXATION METHOD
NAME: SAGAR DAM;  DNAP'''


import numpy as np
from matplotlib import pyplot as plt

#defining variables
t0=0
t1=10
n=10
h=(t1-t0)/(n)
t=np.arange(0,t1+h,h)
A=np.ndarray(shape=(n-1,n-1),dtype=float)
B=-10*np.ones(n-1,dtype=float)
print('the operator matrix be given by:')
print()
print(A)
print()
print()
print('PLOT:')
#input the matrices
for i in range(n-1):
    for j in range (n-1):
        if (i==j):
            A[i][j]=-2
        elif (i==j+1 or i==j-1):
            A[i][j]=1
        else:
            A[i][j]=0

x=np.zeros(n-1,dtype=float)
y=x
w=1.25
Z=0
Y=0

#Doing the iteration and solve for x as a fn of mesh points
for i in range(100):
    #evaluating value of x(j) at ith iteration...
    for j in range(n-1):
        for k in range(n-1):
            if k<j:
                Z=Z+A[j][k]*y[k]
            elif k>j:
                Y=Y+A[j][k]*x[k]
        y[j]=(1-w)*y[j]+ w*(B[j]-Z-Y)/A[j][j]
        Z=0
        Y=0
    x=y
    u=np.zeros(n+1)
    u[0]=0
    u[n]=0
    for j in range(1,n):
        u[j]=x[j-1]
    
    plt.plot(t,u,'y')
plt.plot(t,u,'y',label='solutions of iterations')
plt.plot(t,u,'b',label='final solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.suptitle('plot of x vs t for relaxation method')
plt.show()