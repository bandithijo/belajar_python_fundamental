# string method

course = "Belajar Python bareng Agung Setiawan"

# function len()
length = len(course)
print(length)

# method .upper()
uppercase = course.upper()
print(course)
print(uppercase)

# method .lower()
lowecase = uppercase.lower()
print(lowecase)

# method .capitalize()
capitalize = lowecase.capitalize()
print(capitalize)

# method .title()
titlecase = capitalize.title()
print(titlecase)

# method .replace()
replace = course.replace("Python", "Ruby")
print(replace)

# in
is_include = 'Python' in course
print(is_include)  # True
is_include = 'Ruby' in course
print(is_include)  # False
is_include = 'belajar python' in course
print(is_include)  # False
is_include = 'Belajar bareng' in course
print(is_include)  # False
