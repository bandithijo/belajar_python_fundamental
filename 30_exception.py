# exception

try:
    level = input("Level kamu? ")
    level = int(level)
    print(level)
except ValueError:  # ValueError Exception
    print(f"ValueError: {level} bukan angka")
except:  # GeneralError Exception
    print("Terjadi kesalahan")
