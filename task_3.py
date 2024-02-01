#  **Task3**.
# Write a function that will:
#  -take one parameter`n` in integer form
#  -return a Numpy array of size n*n consecutive integers starting from1
#   The number n is to be given by the user.Display the array and the size of the created array

import numpy as np

def task_3(n):
    return np.arange(1,n*n+1).reshape(n,n)

try:
    print("Write n-value for nxn size matrix:")
    n = int(input())
    print(task_3(n))
except ValueError:
    print("Write the correct value")