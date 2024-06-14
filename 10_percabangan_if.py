# percabangan

is_day = True

if is_day:
    print("Selamat Siang")

print("Selamat menikmati harimu")

print("-" * 80)  # ---

is_day = False

if is_day:
    print("Selamat Siang")
else:
    print("Selamat Malam")

print("Selamat menikmati harimu")

print("-" * 80)  # ---

is_day = False
is_night = False

if is_day:
    print("Selamat Siang")
elif is_night:
    print("Selamat Malam")
else:
    print("Selamat Pagi")

print("Selamat menikmati harimu")
