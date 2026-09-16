"""
WAP to input a list of numbers in a list and create two seperate lists for even and odd numbers.
"""

numbers = list(map(int , input("Enter Numbers : ").split()))

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers in List :",even)
print("Odd Numbers in List :",odd)