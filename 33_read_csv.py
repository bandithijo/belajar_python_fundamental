# read csv

import csv

users = open("./users.csv", "r")

users_csv = csv.reader(users, delimiter=",")

print(users_csv)
# <_csv.reader object at 0x732ee4cf2420>

for user in users_csv:
    print(user)
# ['Rizqi', 'rizqi@nintendo.com', 'admin']
# ['Zelda', 'zelda@nintendo.com', 'moderator']
# ['Link', 'link@nintendo.com', 'admin']

users.close()

print("-" * 80)

users = open("./users.csv", "r")

users_csv = csv.reader(users, delimiter=",")

for user in users_csv:
    print(f"Name: {user[0]} - Username: {user[1]} - Role: {user[2]}")

users.close()
