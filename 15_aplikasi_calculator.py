# aplikasi calculator

operation_list = '+ - * /'
operation = ""

while operation != "exit":
    operation = input("Masukkan jenis Operasi? ")

    if operation == "exit":
        print("Program berhenti.")
        break

    if operation not in operation_list:
        print("Operasi tidak dikenal.")
        continue

    number_1 = int(input("Angka pertama: "))
    number_2 = int(input("Angka kedua  : "))

    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        result = number_1 / number_2

    print(f"Hasil        : {result}")


print("Terima kasih.")
