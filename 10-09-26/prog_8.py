"""
WAP to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
Example: 9875 -> 9+8+7+5 = 29 -> 2+9 = 11 -> 1 + 1 = 2
"""

n = int(input("Enter A numnber : "))
ans = 0
while n > 0:
    rem = n % 10
    ans += rem
    