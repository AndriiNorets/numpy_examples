# **Task6**
# Create a script that outputs a numpy array(multidimensional array)
# in the form of a plot, where one word will be written in a column,
# one in a row and one diagonally.One of these words should be written
# from right to left.

import numpy as np

word_1 = np.array(list("malina"))
word_2 = np.array(list("lizak"))
word_3 = np.array(list("jagona"))

matrxx = np.zeros((7,7),dtype=str)
matrxx[:-1,:-1] =np.diag(word_3)
matrxx[:-1,0] = word_1
matrxx[2,:-2] = word_2

print(matrxx)