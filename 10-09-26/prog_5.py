"""
WAP to input a number and reverse it using arithmatic operators
"""

n = int(input("Enter a Number : "))

rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //=  10

print("Reversed Number :",rev)