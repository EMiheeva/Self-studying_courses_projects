"""
Words in Common

Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).
"""
s1 = input()
s2 = input()

list1 = s1.split()
list2 = s2.split()

print(len(set(list1) & set(list2)))
