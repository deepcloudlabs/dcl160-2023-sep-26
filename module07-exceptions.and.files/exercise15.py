while True:
    try:
        number1 = int(input("Enter numerator: "))
        number2 = int(input("Enter denominator: "))
        result = number1 // number2
    except ValueError as ve:
        print("You must provide a valid integer like '123'")
    except ZeroDivisionError as zde:
        print("denominator cannot be zero!")
    except (PermissionError, FileNotFoundError) as e:
        print(f"{e}")
    else:
        print(result)
        break
    finally:
        print("Hello there!")
