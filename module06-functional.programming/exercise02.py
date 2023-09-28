employees = [  # data
    ("jack bauer", "1", 100_000, "tr1", ["IT", "SALES"], True),
    ("kate austen", "2", 200_000, "tr2", ["IT"], True),
    ("sun kwon", "3", 300_000, "tr3", ["FINANCE"], True),
    ("jin kwon", "4", 250_000, "tr4", ["IT"], False),
    ("james sawyer", "5", 300_000, "tr5", ["FINANCE", "IT"], True)
]
# Imperative Programming: Procedural
total_salary_in_it = 0
for employee in employees:  # external loop
    departments = employee[4]
    full_time = employee[-1]
    if "IT" in departments and full_time:
        salary = employee[2]
        total_salary_in_it += salary
print(total_salary_in_it)
