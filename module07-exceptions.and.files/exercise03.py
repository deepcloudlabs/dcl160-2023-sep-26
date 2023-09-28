employees = [
    ("jack shephard", "Sales", 100000, 1978, True),
    ("kate austen", "IT", 200000, 1985, False),
    ("ben linus", "Finance", 150000, 1967, True),
    ("james sawyer", "HR", 70000, 1979, True),
    ("kim kwon", "Sales", 120000, 1986, True),
    ("sun kwon", "IT", 170000, 1984, False),
    ("hugo reyes", "IT", 120000, 1992, True)
]
file = open("employees.txt", mode="wt")
for fullname, department, salary, birth_year, full_time in employees:
    file.write(f"{fullname},{department},{salary},{birth_year},{full_time}\n")
file.close()
