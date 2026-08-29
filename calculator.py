"""
Simple Calculator Application
------------------------------
A command-line calculator that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def main():
    print("==== SIMPLE CALCULATOR ====")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)\n")

    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = input("Choose an operation (+, -, *, /): ").strip()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
