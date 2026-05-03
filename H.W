# Basic Digit Counter - Counts digits in user input
print("=" * 40)
print("     DIGIT COUNTER PROGRAM")
print("=" * 40)

# Get input from user
user_input = input("\nEnter a number: ")

# Count the digits
digit_count = len(user_input)

# Display result
print(f"\n✅ The number {user_input} has {digit_count} digit(s)")