area_codes = {"izmir": 232, "ankara": 312, "istanbul": {"anadolu": 216, "avrupa": 212}}
print("Area code for 'Ankara' is", area_codes['ankara'])
print(f"Area code for 'Ankara' is {area_codes['ankara']}")
print("Area code for %s is %s" % ('Ankara', area_codes['ankara']))
print("Area code for %s is %s" % ('istanbul-anadolu', area_codes['istanbul']['anadolu']))
print("Area code for %s is %s" % ('istanbul-avrupa', area_codes['istanbul']['avrupa']))
area_codes["antalya"] = 242
print(area_codes.keys())
print(area_codes.values())
