"""
Average Word Length

Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.
Strings have a split() method, which returns the string split into a list, with the given separator. 
By default, the separator is a space, so calling split() will return a list containing the words of the string as items.
"""
text = input().split()

letters = 0
words = 0

for i in text:
    letters += len(i)
    words += 1
    
print(letters/words)
