"""
Write a Python program that asks the user to enter a username and password. 
The user should get unly three attempts.
If the correcrt credentials are entered, display "Login Successful" and stop the loop.
If all attempts are used, display "Account Locked"
"""

user = "anirudh07k"
pwd = "#Anirudh"

username = input("Enter Your Username : ")
password = input("Enter Your Password :")

attempts = 3

while attempts > 0:
    if (username == user) and (password == pwd):
        print("Login Successful :)")
        break
    
    attempts -= 1

