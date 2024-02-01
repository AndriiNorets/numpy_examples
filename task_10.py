# **Task10**
# -Create a matrix of2x3 different values and then calculate
# the sin for each of its values and save to variable "a".
# -Create a new matrix of 2x3 different values and then calculate
# the cos for each of its values and save to the variable "b".
# -Execute the addition function of both matrices previously saved to the variables a and b.

import numpy as np

a1 = np.array([[234,12,777],[5,8322,1]]).reshape(2,3)
a = np.array( [[ np.sin(item) for item in a1[0] ],
               [np.sin(item) for item in a1[1]] ]).reshape(2,3)

b1 = np.array([[234,12,777],[5,8322,1]]).reshape(2,3)
b = np.array( [[ np.cos(item) for item in b1[0] ],
               [np.cos(item) for item in b1[1]] ]).reshape(2,3)

print("Matrix a:\n",a,
      "\n\nMatrix b:\n",b,
      "\n\nSum of matrices a and b:\n",a+b)