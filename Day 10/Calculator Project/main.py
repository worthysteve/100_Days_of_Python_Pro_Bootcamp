from art import logo

# Define basic math operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    continue_calculating = True

    first_number = float(input("Enter the first number: "))

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operator: ")
        while operator not in operations:
            operator = input("Invalid operator. Choose one of +, -, *, /: ")

        second_number = float(input("Enter the second number: "))
        result = operations[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation or q to quit: ").lower()
        if choice == 'y':
            first_number = result if isinstance(result, (int, float)) else 0
        elif choice == 'n':
            continue_calculating = False
            print("\nStarting new calculation...")
            calculator()  # Restart the calculator
            return
        else:
            break

calculator()
