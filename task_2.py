#  **Task2**.
# Create a list consisting of floating point values
# and then write a copy of the list converted to int64 type to the variable.
# Display the new list and note what happens to the decimal values.

import numpy as np

b = np.array([1.23 , 3.532 , 1.5 , 2.8 , 9.57 , 25.54])
b = b.astype('int64')

print(b,b.dtype)
print(b,b.dtype)