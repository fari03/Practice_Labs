a = 5
b = 3
c = 4

result1 = a + b * c  # Multiplication has higher priority than addition
result2 = (a + b) * c  # Parentheses have higher priority than multiplication
result3 = a / b + c  # Division and multiplication have equal priority, evaluated from left to right
result4 = a * b - c  # Multiplication and division have higher priority than subtraction

print(result1)
print(result2)
print(result3)
print(result4)
