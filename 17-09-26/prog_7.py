"""
Write a menu-driven python program where the user can add items, remove items, view cart, and exit.
"""

cart = []
while(True):
    print("1. To add items")
    print("2. To remove items")
    print("3. To view cart")
    print("4. To Exit")

    choice = int(input("Choose an option : "))
    if choice == 1:
        item = input("Enter an item : ")
        cart.append(item)
        print(item, "Added to cart.")
    elif choice == 2:
        item = input("Enter an item : ")
        if item in cart:
            cart.remove(item)
            print(item, "Removed from cart.")
        else:
            print("Item not Found in cart.")
    elif choice == 3:
        if len(cart) == 0:
            print("Cart Is Empty")
        else:
            print("Items in Cart : ",cart)
    elif choice == 4:
        break
    else:
        print("Invalid Choice, Please Try Again!!")