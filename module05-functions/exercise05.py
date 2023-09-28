def gun(x=10, y=20, z=30):
    return x + y * z


my_params = {
    "z": 200,
    "x": 300,
    "y": 100
}

print(gun(**my_params))
print(gun(y=100, z=200, x= 300))

