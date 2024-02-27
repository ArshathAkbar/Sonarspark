class Calculator:
    def __init__(self):
        pass
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y
calculator = Calculator()
result_add = calculator.add(10, 5)
result_subtract = calculator.subtract(10, 5)
result_multiply = calculator.multiply(10, 5)
result_divide = calculator.divide(10, 5)
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
