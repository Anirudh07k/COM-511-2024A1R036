"""
Write a Python program to input a number and check whether it is prime or not.
A number is prime if it has no divisor other than 1 and itself.
"""

n = int(input("Enter a Number : "))
flag = 1

if n <= 1:
    flag = 0
    
for i in range(2, n // 2):
    if n % i == 0:
        flag = 0

if flag == 1:
    print("Number is Prime")
else:
    print("Number is Composite")