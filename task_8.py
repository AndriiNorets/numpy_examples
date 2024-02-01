# **Task8**.
# Write a function that:
# -as an input parameter will take a numpy multidimensional array and the 'direction' parameter
# -the direction parameter determines whether the input array will be split vertically or
# horizontally(the default is to split horizontally)
# -function divides the input array in half
#
# (write a condition that will display a message that the number of rows or columns,
# depending on the direction of division, does not allow the operation)

import numpy as np

def task_8(tab,direction=''):
    if direction == "horizontally":
        if tab.shape[0] %2 ==0:
            val1 = tab[:int(tab.shape[0]/2)]
            val2 = tab[int(tab.shape[0]/2):]
            print(val1,"\n\n",val2)
        else:
            print("matrix has an odd number of rows")
    else:
        if tab.shape[1] %2 ==0:
            val1 = tab[:,:int(tab.shape[1] / 2)]
            val2 = tab[:,int(tab.shape[1] / 2):]
            print(val1, "\n\n", val2)
        else:
            print("matrix has an odd number of columns")

b = np.arange(16).reshape((4,4))
task_8(b,"horizontally")
task_8(b,"")