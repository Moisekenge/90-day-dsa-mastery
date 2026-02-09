"""
Day 1 - Project: Calculator
Build a calculator that takes two numbers and an operator.
Handle division by zero, invalid input. Loop until 'quit'.
"""


def calculator():
    while True:
        user_input = input("Type 'quit' to exit or press Enter to continue: ")
        if user_input == "quit":
            print("Goodbye.")
            break

        try:
            num1 = float(input("Enter a number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter a second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = num1 / num2
            else:
                print("Error: Invalid operator.")
                continue

            print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
