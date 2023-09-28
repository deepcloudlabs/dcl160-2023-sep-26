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
def fun(emp):
    print("fun()")
    return "IT" in emp[4]


def gun(emp):
    print("gun()")
    return emp[-1]


def run(emp):
    print("run()")
    return emp[2]


def topla(x, y):
    print("topla()")
    return x + y


# employees -> [ filter -> filter -> map -> reduce ] -> solution
full_time_it_employee_salaries = reduce(topla, map(run, filter(gun, filter(fun, employees))))
print(full_time_it_employee_salaries)
