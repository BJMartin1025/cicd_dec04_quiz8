import math
def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def multiply (a, b):
    return a*b

def divide (a, b):
    if b == 0:
        return "Error: Division by zero"
    return a/b

def power (a, b):
    return a**b

def sqrt (a):
    if a < 0:
        return "Error: Square root of negative number"
    return a**0.5

def percentage (a, b):
    return (a / 100) * b

def log (a, base=10):
    if a <= 0:
        return "Error: Logarithm of non-positive number"
    return math.log(a, base)

def sin (angle):
    return math.sin(math.radians(angle))

def cos (angle):
    return math.cos(math.radians(angle))

def tan (angle):
    return math.tan(math.radians(angle))