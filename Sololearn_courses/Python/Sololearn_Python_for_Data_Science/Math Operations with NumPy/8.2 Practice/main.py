#Seats in a Theater
#You are given an array that represents the occupancy of seats in a movie theater. A seat marked with 1 is occupied, while one marked 0 means the seat is free.
#However, the array is flat and 1-dimensional. Transform it into a 2-dimensional array, representing the rows of the seats.
#Each row in the theater has 5 seats and there are a total of 30 seats.
#Reshape the array into the corresponding shape and output the row at the given index, which is taken from user input.
#The row index is taken from user input in the given code.

import numpy as np

data = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0])

row = int(input())

data = data.reshape(6,5) #NumPy allows us to change the shape of our arrays using the reshape() function. 
#When you use the reshape method, the array you want to produce needs to have the same number of elements as the original array.

print(data[row])
