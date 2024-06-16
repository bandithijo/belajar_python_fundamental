# file write

"""
mode file:
    1. r => baca
    2. r+ => baca tulis
    3. w => tulis
    4. a => tulis tambah
"""

# check readable or writable
users = open("./users.txt", "r+")

if users.readable():
    print("File dalam mode baca")
else:
    print("File tidak dalam mode baca")

if users.writable():
    print("File dalam mode tulis")
else:
    print("File tidak dalam mode tulis")

users.close()


# write file
users = open("./users.txt", "a")

users.write("\nMario - mario - user")

users.close()
