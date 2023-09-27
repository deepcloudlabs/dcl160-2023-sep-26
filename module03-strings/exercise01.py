"""
1) String -> str -> class
2) character array
3) iterable -> for loop, len()
4) immutable
5) utility methods: is_____(), upper/lower/title, strip/lstrip/rstrip/replace, ...
6) binary array
"""
full_name1 = "kate austen"
full_name2 = 'kate austen'
message1 = "kate's house"
message2 = 'kate\'s house'
message2 = "kate says: \"Hello world!\""
jack = "{\n\tfullname: \"jack bauer\",\n\tsalary: 100000,\n\tiban: \"tr1\"\n}"
print(jack)
jack = """{
    fullname: "jack bauer",
    salary: 100000,
    iban: "tr1"
}"""
sql_select_asian_countries = "select code,name,population,surfaceArea from countries where continent='Asia'"
sql_select_asian_countries = """
select code,name,population,surfaceArea 
from countries 
where continent='Asia'"""
