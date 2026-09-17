"""
WAP to count how many times a particular element appears in a list.
"""

lst = list(map(int, input("Enter Elements : ").split()))
target = int(input("Enter element to find : "))

count = 0
for ele in lst:
    if ele == target:
        count += 1

print(f"Element \"{target}\" occurs {count} Times in list.")


# freq = {}
# lst = [10, 20, 30, 10, 30, 50, 60, 40, 20, 10]
# # lst = list(map(int, input("Enter Elements : ").split()))

# for i in lst:
#     freq[i] = freq.get(i, 0) + 1

# print(freq)