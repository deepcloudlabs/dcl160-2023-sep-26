names = ("jack", "james", "kate", "ben", "jin", "sun")
print(type(names[0]))
print(names[0][0])
print(names[0][1])
print(names[0][2])
print(names[0][3])
print(names[0][-1])

print(names)
sorted_names = sorted(names, key=lambda name: len(name), reverse=True)
print(sorted_names)

employees = [
    ("jack bauer", "1", 100_000, "tr1", ["IT", "SALES"], True),
    ("kate austen", "2", 200_000, "tr2", ["IT"], True),
    ("sun kwon", "3", 300_000, "tr3", ["FINANCE"], True),
    ("jin kwon", "4", 50_000, "tr3", ["IT"], False)
]
employees[0] = ("jack bauer", "1", 150_000, "tr1", ["IT"], True)
# employees[0][2] = 150_000
# employees[0][4] = ["IT"]
