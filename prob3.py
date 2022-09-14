a = int(input("Introduceti a: "))
b = int(input("Introduceti b: "))

def factorial(x):
    if (x != 1):
        return x * factorial(x - 1)
    else:
        return 1

def combinedFactorial(a, b):
    return factorial(b) / factorial(a) * factorial(b - a)

print(combinedFactorial(a,b))