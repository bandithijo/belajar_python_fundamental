# type conversion

year_of_birth = input("Tahun lahir? ")
print(type(year_of_birth))
year_of_birth = int(year_of_birth)
age = 2024 - year_of_birth
print(type(age))
age = str(age)
print("Umur kamu adalah " + age)
