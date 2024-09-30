def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of the try-except block is complete.")


numerator = 10
denominator = 0
result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"The result of the division is: {result}")
