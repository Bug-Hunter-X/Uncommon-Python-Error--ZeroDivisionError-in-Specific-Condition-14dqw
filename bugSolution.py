def function_with_error_handling(x, y):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the exception as needed