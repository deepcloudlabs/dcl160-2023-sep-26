week_day = "tuesday"
match week_day:
    case "monday":
        day = 1
    case "tuesday":
        day = 2
    case "wednesday":
        day = 3
    case "thursday":
        day = 4
    case "friday":
        day = 5
    case "saturday":
        day = 6
    case "sunday":
        day = 0
    case _:
        raise ValueError("Undefined day")
print(f"{week_day}: {day}")
