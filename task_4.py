# **Task4**.
# Write a function that will take 2 parameters:a number,
# which will be the basis for the operation of the power
# and the number of consecutive powers to generate.
# Using the logspace function generate a one-dimensional array of consecutive powers
# of the given number,e.g.generate(2,4) -> [2 4 8 16]

import numpy as np

def task_4(n,m):
    return np.logspace(start = 1,stop = m,
                       num=m,dtype=int,base=n)

print(task_4(2,10))