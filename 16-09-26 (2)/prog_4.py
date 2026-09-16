"""
WAP to input a list of numbers and create a new list containing only unique elements.
"""

numbers = list(map(int , input("Enter Numbers : ").split()))
x = set(numbers)
print("Unique Numbers in List :",list(x))