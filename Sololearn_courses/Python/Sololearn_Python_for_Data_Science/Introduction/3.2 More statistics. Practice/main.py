"""
Number of Vaccinations

Using the same vaccinations dataset, which includes the number of times people got the flu vaccine.
The dataset contains the following numbers:
never: 5
once: 8
twice: 4
3 times: 3
Calculate and output the variance.
We will soon learn about easier ways to calculate the variance and other summary statistics using Python. For now, use Python code to calculate the result using the corresponding equation.
Hint: The variance is the average of the squared differences from the mean.
"""

import numpy as np 
#NumPy (Numerical Python) is a Python library used to work with numerical data. 
#NumPy includes functions and data structures that can perform a wide variety of mathematical operations.

a = np.array([0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ])

mean = np.sum(a)/a.size #mean is "среднее значение"
#the average of the values.

variance = np.sum((a-mean)**2)/a.size #The variance is the average of the squared differences from the mean. 
#The variance means "дисперсия"

print(variance)


#mean: the average of the values.
#median: the middle value.
#standard deviation: the measure of spread.
