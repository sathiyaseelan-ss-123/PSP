username = input("Enter username: ")
password = input("Enter password: ")

if username == "":
    print("Error: Username cannot be empty.")

elif password == "":
    print("Error: Password cannot be empty.")

elif len(password) < 8:
    print("Error: Password must contain at least 8 characters.")

elif username == correct_username and password == correct_password:
    print("Login successful.")

else:
    print("Error: Invalid username or password.")