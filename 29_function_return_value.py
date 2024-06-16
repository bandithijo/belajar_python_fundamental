# function return value

length = len([1, 2, 3, 4])
print(length)  # return 4


def hello_user(name):
    print(f"Hello, {name}!")


hello_user("Rizqi")  # return "Hello, Rizqi!"
helo = hello_user("Bayu")  # return "Hello, Bayu!"
print(helo)  # return None (implisit. default return di Python adalah None)


def hello_user(name):
    print(f"Hello, {name}!")
    return 123


hello_user("Budi")  # return "Hello, Budi!"
helo = hello_user("Bidu")  # return "Hello, Bidu!"
print(helo)  # return 123


def multiply(a, b):
    a = int(a)
    b = int(b)
    return a * b


result = multiply(2, 10)
print(result)  # 20
