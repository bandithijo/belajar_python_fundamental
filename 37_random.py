# random

import random

for index in range(5):
    print(random.random())
    print(random.randint(10, 30))


print("-" * 80)  # ---

users = ["Budi", "Bayu", "Bara", "Bela"]

limit_min = 0
limit_max = len(users) - 1

random_int = random.randint(limit_min, limit_max)
winner = users[random_int]
print(winner)


print("-" * 80)  # ---

winner = random.choice(users)
print(winner)
