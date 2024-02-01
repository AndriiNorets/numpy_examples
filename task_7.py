# **Task7**.
# Write a function that generates a multidimensional matrix of the form:
#  [[2 4 6]
#   [4 2 4]
#   [6 4 2]]
# Under the assumptions:
# -the function takes a parameter n,which specifies the dimensions of the matrix
# as n*n and places multiples of 2 on its successive diagonals diverging from the main diagonal.

import numpy as np

def zadanie7(n):
    result = np.diag([2] * n)
    l = 4
    for i in range(-1,-n,-1):
        result += np.diag([l]*(n+i),k=i)
        result += np.diag([l] * (n + i), k=-i)
        l+=2
    return result

print(zadanie7(10))