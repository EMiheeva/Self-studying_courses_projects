"""
Ticket Office


You are analyzing sales data from a ticket office.
The ticket for an adult is $20, while the ticket for a child under 18 is $5.
The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
For example, "123-08": 24 means that the ticket was bought a 24 year old.
Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.
"""

data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())
total_first=0
total_second=0

for value in data.values():
    if value<18:    
        total_first+=5
    if value>=18:
        total_first+=20
        
for value in data.values():
    if value<age:
        total_second+=5
    if value>=age:
        total_second+=20
        
        
x=int(((total_second-total_first)/total_first)*100) 
print(x)
