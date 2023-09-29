"""
[a-z]       -> \w
[0-9]       -> \d
[^a-z]      -> \W
[^0-9]      -> \D
[ \n\t\r]   -> \s
[^ \n\t\r]   -> \S
"""
import re

identity_numbers = [
    "71534326584",
    "50007188324",
    "29429157706",
    "5246046225",
    "612725205668"
]
for identity in identity_numbers:
    if not re.fullmatch("\d{11}", identity):
        print(f"{identity} is not a valid identity no!")
