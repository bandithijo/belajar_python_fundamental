# module

import matematika
result = matematika.penjumlahan(2, 3)
print(result)


from matematika import penjumlahan, pengurangan
result = penjumlahan(20, 3)
print(result)
resutl = pengurangan(3, 7)
print(result)


from matematika import penjumlahan as plus, pengurangan as minus
result = plus(20, 3)
print(result)
resutl = minus(3, 7)
print(result)


from matematika import *
result = penjumlahan(1, 2)
print(result)
result = pengurangan(3, 2)
print(result)
result = perkalian(3, 2)
print(result)
result = pembagian(2, 2)
print(result)
