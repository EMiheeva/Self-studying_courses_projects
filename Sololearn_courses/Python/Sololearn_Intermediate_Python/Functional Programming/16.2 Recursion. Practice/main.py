"""
Recursion

The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary.
However, the code has an error.
Fix the code by adding the base case for the recursion, then take a number from user input and call the convert() function, to output the result.
"""
def convert(num): 
   if num==0:
      return 0
   return (num % 2 + 10 * convert(num // 2)) 

number = int(input())
print(convert(number))
