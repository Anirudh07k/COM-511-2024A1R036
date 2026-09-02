# WAP to take a word and print it in reverse order using slicing. 
# Also check whether it is the same forward and backward

word = input("Enter a Word : ")

print(word[::-1])
print(word == word[::-1])