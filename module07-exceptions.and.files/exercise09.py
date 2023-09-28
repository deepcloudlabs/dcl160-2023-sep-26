import json

with open("employees.json", mode="rt") as file:
    employees = json.load(file)
    for employee in employees:
        print(employee)
