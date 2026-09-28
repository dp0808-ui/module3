from calculator.operations import add, subtract, multiply, divide

OPERATIONS = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}


def parse_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Error: Invalid number format. Please enter a valid numeric value.")


def start_repl():
    print("Welcome to Python Calculator")
    while True:
        op = input("Enter operation (add, subtract, multiply, divide) or 'exit': ").strip().lower()
        if op in ("exit", "quit"):
            print("Goodbye!")
            break
        if op not in OPERATIONS:
            print(f"Error: Unknown operation '{op}'. Please choose a valid operation.")
            continue

        num1 = parse_number("Enter first number: ")
        num2 = parse_number("Enter second number: ")

        try:
            result = OPERATIONS[op](num1, num2)
            print(f"Result: {result}\n")
        except ValueError as err:
            print(f"Error: {err}\n")
