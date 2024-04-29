"""
Insect Control

The number of insects in a lab doubles in size every month.
Take the initial number of insects as input and output a list, showing the number of insects for each of the next 12 months, starting with 0, which is the initial value.
So, the resulting list should contain 12 items, each showing the number of insects at the beginning of that month.

The formula to calculate the number of insects after N months will be: count*2ᴺ, where count is the initial number of insects.
"""
n = int(input())
answer = [n*2**i for i in range (12)]
print(answer)
