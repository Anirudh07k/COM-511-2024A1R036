"""
WAP to input two lists and create a third list containing common elements.
"""

lst1 = list(map(int, input("Enter List 1 elements : ").split()))
lst2 = list(map(int, input("Enter List 2 elements : ").split()))

lst = []
for x in lst1:
    if x in lst2:
        lst.append(x)

print("Common Elements in lists :",lst)

# lst3 = list(set(lst1) & set(lst2))
# print("Common Elements in lists :",lst3)