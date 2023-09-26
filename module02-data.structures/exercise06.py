employees = [
    ("jack shephard", "Sales", 100000, 1978, True),
    ("kate austen", "IT", 200000, 1985, False),
    ("ben linus", "Finance", 150000, 1967, True),
    ("james sawyer", "HR", 70000, 1979, True),
    ("kim kwon", "Sales", 120000, 1986, True),
    ("sun kwon", "IT", 170000, 1984, False),
    ("hugo reyes", "IT", 120000, 1992, True)
]
print(len(employees))
employees.append(("jack bauer", "Finance", 220000, 1956, False))
print(len(employees))
employees.sort(key=lambda employee: employee[2])
print(employees)
employees.sort(key=lambda employee: employee[3])
print(employees)
