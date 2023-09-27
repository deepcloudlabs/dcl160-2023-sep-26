city1 = "istanbul"
city2 = "istanbul"
city3 = "istanbul"
print(city1[0])
# Error: immutable -> cannot assign elements: city1[0] = "İ"
print(city1.title())
print(city1)
# object pooling -> immutable
# thread safety  <- immutable
# functional programming -> immutable
# value object (domain-driven design) -> immutable
