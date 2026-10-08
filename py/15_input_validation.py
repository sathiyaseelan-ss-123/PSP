MAX_LENGTH = 50

user_input = input("Enter input for the test application: ")

length = len(user_input)

print("Input length:", length)
print("Expected maximum length:", MAX_LENGTH)

if length > MAX_LENGTH:
    print("Warning: Input exceeds the expected length.")
    print("Potential input-validation issue detected.")

else:
    print("Input length is within the expected limit.")