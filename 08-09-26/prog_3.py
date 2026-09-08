"""
Write a Python program to calculate the final bill amount after applying a discount.
The program should take the bill amount as input from the user and apply the discount 
according to the following rules.
After calculating the discount, the program should display the discount amount and 
the final bill amount payable by the customer

Bill Amount     Discount

Above 5000      20 %
3000 to 5000    10 %
Below 3000      No discount
"""

amt = float(input("Enter bill amount : "))

if(amt > 5000):
    discount = amt * 0.20
elif(amt >= 3000 and amt <= 5000):
    discount = amt * 0.10
elif(amt < 3000):
    discount = 0

final_bill = amt - discount

print("Discount :",discount)
print("Final Bill :",final_bill)