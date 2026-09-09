"""
Write a Python program to check whether a number is a perfect number.
A number is perfect is the sum of its proper divisors is equal to the number itself.
"""

n = int(input("Enter a number : "))
count = 0
for i in range(1, n):
    if n % i == 0:
        count += i

if count == n:
    print("Perfect Number")
else:
    print("No one is Perfect, so is this")