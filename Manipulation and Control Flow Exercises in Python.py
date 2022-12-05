# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:50:16 2021

@author: Berto
"""

import numpy as np


#1
def fib(h):
    a, b = 0, 1
    print('The Fibonacci sequence up to',h)
    while a <= h:
        print(a)
        a, b = b, a+b
    
fib(21)


#2
def fact(y):
    if y == 0:
        return 1
    else:
        return y * fact(y-1)

fact(4)


import numpy as np
from numpy.random import randn
from numpy.random import normal
from numpy.random import beta
from numpy.random import seed
import matplotlib.pyplot as plt


#3

def hlot(i, u, c, f):  
    x = np.zeros(i)
    x
    seed(123)
    for i in range(len(x)):
        x[i] = np.mean(beta(u, c, f))
        
    plt.hist(x, bins=50, density=True)

hlot(2000, 200, 10, 4)




#4
def home(i, q, w, e): 
    lower = np.zeros(5000)
    upper = np.zeros(5000)
    within = np.zeros(i)
    seed(1234)
    for i in range(len(lower)):
        x = beta(w, e, q)
        lower[i] = np.mean(x) - 2.576*np.std(x)/np.sqrt(100)
        upper[i] = np.mean(x) + 2.576*np.std(x)/np.sqrt(100)
        interval = np.transpose(np.array([lower, upper]))
        if lower[i]<0.5 and upper[i]>0.5:
            within[i] = 1
        else:
            within[i] = 0
        return np.mean(lower), np.mean(upper), np.mean(within)

home(5000, 100, 10, 4)    



            
