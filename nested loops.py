# Decimal to Binary Converter
num = int(input("Enter decimal number: "))
if num == 0:
    print("Binary: 0")
else:
    binary = ""
    n = abs(num)
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    if num < 0:
        binary = "-" + binary
    print(f"Binary: {binary}")