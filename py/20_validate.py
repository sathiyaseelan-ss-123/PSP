import re

name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
phone = input("Enter phone number: ").strip()
password = input("Enter password: ")

errors = []

# Name validation
if not name:
    errors.append("Name cannot be empty.")

elif not name.replace(" ", "").isalpha():
    errors.append("Name should contain only letters.")

# Email validation
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if not re.match(email_pattern, email):
    errors.append("Invalid email address.")

# Phone validation
if not phone.isdigit() or len(phone) != 10:
    errors.append("Phone number must contain exactly 10 digits.")

# Password validation
if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

if not re.search(r"[A-Z]", password):
    errors.append("Password must contain an uppercase letter.")

if not re.search(r"[a-z]", password):
    errors.append("Password must contain a lowercase letter.")

if not re.search(r"[0-9]", password):
    errors.append("Password must contain a number.")

if errors:

    print("\nRegistration failed.")

    for error in errors:
        print("-", error)

else:

    print("\nRegistration successful!")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)