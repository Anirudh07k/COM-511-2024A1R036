"""
WAP to store repeated values in a tuple and count how many times a given value appears.
"""

tup = (10, 20, 30, 10, 20, 50, 30, 10, 40, 20)

val = int(input("Enter value to count : "))

print(f"value : {val} appears {tup.count(val)} Times")