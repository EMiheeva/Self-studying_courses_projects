"""
Spelling Backwards
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.
"""

def spell(txt):
 if txt=="": 
        return txt
 else:
        print(txt[len(txt)-1])
        return spell(txt[0:len(txt)-1])
txt = input()
print(spell(txt))
