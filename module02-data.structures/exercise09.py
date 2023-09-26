area_codes = {"izmir": 232, "ankara": 312, "istanbul": {"anadolu": 216, "avrupa": 212}}
print("Area code for 'Ankara' is", area_codes['ankara'])
print(f"Area code for 'Ankara' is {area_codes['ankara']}")
print("Area code for %s is %s" % ('Ankara', area_codes['ankara']))
