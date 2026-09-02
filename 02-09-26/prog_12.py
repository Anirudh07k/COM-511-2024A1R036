# WAP to take a password and check whether it contains @ and has at least 8 characters.

password = input("Enter a Password : ")

print("Valid Password : ","@" in password and len(password) >= 8)