# menjumlahkan list

numbers = [3, 6, 5, 7, 4, 8, 9, 2, 1]


# dengan perulangan for
init_number = 0
for number in numbers:
    init_number = init_number + number
print(init_number)  # 45


# dengan function sort(iterable)
total = sum(numbers)
print(total)  # 45
