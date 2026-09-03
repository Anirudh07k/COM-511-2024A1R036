# Take a password and check length, presence of @, and whether first and last characters are different.

password = input("Enter a Password : ")

print("Password Length :",len(password))
print("Is '@' Present - ","@" in password)
print("First & Last Characters are different? ",password[0] != password[-1])