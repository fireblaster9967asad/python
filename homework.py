# Check if a character is in the alphabet
char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character.")
elif char.isalpha():
    print(f"'{char}' is in the alphabet.")
else:
    print(f"'{char}' is not in the alphabet.")