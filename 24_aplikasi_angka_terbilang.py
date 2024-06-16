# aplikasi angka terbilang

numbers_mapping = {
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
}

numbers = input("Masukkan angka (1-9)? ")

output = ""
for number in numbers:
    terbilang = numbers_mapping.get(number, "Invalid")
    output += terbilang + " "

print(output)
