with open("employees.txt", mode="rt") as employees:
    try:
        for line in employees:
            fullname, department, salary, birth_year, full_time = line.split(",")
            print(f"{fullname},{department},{salary},{birth_year},{full_time.strip()}")
    except Exception as e:
        print(e)