import csv

with open("employees.csv", mode="rt") as file:
    employees = csv.reader(file)
    for employee in employees:
        print(employee)
