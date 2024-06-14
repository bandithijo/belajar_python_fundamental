# formatted string

first_name = "Rizqi"
last_name = "Assyaufi"
duration = 10_000

# string concatenation
message = first_name + " [" + last_name + "]" + " (" + str(duration) + ")"
print(message)

# %-format
message = "%s [%s] (%s)" % (first_name, last_name, duration)
print(message)

# str.format
message = "{0} [{1}] ({2})".format(first_name, last_name, duration)
print(message)

# f-strings
message = f"{first_name} [{last_name}] ({duration})"
print(message)
