def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(operand1, operator, operand2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}")
            
    operation_func = operations[operator]
    return operation_func(operand1, operand2)

def main():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        result = calculate(num1, operator, num2)
        print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()