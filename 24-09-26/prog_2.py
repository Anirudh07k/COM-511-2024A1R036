"""
WAP to store all mmonth names in a tuple. Input a month number and display the crossponding month name. 
"""

months = ("January", "Feburary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

num = int(input("Enter Month Number : "))

print("Month : ",months[num - 1])