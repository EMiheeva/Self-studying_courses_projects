#Multiples of 3 & 5
#You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
#Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.

#You can use the modulo operator % to check if a number is a multiple of another number.

#You can provide a condition as the index to select the elements that fulfill the given condition.

import numpy as np
x = np.arange(1, 100)
#y = x[(x%5==0) & (x%3==0)]
#print(y)
print(x[(x%5==0) & (x%3==0)]) #Why create a separate variable y? It's better to save memory.
