"""
WAP to create a simple password validation system.

The program should repeatedly ask the user to enter a password until a valid password is entered.
A password will be considered valid only if it has at least 8 characters and contains the @ symbol.

Once the user enters a valid password, the program should display "Password Accepted" ans stop.
Otherwise, it should dispay "Weak password. Try again" and ask for the password again.
"""

password = input("Enter a Password : ")

if len(password) >= 8 and "@" in password:
    print("Password Accepted")
else:
    print("Weak password. Try Again!!")