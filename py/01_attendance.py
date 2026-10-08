filename = "attendance.txt"

try:
    # Writing attendance records
    with open(filename, "w") as file:
        file.write("101, Arun, Present\n")
        file.write("102, Priya, Absent\n")
        file.write("103, Ravi, Present\n")
        file.write("104, Divya, Present\n")

    # Reading attendance records
    print("Attendance Records:")

    with open(filename, "r") as file:
        for record in file:
            print(record.strip())

except FileNotFoundError:
    print("Error: Attendance file does not exist.")

except Exception as e:
    print("An error occurred:", e)