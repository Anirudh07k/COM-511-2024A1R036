# lst = [10,20,30,40,50,60,70,80,90]

lst = list(map(int, input().split()))
search = int(input("Enter element to Search : "))

print("Linear Search")

found = False
for i in range(len(lst)):
    if lst[i] == search:
        print("Element Found at",i)
        found = True
        break
if found == False:
    print("Element Not found!! Error : 404")


sort_list = sorted(lst)
print("Binary Search")
left = 0
right = len(sort_list) - 1

found = False
while(left <= right):
    mid = left + (right - left) // 2

    if sort_list[mid] == search:
        print("Element Found at index", mid)
        found = True
        break
    elif sort_list[mid] > search:
        right = mid - 1
    else:
        left = mid + 1

if found == False:
    print("Element Not found!! Error : 404")