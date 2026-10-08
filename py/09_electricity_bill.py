total_bill = 0


def calculate_units(previous_reading, current_reading):
    return current_reading - previous_reading


def calculate_bill(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return (100 * 2) + ((units - 100) * 3)
    else:
        return (100 * 2) + (100 * 3) + ((units - 200) * 5)


def update_bill(amount):
    global total_bill
    total_bill += amount


previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

units = calculate_units(previous, current)

if units < 0:
    print("Invalid meter readings.")
else:
    bill = calculate_bill(units)
    update_bill(bill)

    print("Units consumed:", units)
    print("Current bill: ₹", bill)
    print("Total bill: ₹", total_bill)