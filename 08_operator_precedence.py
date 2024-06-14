# operator precedence

"""
urutan:
    - tanda kurung
    - perpangkatan
    - perkalian atau pembagian
    - penjumlahan atau pengurangan
"""

number = 2 + 10 * 5
print(number)  # 52

number = 2 + 10 * 5 ** 2
print(number)  # 252

number = (2 + 10) * 5 ** 2
print(number)  # 300
