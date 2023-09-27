message = "Hello Mars!"
print(len(message))
print(type(message))
print(type(message[0]))
print(type(message[-1]))
x = "\u20ba"
print(x)
print(len(x))
print(type(x))
encoded_x = x.encode("utf-8")
print(type(encoded_x))
print(encoded_x)
decoded_x = encoded_x.decode("utf-8")
print(type(decoded_x))
print(decoded_x)

