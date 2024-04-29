"""
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.
"""
# variant 1
word=input()
letter=input()
n=len(word)
per=((word.count(letter)/n)*100)
print(int(per))
"""
#variant 2
stri=input()
L= input()
print(int(stri.count(L)/len(stri)*100))
"""
