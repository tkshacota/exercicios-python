# Simple calculator in Python

while True:
    try:
        expression = input("Enter an expression (or 'q' to quit): ")
        if expression.strip().lower() == "q":
            print("Goodbye!")
            break

        result = eval(expression, {"__builtins__": {}}, {})
        print("Result:", result)
    except Exception:
        print("Invalid expression. Please try again.")
