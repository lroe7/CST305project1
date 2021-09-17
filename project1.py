# Lauren Roe
# CST-305
# This is my own work

# The equation I am using is for ethernet frame  rate
# The equation is df/dp = k/p
# f is the number of frames, p is the number of packets(frame size)
# k is constant that represents the size of a network bandwidth

import numpy as np                  # imported to define p as a space of numbers
import matplotlib.pyplot as plt     # imported to see the solution as a plot
from scipy.integrate import odeint  # imported to solve the ODE


def model(f, p, k):   # function that returns df/dp
    dfdp = k / p    # the ODE explained above
    return dfdp     # returns df/dp


f0 = 5              # initial condition for f(0)

p = np.linspace(1, 20)                   # creates evenly spaced values from 1-20 for p

k = 5                                   # using a constant of 5 bits/sec
f1 = odeint(model, f0, p, args=(k,))    # solves the ODE for f1
k = 10                                  # using a constant of 10 bits/sec
f2 = odeint(model, f0, p, args=(k,))    # solves the ODE for f2
k = 15                                  # using a constant of 15 bits/sec
f3 = odeint(model, f0, p, args=(k,))    # solves the ODE for f3

plt.plot(p, f1, 'r-', linewidth=2, label='k=5')     # plots results for p=5
plt.plot(p, f2, 'b:', linewidth=2, label='k=10')    # plots results for p=10
plt.plot(p, f3, 'g--', linewidth=2, label='k=15')   # plots results for p=15

plt.xlabel('packets')       # labels x-axis with packets
plt.ylabel('f(p)')          # labels y-axis as f(p)
plt.legend()                # plots the key for which line represents which value of p
plt.show()                  # displays the plot
