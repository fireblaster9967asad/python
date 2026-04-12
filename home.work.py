import math


number = float(input("Enter a number: "))


if number >= 0:
    sqrt_result = math.sqrt(number)
    print(f"The square root of {number} is: {sqrt_result}")
else:
    print("Error: Cannot calculate square root of a negative number!")