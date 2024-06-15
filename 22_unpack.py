# unpack

numbers = (1, 2, 3)

x, y, z = numbers
print(x, y, z)

x, _, z = numbers
print(x, z)

_, _, z = numbers
print(z)
print(_, _, z)

x, *all = numbers
print(x, all)
print(x, tuple(all))
