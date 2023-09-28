with open("employees.txt", mode="rt") as employees:
    for line in employees:
        fullname, department, salary, birth_year, full_time = line.split(",")
        print(f"{fullname},{department},{salary},{birth_year},{full_time.strip()}")
