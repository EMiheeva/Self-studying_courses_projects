"""
Letter Counter
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.
"""

text = input()

len = len(text)

dict = {}

for i in range(len):
    if text[i] in dict:
        dict[text[i]] += 1
    else:
        dict[text[i]] = 1

print (dict)
