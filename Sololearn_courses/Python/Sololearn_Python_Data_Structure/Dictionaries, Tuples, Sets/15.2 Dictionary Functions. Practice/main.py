"""
Fuzzy Search

You are making a phonebook. The contacts are stored in a dictionary, where the key is the name and the value is a list, representing the number and the email of the contact.
You need to implement search: take the name of the contact as input and output the email.
If the contact is not found, output "Not found".
"""
contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
user_name = input()
if user_name in contacts:
    print(contacts[user_name][1])
else:
    print("Not found")
