# Take a sentence containing double spaces and unwanted spaces at the beginning or end. Clean the Sentence

sentence = input("Enter a Sentence : ")

sentence = sentence.strip()
sentence = sentence.replace("  "," ")

print("Cleaned Sentence :",sentence)