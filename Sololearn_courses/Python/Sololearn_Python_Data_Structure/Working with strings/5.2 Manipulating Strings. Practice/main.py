"""
You are making a text editor and need to implement find/replace functionality.
The code declares a text string. You need to take two string inputs, which represent the substring to find and what to replace it with in the text.
Your program needs to output the number of replacements made, along with the new text.
"""
text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."
whom_replace = input()
what_replace = input()
print(text.count(whom_replace))
print(text.replace(whom_replace,what_replace))
