def gun(x=10, y=20, z=30):
    return x + y * z


print(gun())
print(gun(3))
print(gun(3, 2))
print(gun(3, 2, 1))
print(gun(z=1, y=2))
