area_codes = {"izmir": 232, "ankara": 312, "istanbul": {"anadolu": 216, "avrupa": 212}}
first_city, second_city, *rest_cities = area_codes
print(first_city)
print(second_city)
print(rest_cities)
