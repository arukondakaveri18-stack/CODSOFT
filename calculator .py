# Calculator with 3-digit validation (values already given)

num1 = 123
num2 = 456
op = '+'

if num1 >= 100 and num2 >= 100:
    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero")
    else:
        print("Invalid operation")
else:
    print("Please enter at least 3-digit numbers")



# Define numbers
num1 = 123
num2 = 456

# Addition
addition = num1 + num2
print("Addition:", addition)

# Subtraction
subtraction = num1 - num2
print("Subtraction:", subtraction)

# Multiplication
multiplication = num1 * num2
print("Multiplication:", multiplication)

# Division
division = num1 / num2
print("Division:", division)