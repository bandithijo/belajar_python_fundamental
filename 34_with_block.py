# with block

import csv

users = open("./users.csv", "r")

users_csv = csv.reader(users, delimiter=",")

print(users_csv)

for user in users_csv:
    print(user)

users.close()


# cara di atas tidak aman.
# karna jika terjadi error setelah function open(),
# maka buffer tidak akan tertutup
# lebih direkomendasikan dibungkus dalam with block
with open("./users.csv", "r") as users:

    raise Exception("Error loh ini")

    users_csv = csv.reader(users, delimiter=",")

    print(users_csv)

    for user in users_csv:
        print(user)

    users.close()
