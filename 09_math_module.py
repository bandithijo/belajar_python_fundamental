# math module

import math

# pembulatan ke atas
number = 5.8
number = round(number)
print(number)  # 6

# pembulatan ke atas
number = 5.5
number = round(number)
print(number)  # 6

# pembulatan ke bawah
number = 5.3
number = round(number)
print(number)  # 5

# pembulatan ke atas dengan function Math.ceil()
number = 5.2
number = math.ceil(number)
print(number)  # 6

# pembulatan ke bawah dengan function Math.floor()
number = 5.8
number = math.floor(number)
print(number)  # 5
