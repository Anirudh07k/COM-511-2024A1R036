"""
WAP to rotate a list from one position to the right
"""

numbers = list(map(int , input("Enter Numbers : ").split()))

print(numbers[-1:] + numbers[:-1])    