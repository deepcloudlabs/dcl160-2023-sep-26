state = 42


def fun():  # side effect
    global state
    state = state + 1
    return state == 42


print(state)
fun()
fun()
print(state)
