"""
WAP to input four numbers from the user and find the greatest number among them.
"""

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))
num4 = int(input("Enter 4th Number : "))

if (num1 >= num2) and (num1 >= num3)  and (num1 >= num4):
    great = num1
elif (num2 >= num1) and (num2 >= num3)  and (num2 >= num4):
    great = num2
elif (num3 >= num1) and (num3 >= num2)  and (num3 >= num4):
    great = num3
else:
    great = num4

print("Greatest Number is :",great)