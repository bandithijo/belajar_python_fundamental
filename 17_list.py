# struktur data list (array)

# list pada umumnya berisi data dengan tipe data yang sama
members = ["Budi", "Bayu", "Bagus", "Bagas"]
print(members)
print(members[1])
print(members[2:4])
print(members[:3])
print(members[1:])
print(members[:])

for member in members:
    print(f"Name: {member}")

numbers = [3, 6, 5, 7, 4, 8, 9, 2, 1]
print(numbers)


# list juga dapat berisi apa saja
user = ["Budi", 89, 13.5, True, { "age": 36 }, ["Ruby", "Python", "JavaScript"]]
print(user)
print(user[1])
print(user[2:4])
print(user[:3])
print(user[1:])
print(user[:])
