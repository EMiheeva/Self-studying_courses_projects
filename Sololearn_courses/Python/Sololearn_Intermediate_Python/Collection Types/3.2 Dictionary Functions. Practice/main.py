"""
Dictionary Functions

You are working on data that represents the economic freedom rank by country.
Each country name and rank are stored in a dictionary, with the key being the country name.
Complete the program to take the country name as input and output its corresponding economic freedom rank.
In case the provided country name is not present in the data, output "Not found".
Recall the get() method of a dictionary, that allows you to specify a default value.
"""
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
country = input()
print(data.get(country, "Not found"))
