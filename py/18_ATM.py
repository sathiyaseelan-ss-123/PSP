try:

    pin = int(input("Enter PIN: "))

    if pin != correct_pin:
        raise ValueError("Invalid PIN.")

    print("\n1. Check Balance")
    print("2. Withdraw Money")

    choice = int(input("Enter choice: "))

    if choice == 1:

        print("Available balance: ₹", balance)

    elif choice == 2:

        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > balance:
            raise ValueError("Insufficient balance.")

        balance -= amount

        print("Please collect your cash.")
        print("Remaining balance: ₹", balance)

    else:
        raise ValueError("Invalid menu choice.")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)