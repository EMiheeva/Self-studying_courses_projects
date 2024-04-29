"""
Basketball Players
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.
Output the result using the print statement.
"""

import numpy as np

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = np.mean(players) #average value (sum of all elements by their number)
standard_deviation = np.std(players) #standard deviation, square root of variance(dispersion)
variance = np.var(players) #dispersion (see lesson 3.1)

#print(mean)
#print(variance)
#print(standard_deviation)
#print(mean-standard_deviation) #exactly subtract and add to mean, not variance
#print(mean+standard_deviation)

result = 0
for i in players:
    if i >= mean-standard_deviation and i <= mean+standard_deviation:
        result += 1
print(result)
