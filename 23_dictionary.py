# struktur data dictionary

user = {
    "name": "Rizqi Assyaufi",
    "age": 36,
    "is_admin": True
}

print(user)
print(user["name"])
print(user.get("age"))
print(user.get("is_admin"))
print(user.get("username", None))


user["name"] = "Rizqi Nur"
print(user)
print(user["name"])
