# WAP to calculate Simple Interst and total amount using principal, rate, and time entered by the user

amount = float(input("Enter Principal Amount :- "))
rate = float(input("Enter Rate :- "))
time = float(input("Enter Time Period :- "))

si = (amount * rate * time) / 100

print("Simple Interst :- ",si)
print("total Amount :- ",amount + si)