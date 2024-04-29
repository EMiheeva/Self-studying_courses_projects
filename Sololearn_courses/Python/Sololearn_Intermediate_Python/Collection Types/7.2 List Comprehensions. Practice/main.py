"""
List Comprehensions

Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.
Sample Input
awesome
Sample Output
['w', 's', 'm']
Use a list comprehension to create the required list of letters and output it.
"""
word = input()
vowels = [ "a", "e", "i", "o", "u"]
mas = [i for i in word if i not in vowels]
print(mas)
