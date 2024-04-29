"""
You are making a digital menu to order food.
The menu is stored as a list of items.
Your program needs to take the index of the item as input and output the item name.
In case the index is not valid, you should output "Item not found".
In case the index is valid and the item name is output successfully, you should output "Thanks for your order".
"""
menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    n = int(input())
    print(menu[n])
    print("Thanks for your order")
except:
    print("Item not found")
