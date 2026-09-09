"""
Write a Python program that asks the user to enter a username and password. 
The user should get unly three attempts.
If the correcrt credentials are entered, display "Login Successful" and stop the loop.
If all attempts are used, display "Account Locked"
"""

user = "anirudh07k"
pwd = "#Anirudh"

attempts = 3
while attempts > 0:
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    if (username == user) and (password == pwd):
        print("Login Successful :)")
        break
    else:
        attempts -= 1
        print("Wrong Details !!! Attempts Left :",attempts)

if attempts == 0:
    print("Account Locked")