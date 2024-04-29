"""
Let's test your coding skills!
Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.
"""
# My variant
string = input()
count = 0
for i in string:
    print(i*(count+1))
    count+=1
"""
Sololearn variant
word = input()
print()
i = 0
while (i < len(word)):
  print(word[i]*(i+1))
  i+=1 
  #i++ - habit from C++ syntax
 """
