# **Task11**
# Generate a 3x3 matrix and then:
# - display each row in a loop
# - display each element in the loop

import numpy as np

task_11 = np.random.randint(9999,size=(3,3))

for item in task_11:
        print(item,"\n")

for item in task_11.flat:
    print(item)