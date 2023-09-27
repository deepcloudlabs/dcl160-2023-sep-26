"""
Leap Year Test
2000 Leap Year
2001 Not a Leap Year
2002 Not a Leap Year
2003 Not a Leap Year
2004 Leap Year
2100 Not a Leap Year
2200 Not a Leap Year
2300 Not a Leap Year
2400 Leap Year
11:20
"""
year = int(input("enter an integer: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
