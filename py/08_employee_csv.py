import csv

filename = "employees.csv"

try:
    salary_limit = float(input("Enter salary amount: "))

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print("\nEmployees with salary above", salary_limit)

        for employee in reader:
            salary = float(employee["salary"])

            if salary > salary_limit:
                print(
                    employee["id"],
                    employee["name"],
                    employee["salary"]
                )

except FileNotFoundError:
    print("Error: CSV file not found.")

except ValueError:
    print("Error: Please enter a valid salary.")

except Exception as e:
    print("Error:", e)