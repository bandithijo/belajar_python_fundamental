# function keyword argument

"""
keyword argument digunakan agar argument yang dikirimkan lebih readable
"""


def halo_user(name, language):
    print(f"Hello, {name}!")
    print(f"Selamat belajar {language}")


halo_user("Rizqi", "Python")  # positional argument
halo_user(language="Python", name="Rizqi")  # keyword argument


def calculate_total_cost(total_price, shipping_cost, discount):
    total = total_price + shipping_cost - discount
    print(total)


calculate_total_cost(10_000, 5_000, 2_000)
calculate_total_cost(total_price=10_000, shipping_cost=5_000, discount=2_000)
