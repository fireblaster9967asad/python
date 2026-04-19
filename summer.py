age = int(input("Enter your age: "))
score = float(input("Enter test score (0-100): "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

if score >= 60:
    print("Passed!")
else:
    print("Failed!")

result = "Even" if score % 2 == 0 else "Odd"
print(f"Score is {result}")