names = ["jack", "james", "kate", "ben", "jin", "sun"]  # list: ordered, duplicate
print(names[2:5:1])
print(names[2:6:2])
print(names[2:])
print(names[:5])
print(names[:])
# del names[:]
# del names[::2]
#names[2:5] = []
#names[1:] = []
names[:-2] = []
print(names)
