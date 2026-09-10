# Write a program to illustrate iteration over the list and dictionary.

# Program to illustrate iteration over a list and dictionary

# List
list = [10, 20, 30, 40, 50]

print("Iteration over List:")
for item in list:
    print(item)

# Dictionary
dictionary = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

print("\nIteration over Dictionary:")
for key, value in dictionary.items():
    print(key, ":", value)