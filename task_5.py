#   **Task5**.
#  Write a function that:
# -on the input it takes one parameter specifying the length of the vector,
# -on the basis of the parameter generates a vector,
# but in reverse order(that is, for example, for n=3=>[3 2 1])
# -generates a diagonal matrix with the aforementioned vector as a diagonal

import numpy as np

def zad5(n):
    return np.diag([i for i in range(n,0,-1)])

print(zad5(10))