# operator perbandingan

result = 4 > 3
print(result)  # True

result = 4 >= 3
print(result)  # True

result = 4 < 3
print(result)  # False

result = 4 <= 3
print(result)  # False

result = 4 == 3
print(result)  # False

result = 3 == 3
print(result)  # True

result = 3 == '3'
print(result)  # False

result = 4 != 3
print(result)  # True

print('-' * 80)  # ---

grade = 6.8

if grade >= 8:
    print("Nilai kamu A")
elif grade >= 7:
    print("Nilai kamu B")
elif grade >= 6:
    print("Nilai kamu C")
elif grade >= 5:
    print("Nilai kamu D")
elif grade < 5:
    print("Nilai kamu E")
else:
    print("Nilai kamu tidak ada")
