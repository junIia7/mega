# src/main.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    try:
        operation = input("Введите операцию (+, -, *, /) и нажмите Enter: ").strip()
        if operation:
            a = float(input("Введите первое число: ").strip())
            b = float(input("Введите второе число: ").strip())
            if operation == '+':
                print(f"{a} + {b} = {add(a, b)}")
            elif operation == '-':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif operation == '*':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif operation == '/':
                print(f"{a} / {b} = {divide(a, b)}")
            else:
                print("Некорректная операция.")
        else:
            print("Введите операцию.")
    except ValueError:
        print("Некорректные данные.")