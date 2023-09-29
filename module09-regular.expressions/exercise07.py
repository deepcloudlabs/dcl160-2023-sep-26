import re

pattern = "\s*k\w{11,}\s*"
with open("dictionary-tur.txt", mode="rt") as tr_dictionary:
    for word in tr_dictionary.readlines():
        if re.fullmatch(pattern, word):
            print(word.strip())
