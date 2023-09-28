from functools import reduce

employees = [  # data
    ("jack bauer", "1", 100_000, "tr1", ["IT", "SALES"], True),
    ("kate austen", "2", 200_000, "tr2", ["IT"], True),
    ("sun kwon", "3", 300_000, "tr3", ["FINANCE"], True),
    ("jin kwon", "4", 250_000, "tr4", ["IT"], False),
    ("james sawyer", "5", 300_000, "tr5", ["FINANCE", "IT"], True)
]

# HoF + Pure Function
# MapReduce: HDFS + MapReduce
# Pipeline: Function (HoF) Composition
works_in_it = lambda employee: "IT" in employee[4]
is_full_time_employee = lambda employee: employee[-1]
to_salary = lambda employee: employee[2]
into_total_salary = lambda accumulator, salary: accumulator + salary
full_time_it_employee_salaries = reduce(into_total_salary, map(to_salary, filter(is_full_time_employee,filter(works_in_it, employees))))
print(full_time_it_employee_salaries)
