from dictionary.utility import search

for word in search("\w{8}"):
    print(word.strip())
