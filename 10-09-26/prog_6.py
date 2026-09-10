"""
WAP to input a decimal number and convert it into binary without using bulit-in bin() function
"""

n = int(input("Enter a Decimal Number : "))
ans = 0

i = 0
while n > 0:
    rem = n % 2
    ans += rem * (10 ** i)
    n //= 2
    i += 1

print("Binary Number :",ans)