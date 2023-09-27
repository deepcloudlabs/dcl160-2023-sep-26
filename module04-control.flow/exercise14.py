week_day = "friday"
lookup = {"monday": 1,
          "tuesday": 2,
          "wednesday": 3,
          "thursday": 4,
          "friday": 5,
          "saturday": 6,
          "sunday": 0
          }
day = lookup[week_day] # O(1)
print(f"{week_day}: {day}")
