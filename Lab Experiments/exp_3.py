"""
Consider the string “Welcome to Python world”. Perform the following operations:
Count the number of alphabets in the given string.
To extract characters in the given, range from the given string.
Check if the string is alphanumeric or not.
"""


# Program to perform operations on a string

string = "Welcome to Python world"

# Count the number of alphabets
count = 0

for character in string:
    if character.isalpha():
        count += 1

print("Given string:", string)
print("Number of alphabets:", count)

# Extract characters from a given range
print("Characters from index 0 to 6:", string[0:7])

# Check whether the string is alphanumeric
print("Is the string alphanumeric?:", string.isalnum())