import re

line = "1     \t\t     \t 2      3 \t     4     5     \t   "
# "1,2,3,4,5"
print(re.sub("\s+", ",", line.strip()).split(","))
