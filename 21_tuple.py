# struktur data tuple

"""
tuple bersifat immutable (tidak dapat diubah)
"""

numbers = (3, 6, 5, 7, 4, 8, 9, 2, 1)
print(numbers)
numbers[0] = 0  # TypeError: 'tuple' object does not support item assignment
print(numbers[3])
