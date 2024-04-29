"""
Reading Files

You need to make a program to read the given number of characters of a file.
Take a number N as input and output the first N characters of the books.txt file.
"""
file = open("/usercode/files/books.txt")
n = int(input())
l = file.read()
print(l[:n])
file.close()
