# **Task9**.
# Use the functions of the Numpy library learned in class and create an array5x5,
# which will contain successive values of the Fibonacci sequence

import numpy as np

mat = [0,1]
for i in range(2,25):
    mat.append(mat[i-1]+mat[i-2])

mat = np.array(mat)
mat = mat.reshape((5,5))

print(mat)