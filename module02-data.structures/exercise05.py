names = ("jack", "james", "kate", "ben", "jin", "kate", "sun", "james", "kate")
print(names)
print(names.count("kate"))
print(names.count("james"))
print(names.index("kate"))
print(names.index("kate",3))
print(names.index("kate",6))
print(names.count("adam"))
print("ben" in names)
print("adam" in names)
#Value Error: print(names.index("adam"))
