inventory = {
    101: {"name": "Laptop", "quantity": 10, "price": 55000},
    102: {"name": "Mouse", "quantity": 25, "price": 700},
    103: {"name": "Keyboard", "quantity": 15, "price": 1200},
    104: {"name": "Monitor", "quantity": 8, "price": 8500}
}

print("Available Inventory")
print("-" * 40)

for product_id, details in inventory.items():
    print("Product ID:", product_id)
    print("Name:", details["name"])
    print("Quantity:", details["quantity"])
    print("Price:", details["price"])
    print("-" * 40)