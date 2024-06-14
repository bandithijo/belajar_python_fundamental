# operator logika

name = "Rizqi Assyaufi"

if len(name) > 3:
    print(f"Welcome, {name}")
else:
    print("Nama terlalu pendek")

print("-" * 80)  # ---

name = "Riz"
bypass_validation = True

if len(name) > 3 or bypass_validation:
    print(f"Welcome, {name}")
else:
    print("Nama terlalu pendek")


print("-" * 80)  # ---

name = "Riz"
bypass_validation = True

if len(name) > 3 and bypass_validation:
    print(f"Welcome, {name}")
else:
    print("Nama terlalu pendek")
