jack = ("jack shephard", "Sales", 100000, 1978, True)
# full_name = jack[0]
# dept = jack[1]
# salary = jack[2]
full_name, dept, salary, *rest = jack  # unpacking
print(full_name)
print(dept)
print(salary)
print(rest)
