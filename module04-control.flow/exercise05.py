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
if not year % 4 == 0:
    print("Not a leap year.")
elif not year % 100 == 0:
    print("A leap year.")
elif not year % 400 == 0:
    print("Not a leap year.")
else:
    print("A leap year.")
