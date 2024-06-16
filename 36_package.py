# package

import marketplace.matematika
result = marketplace.matematika.penjumlahan(3, 4)
print(result)


from marketplace import matematika
result = matematika.penjumlahan(6, 1)
print(result)


from marketplace.matematika import penjumlahan, pengurangan
result = penjumlahan(1, 6)
print(result)
result = pengurangan(1, 6)
print(result)


from marketplace.matematika import penjumlahan as plus, pengurangan as minus
result = plus(2, 5)
print(result)
result = minus(2, 5)
print(result)
