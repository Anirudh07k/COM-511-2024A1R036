"""
WAP program to print numbers from 1 to 50, but skip all numbers divisible by 4.
"""

i = 1
while (i <= 50):
    if i % 4 != 0:
        print(i, end= " ")
    i += 1