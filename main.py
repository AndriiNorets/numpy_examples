import numpy as np

# **Task1**
# Using the arange function, create a Numpy array of 20 consecutive multiples of the number 2.
a = np.arange(0,40,2)
# print(a)

#  **Task2**.
# Create a list consisting of floating point values
# and then write a copy of the list converted to int64 type to the variable.
# Display the new list and note what happens to the decimal values.
b = np.array([1.23 , 3.532 , 1.5 , 2.8 , 9.57 , 25.54])
# print(b,b.dtype)
b = b.astype('int64')
# print(b,b.dtype)

#  **Task3**.
# Write a function that will:
#  -take one parameter`n` in integer form
#  -return a Numpy array of size n*n consecutive integers starting from1
#   The number n is to be given by the user.Display the array and the size of the created array

def task_3(n):
    return np.arange(1,n*n+1).reshape(n,n)

# try:
#     n = int(input())
#     print(task_3(n))
# except ValueError:
#     print("Write the correct value")

# **Task4**.
# Write a function that will take 2 parameters:a number,
# which will be the basis for the operation of the power
# and the number of consecutive powers to generate.
# Using the logspace function generate a one-dimensional array of consecutive powers
# of the given number,e.g.generate(2,4) -> [2 4 8 16]

def task_4(n,m):
    return np.logspace(start = 1,stop = m,
                       num=m,dtype=int,base=n)

# print(task_4(2,4))

#   **Task5**.
#  Write a function that:
# -on the input it takes one parameter specifying the length of the vector,
# -on the basis of the parameter generates a vector,
# but in reverse order(that is, for example, for n=3=>[3 2 1])
# -generates a diagonal matrix with the aforementioned vector as a diagonal
def zad5(n):
    return np.diag([i for i in range(n,0,-1)])

# print(zad5(5))

# **Task6**
# Create a script that outputs a numpy array(multidimensional array)
# in the form of a plot, where one word will be written in a column,
# one in a row and one diagonally.One of these words should be written
# from right to left.

word_1 = np.array(list("malina"))
word_2 = np.array(list("lizak"))
word_3 = np.array(list("jagona"))

matrxx = np.zeros((7,7),dtype=str)
matrxx[:-1,:-1] =np.diag(word_3)
matrxx[:-1,0] = word_1
matrxx[2,:-2] = word_2

# print(matrxx)

# **Task7**.
# Write a function that generates a multidimensional matrix of the form:
#  [[2 4 6]
#   [4 2 4]
#   [6 4 2]]
# Under the assumptions:
# -the function takes a parameter n,which specifies the dimensions of the matrix
# as n*n and places multiples of 2 on its successive diagonals diverging from the main diagonal.

def zadanie7(n):
    result = np.diag([2] * n)
    l = 4
    for i in range(-1,-n,-1):
        result += np.diag([l]*(n+i),k=i)
        result += np.diag([l] * (n + i), k=-i)
        l+=2
    return result

# print(zadanie7(4))

# **Task8**.
# Write a function that:
# -as an input parameter will take a numpy multidimensional array and the 'direction' parameter
# -the direction parameter determines whether the input array will be split vertically or
# horizontally(the default is to split horizontally)
# -function divides the input array in half
#
# (write a condition that will display a message that the number of rows or columns,
# depending on the direction of division, does not allow the operation)

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

# task_8(b,"horizontally")


# **Task9**.
# Use the functions of the Numpy library learned in class and create an array5x5,
# which will contain successive values of the Fibonacci sequence

mat = [0,1]
for i in range(2,25):
    mat.append(mat[i-1]+mat[i-2])

mat = np.array(mat)
mat = mat.reshape((5,5))

# print(mat)

# **Task10**
# -Create a matrix of2x3 different values and then calculate
# the sin for each of its values and save to variable "a".
# -Create a new matrix of 2x3 different values and then calculate
# the cos for each of its values and save to the variable "b".
# -Execute the addition function of both matrices previously saved to the variables a and b.

a1 = np.array([[234,12,777],[5,8322,1]]).reshape(2,3)
a = np.array( [[ np.sin(item) for item in a1[0] ],
               [np.sin(item) for item in a1[1]] ]).reshape(2,3)

b1 = np.array([[234,12,777],[5,8322,1]]).reshape(2,3)
b = np.array( [[ np.cos(item) for item in b1[0] ],
               [np.cos(item) for item in b1[1]] ]).reshape(2,3)

# print("Matrix a:\n",a,
#       "\n\nMatrix b:\n",b,
#       "\n\nSum of matrices a and b:\n",a+b)

# **Task11**
# Generate a 3x3 matrix and then:
# - display each row in a loop
# - display each element in the loop

task_11 = np.random.randint(9999,size=(3,3))

# for item in task_11:
#         print(item,"\n")

# for item in task_11.flat:
#     print(item)






