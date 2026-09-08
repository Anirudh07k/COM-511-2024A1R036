"""
Write a python program to check whether a comment is spam or not. 
A comment should be treated as spam if it contains any of these keywords.
"make a lot of money", "buy now", "subscribe this", or "click this"
"""

cmt = input("Enter a comment : ")

if("make a lot of money" in cmt.lower() or
   "buy now" in cmt.lower() or
   "subcribe this" in cmt.lower() or
   "click this" in cmt.lower()):
    print("Spam Comment !!!")
else:
    print("Legit Comment. :)")