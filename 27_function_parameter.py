# function dengan parameter

def halo_user(name):
    print(f"Hello, {name}!")
    print("Selamat belajar Python")


halo_user("Rizqi")


# position argument
def halo_user(name, language):
    print(f"Hello, {name}!")
    print(f"Selamat belajar {language}")


halo_user("Rizqi", "Python")
