shopping_cart = []

while True:
    print("\nShopping Cart")
    print("1. Add product")
    print("2. Remove product")
    print("3. Display cart")
    print("4. Display first two products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        shopping_cart.append(product)
        print("Product added.")

    elif choice == "2":
        product = input("Enter product to remove: ")

        if product in shopping_cart:
            shopping_cart.remove(product)
            print("Product removed.")
        else:
            print("Product not found.")

    elif choice == "3":
        print("Shopping Cart:", shopping_cart)

    elif choice == "4":
        print("First two products:", shopping_cart[:2])

    elif choice == "5":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")