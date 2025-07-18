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
    # print("Addition:", add(2, 3))
    # print("Subtraction:", subtract(5, 2))
    # print("Addition:", add(6, 7))

    a = int(input('1st number :'))
    b = int(input('2st number :'))
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("multiply:", multiply(a, b))
    print("divide:", divide(a, b))