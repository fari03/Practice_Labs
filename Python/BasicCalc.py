class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Example usage
calculator = Calculator()

result_add = calculator.add(5, 3)
print("Addition:", result_add)

result_subtract = calculator.subtract(5, 3)
print("Subtraction:", result_subtract)

result_multiply = calculator.multiply(5, 3)
print("Multiplication:", result_multiply)

result_divide = calculator.divide(5, 3)
print("Division:", result_divide)
