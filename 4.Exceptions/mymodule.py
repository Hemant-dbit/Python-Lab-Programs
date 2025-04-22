# mymodule.py

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def primeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def powNumber(base, exponent):
    return base ** exponent
