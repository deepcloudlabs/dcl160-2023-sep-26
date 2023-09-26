ege = {"izmir": 232}
akdeniz = {"antalya": 242}
marmara = {"istanbul": {"anadolu": 216, "avrupa": 212}}
area_codes = {*ege, *akdeniz, *marmara}  # packing keys
area_codes = {**ege, **akdeniz, **marmara}  # packing (key -> value)
print(area_codes)
print(f"is antalya in Turkey? %s" % ("antalya" in area_codes))
print(f"is amsterdam in Turkey? %s" % ("amsterdam" in area_codes))

