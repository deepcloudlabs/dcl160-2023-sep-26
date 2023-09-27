numbers = [4, 8, None, 15, None, None, 16, None, 23, None, 42, None, None]
if_not_none = lambda value: value is not None
print(type(if_not_none))
# declarative programming -> what : functional programming
#  i) HoF (higher-order function): filter -> generator function, lazy evaluation
# ii) Pure function
# internal loop
series = list(filter(lambda value: value is not None, numbers))
print(series)
