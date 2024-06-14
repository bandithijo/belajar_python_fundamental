# menerima input dari user

price = 100_000
print("Harga Produk: Rp " + str(price))
discount = 0.5
print("Discount: " + str(discount))

payment = input("Bayar sejumlah uang? Rp ")

total_price = price * discount
print("Total Harga: Rp " + str(int(total_price)))

total_return = int(payment) - int(total_price)
print("Kembalian: Rp " + str(total_return))
