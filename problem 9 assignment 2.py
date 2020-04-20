''' Problem 9 assignment 2
ADAPTIVE STEP SIZE CONTROL
NAME: SAGAR DAM;   DNAP'''

from numpy import *
from matplotlib import pyplot as plt

y=[] # y corresponding to t
z=[] # z corresponding to y


#defining the ODE
def fun(t,x):
    fun = (x**2+x)/t
    return fun
    
# Set initial conditions.
t = 1
x = -2
y.append(t)
z.append(x)
# Set initial step size.
dt = 1e-1

# Set minimal step size.
dt_min = 1e-4

# Set relative change tolerances.
dx_max = 0.01  # Enables faster speed.
dx_min = 0.0008 # Controls accuracy.
x_tol = 1e-4

while (t < 6):
    #rate(100)
    # Calculate partial steps.
    k1 = fun(t,x)
    k2 = fun(t+dt/2, x+dt*k1/2)
    k3 = fun(t+dt/2, x+dt*k2/2)
    k4 = fun(t+dt,   x+dt*k3)
    # Combine partial steps.
    step_x = x + dt/6*(k1+2*k2+2*k3+k4)

    # Calculate partial steps.
    k2 = fun(t+dt/4, x+dt*k1/4)
    k3 = fun(t+dt/4, x+dt*k2/4)
    k4 = fun(t+dt/2, x+dt*k3/2)
    # Combine partial steps.
    half_step_x = x + dt/12*(k1+2*k2+2*k3+k4)

    # Calculate partial steps.
    k2 = fun(t+dt,   x+dt*k1)
    k3 = fun(t+dt,   x+dt*k2)
    k4 = fun(t+2*dt, x+2*dt*k3)
    # Combine partial steps.
    dble_step_x = x + dt/3*(k1+2*k2+2*k3+k4)

    if (abs(step_x) < x_tol): # Use a fixed step size for small values of x.
        if (dt != dt_min):
            print("New step size",dt_min)
            dt = dt_min
        new_x = step_x
    else:
        if (abs(step_x)>x_tol and abs(step_x-half_step_x)/abs(step_x)>dx_max):
            dt = dt/2 # Error is too large; decrease step size.
            print("New step size",dt)
            new_x = half_step_x
        elif (abs(step_x)>x_tol and abs(step_x-dble_step_x)/abs(step_x)<dx_min):
            dt = dt*2 # Larger error is acceptable; increase step size.
            print("New step size",dt)
            new_x = dble_step_x
        else:
            new_x = step_x # This step size is just right.
    y.append(t+dt)
    x = new_x
    z.append(x)
    t = t + dt
    
plt.suptitle('Plotting of curve and mesh points')  
plt.plot(y,z,'y',label='solid line')
plt.plot(y,z,'ro',markersize=1,label='mesh points')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()