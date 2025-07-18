# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

# Sample usage
if __name__ == "__main__":
    print("Addition:", add(2, 3))
    print("Subtraction:", subtract(5, 2))