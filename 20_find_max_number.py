# find max number

numbers = [3, 6, 5, 7, 4, 8, 9, 2, 1]


# menggunakan perulangan for
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)


# menggunakan function sorted() dan mengambil element terakhir
sorted_num = sorted(numbers)
max_number = sorted_num[-1]
print(max_number)


# menggunakan function max()
max_number = max(numbers)
print(max_number)
