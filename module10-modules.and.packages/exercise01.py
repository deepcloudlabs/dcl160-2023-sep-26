import sys

c = complex(2, 4)  # 2 + 4i
help(c)
help(list)

for builtin_module in dir(__builtins__):
    print(builtin_module)

for pth in sys.path:
    print(pth)