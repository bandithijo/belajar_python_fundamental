# list method

# list pada umumnya berisi data dengan tipe data yang sama
members = ["Budi", "Bayu", "Bagus", "Bagas"]

# menambahkan element baru ke akhir list
print(members)
members.append("Juki")
print(members)

# menambahkan element baru namun dengan posisi yang bisa diatur
members.insert(2, "Joko")
print(members)

numbers = [3, 6, 5, 7, 4, 8, 9, 2, 1]

# mengurutkan dari kecil ke besar
print(numbers)
numbers.sort()
print(numbers)

print(members)
members.sort()
print(members)

# membuang sebuah element dengan indexnya
members.pop(2)
print(members)
# membuang sebuah element dengan valuenya
members.remove("Budi")
print(members)
