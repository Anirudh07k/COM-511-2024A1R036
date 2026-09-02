# WAP to take a word and count the number of vowels a,e,i,o,u

word = input("Enter a Word : ")

word = word.lower()

count = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")

print(f"Count of vowels in {word} is : {count}")