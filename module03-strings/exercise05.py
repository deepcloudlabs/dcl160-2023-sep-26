line1 = "      \n\n\t\t      data1      \t\t\n\t data2      \n\t\t    data3   \n\n\t    "
print(f"line.lstrip(): {line1.lstrip()}")
print(f"line.rstrip(): {line1.rstrip()}")
print(f"line.strip(): {line1.strip()}")
line2 = "to be or not to be"
print(f"line2.replace('to','2'): {line2.replace('to','2')}")
line3 = "12345678910,         jack bauer,\t\t   tr1 \t   ,  100000,     \t 1956"
print(line3.split(","))
for token in line3.split(","):
    print(token.strip())
