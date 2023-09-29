import re

pattern = "\s*[^iaeuo]*\s*"
with open("dictionary-eng.txt", mode="rt") as en_dictionary:
    for word in en_dictionary.readlines():
        if re.fullmatch(pattern, word):
            print(word.strip())
