# file read

users = open("./users.txt", "r")

print(users)
# <_io.TextIOWrapper name='./users.txt' mode='r' encoding='UTF-8'>

print(users.read())
# Rizqi Assyaufi - rizqiassyaufi - admin
# Zelda - zelda - moderator
# Link - link - user

users.close()

print("-" * 80)  # ---

users = open("./users.txt", "r")

print(users.readline())
# Rizqi Assyaufi - rizqiassyaufi - admin

users.close()

print("-" * 80)  # ---

users = open("./users.txt", "r")

print(users.readline())
# Rizqi Assyaufi - rizqiassyaufi - admin
print(users.readline())
# Zelda - zelda - moderator
print(users.readline())
# Link - link - user

users.close()

print("-" * 80)  # ---

users = open("./users.txt", "r")

users_list = users.readlines()

print(users_list)

index = 1
for user in users_list:
    print(f"({index}) {user}")
    index += 1

users.close()

print("-" * 80)  # ---

try:
    users = open("./user.txt", "r")

    users_list = users.readlines()

    print(users_list)

    index = 1
    for user in users_list:
        print(f"({index}) {user}")
        index += 1

    users.close()
except FileNotFoundError:
    print("FileNotFoundError: file tidak ada")
