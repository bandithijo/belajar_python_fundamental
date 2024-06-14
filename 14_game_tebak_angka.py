# game tabak angka

live_start = 3
live_end = 0
secret_number = 8

while live_start > live_end:
    user_number = int(input("Masukkan angka (1-9)? "))

    if user_number == secret_number:
        print("Gotcha!")
        break

    live_start -= 1

if user_number == secret_number:
    print("Congratulation!")
else:
    print("You fail!")
