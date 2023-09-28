import pickle

with open("employees.pkl", mode="rb") as file:
    employees = pickle.load(file)
    for employee in employees:
        print(employee)
